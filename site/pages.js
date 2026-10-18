// Pages of SCE Lab Live.
const S = window.SCE;
const C = S.charts;

// ---------------- calculations readers can inspect ----------------
dash.calc('effects', {
  inputs: ['stats_monthly', 'questions'],
  title: 'Web and memory effects',
  description: 'Per month and question: web minus no web, and memory minus no memory, in the question’s headline statistic (median for point forecasts, mean for probabilities).',
  fn: (stats_monthly, questions) => {
    const pct = new Map(questions.filter((q) => q.key && q.unit === '%').map((q) => [q.item, q.stat]));
    const by = new Map(stats_monthly.map((r) => [r.wave + '|' + r.arm + '|' + r.item, r]));
    const out = [];
    for (const w of new Set(stats_monthly.map((r) => r.wave))) {
      for (const [item, stat] of pct) {
        const v = (arm) => (by.get(w + '|' + arm + '|' + item) || {})[stat];
        const [a, b, c, d] = ['A_noweb_nomemory', 'B_web_nomemory', 'C_noweb_memory', 'D_web_memory'].map(v);
        if (a == null && b == null) continue;
        const diff = (x, y) => (x == null || y == null ? null : Math.round((x - y) * 100) / 100);
        out.push({ wave: w, item, stat, web_without_memory: diff(b, a), web_with_memory: diff(d, c), memory_without_web: diff(c, a), memory_with_web: diff(d, b) });
      }
    }
    return out;
  },
});

dash.calc('news_domains', {
  inputs: ['news'],
  title: 'Search results per news site',
  description: 'How many times each site appeared in the web search results the personas read this month (all days, both web versions).',
  fn: (news) => {
    const m = new Map();
    for (const r of news) m.set(r.domain, (m.get(r.domain) || 0) + r.interviews);
    return Array.from(m, ([domain, results]) => ({ domain, results })).sort((a, b) => b.results - a.results);
  },
});

const HEADLINE = ['Q8v2part2', 'Q9bv2part2', 'Q1apart2', 'Q9_binmean', 'Q4new', 'Q5new', 'Q6new', 'Q13new', 'Q22new',
  'Q25v2part2', 'Q26v2part2', 'Q30new', 'Q31v2part2', 'Q3'];
const DENS_NAMES = { Q9: 'Inflation, next 12 months', Q9c: 'Inflation, 12 months starting 2 years ahead',
  Q9new2: 'Inflation, 12 months starting 4 years ahead', Q24: 'Earnings growth in the same job, next 12 months', C1: 'National home prices, next 12 months' };
const statName = (s) => (s === 'median' ? 'median' : 'mean');

