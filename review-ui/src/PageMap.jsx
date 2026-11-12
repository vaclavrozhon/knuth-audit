import React, { useEffect, useMemo, useRef, useState } from "react";
import { ArrowLeft, ArrowRight, ExternalLink, ZoomIn } from "lucide-react";

const STATES = {
  reviewed: { color: "#438769", label: "Reviewed" },
  not_reviewed: { color: "#dfe3dd", label: "Not reviewed" },
};

export function PageLegend() {
  return <div className="page-map-legend">{Object.entries(STATES).map(([key, value]) =>
    <span key={key}><i style={{ background: value.color }} />{value.label}</span>)}
    <span><i style={{ background: "#c94e4e" }} />Audit-supported error · separate marker</span>
  </div>;
}

export function PageStrip({ volume, findings, onOpen }) {
  const map = volume.page_map;
  const [selected, setSelected] = useState(1);
  const [hover, setHover] = useState(null);
  const [zoom, setZoom] = useState(1);
  const scrollRef = useRef(null);
  const byId = useMemo(() => new Map(findings.map(f => [f.id, f])), [findings]);
  useEffect(() => {
    const el = scrollRef.current;
    if (!el || !map) return;
    const position = (selected - .5) / map.total * el.scrollWidth;
    if (position < el.scrollLeft || position > el.scrollLeft + el.clientWidth) {
      el.scrollLeft = Math.max(0, position - el.clientWidth / 2);
    }
  }, [selected, zoom, map?.total]);
  if (!map) return null;
  const number = Math.min(selected, map.total);
  const current = map.pages[number - 1];
  const preview = map.pages[(hover || number) - 1];
  const ids = [...new Set([...current.errors, ...current.candidates, ...current.related])];
  const atPointer = event => {
    const rect = event.currentTarget.getBoundingClientRect();
    return Math.max(1, Math.min(map.total, Math.floor((event.clientX - rect.left) / rect.width * map.total) + 1));
  };
  function move(delta) { setHover(null); setSelected(n => Math.max(1, Math.min(map.total, n + delta))); }
  function keyDown(event) {
    const delta = { ArrowLeft: -1, ArrowRight: 1, PageUp: -10, PageDown: 10 }[event.key];
    if (delta !== undefined || ["Home", "End"].includes(event.key)) {
      event.preventDefault(); event.stopPropagation();
      if (delta !== undefined) move(delta);
      else { setHover(null); setSelected(event.key === "Home" ? 1 : map.total); }
    }
  }
  return <article className="page-map-card" data-page-volume={volume.id}>
    <header>
      <div><span className="page-map-volume">{volume.label}</span><h3>{volume.title}</h3></div>
      <label className="page-map-zoom"><ZoomIn size={14} /><span>Zoom</span><select aria-label={`Page map zoom for ${volume.label}`} value={zoom} onChange={e => setZoom(Number(e.target.value))}>
        <option value={1}>Fit</option><option value={2}>2×</option><option value={4}>4×</option>
      </select></label>
    </header>
    <div className="page-map-summary">
      <span><b>{map.counts.reviewed || 0}</b> reviewed</span>
      <span><b>{map.counts.not_reviewed || 0}</b> not reviewed</span>
      <span><b>{map.counts.with_errors || 0}</b> with error markers</span>
      <span>{map.total} file pages</span>
    </div>
    <div className="page-map-scroll" ref={scrollRef} tabIndex={zoom > 1 ? 0 : undefined} aria-label={`Scrollable page map for ${volume.label}`}>
      <div className="page-map-wide" style={{ width: `${zoom * 100}%` }}>
        <svg className="page-map-bar" viewBox={`0 0 ${map.total} 36`} preserveAspectRatio="none"
          role="slider" tabIndex={0} aria-label={`Page map for ${volume.label}`}
          aria-valuemin={1} aria-valuemax={map.total} aria-valuenow={number}
          aria-valuetext={`File page ${number}${current.printed_page ? `, printed page ${current.printed_page}` : ""}: ${STATES[current.state].label}${current.errors.length ? ", audit-supported error" : ""}`}
          onKeyDown={keyDown} onPointerMove={e => setHover(atPointer(e))}
          onPointerLeave={() => setHover(null)} onClick={e => { setSelected(atPointer(e)); setHover(null); }}>
          {map.pages.map(p => <g key={p.file_page}>
            <rect x={p.file_page - 1} y={0} width={1} height={36} fill={STATES[p.state].color} data-state={p.state} />
            {p.errors.length > 0 && <rect x={p.file_page - 1} y={27} width={1} height={9} fill="#c94e4e" data-error-marker="true" />}
          </g>)}
          <rect x={number - 1} y={1} width={1} height={34} fill="none" stroke="#142e25" strokeWidth={2} vectorEffect="non-scaling-stroke" />
        </svg>
        <div className="page-map-axis"><span>1</span><span>{Math.round(map.total / 4)}</span><span>{Math.round(map.total / 2)}</span><span>{Math.round(map.total * .75)}</span><span>{map.total}</span></div>
      </div>
    </div>
    <div className="page-map-preview" aria-hidden="true">File page {preview.file_page}{preview.printed_page ? ` · Printed ${preview.printed_page}` : ""} <span style={{ color: STATES[preview.state].color === "#dfe3dd" ? "#748078" : STATES[preview.state].color }}>— {STATES[preview.state].label}</span></div>
    <div className="page-map-detail">
      <div className="page-map-controls">
        <button aria-label={`Previous page in ${volume.label}`} disabled={number === 1} onClick={() => move(-1)}><ArrowLeft size={15} /></button>
        <label>File page <input aria-label={`File page in ${volume.label}`} type="number" min={1} max={map.total} value={number}
          onChange={e => { const n = Number(e.target.value); if (Number.isInteger(n) && n >= 1 && n <= map.total) { setSelected(n); setHover(null); } }} /></label>
        <button aria-label={`Next page in ${volume.label}`} disabled={number === map.total} onClick={() => move(1)}><ArrowRight size={15} /></button>
        {current.printed_page && <span>Printed {current.printed_page}</span>}
        {volume.book_available !== false ? <a href={`/files?path=${encodeURIComponent(volume.book_path)}${volume.format === "pdf" ? `#page=${number}` : ""}`} target="_blank" rel="noreferrer">{volume.format === "pdf" ? "Open page" : "Download DjVu"}<ExternalLink size={13} /></a> : <span>Book not included</span>}
      </div>
      <div className="page-map-verdict"><i style={{ background: STATES[current.state].color }} /><strong>{STATES[current.state].label}</strong>{current.errors.length > 0 && <span className="page-error-label">Audit-supported error</span>}</div>
      {current.reading_only && current.recorded_coverage !== "pending" && <p>The earlier reading record has not yet been accepted as a complete page review.</p>}
      {current.scope && <p>{current.scope}</p>}
      {ids.length > 0 ? <div className="page-map-findings">{ids.map(id => {
        const finding = byId.get(id); if (!finding) return null;
        return <button key={id} onClick={() => onOpen(id)}><span>{id}</span>{finding.title}<small>{current.related.includes(id) ? "Related evidence; exact defect location pending" : finding.status === "candidate" ? "Candidate" : finding.kind === "program" ? "Companion program" : id === "F117" ? "Local PDF artifact" : "Audit supported"}</small><ArrowRight size={14}/></button>;
      })}</div> : <p>{current.state === "reviewed" ? "No additional error found in the recorded review. Published errata are excluded." : "No finding is mapped to this page. This does not mean its content has been checked."}</p>}
      {current.review_exceptions.length > 0 && <details className="page-map-skips" open><summary>Review exceptions ({current.review_exceptions.length})</summary><ul>{current.review_exceptions.map((s, i) => <li key={i}>{s}</li>)}</ul></details>}
      {current.bibliography_skips.length > 0 && <details className="page-map-skips"><summary>{current.bibliography_skips.length} bibliography checks skipped</summary><ul>{current.bibliography_skips.map((s, i) => <li key={i}>{s}</li>)}</ul></details>}
      {current.evidence.length > 0 && <details className="page-map-sources"><summary>Review evidence ({current.evidence.length})</summary><ul>{current.evidence.map(p => <li key={p}><a href={`/files?path=${encodeURIComponent(p)}`} target="_blank" rel="noreferrer">{p.split('/').pop()}</a></li>)}</ul></details>}
    </div>
    {map.unmapped_findings.length > 0 && <p className="page-map-caveat">{map.unmapped_findings.length} findings still need an exact book-page location or concern another source. Related evidence is linked in the page details and does not change coverage.</p>}
  </article>;
}

export default function PageAtlas({ volumes, findings, onOpen }) {
  return <section className="page-atlas">
    <div className="page-atlas-heading"><div className="eyebrow">THE AUDIT, PAGE BY PAGE</div><h2>A map of every volume.</h2><p>Move along a bar to explore. Click a page to inspect its findings, or use the arrow keys.</p></div>
    <PageLegend />
    <p className="page-map-method">Green means Reviewed: the printed text, exercises and answers have been checked within the stated scope. Any exceptions appear in the details. Gray means Not reviewed. A red strip marks an audit-supported error independently of coverage. Published errata are excluded from findings, counts, and markers.</p>
    {volumes.map(v => <PageStrip key={v.id} volume={v} findings={findings} onOpen={onOpen} />)}
  </section>;
}
