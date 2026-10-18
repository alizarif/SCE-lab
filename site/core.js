// Shared state, helpers and page switching for SCE Lab Live.
(function () {
  const S = (window.SCE = window.SCE || {});
  S.pages = {};          // id -> {init(root), draw(root)}
  S.ready = {};          // id -> true once the template is in place
  S.current = 'overview';
  S.state = { item: 'Q8v2part2', stat: 'median', view: 'mtd', arms: null, person: null, sort: 'interview_day', sortDir: 1 };

  const ARM_ORDER = ['A_noweb_nomemory', 'B_web_nomemory', 'C_noweb_memory', 'D_web_memory'];
  S.ARM_ORDER = ARM_ORDER;
  S.armShort = (a) => ({ A_noweb_nomemory: 'A', B_web_nomemory: 'B', C_noweb_memory: 'C', D_web_memory: 'D' }[a] || a);
  S.armName = (a) => {
    const d = S.get('arms');
    const r = d.ok ? d.rows.find((x) => x.arm === a) : null;
    return r ? r.name : a;
  };
  S.armColor = (a) => {
    const i = ARM_ORDER.indexOf(a);
    return dash.colors[(i < 0 ? 4 : i) % dash.colors.length];
  };
  S.armList = () => {
    const d = S.get('arms');
    return d.ok ? d.rows.map((r) => r.arm) : ARM_ORDER.slice();
  };

  // dash.data wrapper → {ok, status, rows, message}
  S.get = (id) => {
    const d = dash.data(id);
    const rows = Array.isArray(d.data) ? d.data : [];
    return { ok: d.status === 'ok', status: d.status, rows, message: d.message, refreshing: d.refreshing };
  };

  // ---------- formatting ----------
  const f1 = d3.format(',.1f');
  const f2 = d3.format(',.2f');
  const fInt = d3.format(',');
  S.fmtInt = (v) => (v == null || isNaN(v) ? '—' : fInt(Math.round(v)));
  S.fmtMoney = (v) => (v == null || isNaN(v) ? '—' : '$' + f2(v));
  S.fmtNum = (v, unit) => {
    if (v == null || isNaN(v)) return '—';
    const s = Math.abs(v) >= 100 ? fInt(Math.round(v)) : f1(v);
    return s.replace(/\.0$/, '') + (unit || '');
  };
  S.fmtPP = (v) => (v == null || isNaN(v) ? '—' : (v > 0 ? '+' : v < 0 ? '−' : '±') + f1(Math.abs(v)).replace(/\.0$/, '') + ' pp');
  S.parseDay = (s) => new Date(String(s).slice(0, 10) + 'T00:00:00Z');
  S.fmtDay = (s) => (s ? d3.utcFormat('%b %-d, %Y')(S.parseDay(s)) : '—');
  S.fmtDayShort = (s) => d3.utcFormat('%b %-d')(S.parseDay(s));
  S.fmtWave = (w) => (w ? d3.utcFormat('%B %Y')(new Date(w + '-01T00:00:00Z')) : '—');
  S.fmtStamp = (s) => {
    if (!s) return '—';
    const d = new Date(s);
    return isNaN(d) ? s : d3.utcFormat('%b %-d, %Y, %H:%M UTC')(d);
  };

  // ---------- questions ----------
  S.q = (item) => {
    const d = S.get('questions');
    return (d.ok && d.rows.find((r) => r.item === item)) || { item, label: item, unit: '', stat: 'mean', text: '' };
  };
  S.label = (item) => S.q(item).label;
  S.unit = (item) => S.q(item).unit || '';
  S.statOf = (item) => S.q(item).stat || 'mean';

  // ---------- small DOM helpers ----------
  S.el = (tag, attrs, text) => {
    const e = document.createElement(tag);
    if (attrs) for (const [k, v] of Object.entries(attrs)) {
      if (v == null) continue;
      if (k === 'class') e.className = v; else e.setAttribute(k, v);
    }
    if (text != null) e.textContent = text;
    return e;
  };
  S.mark = (e, source, field, where) => {
    e.setAttribute('data-source', source);
    if (field) e.setAttribute('data-field', field);
    if (where) e.setAttribute('data-where', Object.entries(where).map(([k, v]) => encodeURIComponent(k) + '=' + encodeURIComponent(v)).join('&'));
    return e;
  };
  S.$ = (sel, root) => (root || document).querySelector(sel);
  S.$$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));
  S.fill = (root, id, fn) => S.$$(`[data-source="${id}"][data-field]`, root).forEach(fn);

  // fill marks of a one-row dataset
  S.fillRow = (root, id, fmt) => {
    const d = S.get(id);
    S.$$(`[data-source="${id}"][data-field][data-row="0"]`, root).forEach((e) => {
      if (!d.ok) { e.textContent = '—'; return; }
      e.classList.remove('dash-skeleton');
      const f = e.getAttribute('data-field');
      const v = d.rows[0] ? d.rows[0][f] : null;
      e.textContent = fmt && fmt[f] ? fmt[f](v) : v == null ? '—' : typeof v === 'number' ? S.fmtInt(v) : String(v);
    });
  };

  S.empty = (box, text, failed) => {
    box.replaceChildren(S.el('div', { class: 'sce-empty' + (failed ? ' sce-failed' : '') }, text));
  };
  S.notReady = (box, ids) => {
    for (const id of ids) {
      const d = S.get(id);
      if (d.status === 'error' || d.status === 'connect' || d.status === 'declined' || d.status === 'missing') { S.empty(box, 'Failed to load', true); return true; }
      if (!d.ok) { box.replaceChildren(); box.classList.add('dash-skeleton'); return true; }
    }
    box.classList.remove('dash-skeleton');
    return false;
  };

  // select helpers
  S.setOptions = (sel, opts, value) => {
    const cur = value != null ? value : sel.value;
    const same = sel.options.length === opts.length && opts.every((o, i) => sel.options[i].value === String(o.value));
    if (!same) sel.replaceChildren(...opts.map((o) => new Option(o.label, o.value)));
    if (opts.some((o) => String(o.value) === String(cur))) sel.value = cur;
    else if (opts.length) sel.value = opts[0].value;
    return sel.value;
  };
  S.seg = (box, value, onPick) => {
    S.$$('button', box).forEach((b) => {
      b.setAttribute('aria-pressed', b.dataset.v === value ? 'true' : 'false');
      if (!b._wired) { b._wired = true; b.addEventListener('click', () => onPick(b.dataset.v)); }
    });
  };
  S.legend = (box, arms) => {
    box.replaceChildren(...arms.map((a) => {
      const s = S.el('span');
      const sw = S.el('i', { class: 'sce-sw' });
      sw.style.background = S.armColor(a);
      s.append(sw, document.createTextNode(S.armName(a)));
      return s;
    }));
  };
  S.waves = (rows) => Array.from(new Set(rows.map((r) => r.wave))).sort();

  // ---------- pages ----------
  S.show = (id, fromLink) => {
    if (!document.getElementById(id) || !S.pages[id]) id = 'overview';
    S.current = id;
    S.$$('.sce-tab').forEach((t) => t.setAttribute('aria-selected', t.dataset.page === id ? 'true' : 'false'));
    S.$$('.sce-page').forEach((p) => { p.hidden = p.id !== id; });
    const root = document.getElementById(id);
    if (!S.ready[id]) {
      const tpl = document.getElementById('tpl-' + id);
      root.replaceChildren(tpl.content.cloneNode(true));
      root.setAttribute('data-fresh', '1');
      S.ready[id] = true;
      if (S.pages[id].init) S.pages[id].init(root);
    }
    if (!fromLink) dash.setLink(id);
    S.draw();
  };
  S.draw = () => {
    S.drawHeader();
    const id = S.current;
    const root = document.getElementById(id);
    if (S.ready[id] && S.pages[id] && !root.hidden) {
      try { S.pages[id].draw(root); } catch (e) { console.error(e); throw e; }
    }
  };

  S.latestWave = () => {
    const st = S.get('status');
    return st.ok && st.rows[0] ? st.rows[0].wave : null;
  };

  S.drawHeader = () => {
    const head = document.getElementById('top');
    S.fillRow(head, 'status', {
      generated_utc: S.fmtStamp, start_date: S.fmtDay,
      people_month: S.fmtInt, participants: S.fmtInt, interviews_month: S.fmtInt,
    });
    const st = S.get('status');
    const w = st.ok && st.rows[0] ? st.rows[0].wave : null;
    const tm = document.getElementById('take-month');
    if (w) tm.textContent = S.fmtWave(w) + "'s";
    const sm = S.get('stats_monthly');
    const box = document.getElementById('take-infl');
    if (w && sm.ok) {
      const pick = (arm) => sm.rows.find((r) => r.wave === w && r.arm === arm && r.item === 'Q8v2part2');
      const b = pick('B_web_nomemory');
      const a = pick('A_noweb_nomemory');
      const eb = document.getElementById('take-b');
      const ea = document.getElementById('take-a');
      if (a && b) {
        S.mark(eb, 'stats_monthly', 'median', { wave: w, arm: 'B_web_nomemory', item: 'Q8v2part2' });
        S.mark(ea, 'stats_monthly', 'median', { wave: w, arm: 'A_noweb_nomemory', item: 'Q8v2part2' });
        eb.textContent = S.fmtNum(b.median, '%');
        ea.textContent = S.fmtNum(a.median, '%');
        box.hidden = false;
      } else box.hidden = true;
    } else box.hidden = true;
  };

  // tab wiring
  S.$$('.sce-tab').forEach((t) => t.addEventListener('click', () => S.show(t.dataset.page)));
  document.querySelector('.sce-tabs').addEventListener('keydown', (e) => {
    if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    const tabs = S.$$('.sce-tab');
    const i = tabs.findIndex((t) => t.dataset.page === S.current);
    const n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
    n.focus();
    S.show(n.dataset.page);
  });

  let redrawTimer = null;
  S.redraw = () => { clearTimeout(redrawTimer); redrawTimer = setTimeout(S.draw, 0); };
})();