// =============================== Overview ===============================
S.pages.overview = {
  draw(root) {
    S.fillRow(root, 'status', {
      cost_month: S.fmtMoney, cost_total: S.fmtMoney, last_run_date: S.fmtDay,
    });
    const st = S.get('status');
    const s0 = st.ok ? st.rows[0] : null;
    const prog = root.querySelector('#ov-prog');
    if (s0) prog.style.width = Math.min(100, (100 * s0.interviews_month) / (s0.interviews_month_target || 1)) + '%';
    const w = S.latestWave();
    const arms = S.armList();
    S.legend(root.querySelector('#ov-legend'), arms);
    S.legend(root.querySelector('#ov-legend2'), arms);

    // month-to-date inflation
    const box = root.querySelector('#ov-infl');
    if (!S.notReady(box, ['stats_mtd', 'arms', 'status'])) {
      const rows = S.get('stats_mtd').rows.filter((r) => r.item === 'Q8v2part2' && r.wave === w);
      C.line(box, {
        unit: '%', aria: 'Median one-year inflation expectation, month to date, by version',
        series: arms.map((a) => ({ name: S.armName(a), color: S.armColor(a),
          points: rows.filter((r) => r.arm === a).map((r) => ({ x: S.parseDay(r.date), y: r.median, n: r.n })) })),
        tipFmt: (p) => S.fmtNum(p.y, '%') + `  (n=${S.fmtInt(p.n)})`,
        emptyText: 'No answers this month yet.',
      });
    }

    // calendar
    const cal = root.querySelector('#ov-cal');
    if (!S.notReady(cal, ['schedule', 'status'])) {
      const rows = S.get('schedule').rows.filter((r) => r.wave === w);
      const today = s0 ? s0.today : null;
      const grid = S.el('div', { class: 'sce-cal' });
      ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].forEach((d) => grid.append(S.el('div', { class: 'sce-cal-h' }, d)));
      if (rows.length) {
        const first = S.parseDay(rows[0].date);
        const monthStart = new Date(Date.UTC(first.getUTCFullYear(), first.getUTCMonth(), 1));
        for (let i = 0; i < monthStart.getUTCDay(); i++) grid.append(S.el('div'));
        const byDate = new Map(rows.map((r) => [r.date, r]));
        const nDays = new Date(Date.UTC(first.getUTCFullYear(), first.getUTCMonth() + 1, 0)).getUTCDate();
        for (let d = 1; d <= nDays; d++) {
          const iso = d3.utcFormat('%Y-%m-%d')(new Date(Date.UTC(first.getUTCFullYear(), first.getUTCMonth(), d)));
          const r = byDate.get(iso);
          const cell = S.el('div', { class: 'sce-day', 'data-status': r ? r.status : 'off', 'data-today': iso === today ? '1' : null });
          cell.append(S.el('b', null, String(d)));
          if (r) {
            const line = S.el('span');
            const pp = S.mark(S.el('span', null, S.fmtInt(r.people)), 'schedule', 'people', { date: r.date });
            line.append(pp, document.createTextNode(' people'));
            cell.append(line);
            cell.title = `${S.fmtDay(r.date)}: ${r.people} people, ${r.interviews_done} of ${r.interviews_planned} interviews done`;
          } else {
            cell.append(S.el('span', null, ''));
            cell.style.opacity = '.45';
          }
          grid.append(cell);
        }
      }
      cal.replaceChildren(grid);
    }

    // headline strips: point forecasts and probabilities on their own scales
    const sm = S.get('stats_monthly').rows.filter((r) => r.wave === w);
    const rh = S.get('real_history').rows;
    const strip = (box, items) => {
      if (S.notReady(box, ['stats_monthly', 'real_history', 'questions', 'arms', 'status'])) return;
      const rowsOut = [];
      for (const item of items) {
        const stat = S.statOf(item);
        const vals = arms.map((a) => {
          const r = sm.find((x) => x.arm === a && x.item === item);
          return { key: a, name: S.armName(a), color: S.armColor(a), v: r ? r[stat] : null, n: r ? r.n : null };
        });
        if (vals.every((v) => v.v == null)) continue;
        const real = rh.filter((x) => x.item === item).sort((a, b) => b.year - a.year)[0];
        rowsOut.push({ item, label: S.label(item), values: vals, ref: real ? real[stat] : null,
          right: real ? `real ${real.year}: ${S.fmtNum(real[stat], '%')}` : null });
      }
      C.dotRows(box, { rows: rowsOut, unit: '%', refName: 'Real answers, latest year', aria: 'This month by question and version',
        onPick: (r) => { S.state.item = r.item; S.state.statTouched = false; S.show('trends'); } });
    };
    strip(root.querySelector('#ov-strip'), HEADLINE.filter((i) => S.statOf(i) === 'median'));
    strip(root.querySelector('#ov-strip2'), HEADLINE.filter((i) => S.statOf(i) !== 'median'));
  },
};

