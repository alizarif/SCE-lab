// Minimal stand-in for the dashboard runtime: loads data/<id>.json on first use and redraws when it arrives.
(function () {
  const store = {};          // id -> {status, data, message}
  const calcs = {};          // id -> {inputs, fn}
  const listeners = [];
  let stamp = '';
  let pending = null;
  const notify = () => {
    if (pending) return;
    pending = requestAnimationFrame(() => { pending = null; for (const fn of listeners) fn(); });
  };
  const load = (id) => {
    store[id] = { status: 'loading', data: [] };
    fetch('data/' + id + '.json' + stamp, { cache: 'no-cache' })
      .then((r) => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then((rows) => { store[id] = { status: 'ok', data: rows }; notify(); })
      .catch((e) => { store[id] = { status: 'error', data: [], message: String(e) }; notify(); });
  };
  const data = (id) => {
    if (calcs[id]) {
      const c = calcs[id];
      const ins = c.inputs.map(data);
      if (ins.some((d) => d.status === 'error')) return { status: 'error', data: [] };
      if (ins.some((d) => d.status !== 'ok')) return { status: 'loading', data: [] };
      const key = ins.map((d) => d.data);
      if (!c.cache || c.key.some((k, i) => k !== key[i])) {
        try { c.cache = { status: 'ok', data: c.fn(...key) }; } catch (e) { c.cache = { status: 'error', data: [], message: String(e) }; }
        c.key = key;
      }
      return c.cache;
    }
    if (!store[id]) load(id);
    return store[id];
  };
  const css = (n) => `var(--series-${n})`;
  window.dash = {
    data,
    onData(fn) { listeners.push(fn); fn(); },
    calc(id, o) { calcs[id] = { inputs: o.inputs, fn: o.fn }; },
    colors: [1, 2, 3, 4, 5, 6, 7, 8].map(css),
    setLink(name) { try { history.replaceState(null, '', '#' + name); } catch (e) { /* ignore */ } },
    params: () => ({}), setParams() {}, resetParams() {}, refresh() {},
  };
  let w = window.innerWidth;
  window.addEventListener('resize', () => { if (Math.abs(window.innerWidth - w) > 4) { w = window.innerWidth; notify(); } });
})();
