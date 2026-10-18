// Small chart kit (d3) for SCE Lab Live. Every chart sizes itself from its box and redraws on resize.
(function () {
  const S = window.SCE;
  const C = (S.charts = {});
  const NS = 'http://www.w3.org/2000/svg';

  // measure text width as drawn at 11px
  let meas = null;
  C.textW = (s, size) => {
    if (!meas) {
      const svg = document.createElementNS(NS, 'svg');
      svg.setAttribute('width', '0'); svg.setAttribute('height', '0');
      svg.style.position = 'absolute'; svg.style.visibility = 'hidden';
      meas = document.createElementNS(NS, 'text');
      meas.style.fontFamily = 'var(--font-anthropic-sans)';
      svg.appendChild(meas);
      document.getElementById('dash-root').appendChild(svg);
    }
    meas.style.fontSize = (size || 11) + 'px';
    meas.textContent = s;
    return meas.getComputedTextLength() || String(s).length * 6;
  };

  // tooltip in a position:relative box
  C.tip = (box) => {
    let t = box.querySelector(':scope > .sce-tip');
    if (!t) { t = S.el('div', { class: 'sce-tip', role: 'status' }); box.appendChild(t); }
    return {
      show(head, lines, x, y) {
        const kids = [S.el('div', { class: 'sce-tip-h' }, head)];
        for (const l of lines) {
          const r = S.el('div', { class: 'sce-tip-r' });
          if (l.color) { const sw = S.el('i', { class: 'sce-sw' }); sw.style.background = l.color; r.append(sw); }
          r.append(document.createTextNode(l.name));
          if (l.value != null) r.append(S.el('b', null, l.value));
          kids.push(r);
        }
        t.replaceChildren(...kids);
        t.style.display = 'block';
        const bw = box.clientWidth, tw = t.offsetWidth, th = t.offsetHeight;
        let left = x + 14; if (left + tw > bw) left = Math.max(0, x - tw - 14);
        let top = y - th / 2; top = Math.max(0, Math.min(top, box.clientHeight - th));
        t.style.left = left + 'px'; t.style.top = top + 'px';
      },
      hide() { t.style.display = 'none'; },
    };
  };

  const svgIn = (box, w, h) => {
    const keep = box.querySelector(':scope > .sce-tip');
    box.replaceChildren();
    const svg = d3.select(box).append('svg').attr('width', '100%').attr('viewBox', `0 0 ${w} ${h}`).attr('height', h)
      .attr('role', 'img');
    if (keep) box.appendChild(keep);
    return svg;
  };
  const cleanAxis = (g) => g.attr('font-size', null).attr('font-family', null).attr('class', 'sce-axis');
  const yTickFmt = (unit) => (v) => S.fmtNum(v, unit);

  // ---------- line chart over dates, with optional bands, refs and end dots ----------
  C.line = (box, o) => {
    const W = Math.max(280, box.clientWidth || 600), H = o.height || 300;
    const pts = o.series.flatMap((s) => s.points);
    if (!pts.length) { S.empty(box, o.emptyText || 'No answers yet.'); return; }
    const ys = pts.flatMap((p) => [p.y, o.band ? p.lo : null, o.band ? p.hi : null]).filter((v) => v != null && !isNaN(v));
    (o.refs || []).forEach((r) => ys.push(r.y));
    (o.extra || []).forEach((r) => ys.push(r.y));
    let [y0, y1] = d3.extent(ys);
    if (y0 === y1) { y0 -= 1; y1 += 1; }
    if (o.zero) { y0 = Math.min(0, y0); y1 = Math.max(0, y1); }
    const y = d3.scaleLinear([y0, y1], [H - 28, 12]).nice(5);
    const fy = o.yFmt || yTickFmt(o.unit);
    const ticks = y.ticks(5);
    const ml = Math.ceil(d3.max(ticks, (t) => C.textW(fy(t)))) + 12;
    const extraW = o.extra && o.extra.length ? (o.extraW || 90) : 0;
    const mr = 14 + extraW;
    const xs = pts.map((p) => p.x);
    let [x0, x1] = d3.extent(xs);
    if (+x0 === +x1) { x0 = d3.utcDay.offset(x0, -1); x1 = d3.utcDay.offset(x1, 1); }
    const x = (o.xScale || d3.scaleUtc)([x0, x1], [ml, W - mr]);
    const svg = svgIn(box, W, H);
    svg.attr('aria-label', o.aria || 'Line chart');
    svg.append('g').attr('class', 'sce-grid').selectAll('line').data(ticks).join('line')
      .attr('x1', ml).attr('x2', W - mr).attr('y1', (t) => y(t)).attr('y2', (t) => y(t));
    svg.append('g').selectAll('text').data(ticks).join('text').attr('x', ml - 8).attr('y', (t) => y(t)).attr('dy', '0.32em')
      .attr('text-anchor', 'end').text(fy);
    const nT = Math.max(2, Math.min(o.xTicks || 8, Math.floor((W - ml - mr) / 70)));
    const xAxis = d3.axisBottom(x).ticks(nT).tickSizeOuter(0).tickFormat(o.xFmt || d3.utcFormat('%b %-d'));
    if (o.tickValues) xAxis.tickValues(o.tickValues);
    else if (!o.xScale) {
      const days = Array.from(new Set(xs.map((d) => +d))).sort((a, b) => a - b).map((d) => new Date(d));
      if (days.length <= nT) xAxis.tickValues(days);
      else xAxis.ticks(d3.utcDay.every(Math.ceil(days.length / nT)));
    }
    svg.append('g').attr('transform', `translate(0,${H - 28})`).call(xAxis).call(cleanAxis);
    if (o.zero && y0 < 0) svg.append('line').attr('x1', ml).attr('x2', W - mr).attr('y1', y(0)).attr('y2', y(0))
      .style('stroke', 'var(--cds-chart-reference)').attr('stroke-dasharray', '3 3');
    for (const r of o.refs || []) {
      svg.append('line').attr('x1', ml).attr('x2', W - mr).attr('y1', y(r.y)).attr('y2', y(r.y))
        .style('stroke', 'var(--cds-chart-reference)').attr('stroke-dasharray', '4 3');
      svg.append('text').attr('x', W - mr - 4).attr('y', y(r.y) - 5).attr('text-anchor', 'end').text(r.label);
    }
    for (const s of o.series) {
      const p = s.points.filter((d) => d.y != null && !isNaN(d.y)).sort((a, b) => a.x - b.x);
      if (o.band) {
        const b = p.filter((d) => d.lo != null && d.hi != null);
        if (b.length > 1) svg.append('path').datum(b).style('fill', s.color).attr('fill-opacity', s.bandOpacity || 0.1)
          .attr('d', d3.area().x((d) => x(d.x)).y0((d) => y(d.lo)).y1((d) => y(d.hi)));
        else if (b.length === 1) svg.append('line').attr('x1', x(b[0].x)).attr('x2', x(b[0].x)).attr('y1', y(b[0].lo)).attr('y2', y(b[0].hi))
          .style('stroke', s.color).attr('stroke-opacity', 0.35).attr('stroke-width', 6).attr('stroke-linecap', 'round');
      }
      if (p.length > 1) svg.append('path').datum(p).style('fill', 'none').style('stroke', s.color).attr('stroke-width', 2)
        .attr('stroke-linejoin', 'round').attr('stroke-linecap', 'round').attr('stroke-dasharray', s.dashed ? '5 4' : null)
        .attr('d', d3.line().x((d) => x(d.x)).y((d) => y(d.y)));
      svg.append('g').selectAll('circle').data(p).join('circle').attr('cx', (d) => x(d.x)).attr('cy', (d) => y(d.y))
        .attr('r', p.length > 40 ? 0 : 3).style('fill', s.color);
    }
    // dots outside the time axis (e.g. personas this month), in their own column on the right
    if (o.extra && o.extra.length) {
      const cx = W - extraW / 2;
      svg.append('line').attr('x1', W - extraW + 6).attr('x2', W - extraW + 6).attr('y1', 12).attr('y2', H - 28).style('stroke', 'var(--cds-chart-grid)');
      svg.append('text').attr('x', cx).attr('y', H - 10).attr('text-anchor', 'middle').text(o.extraLabel || '');
      const ex = o.extra.map((d, i) => ({ ...d, cx: cx + (i - (o.extra.length - 1) / 2) * 12 }));
      svg.append('g').selectAll('circle').data(ex).join('circle').attr('cx', (d) => d.cx).attr('cy', (d) => y(d.y)).attr('r', 5)
        .style('fill', (d) => d.color).style('stroke', 'var(--color-panel)').attr('stroke-width', 1.5);
    }
    // hover
    const tip = C.tip(box);
    const allX = Array.from(new Set(pts.map((p) => +p.x))).sort((a, b) => a - b);
    const rule = svg.append('line').attr('y1', 12).attr('y2', H - 28).style('stroke', 'var(--cds-chart-axis)').attr('opacity', 0);
    const hot = svg.append('g');
    svg.append('rect').attr('x', ml).attr('y', 0).attr('width', Math.max(0, W - mr - ml)).attr('height', H).style('fill', 'transparent')
      .on('mousemove', (ev) => {
        const [mx] = d3.pointer(ev);
        const xv = x.invert(mx);
        const i = d3.bisectCenter(allX, +xv);
        const xx = allX[i];
        rule.attr('x1', x(new Date(xx))).attr('x2', x(new Date(xx))).attr('opacity', 1);
        const lines = [];
        hot.selectAll('*').remove();
        for (const s of o.series) {
          const d = s.points.find((p) => +p.x === xx);
          if (!d || d.y == null) continue;
          hot.append('circle').attr('cx', x(d.x)).attr('cy', y(d.y)).attr('r', 4.5).style('fill', s.color).style('stroke', 'var(--color-panel)').attr('stroke-width', 1.5);
          lines.push({ color: o.series.length > 1 ? s.color : null, name: s.name, value: (o.tipFmt || ((p) => S.fmtNum(p.y, o.unit)))(d) });
        }
        const box2 = box.getBoundingClientRect(), sv = svg.node().getBoundingClientRect();
        const scale = sv.width / W;
        tip.show((o.tipHead || ((v) => d3.utcFormat('%a %b %-d, %Y')(v)))(new Date(xx)), lines, x(new Date(xx)) * scale + (sv.left - box2.left), d3.pointer(ev)[1] * scale);
      })
      .on('mouseleave', () => { tip.hide(); rule.attr('opacity', 0); hot.selectAll('*').remove(); });
  };

  // ---------- rows of dots on a shared axis (label above each track) ----------
  C.dotRows = (box, o) => {
    const W = Math.max(280, box.clientWidth || 600);
    const rowH = o.rowH || 46, top = 8, bottom = 26;
    const rows = o.rows;
    if (!rows.length) { S.empty(box, o.emptyText || 'No answers yet.'); return; }
    const H = top + rows.length * rowH + bottom;
    const vals = rows.flatMap((r) => r.values.map((v) => v.v).concat(r.ref != null ? [r.ref] : [])).filter((v) => v != null && !isNaN(v));
    if (!vals.length) { S.empty(box, o.emptyText || 'No answers yet.'); return; }
    let [a, b] = o.domain || d3.extent(vals);
    if (o.zero) { a = Math.min(0, a); b = Math.max(0, b); }
    if (a === b) { a -= 1; b += 1; }
    const ml = 8, mr = 12;
    const x = d3.scaleLinear([a, b], [ml, W - mr]).nice(6);
    const svg = svgIn(box, W, H);
    svg.attr('aria-label', o.aria || 'Dot chart');
    const ticks = x.ticks(Math.max(3, Math.floor(W / 90)));
    svg.append('g').attr('class', 'sce-grid').selectAll('line').data(ticks).join('line')
      .attr('x1', (t) => x(t)).attr('x2', (t) => x(t)).attr('y1', top).attr('y2', H - bottom);
    svg.append('g').selectAll('text').data(ticks).join('text').attr('x', (t) => x(t)).attr('y', H - 8).attr('text-anchor', 'middle')
      .text(o.tickFmt || ((t) => S.fmtNum(t, o.unit)));
    if (o.zero) svg.append('line').attr('x1', x(0)).attr('x2', x(0)).attr('y1', top).attr('y2', H - bottom).style('stroke', 'var(--cds-chart-reference)');
    const tip = C.tip(box);
    rows.forEach((r, i) => {
      const g = svg.append('g').attr('transform', `translate(0,${top + i * rowH})`);
      let lab = r.label;
      const maxW = W - ml - mr - (r.right ? C.textW(r.right) + 12 : 0);
      if (C.textW(lab, 12) > maxW) { while (lab.length > 4 && C.textW(lab + '…', 12) > maxW) lab = lab.slice(0, -1); lab += '…'; }
      g.append('text').attr('class', 'sce-lbl').attr('x', ml).attr('y', 13).style('font-size', '12px').text(lab);
      if (r.right) g.append('text').attr('x', W - mr).attr('y', 13).attr('text-anchor', 'end').text(r.right);
      const cy = 31;
      const vs = r.values.filter((v) => v.v != null && !isNaN(v.v));
      if (vs.length > 1) {
        const [lo, hi] = d3.extent(vs, (v) => v.v);
        g.append('line').attr('x1', x(lo)).attr('x2', x(hi)).attr('y1', cy).attr('y2', cy).style('stroke', 'var(--cds-chart-muted)').attr('stroke-width', 2).attr('stroke-linecap', 'round');
      }
      if (r.ref != null && !isNaN(r.ref)) {
        g.append('line').attr('x1', x(r.ref)).attr('x2', x(r.ref)).attr('y1', cy - 9).attr('y2', cy + 9).style('stroke', 'var(--color-fg-muted)').attr('stroke-width', 2.5).attr('stroke-linecap', 'round');
      }
      g.selectAll('circle').data(vs).join('circle').attr('cx', (v) => x(v.v)).attr('cy', cy).attr('r', 5.5)
        .style('fill', (v) => (v.open ? 'var(--color-panel)' : v.color)).style('stroke', (v) => (v.open ? v.color : 'var(--color-panel)'))
        .attr('stroke-width', (v) => (v.open ? 2 : 1.5));
      g.append('rect').attr('x', 0).attr('y', 0).attr('width', W).attr('height', rowH).style('fill', 'transparent')
        .style('cursor', o.onPick ? 'pointer' : null)
        .on('click', () => o.onPick && o.onPick(r))
        .on('mousemove', (ev) => {
          const lines = r.values.map((v) => ({ color: v.color, name: v.name, value: (o.fmt || ((z) => S.fmtNum(z, o.unit)))(v.v) + (v.n != null ? `  (n=${S.fmtInt(v.n)})` : '') }));
          if (r.ref != null) lines.push({ name: o.refName || 'Reference', value: (o.fmt || ((z) => S.fmtNum(z, o.unit)))(r.ref) });
          const sv = svg.node().getBoundingClientRect(), bb = box.getBoundingClientRect();
          const sc = sv.width / W;
          tip.show(r.label, lines, d3.pointer(ev, svg.node())[0] * sc, (top + i * rowH + cy) * sc + (sv.top - bb.top));
        })
        .on('mouseleave', () => tip.hide());
    });
  };

  // ---------- grouped vertical bars ----------
  C.groupedBars = (box, o) => {
    const W = Math.max(280, box.clientWidth || 600), H = o.height || 300;
    const all = o.series.flatMap((s) => s.values).filter((v) => v != null);
    if (!all.length) { S.empty(box, o.emptyText || 'No answers yet.'); return; }
    const y = d3.scaleLinear([0, d3.max(all) || 1], [H - 40, 10]).nice(5);
    const ticks = y.ticks(5);
    const ml = Math.ceil(d3.max(ticks, (t) => C.textW(S.fmtNum(t, o.unit)))) + 12;
    const x0 = d3.scaleBand(o.cats, [ml, W - 8]).paddingInner(0.22).paddingOuter(0.05);
    const x1 = d3.scaleBand(o.series.map((s) => s.key), [0, x0.bandwidth()]).padding(0.08);
    const svg = svgIn(box, W, H);
    svg.attr('aria-label', o.aria || 'Bar chart');
    svg.append('g').attr('class', 'sce-grid').selectAll('line').data(ticks).join('line').attr('x1', ml).attr('x2', W - 8).attr('y1', (t) => y(t)).attr('y2', (t) => y(t));
    svg.append('g').selectAll('text').data(ticks).join('text').attr('x', ml - 8).attr('y', (t) => y(t)).attr('dy', '0.32em').attr('text-anchor', 'end').text((t) => S.fmtNum(t, o.unit));
    const catW = x0.bandwidth();
    const rot = d3.max(o.cats, (c) => C.textW(c)) > catW + 10;
    const lab = svg.append('g').selectAll('text').data(o.cats).join('text')
      .attr('text-anchor', rot ? 'end' : 'middle')
      .attr('transform', (c) => `translate(${x0(c) + catW / 2},${H - 24}) rotate(${rot ? -30 : 0})`).text((c) => c);
    if (rot) lab.attr('dy', '0.9em');
    const tip = C.tip(box);
    o.cats.forEach((c, ci) => {
      const g = svg.append('g').attr('transform', `translate(${x0(c)},0)`);
      o.series.forEach((s) => {
        const v = s.values[ci];
        if (v == null) return;
        const bw = Math.min(32, x1.bandwidth());
        const bx = x1(s.key) + (x1.bandwidth() - bw) / 2;
        g.append('rect').attr('x', bx).attr('width', bw).attr('y', y(v)).attr('height', Math.max(0, y(0) - y(v))).attr('rx', Math.min(4, bw / 2)).style('fill', s.color);
      });
      g.append('rect').attr('x', 0).attr('y', 0).attr('width', catW).attr('height', H - 40).style('fill', 'transparent')
        .on('mousemove', (ev) => {
          const sv = svg.node().getBoundingClientRect(), sc = sv.width / W;
          tip.show(c, o.series.map((s) => ({ color: s.color, name: s.name, value: S.fmtNum(s.values[ci], o.unit) })), (x0(c) + catW / 2) * sc, d3.pointer(ev, svg.node())[1] * sc);
        })
        .on('mouseleave', () => tip.hide());
    });
  };

  // ---------- stacked bars over days ----------
  C.stackDays = (box, o) => {
    const W = Math.max(280, box.clientWidth || 600), H = o.height || 240;
    if (!o.days.length) { S.empty(box, 'No runs yet.'); return; }
    const tot = o.days.map((_, i) => d3.sum(o.series, (s) => s.values[i] || 0));
    const y = d3.scaleLinear([0, d3.max(tot) || 1], [H - 28, 10]).nice(4);
    const ticks = y.ticks(4);
    const fy = o.yFmt || S.fmtInt;
    const ml = Math.ceil(d3.max(ticks, (t) => C.textW(fy(t)))) + 12;
    const x = d3.scaleBand(o.days, [ml, W - 8]).padding(0.25);
    const svg = svgIn(box, W, H);
    svg.attr('aria-label', o.aria || 'Bars per day');
    svg.append('g').attr('class', 'sce-grid').selectAll('line').data(ticks).join('line').attr('x1', ml).attr('x2', W - 8).attr('y1', (t) => y(t)).attr('y2', (t) => y(t));
    svg.append('g').selectAll('text').data(ticks).join('text').attr('x', ml - 8).attr('y', (t) => y(t)).attr('dy', '0.32em').attr('text-anchor', 'end').text(fy);
    const every = Math.max(1, Math.ceil(o.days.length / Math.floor((W - ml) / 56)));
    svg.append('g').selectAll('text').data(o.days.filter((_, i) => i % every === 0)).join('text')
      .attr('x', (d) => x(d) + x.bandwidth() / 2).attr('y', H - 10).attr('text-anchor', 'middle').text((d) => S.fmtDayShort(d));
    const bw = Math.min(32, x.bandwidth());
    const tip = C.tip(box);
    o.days.forEach((d, i) => {
      let acc = 0;
      const bx = x(d) + (x.bandwidth() - bw) / 2;
      o.series.forEach((s) => {
        const v = s.values[i] || 0;
        if (!v) return;
        svg.append('rect').attr('x', bx).attr('width', bw).attr('y', y(acc + v)).attr('height', Math.max(0, y(acc) - y(acc + v))).style('fill', s.color);
        acc += v;
      });
      svg.append('rect').attr('x', x(d)).attr('width', x.bandwidth()).attr('y', 0).attr('height', H - 28).style('fill', 'transparent')
        .on('mousemove', (ev) => {
          const sv = svg.node().getBoundingClientRect(), sc = sv.width / W;
          tip.show(S.fmtDay(d), o.series.map((s) => ({ color: s.color, name: s.name, value: fy(s.values[i] || 0) })).concat([{ name: 'Total', value: fy(tot[i]) }]),
            (x(d) + x.bandwidth() / 2) * sc, d3.pointer(ev, svg.node())[1] * sc);
        })
        .on('mouseleave', () => tip.hide());
    });
  };

  // ---------- horizontal bars with labels above ----------
  C.hbars = (box, o) => {
    const W = Math.max(260, box.clientWidth || 500);
    const rowH = 34, H = o.rows.length * rowH + 6;
    if (!o.rows.length) { S.empty(box, o.emptyText || 'Nothing yet.'); return; }
    const x = d3.scaleLinear([0, d3.max(o.rows, (r) => r.v) || 1], [0, W - 60]);
    const svg = svgIn(box, W, H);
    svg.attr('aria-label', o.aria || 'Bar chart');
    o.rows.forEach((r, i) => {
      const g = svg.append('g').attr('transform', `translate(0,${i * rowH})`);
      g.append('text').attr('class', 'sce-lbl').attr('x', 0).attr('y', 11).text(r.label);
      g.append('rect').attr('x', 0).attr('y', 17).attr('height', 10).attr('rx', 4).attr('width', Math.max(2, x(r.v))).style('fill', o.color || dash.colors[0]);
      g.append('text').attr('x', Math.max(2, x(r.v)) + 6).attr('y', 26).text((o.fmt || S.fmtInt)(r.v));
    });
  };

  // ---------- scatter with diagonal ----------
  C.scatter = (box, o) => {
    const W = Math.max(280, box.clientWidth || 500), H = o.height || 340;
    const pts = o.points.filter((p) => p.x != null && p.y != null && !isNaN(p.x) && !isNaN(p.y));
    if (!pts.length) { S.empty(box, o.emptyText || 'No pairs yet.'); return; }
    const all = pts.flatMap((p) => [p.x, p.y]).sort(d3.ascending);
    let lo = d3.quantile(all, 0.02), hi = d3.quantile(all, 0.98);
    if (lo === hi) { lo -= 1; hi += 1; }
    const pad = (hi - lo) * 0.06;
    const dom = [lo - pad, hi + pad];
    const y = d3.scaleLinear(dom, [H - 38, 10]).nice(5);
    const ticks = y.ticks(5);
    const ml = Math.ceil(d3.max(ticks, (t) => C.textW(S.fmtNum(t, o.unit)))) + 26;
    const x = d3.scaleLinear(y.domain(), [ml, W - 10]);
    const svg = svgIn(box, W, H);
    svg.attr('aria-label', o.aria || 'Scatter chart');
    svg.append('g').attr('class', 'sce-grid').selectAll('line').data(ticks).join('line').attr('x1', ml).attr('x2', W - 10).attr('y1', (t) => y(t)).attr('y2', (t) => y(t));
    svg.append('g').selectAll('text').data(ticks).join('text').attr('x', ml - 8).attr('y', (t) => y(t)).attr('dy', '0.32em').attr('text-anchor', 'end').text((t) => S.fmtNum(t, o.unit));
    const xt = x.ticks(Math.max(3, Math.floor((W - ml) / 70)));
    svg.append('g').selectAll('text').data(xt).join('text').attr('x', (t) => x(t)).attr('y', H - 22).attr('text-anchor', 'middle').text((t) => S.fmtNum(t, o.unit));
    svg.append('text').attr('x', (ml + W - 10) / 2).attr('y', H - 4).attr('text-anchor', 'middle').text(o.xLabel || '');
    svg.append('text').attr('transform', `translate(10,${(H - 38) / 2}) rotate(-90)`).attr('text-anchor', 'middle').text(o.yLabel || '');
    const [d0, d1] = y.domain();
    svg.append('line').attr('x1', x(d0)).attr('y1', y(d0)).attr('x2', x(d1)).attr('y2', y(d1)).style('stroke', 'var(--cds-chart-reference)').attr('stroke-dasharray', '4 3');
    const clamp = (v, s) => Math.max(s.domain()[0], Math.min(s.domain()[1], v));
    // jitter: answers are often round numbers
    const jit = (p) => ((p.id * 9301 + 49297) % 233280) / 233280 - 0.5;
    const span = (d1 - d0) * 0.012;
    const tip = C.tip(box);
    svg.append('g').selectAll('circle').data(pts).join('circle')
      .attr('cx', (p) => x(clamp(p.x + jit(p) * span, x)))
      .attr('cy', (p) => y(clamp(p.y + jit({ id: p.id + 7 }) * span, y)))
      .attr('r', 3.5).style('fill', o.color).attr('fill-opacity', (p) => (p.x < d0 || p.x > d1 || p.y < d0 || p.y > d1 ? 0.25 : 0.55))
      .on('mousemove', (ev, p) => {
        const sv = svg.node().getBoundingClientRect(), sc = sv.width / W;
        const [px, py] = d3.pointer(ev, svg.node());
        tip.show('Person ' + p.id, [{ name: o.xLabel, value: S.fmtNum(p.x, o.unit) }, { name: o.yLabel, value: S.fmtNum(p.y, o.unit) }].concat(p.extra || []), px * sc, py * sc);
      })
      .on('mouseleave', () => tip.hide());
  };
})();