// =============================== Trends ===============================
S.pages.trends = {
  init(root) {
    root.querySelector('#tr-item').addEventListener('change', (e) => { S.state.item = e.target.value; S.redraw(); });
  },
  draw(root) {
    const qs = S.get('questions');
    const sd = S.get('stats_daily');
    const sel = root.querySelector('#tr-item');
    if (qs.ok && sd.ok) {
      const have = new Set(sd.rows.map((r) => r.item));
      const opts = qs.rows.filter((q) => have.has(q.item)).sort((a, b) => a.order - b.order).map((q) => ({ value: q.item, label: q.label }));
      S.state.item = S.setOptions(sel, opts, S.state.item);
    }
    const item = S.state.item;
    if (!S.state.statTouched) S.state.stat = S.statOf(item);
    S.seg(root.querySelector('#tr-stat'), S.state.stat, (v) => { S.state.stat = v; S.state.statTouched = true; S.redraw(); });
    S.seg(root.querySelector('#tr-view'), S.state.view, (v) => { S.state.view = v; S.redraw(); });
    const arms = S.armList();
    if (!S.state.arms) S.state.arms = new Set(arms);
    const chips = root.querySelector('#tr-arms');
    chips.replaceChildren(...arms.map((a) => {
      const b = S.el('button', { type: 'button', class: 'sce-chip', 'aria-pressed': S.state.arms.has(a) ? 'true' : 'false' });
      const sw = S.el('i', { class: 'sce-sw' }); sw.style.background = S.armColor(a);
      b.append(sw, document.createTextNode(S.armName(a)));
      b.addEventListener('click', () => { if (S.state.arms.has(a)) { if (S.state.arms.size > 1) S.state.arms.delete(a); } else S.state.arms.add(a); S.redraw(); });
      return b;
    }));
    const q = S.q(item);
    root.querySelector('#tr-title').textContent = `${q.label} · ${statName(S.state.stat)}${S.state.view === 'mtd' ? ', month to date' : ', each day'}`;
    root.querySelector('#tr-text').textContent = q.text ? `“${q.text}”` : '';
    const box = root.querySelector('#tr-chart');
    const src = S.state.view === 'mtd' ? 'stats_mtd' : 'stats_daily';
    if (!S.notReady(box, [src, 'arms', 'questions'])) {
      const rows = S.get(src).rows.filter((r) => r.item === item);
      const unit = S.unit(item);
      const sel2 = arms.filter((a) => S.state.arms.has(a));
      C.line(box, {
        unit, band: true, aria: q.label,
        series: sel2.map((a) => ({ name: S.armName(a), color: S.armColor(a), bandOpacity: sel2.length > 1 ? 0.07 : 0.16,
          points: rows.filter((r) => r.arm === a).map((r) => ({ x: S.parseDay(r.date), y: r[S.state.stat], lo: r.p25, hi: r.p75, n: r.n })) })),
        tipFmt: (p) => `${S.fmtNum(p.y, unit)}  (n=${S.fmtInt(p.n)})`,
      });
    }
    // monthly table
    const tb = root.querySelector('#tr-table');
    const sm = S.get('stats_monthly');
    const cols = [['n', 'Answers'], ['mean', 'Mean'], ['median', 'Median'], ['sd', 'SD'], ['p25', '25th pct'], ['p75', '75th pct'], ['min', 'Min'], ['max', 'Max']];
    const head = S.el('tr');
    head.append(S.el('th', null, 'Month'), S.el('th', null, 'Version'), ...cols.map(([, l]) => S.el('th', { class: 'sce-num' }, l)));
    tb.tHead.replaceChildren(head);
    if (sm.ok) {
      const unit = S.unit(item);
      const rows = sm.rows.filter((r) => r.item === item).sort((a, b) => (b.wave.localeCompare(a.wave)) || S.ARM_ORDER.indexOf(a.arm) - S.ARM_ORDER.indexOf(b.arm));
      tb.tBodies[0].replaceChildren(...rows.map((r) => {
        const tr = S.el('tr');
        const arm = S.el('td'); const an = S.el('span', { class: 'sce-armname' }); const sw = S.el('i', { class: 'sce-sw' }); sw.style.background = S.armColor(r.arm);
        an.append(sw, document.createTextNode(S.armName(r.arm))); arm.append(an);
        tr.append(S.el('td', null, S.fmtWave(r.wave)), arm, ...cols.map(([k]) => S.mark(S.el('td', { class: 'sce-num' }, k === 'n' ? S.fmtInt(r[k]) : S.fmtNum(r[k], k === 'sd' ? '' : unit)), 'stats_monthly', k, { wave: r.wave, arm: r.arm, item: r.item })));
        return tr;
      }));
    }
  },
};

// =============================== Web & memory ===============================
S.pages.arms = {
  init(root) {
    root.querySelector('#ar-wave').addEventListener('change', () => S.redraw());
    root.querySelector('#ar-item').addEventListener('change', (e) => { S.state.armItem = e.target.value; S.redraw(); });
  },
  draw(root) {
    const sm = S.get('stats_monthly');
    const wsel = root.querySelector('#ar-wave');
    if (sm.ok) S.setOptions(wsel, S.waves(sm.rows).reverse().map((w) => ({ value: w, label: S.fmtWave(w) })));
    const w = wsel.value;
    const eff = dash.data('effects');
    const effRows = Array.isArray(eff.data) ? eff.data.filter((r) => r.wave === w) : [];
    const draw = (id, kA, kB, nameA, nameB, arm) => {
      const box = root.querySelector('#' + id);
      if (eff.status !== 'ok') { if (eff.status === 'error') S.empty(box, 'Failed to load', true); else box.classList.add('dash-skeleton'); return; }
      box.classList.remove('dash-skeleton');
      const color = S.armColor(arm);
      C.dotRows(box, {
        zero: true, unit: '', fmt: S.fmtPP, tickFmt: (t) => S.fmtPP(t).replace(' pp', ''),
        rows: effRows.map((r) => ({ item: r.item, label: `${S.label(r.item)} · ${statName(r.stat)}`,
          values: [{ name: nameA, color, v: r[kA] }, { name: nameB, color, v: r[kB], open: true }] })),
        onPick: (r) => { S.state.armItem = r.item; S.redraw(); },
        emptyText: 'No answers for this month yet.',
      });
    };
    draw('ar-web', 'web_without_memory', 'web_with_memory', 'Without memory (B − A)', 'With memory (D − C)', 'B_web_nomemory');
    draw('ar-mem', 'memory_without_web', 'memory_with_web', 'Without web (C − A)', 'With web (D − B)', 'C_noweb_memory');
    // 2×2 matrix
    const isel = root.querySelector('#ar-item');
    const qs = S.get('questions');
    if (qs.ok && sm.ok) {
      const have = new Set(sm.rows.filter((r) => r.wave === w).map((r) => r.item));
      S.state.armItem = S.setOptions(isel, qs.rows.filter((q) => q.key && have.has(q.item)).sort((a, b) => a.order - b.order).map((q) => ({ value: q.item, label: q.label })), S.state.armItem || 'Q8v2part2');
    }
    const item = isel.value;
    const stat = S.statOf(item);
    const unit = S.unit(item);
    const mx = root.querySelector('#ar-matrix');
    const cell = (arm) => {
      const r = sm.ok ? sm.rows.find((x) => x.wave === w && x.arm === arm && x.item === item) : null;
      const c = S.el('div', { class: 'sce-mc' });
      const top = S.el('span', { class: 'sce-armname' }); const sw = S.el('i', { class: 'sce-sw' }); sw.style.background = S.armColor(arm);
      top.append(sw, document.createTextNode(S.armName(arm)));
      const big = S.el('div', { class: 'sce-big' }, r ? S.fmtNum(r[stat], unit) : '—');
      if (r) S.mark(big, 'stats_monthly', stat, { wave: w, arm, item });
      const n = S.el('div', { class: 'sce-note' });
      if (r) { n.append(document.createTextNode('n = ')); n.append(S.mark(S.el('span', null, S.fmtInt(r.n)), 'stats_monthly', 'n', { wave: w, arm, item })); }
      c.append(top, big, n);
      return c;
    };
    mx.replaceChildren(
      S.el('div', { class: 'sce-mh' }, ''), S.el('div', { class: 'sce-mh' }, 'No memory'), S.el('div', { class: 'sce-mh' }, 'Memory'),
      S.el('div', { class: 'sce-mh' }, 'No web'), cell('A_noweb_nomemory'), cell('C_noweb_memory'),
      S.el('div', { class: 'sce-mh' }, 'Web'), cell('B_web_nomemory'), cell('D_web_memory'),
    );
    root.querySelector('#ar-matrix-note').textContent = `${S.label(item)}: ${statName(stat)} answer in ${S.fmtWave(w)}, by version.`;
  },
};

// =============================== Distributions ===============================
S.pages.dist = {
  init(root) {
    ['#di-q', '#di-wave', '#di-c'].forEach((s) => root.querySelector(s).addEventListener('change', () => S.redraw()));
  },
  draw(root) {
    const den = S.get('density');
    const arms = S.armList();
    S.legend(root.querySelector('#di-legend'), arms);
    const qsel = root.querySelector('#di-q');
    const wsel = root.querySelector('#di-wave');
    if (den.ok) {
      const qsIn = Array.from(new Set(den.rows.map((r) => r.question)));
      S.setOptions(qsel, Object.keys(DENS_NAMES).filter((q) => qsIn.includes(q)).map((q) => ({ value: q, label: DENS_NAMES[q] })));
      S.setOptions(wsel, S.waves(den.rows).reverse().map((w) => ({ value: w, label: S.fmtWave(w) })));
    }
    root.querySelector('#di-title').textContent = DENS_NAMES[qsel.value] || '—';
    const box = root.querySelector('#di-den');
    if (!S.notReady(box, ['density', 'arms'])) {
      const rows = den.rows.filter((r) => r.question === qsel.value && r.wave === wsel.value);
      const bins = Array.from(new Set(rows.map((r) => r.bin))).sort((a, b) => b - a);
      const cats = bins.map((b) => rows.find((r) => r.bin === b).range);
      C.groupedBars(box, { cats, unit: '', aria: 'Average probability by range', height: 320,
        series: arms.map((a) => ({ key: a, name: S.armName(a), color: S.armColor(a), values: bins.map((b) => { const r = rows.find((x) => x.arm === a && x.bin === b); return r ? r.prob : null; }) })) });
    }
    // choices
    const ch = S.get('choices');
    const csel = root.querySelector('#di-c');
    if (ch.ok) {
      const items = Array.from(new Set(ch.rows.map((r) => r.item)));
      S.setOptions(csel, items.map((i) => ({ value: i, label: S.label(i) })).sort((a, b) => S.q(a.value).order - S.q(b.value).order), S.state.choiceItem || 'Q1');
      S.state.choiceItem = csel.value;
    }
    root.querySelector('#di-ctitle').textContent = `${S.label(csel.value)} · ${S.fmtWave(wsel.value || S.latestWave())}`;
    const cbox = root.querySelector('#di-ch');
    if (!S.notReady(cbox, ['choices', 'arms'])) {
      const w = wsel.value || S.latestWave();
      const rows = ch.rows.filter((r) => r.item === csel.value && r.wave === w);
      const codes = Array.from(new Set(rows.map((r) => r.code))).sort((a, b) => a - b);
      C.dotRows(cbox, { unit: '%', domain: [0, Math.max(10, d3.max(rows, (r) => (r.share || 0) * 100) || 0)],
        rows: codes.map((c) => ({ label: rows.find((r) => r.code === c).answer,
          values: arms.map((a) => { const r = rows.find((x) => x.arm === a && x.code === c); return { name: S.armName(a), color: S.armColor(a), v: r && r.share != null ? r.share * 100 : null, n: r ? r.n : null }; }) })),
        emptyText: 'Nobody was asked this question this month yet.' });
    }
  },
};

// =============================== Groups ===============================
S.pages.groups = {
  init(root) {
    ['#gr-item', '#gr-dim', '#gr-wave'].forEach((s) => root.querySelector(s).addEventListener('change', () => S.redraw()));
  },
  draw(root) {
    const g = S.get('groups');
    const arms = S.armList();
    S.legend(root.querySelector('#gr-legend'), arms);
    const isel = root.querySelector('#gr-item'), dsel = root.querySelector('#gr-dim'), wsel = root.querySelector('#gr-wave');
    if (g.ok) {
      S.setOptions(isel, Array.from(new Set(g.rows.map((r) => r.item))).sort((a, b) => S.q(a).order - S.q(b).order).map((i) => ({ value: i, label: S.label(i) })), isel.value || 'Q8v2part2');
      S.setOptions(dsel, Array.from(new Set(g.rows.map((r) => r.dimension))).map((d) => ({ value: d, label: d })));
      S.setOptions(wsel, S.waves(g.rows).reverse().map((w) => ({ value: w, label: S.fmtWave(w) })));
    }
    const item = isel.value;
    if (!S.state.grStatTouched || S.state.grItem !== item) { S.state.grStat = S.statOf(item); S.state.grItem = item; S.state.grStatTouched = false; }
    S.seg(root.querySelector('#gr-stat'), S.state.grStat, (v) => { S.state.grStat = v; S.state.grStatTouched = true; S.redraw(); });
    root.querySelector('#gr-title').textContent = `${S.label(item)} · ${statName(S.state.grStat)} by ${dsel.value.toLowerCase()}`;
    const box = root.querySelector('#gr-chart');
    if (!S.notReady(box, ['groups', 'arms'])) {
      const rows = g.rows.filter((r) => r.item === item && r.dimension === dsel.value && r.wave === wsel.value);
      const ORDER = ['Under 40', '40 to 60', 'Over 60', 'High School', 'Some College', 'College', 'Under 50k', '50k to 100k', 'Over 100k', 'Low', 'High'];
      const groups = Array.from(new Set(rows.map((r) => r.group))).sort((a, b) => {
        const ia = ORDER.indexOf(a), ib = ORDER.indexOf(b);
        return ia >= 0 && ib >= 0 ? ia - ib : ia >= 0 ? -1 : ib >= 0 ? 1 : a.localeCompare(b);
      });
      const unit = S.unit(item);
      C.dotRows(box, { unit, rows: groups.map((gr) => {
        const nTot = d3.max(rows.filter((r) => r.group === gr), (r) => r.n);
        return { label: gr, right: `n ≈ ${S.fmtInt(nTot)} per version`,
          values: arms.map((a) => { const r = rows.find((x) => x.group === gr && x.arm === a); return { name: S.armName(a), color: S.armColor(a), v: r ? r[S.state.grStat] : null, n: r ? r.n : null }; }) };
      }) });
    }
  },
};

// =============================== Real vs persona ===============================
S.pages.real = {
  init(root) {
    root.querySelector('#re-item').addEventListener('change', () => S.redraw());
  },
  draw(root) {
    const rh = S.get('real_history');
    const arms = S.armList();
    S.legend(root.querySelector('#re-legend'), arms);
    const isel = root.querySelector('#re-item');
    if (rh.ok) {
      S.setOptions(isel, Array.from(new Set(rh.rows.map((r) => r.item))).sort((a, b) => S.q(a).order - S.q(b).order).map((i) => ({ value: i, label: S.label(i) })), isel.value || 'Q8v2part2');
    }
    const item = isel.value;
    const stat = S.statOf(item);
    const unit = S.unit(item);
    const w = S.latestWave();
    root.querySelector('#re-title').textContent = `${S.label(item)} · ${statName(stat)}`;
    const box = root.querySelector('#re-hist');
    if (!S.notReady(box, ['real_history', 'stats_monthly', 'arms', 'status'])) {
      const rows = rh.rows.filter((r) => r.item === item).sort((a, b) => a.year - b.year);
      const sm = S.get('stats_monthly').rows.filter((r) => r.wave === w && r.item === item);
      C.line(box, {
        unit, band: true, aria: 'Real answers by year and personas this month',
        xFmt: d3.utcFormat('%Y'), tickValues: rows.map((r) => new Date(Date.UTC(r.year, 6, 1))),
        series: [{ name: 'Real SCE answers', color: 'var(--color-fg-muted)', bandOpacity: 0.12,
          points: rows.map((r) => ({ x: new Date(Date.UTC(r.year, 6, 1)), y: r[stat], lo: r.p25, hi: r.p75, n: r.n })) }],
        tipHead: (d) => 'Real SCE, ' + d.getUTCFullYear(),
        tipFmt: (p) => `${S.fmtNum(p.y, unit)}  (n=${S.fmtInt(p.n)})`,
        extra: arms.map((a) => { const r = sm.find((x) => x.arm === a); return r ? { y: r[stat], color: S.armColor(a) } : null; }).filter(Boolean),
        extraLabel: 'Personas ' + d3.utcFormat('%b %Y')(new Date((w || '2026-01') + '-01T00:00:00Z')), extraW: 96,
      });
    }
    S.legend(root.querySelector('#re-legend2'), arms);
    const bbox = root.querySelector('#re-bins');
    if (!S.notReady(bbox, ['pair_bins', 'arms', 'status'])) {
      const rows = S.get('pair_bins').rows.filter((r) => r.item === item && r.wave === w);
      const bins = Array.from(new Set(rows.map((r) => r.bin))).sort((a, b) => a - b);
      if (!rows.length) S.empty(bbox, 'Person-by-person comparisons are kept for ten headline questions. Pick one of them, such as expected inflation or the chance of higher unemployment.');
      else C.dotRows(bbox, { unit, refName: 'Real median of the group', rows: bins.map((b) => {
        const g = rows.filter((r) => r.bin === b);
        return { label: 'Last real answer ' + g[0].range, right: 'n ≈ ' + S.fmtInt(d3.max(g, (r) => r.people)), ref: g[0].real_median,
          values: arms.map((a) => { const r = g.find((x) => x.arm === a); return { name: S.armName(a), color: S.armColor(a), v: r ? r.persona_median : null, n: r ? r.people : null }; }) };
      }) });
    }
    const tb = root.querySelector('#re-fit');
    tb.tHead.replaceChildren((() => { const tr = S.el('tr'); tr.append(S.el('th', null, 'Version'), S.el('th', { class: 'sce-num' }, 'People'), S.el('th', { class: 'sce-num' }, 'Correlation'), S.el('th', { class: 'sce-num' }, 'Gap')); return tr; })());
    const fit = S.get('pair_fit');
    const fr = fit.ok ? fit.rows.filter((r) => r.item === item && r.wave === w) : [];
    tb.tBodies[0].replaceChildren(...fr.map((r) => {
      const tr = S.el('tr');
      const td = S.el('td'); const an = S.el('span', { class: 'sce-armname' }); const sw = S.el('i', { class: 'sce-sw' }); sw.style.background = S.armColor(r.arm);
      an.append(sw, document.createTextNode(S.armName(r.arm))); td.append(an);
      const where = { wave: w, item, arm: r.arm };
      tr.append(td,
        S.mark(S.el('td', { class: 'sce-num' }, S.fmtInt(r.people)), 'pair_fit', 'people', where),
        S.mark(S.el('td', { class: 'sce-num' }, r.corr == null ? '—' : d3.format('.2f')(r.corr)), 'pair_fit', 'corr', where),
        S.mark(S.el('td', { class: 'sce-num' }, r.gap == null ? '—' : (r.gap > 0 ? '+' : '') + S.fmtNum(r.gap, unit)), 'pair_fit', 'gap', where));
      return tr;
    }));
    if (!fr.length) { const tr = S.el('tr'); tr.append(S.el('td', { colspan: '4', class: 'sce-note' }, fit.ok ? 'Not compared for this question.' : 'Loading…')); tb.tBodies[0].replaceChildren(tr); }
  },
};

// =============================== Panel ===============================
S.pages.people = {
  draw(root) {
    S.fillRow(root, 'status', {});
    const grid = root.querySelector('#pa-grid');
    if (S.notReady(grid, ['panel'])) return;
    const rows = S.get('panel').rows;
    const ORDER = ['Under 40', '40 to 60', 'Over 60', 'High School', 'Some College', 'College', 'Under 50k', '50k to 100k', 'Over 100k', 'Low', 'High'];
    const dims = Array.from(new Set(rows.map((r) => r.dimension)));
    const maxShare = d3.max(rows, (r) => r.share) || 1;
    grid.replaceChildren(...dims.map((dim) => {
      let g = rows.filter((r) => r.dimension === dim);
      g = dim === 'State' ? g.sort((a, b) => b.people - a.people).slice(0, 12)
        : g.sort((a, b) => { const ia = ORDER.indexOf(a.group), ib = ORDER.indexOf(b.group); return ia >= 0 && ib >= 0 ? ia - ib : b.people - a.people; });
      const card = S.el('div', { class: 'sce-card', id: 'pa-' + dim.toLowerCase().replace(/[^a-z]+/g, '-') });
      card.append(S.el('h3', null, dim === 'State' ? 'State (12 largest)' : dim));
      const t = S.el('table', { class: 'sce-table' });
      const hr = S.el('tr'); hr.append(S.el('th', null, 'Group'), S.el('th', { class: 'sce-num' }, 'People'), S.el('th', null, 'Share'), S.el('th', { class: 'sce-num' }, 'This month'));
      t.append(S.el('thead')); t.tHead.append(hr);
      const tb = S.el('tbody');
      for (const r of g) {
        const where = { dimension: r.dimension, group: r.group };
        const tr = S.el('tr');
        const sh = S.mark(S.el('td'), 'panel', 'share', where);
        const bar = S.el('i', { class: 'sce-inbar' }); bar.style.width = Math.round(70 * r.share / maxShare) + 'px';
        sh.append(bar, document.createTextNode(d3.format('.0%')(r.share)));
        tr.append(S.el('td', null, r.group), S.mark(S.el('td', { class: 'sce-num' }, S.fmtInt(r.people)), 'panel', 'people', where), sh,
          S.mark(S.el('td', { class: 'sce-num' }, S.fmtInt(r.interviewed_month)), 'panel', 'interviewed_month', where));
        tb.append(tr);
      }
      t.append(tb);
      const box = S.el('div', { class: 'sce-tablebox sce-free' }); box.append(t);
      card.append(box);
      return card;
    }));
  },
};

// =============================== News ===============================
S.pages.news = {
  init(root) {
    root.querySelector('#nw-date').addEventListener('change', () => S.redraw());
    root.querySelector('#nw-arm').addEventListener('change', () => S.redraw());
  },
  draw(root) {
    const n = S.get('news');
    const dsel = root.querySelector('#nw-date'), asel = root.querySelector('#nw-arm');
    if (n.ok) {
      S.setOptions(dsel, Array.from(new Set(n.rows.map((r) => r.date))).sort().reverse().map((d) => ({ value: d, label: S.fmtDay(d) })));
      S.setOptions(asel, Array.from(new Set(n.rows.map((r) => r.arm))).sort().map((a) => ({ value: a, label: S.armName(a) })));
    }
    const tb = root.querySelector('#nw-table');
    const rows = n.ok ? n.rows.filter((r) => r.date === dsel.value && r.arm === asel.value).sort((a, b) => b.interviews - a.interviews) : [];
    root.querySelector('#nw-title').textContent = dsel.value ? `Most-read pages, ${S.fmtDay(dsel.value)}` : 'Most-read pages';
    tb.tBodies[0].replaceChildren(...rows.map((r) => {
      const tr = S.el('tr');
      const td = S.el('td');
      const where = { date: r.date, arm: r.arm, url: r.url };
      const t = S.mark(S.el('div', { class: 'sce-news-title' }), 'news', 'title', where);
      if (/^https:\/\//.test(r.url)) { const a = S.el('a', { href: r.url, target: '_blank', rel: 'noopener noreferrer' }, r.title); t.append(a); } else t.textContent = r.title;
      td.append(t, S.mark(S.el('div', { class: 'sce-note' }, r.domain), 'news', 'domain', where));
      if (r.snippet) td.append(S.el('div', { class: 'sce-news-snip sce-note' }, r.snippet));
      const c = S.mark(S.el('td', { class: 'sce-num' }, S.fmtInt(r.interviews)), 'news', 'interviews', where);
      tr.append(td, c);
      return tr;
    }));
    if (n.ok && !rows.length) { const tr = S.el('tr'); tr.append(S.el('td', { colspan: '2', class: 'sce-note' }, 'No web searches this day.')); tb.tBodies[0].replaceChildren(tr); }
    const box = root.querySelector('#nw-dom');
    const nd = dash.data('news_domains');
    if (nd.status !== 'ok') { if (nd.status === 'error') S.empty(box, 'Failed to load', true); else box.classList.add('dash-skeleton'); }
    else { box.classList.remove('dash-skeleton'); C.hbars(box, { rows: nd.data.slice(0, 15).map((r) => ({ label: r.domain, v: r.results })), color: S.armColor('B_web_nomemory') }); }
  },
};

// =============================== Runs & quality ===============================
S.pages.ops = {
  init(root) {
    root.querySelector('#op-wave').addEventListener('change', () => S.redraw());
    root.querySelector('#op-arm').addEventListener('change', () => S.redraw());
  },
  draw(root) {
    const rd = S.get('runs_daily');
    const arms = S.armList();
    S.legend(root.querySelector('#op-legend'), arms);
    const days = rd.ok ? Array.from(new Set(rd.rows.map((r) => r.date))).sort() : [];
    const val = (d, a, k) => { const r = rd.rows.find((x) => x.date === d && x.arm === a); return r ? r[k] : 0; };
    const b1 = root.querySelector('#op-n'), b2 = root.querySelector('#op-cost');
    if (!S.notReady(b1, ['runs_daily', 'arms'])) C.stackDays(b1, { days, aria: 'Interviews per day by version', series: arms.map((a) => ({ name: S.armName(a), color: S.armColor(a), values: days.map((d) => val(d, a, 'interviews')) })) });
    if (!S.notReady(b2, ['runs_daily', 'arms'])) C.stackDays(b2, { days, aria: 'Spend per day by version', yFmt: S.fmtMoney, series: arms.map((a) => ({ name: S.armName(a), color: S.armColor(a), values: days.map((d) => val(d, a, 'cost')) })) });
    // run log
    const t = root.querySelector('#op-runs');
    const cols = [['interviews', 'Interviews', S.fmtInt], ['late', 'From earlier days', S.fmtInt], ['errors', 'Failed answers', S.fmtInt], ['reasks', 'Re-asked', S.fmtInt],
      ['calls', 'API calls', S.fmtInt], ['prompt_tokens', 'Input tokens', S.fmtInt], ['completion_tokens', 'Output tokens', S.fmtInt], ['cost', 'Cost', S.fmtMoney], ['seconds_per_interview', 'Seconds / interview', (v) => S.fmtNum(v)]];
    const hr = S.el('tr'); hr.append(S.el('th', null, 'Day'), S.el('th', null, 'Version'), ...cols.map(([, l]) => S.el('th', { class: 'sce-num' }, l)));
    t.tHead.replaceChildren(hr);
    const rr = rd.ok ? rd.rows.slice().sort((a, b) => b.date.localeCompare(a.date) || S.ARM_ORDER.indexOf(a.arm) - S.ARM_ORDER.indexOf(b.arm)) : [];
    t.tBodies[0].replaceChildren(...rr.map((r) => {
      const tr = S.el('tr');
      tr.append(S.el('td', null, S.fmtDay(r.date)), S.el('td', null, S.armName(r.arm)),
        ...cols.map(([k, , f]) => S.mark(S.el('td', { class: 'sce-num' }, f(r[k])), 'runs_daily', k, { date: r.date, arm: r.arm })));
      return tr;
    }));
    // quality
    const qd = S.get('quality');
    const wsel = root.querySelector('#op-wave'), asel = root.querySelector('#op-arm');
    if (qd.ok) S.setOptions(wsel, S.waves(qd.rows).reverse().map((w) => ({ value: w, label: S.fmtWave(w) })));
    S.setOptions(asel, arms.map((a) => ({ value: a, label: S.armName(a) })));
    const qt = root.querySelector('#op-q');
    const qc = [['asked', 'Asked', S.fmtInt], ['answered', 'Answered', S.fmtInt], ['reasked', 'Re-asked', S.fmtInt], ['errors', 'Failed', S.fmtInt], ['latency', 'Seconds', (v) => S.fmtNum(v)], ['cost', 'Cost', S.fmtMoney]];
    const qh = S.el('tr'); qh.append(S.el('th', null, 'Question'), ...qc.map(([, l]) => S.el('th', { class: 'sce-num' }, l)), S.el('th', null, 'Why re-asked'));
    qt.tHead.replaceChildren(qh);
    const qr = qd.ok ? qd.rows.filter((r) => r.wave === wsel.value && r.arm === asel.value).sort((a, b) => S.q(a.item).order - S.q(b.item).order) : [];
    qt.tBodies[0].replaceChildren(...qr.map((r) => {
      const tr = S.el('tr');
      const where = { wave: r.wave, arm: r.arm, item: r.item };
      tr.append(S.mark(S.el('td', null, r.label), 'quality', 'label', where), ...qc.map(([k, , f]) => S.mark(S.el('td', { class: 'sce-num' }, f(r[k])), 'quality', k, where)),
        S.mark(S.el('td', null, r.reask_reasons || ''), 'quality', 'reask_reasons', where));
      return tr;
    }));
  },
};

// =============================== Method ===============================
S.pages.method = {
  draw(root) { S.fillRow(root, 'status', { start_date: S.fmtDay, wave: S.fmtWave, reasoning: (v) => { try { return JSON.parse(v).effort || v; } catch (e) { return v || 'default'; } } }); },
};

// =============================== start ===============================
dash.onData(() => S.draw());
(function start() {
  const id = (location.hash || '').slice(1);
  S.show(S.pages[id] ? id : 'overview', true);
  if (S.pages[id]) { const el = document.getElementById('tab-' + id); if (el) el.scrollIntoView({ block: 'nearest' }); }
})();
