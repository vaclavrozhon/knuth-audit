import React, { useState, useEffect, useRef, useMemo } from "react";
import PageAtlas, { PageStrip, PageLegend } from "./PageMap.jsx";
import { createRoot } from "react-dom/client";
import {
  BookOpen,
  Layers3,
  Search,
  Star,
  Check,
  CheckCheck,
  ArrowUpRight,
  ArrowRight,
  ArrowLeft,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  X,
  LayoutGrid,
  List,
  PanelTop,
  SlidersHorizontal,
  MessageSquare,
  FileText,
  Code2,
  Image,
  Download,
  RefreshCw,
  CircleHelp,
  Clock3,
  ExternalLink,
  AlertCircle,
  CheckCircle2,
  Globe2,
  Keyboard,
  Bookmark,
  ZoomIn,
  ZoomOut,
  Menu,
  LoaderCircle,
  FlaskConical,
  LibraryBig,
} from "lucide-react";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";
import "./style.css";

const SEVERITY = {
  critical: {
    label: "Critical",
    short: "P1",
    hint: "Affects the correctness of an algorithm, reduction, or claim.",
  },
  high: {
    label: "High",
    short: "P2",
    hint: "Changes a result, required assumptions, or a central formula.",
  },
  medium: {
    label: "Medium",
    short: "P3",
    hint: "A local count, proof step, or expression needs correction.",
  },
  low: {
    label: "Low",
    short: "P4",
    hint: "A label, reference, or minor inconsistency.",
  },
  unclassified: {
    label: "Unclassified",
    short: "—",
    hint: "The impact has not yet been assessed.",
  },
};
const AUDIT = {
  confirmed: "Audit supported",
  candidate: "Candidate",
  dismissed: "Dismissed",
};
const REVIEW = {
  pending: "Awaiting my review",
  verified: "Verified by me",
  followup: "Needs more work",
  rejected: "I disagree with this finding",
};
const CHAPTER = {
  MPR: "Mathematical Preliminaries",
  Backtracking: "Backtracking",
  DLX: "Dancing Links",
  SAT: "Satisfiability",
  Other: "Other",
};
const severityOf = (f) => f.annotation?.severity || f.severity;
const normalize = (s) =>
  s
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "")
    .toLowerCase();
const fileUrl = (p) => "/files?path=" + encodeURIComponent(p);
const count = (n) => n.toLocaleString("en-US");
const safeParse = (key, fallback) => {
  try {
    return JSON.parse(localStorage.getItem(key)) ?? fallback;
  } catch {
    return fallback;
  }
};
function IconButton({
  title,
  children,
  onClick,
  active = false,
  disabled = false,
  ...props
}) {
  return (
    <button
      type="button"
      className={"icon-button " + (active ? "active" : "")}
      aria-label={title}
      title={title}
      onClick={onClick}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
}
function Severity({ value, compact = false }) {
  const s = SEVERITY[value] || SEVERITY.unclassified;
  return (
    <span className={"severity " + value} title={s.hint}>
      <i />
      {!compact && <span>{s.short}</span>}
      {s.label}
    </span>
  );
}
function Empty({ title, children }) {
  return (
    <div className="empty">
      <Search size={30} />
      <h3>{title}</h3>
      <p>{children}</p>
    </div>
  );
}

function useAnnotations() {
  const [values, setValues] = useState({}),
    [saving, setSaving] = useState({});
  const refs = useRef({}),
    pending = useRef({}),
    timers = useRef({}),
    inflight = useRef(new Set()),
    revisions = useRef({}),
    blocked = useRef(new Set()),
    sending = useRef({});
  const updateState = (id, value) => {
    refs.current = { ...refs.current, [id]: value };
    setValues(refs.current);
  };
  const status = (id, value) => setSaving((old) => ({ ...old, [id]: value }));
  const stash = (id) => {
    try {
      localStorage.setItem(
        "knuth-draft-" + id,
        JSON.stringify({
          fields: { ...sending.current[id], ...pending.current[id] },
          revision: revisions.current[id] ?? 0,
        }),
      );
    } catch {
      status(id, "local-error");
    }
  };
  async function flush(id, force = false) {
    if (blocked.current.has(id) && !force) return;
    if (force) blocked.current.delete(id);
    clearTimeout(timers.current[id]);
    if (
      inflight.current.has(id) ||
      !Object.keys(pending.current[id] || {}).length
    )
      return;
    const fields = pending.current[id];
    pending.current[id] = {};
    sending.current[id] = fields;
    inflight.current.add(id);
    status(id, "saving");
    try {
      const response = await fetch("/api/annotations/" + id, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...fields,
          revision: revisions.current[id] ?? 0,
        }),
      });
      const body = await response.json();
      if (!response.ok) {
        if (response.status === 409) {
          revisions.current[id] = body.current.revision;
          blocked.current.add(id);
          throw new Error("conflict");
        }
        throw new Error("error");
      }
      revisions.current[id] = body.revision;
      delete sending.current[id];
      updateState(id, { ...body, ...pending.current[id] });
      if (!Object.keys(pending.current[id]).length) {
        localStorage.removeItem("knuth-draft-" + id);
        status(id, "saved");
      } else stash(id);
    } catch (error) {
      delete sending.current[id];
      pending.current[id] = { ...fields, ...pending.current[id] };
      stash(id);
      status(id, error.message === "conflict" ? "conflict" : "error");
      inflight.current.delete(id);
      return;
    }
    inflight.current.delete(id);
    if (Object.keys(pending.current[id] || {}).length) flush(id);
  }
  function change(id, patch) {
    updateState(id, { ...refs.current[id], ...patch });
    pending.current[id] = { ...pending.current[id], ...patch };
    stash(id);
    status(id, blocked.current.has(id) ? "conflict" : "pending");
    clearTimeout(timers.current[id]);
    timers.current[id] = setTimeout(() => flush(id), 650);
  }
  function ingest(findings) {
    const next = { ...refs.current };
    for (const f of findings) {
      if (
        inflight.current.has(f.id) ||
        Object.keys(pending.current[f.id] || {}).length
      )
        continue;
      next[f.id] = f.annotation;
      revisions.current[f.id] = f.annotation.revision;
      const draft = safeParse("knuth-draft-" + f.id, null);
      if (draft?.fields && Object.keys(draft.fields).length) {
        pending.current[f.id] = draft.fields;
        next[f.id] = { ...next[f.id], ...draft.fields };
        if (draft.revision === f.annotation.revision) {
          status(f.id, "pending");
          timers.current[f.id] = setTimeout(() => flush(f.id), 1000);
        } else {
          blocked.current.add(f.id);
          status(f.id, "conflict");
        }
      }
    }
    refs.current = next;
    setValues(next);
  }
  useEffect(() => {
    const handler = (e) => {
      if (
        inflight.current.size ||
        Object.values(pending.current).some((x) => Object.keys(x).length)
      ) {
        e.preventDefault();
        e.returnValue = "";
      }
    };
    window.addEventListener("beforeunload", handler);
    return () => window.removeEventListener("beforeunload", handler);
  }, []);
  return {
    values,
    saving,
    change,
    ingest,
    flush,
    retry: (id) => flush(id, true),
  };
}

function FindingCard({ finding: f, mode, onOpen, onStar, index }) {
  const a = f.annotation,
    s = severityOf(f);
  return (
    <article
      className={"finding-card " + mode + " " + s}
      tabIndex={0}
      role="button"
      aria-label={`${f.id}: ${f.title}`}
      onClick={() => onOpen(f.id)}
      onKeyDown={(e) => {
        if (e.target === e.currentTarget && ["Enter", " "].includes(e.key)) {
          e.preventDefault();
          onOpen(f.id);
        }
      }}
    >
      <div className="card-head">
        <span className="finding-id">{f.id}</span>
        <Severity value={s} />
        <IconButton
          title={a.starred ? "Remove bookmark" : "Bookmark finding"}
          active={a.starred}
          onClick={(e) => {
            e.stopPropagation();
            onStar(f.id, !a.starred);
          }}
        >
          <Star size={17} fill={a.starred ? "currentColor" : "none"} />
        </IconButton>
      </div>
      <div className="card-body">
        <div className="card-category">
          Volume {f.volume_label} · {CHAPTER[f.chapter] || f.chapter}
          {f.kind === "program" && <span>· Companion program</span>}
        </div>
        <h3>{f.title}</h3>
        <p>{f.impact || f.summary}</p>
      </div>
      <div className="card-bottom">
        <span className="card-location">
          <BookOpen size={14} />
          {f.pages.length
            ? `p. ${f.pages.slice(0, 3).join(", ")}`
            : f.kind === "program"
              ? "Program source"
              : `Volume ${f.volume_label}`}
        </span>
        <span className="card-marks">
          {f.status !== "confirmed" && (
            <span className="audit-mini">{AUDIT[f.status]}</span>
          )}
          {a.note && (
            <span className="has-note" title="Has your note">
              <MessageSquare size={14} />
            </span>
          )}
          {a.review !== "pending" ? (
            <span
              className={"review-mark " + a.review}
              title={REVIEW[a.review]}
            >
              {a.review === "verified" ? (
                <CheckCheck size={16} />
              ) : a.review === "rejected" ? (
                <X size={16} />
              ) : (
                <Clock3 size={16} />
              )}
            </span>
          ) : (
            <ArrowUpRight size={16} className="card-arrow" />
          )}
        </span>
      </div>
    </article>
  );
}

function DocumentView({ path, onDocument, onBack, findingId }) {
  const [doc, setDoc] = useState(null),
    [error, setError] = useState(""),
    [showAll, setShowAll] = useState(false);
  useEffect(() => {
    let active = true;
    setDoc(null);
    setError("");
    setShowAll(false);
    fetch("/api/document?path=" + encodeURIComponent(path))
      .then(async (r) => {
        const d = await r.json();
        if (!r.ok) throw new Error(d.error);
        if (active) setDoc(d);
      })
      .catch((e) => {
        if (active) setError(e.message);
      });
    return () => {
      active = false;
    };
  }, [path]);
  const excerpt = useMemo(() => {
    if (!doc || !path.endsWith(".md") || !findingId) return null;
    const lines = doc.text.split("\n"),
      pattern = new RegExp("\\b" + findingId + "\\b");
    const start = lines.findIndex(
      (line) => /^#{1,6} /.test(line) && pattern.test(line),
    );
    if (start < 0) return null;
    const level = lines[start].match(/^#+/)[0].length;
    let end = lines.length;
    for (let i = start + 1; i < lines.length; i++) {
      const m = lines[i].match(/^(#{1,6}) /);
      if (m && m[1].length <= level && !pattern.test(lines[i])) {
        end = i;
        break;
      }
    }
    return lines.slice(start, end).join("\n");
  }, [doc, path, findingId]);
  function resolve(href) {
    const parts = path.split("/").slice(0, -1);
    for (const bit of href.split("/")) {
      if (bit === "..") parts.pop();
      else if (bit !== ".") parts.push(bit);
    }
    return parts.join("/");
  }
  return (
    <div className="document-view">
      <button className="text-button" onClick={onBack}>
        <ArrowLeft size={15} /> Back to evidence
      </button>
      <div className="document-heading">
        <h3>{path.split("/").at(-1)}</h3>
        <a
          href={fileUrl(path)}
          target="_blank"
          rel="noreferrer"
          title="Open full file"
        >
          <ExternalLink size={16} />
        </a>
      </div>
      <p className="muted">
        {path.endsWith(".md")
          ? "Audit notes retain their source language. The current assessment is on the Explanation tab."
          : "Original source file, preserved in its original language."}
      </p>
      {error ? (
        <p className="error-line">{error}</p>
      ) : !doc ? (
        <div className="loading-line">
          <LoaderCircle className="spin" size={18} /> Loading evidence…
        </div>
      ) : (
        <>
          {doc.truncated && (
            <p>
              Showing the first 2 MB. Use the link above to open the full file.
            </p>
          )}
          {excerpt && (
            <div className="document-scope">
              <span>
                {showAll ? "Full document" : `Section for ${findingId}`}
              </span>
              <button onClick={() => setShowAll(!showAll)}>
                {showAll ? "This finding only" : "Show full document"}
              </button>
            </div>
          )}
          {path.endsWith(".md") ? (
            <div className="markdown">
              <Markdown
                remarkPlugins={[remarkGfm, remarkMath]}
                rehypePlugins={[rehypeKatex]}
                components={{
                  a: ({ href, children }) =>
                    /^https?:/.test(href || "") ? (
                      <a href={href} target="_blank" rel="noreferrer">
                        {children}
                      </a>
                    ) : (
                      <a
                        href={fileUrl(resolve(href || ""))}
                        onClick={(e) => {
                          if ((href || "").endsWith(".md")) {
                            e.preventDefault();
                            onDocument(resolve(href));
                          }
                        }}
                        target="_blank"
                        rel="noreferrer"
                      >
                        {children}
                      </a>
                    ),
                  img: ({ src, alt }) => (
                    <a
                      href={
                        /^https?:/.test(src || "")
                          ? src
                          : fileUrl(resolve(src || ""))
                      }
                      target="_blank"
                      rel="noreferrer"
                    >
                      {alt || "Image"}
                    </a>
                  ),
                }}
              >
                {!showAll && excerpt ? excerpt : doc.text}
              </Markdown>
            </div>
          ) : (
            <pre className="source-code">{doc.text}</pre>
          )}
        </>
      )}
    </div>
  );
}

function ReviewPanel({
  finding: f,
  onClose,
  onNext,
  onPrevious,
  position,
  total,
  save,
  onChange,
  onRetry,
  onFlush,
  bookPath,
}) {
  const [tab, setTab] = useState("explanation"),
    [doc, setDoc] = useState(null),
    [imageIndex, setImageIndex] = useState(0),
    [zoom, setZoom] = useState(false);
  const panel = useRef(),
    body = useRef(),
    previousFocus = useRef(document.activeElement);
  const images = f.evidence
    .filter((e) => e.kind === "image")
    .sort(
      (a, b) =>
        (b.name.startsWith(f.volume) ? 1 : 0) - (a.name.startsWith(f.volume) ? 1 : 0),
    );
  const docs = f.evidence.filter((e) => e.kind === "document");
  const a = f.annotation;
  useEffect(() => {
    setTab("explanation");
    setDoc(null);
    setImageIndex(0);
    setZoom(false);
    body.current?.scrollTo(0, 0);
    panel.current?.querySelector(".detail-columns")?.scrollTo(0, 0);
  }, [f.id]);
  useEffect(() => {
    document.body.style.overflow = "hidden";
    panel.current?.querySelector("button")?.focus();
    const focus = previousFocus.current;
    return () => {
      document.body.style.overflow = "";
      focus?.focus();
    };
  }, []);
  function trap(e) {
    if (e.key === "Tab") {
      const els = [
        ...panel.current.querySelectorAll(
          'button,a[href],select,textarea,input,[tabindex="0"]',
        ),
      ].filter((x) => !x.disabled && x.getClientRects().length);
      const first = els[0],
        last = els.at(-1);
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  }
  const img = images[imageIndex];
  return (
    <div
      className="modal-backdrop"
      onMouseDown={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
    >
      <section
        className="review-panel"
        ref={panel}
        role="dialog"
        aria-modal="true"
        aria-labelledby="detail-title"
        onKeyDown={trap}
      >
        <header className="detail-top">
          <div className="detail-breadcrumb">
            <BookOpen size={17} />
            <span>Volume {f.volume_label}</span>
            <ChevronRight size={14} />
            <b>{f.id}</b>
          </div>
          <div className="detail-navigation">
            <span>
              {position > 0 ? `${position} / ${total}` : "Selected finding"}
            </span>
            <IconButton
              title="Previous finding (←)"
              onClick={onPrevious}
              disabled={total < 2}
            >
              <ChevronLeft size={20} />
            </IconButton>
            <IconButton
              title="Next finding (→)"
              onClick={onNext}
              disabled={total < 2}
            >
              <ChevronRight size={20} />
            </IconButton>
            <IconButton
              title="Jump to my notes"
              className="icon-button mobile-note-jump"
              onClick={() => {
                panel.current?.querySelector("#personal-note")?.focus();
              }}
            >
              <MessageSquare size={18} />
            </IconButton>
            <span className="v-divider" />
            <IconButton title="Close (Esc)" onClick={onClose}>
              <X size={21} />
            </IconButton>
          </div>
        </header>
        <div className="detail-columns">
          <div className="detail-content" ref={body}>
            <div className="detail-intro">
              <div className="detail-badges">
                <Severity value={severityOf(f)} />
                <span className={"audit-status " + f.status}>
                  {f.status === "confirmed" && <Check size={13} />}{" "}
                  {AUDIT[f.status]}
                </span>
                {f.kind === "program" && (
                  <span className="audit-status">Companion program</span>
                )}
              </div>
              <h2 id="detail-title">{f.title}</h2>
              <p className="detail-target">{f.target}</p>
            </div>
            <div className="tabs" role="tablist" aria-label="Finding evidence">
              {[
                ["explanation", "Explanation", FileText],
                ["page", "Book page", BookOpen],
                ["evidence", "Evidence", FlaskConical],
              ].map(([key, label, Icon]) => (
                <button
                  key={key}
                  role="tab"
                  aria-selected={tab === key}
                  className={tab === key ? "selected" : ""}
                  onClick={() => {
                    setTab(key);
                    setDoc(null);
                  }}
                >
                  <Icon size={16} />
                  {label}
                  {key === "evidence" && <small>{f.evidence.length}</small>}
                </button>
              ))}
            </div>
            <div className="tab-content">
              {doc ? (
                <DocumentView
                  findingId={f.id}
                  path={doc}
                  onDocument={setDoc}
                  onBack={() => setDoc(null)}
                />
              ) : tab === "explanation" ? (
                <>
                  <div className={"impact-box " + severityOf(f)}>
                    <span className="eyebrow">WHY THIS NEEDS REVIEW</span>
                    <p>{f.impact || SEVERITY[severityOf(f)].hint}</p>
                  </div>
                  <h3 className="section-label">What the audit found</h3>
                  <p className="finding-summary">{f.summary}</p>
                  {f.publication_review ? <div className="publication-review">
                    <h3 className="section-label">Publication review · November 12, 2026</h3>
                    <p>{f.publication_review.reason}</p>
                    <p className="muted">{f.publication_review.decision === "retained"
                      ? "Correctness retained. No matching prior report found in the checked sources; absolute priority is not established."
                      : f.publication_review.decision === "candidate"
                        ? "Returned to candidate status after review."
                        : "The earlier confirmed assessment was withdrawn after review."}</p>
                    <button className="text-button" onClick={() => setDoc(f.publication_review.evidence)}>Read review record <ArrowRight size={15}/></button>
                  </div> : f.imported && <p className="import-note">Imported from the volume audit. This candidate or dismissed entry was outside the confirmed-card publication review.</p>}
                  {f.novelty === "previously_publicly_discussed" && <p className="import-note">Previously discussed publicly; this is not a claim of a new discovery.</p>}
                  <div className="verification-route">
                    <span className="route-number">01</span>
                    <div>
                      <b>Check the original wording</b>
                      <p>Read the typeset page and check the assumptions.</p>
                      <button
                        className="text-button"
                        onClick={() => setTab("page")}
                      >
                        View page <ArrowRight size={15} />
                      </button>
                    </div>
                  </div>
                  <div className="verification-route">
                    <span className="route-number">02</span>
                    <div>
                      <b>Follow the argument and reproduce it</b>
                      <p>
                        The original audit notes include counterexamples,
                        verification scope, and errata checks.
                      </p>
                      {docs.length ? (
                        <button
                          className="text-button"
                          onClick={() => setDoc(docs[0].path)}
                        >
                          Read original audit notes <ArrowRight size={15} />
                        </button>
                      ) : (
                        <button
                          className="text-button"
                          onClick={() => setTab("evidence")}
                        >
                          Open evidence <ArrowRight size={15} />
                        </button>
                      )}
                    </div>
                  </div>
                  <div className="verification-route">
                    <span className="route-number">03</span>
                    <div>
                      <b>Record your own conclusion</b>
                      <p>
                        Your verdict and notes are recorded separately from the
                        audit conclusion.
                      </p>
                    </div>
                  </div>
                  <p className="evidence-caveat">
                    <CircleHelp size={16} />
                    <span>
                      “Audit supported” refers to our evidence. Knuth has not
                      confirmed the finding. Prior-publication checks have the
                      limitations recorded above. A
                      physical copy has not yet been checked.
                    </span>
                  </p>
                </>
              ) : tab === "page" ? (
                <>
                  {images.length ? (
                    <>
                      <div className="image-toolbar">
                        <select
                          aria-label="Select page"
                          value={imageIndex}
                          onChange={(e) => {
                            setImageIndex(+e.target.value);
                            setZoom(false);
                          }}
                        >
                          {images.map((im, i) => (
                            <option key={im.path} value={i}>
                              {im.name.includes("vol4b")
                                ? "Book · "
                                : im.name.includes("fasc")
                                  ? "Author’s PS · "
                                  : ""}
                              {im.name}
                            </option>
                          ))}
                        </select>
                        <IconButton
                          title={zoom ? "Zoom out" : "Zoom in"}
                          active={zoom}
                          onClick={() => setZoom(!zoom)}
                        >
                          {zoom ? <ZoomOut size={17} /> : <ZoomIn size={17} />}
                        </IconButton>
                        <a
                          className="icon-button"
                          href={fileUrl(img.path)}
                          target="_blank"
                          rel="noreferrer"
                          aria-label="Open image in a new tab"
                        >
                          <ExternalLink size={17} />
                        </a>
                      </div>
                      <div className={"page-image " + (zoom ? "zoomed" : "")}>
                        <img
                          src={fileUrl(img.path)}
                          alt={"Original typesetting: " + img.name}
                        />
                      </div>
                    </>
                  ) : (
                    <Empty title="No page image is attached">
                      Open the book file or the attached source evidence.
                    </Empty>
                  )}
                  {f.book_available === false && <p className="muted">The book is not included. Use the argument, source references and any attached excerpt; you can add your own copy locally as described in the README.</p>}
                  {f.book_available !== false && f.book_format === "djvu" && <p className="book-download">
                    <a href={fileUrl(f.book_path)} download><Download size={15} /> Download Volume {f.volume_label} (DjVu)</a>
                    <span>Use the attached page images in this browser. Printed pages and file pages differ.</span>
                  </p>}
                  {f.book_available !== false && f.book_format === "pdf" && f.page_offset !== null && f.pages.length > 0 && (
                    <div className="pdf-links">
                      {f.pages.map((p) => (
                        <a
                          key={p}
                          href={fileUrl(f.book_path) + `#page=${p + f.page_offset}`}
                          target="_blank"
                          rel="noreferrer"
                        >
                          <BookOpen size={15} /> PDF · page {p}
                          <ArrowUpRight size={15} />
                        </a>
                      ))}
                    </div>
                  )}
                </>
              ) : (
                <>
                  <p className="muted">
                    Original audit sources, preserved in their original
                    language. Some notes are in Czech; checker output is in the
                    result files.
                  </p>
                  <div className="evidence-list">
                    {f.evidence.map((e) => (
                      <button
                        key={e.path}
                        onClick={() => {
                          if (e.kind === "image") {
                            setTab("page");
                            setImageIndex(
                              images.findIndex((x) => x.path === e.path),
                            );
                          } else if (
                            ["document", "code", "data"].includes(e.kind) &&
                            /\.(md|txt|json|py|cpp|c|w|log)$/.test(e.name)
                          ) {
                            setDoc(e.path);
                          } else
                            window.open(fileUrl(e.path), "_blank", "noopener");
                        }}
                      >
                        <span className={"file-icon " + e.kind}>
                          {e.kind === "image" ? (
                            <Image size={19} />
                          ) : e.kind === "code" ? (
                            <Code2 size={19} />
                          ) : (
                            <FileText size={19} />
                          )}
                        </span>
                        <span>
                          <b>{e.name}</b>
                          <small>
                            {e.kind === "document"
                              ? "Original audit notes (Czech)"
                              : e.kind === "image"
                                ? "Original page"
                                : e.kind === "code"
                                  ? "Verification program"
                                  : "Source"}{" "}
                            ·{" "}
                            {e.bytes > 1e6
                              ? (e.bytes / 1e6).toFixed(1) + " MB"
                              : Math.max(1, Math.round(e.bytes / 1024)) + " kB"}
                          </small>
                        </span>
                        <ChevronRight size={17} />
                      </button>
                    ))}
                  </div>
                </>
              )}
            </div>
          </div>
          <aside className="notes-panel">
            <div className="notes-title">
              <MessageSquare size={19} />
              <h3>My review</h3>
            </div>
            <p className="muted">Space for your own assessment.</p>
            <label className="field-label" htmlFor="review-verdict">
              My verdict
            </label>
            <select
              id="review-verdict"
              className={"verdict " + a.review}
              value={a.review}
              onChange={(e) => onChange(f.id, { review: e.target.value })}
            >
              {Object.entries(REVIEW).map(([k, v]) => (
                <option key={k} value={k}>
                  {v}
                </option>
              ))}
            </select>
            <div className="note-label">
              <label className="field-label" htmlFor="personal-note">
                Note
              </label>
              <span className={"save-status " + (save || "saved")}>
                {["pending", "saving"].includes(save) ? (
                  <>
                    <LoaderCircle size={11} className="spin" /> Saving
                  </>
                ) : ["error", "local-error"].includes(save) ? (
                  "Not saved"
                ) : save === "conflict" ? (
                  "Conflicting changes"
                ) : (
                  <>
                    <Check size={12} /> Saved
                  </>
                )}
              </span>
            </div>
            <textarea
              id="personal-note"
              placeholder="Your counterexample, calculation, or question…"
              value={a.note}
              maxLength={100000}
              onChange={(e) => onChange(f.id, { note: e.target.value })}
              onBlur={() => onFlush(f.id)}
            />
            {["error", "conflict", "local-error"].includes(save) && (
              <div className="save-error">
                <p>
                  {save === "conflict"
                    ? "This note changed in another window. Your draft is still here."
                    : "Saving to disk failed. Keep this window open to preserve your draft."}
                </p>
                <button onClick={() => onRetry(f.id)}>
                  {save === "conflict" ? "Save this version" : "Retry saving"}
                </button>
              </div>
            )}
            <span className="note-help">
              Notes are saved automatically on this computer.
            </span>
            <div className="notes-separator" />
            <label className="field-label" htmlFor="personal-severity">
              My severity rating
            </label>
            <select
              id="personal-severity"
              value={a.severity || ""}
              onChange={(e) =>
                onChange(f.id, { severity: e.target.value || null })
              }
            >
              <option value="">
                Audit rating · {SEVERITY[f.severity].label}
              </option>
              {Object.entries(SEVERITY).map(([k, v]) => (
                <option key={k} value={k}>
                  {v.label}
                </option>
              ))}
            </select>
            <p className="small-muted">
              A provisional impact rating. You can reset it at any time.
            </p>
            <button
              className={"bookmark-button " + (a.starred ? "active" : "")}
              onClick={() => onChange(f.id, { starred: !a.starred })}
            >
              <Star size={16} fill={a.starred ? "currentColor" : "none"} />
              {a.starred ? "Bookmarked" : "Bookmark for later"}
            </button>
            <div className="note-bottom">
              <LibraryBig size={24} />
              <span>
                TAOCP · {f.volume_label}<small>{f.edition}</small>
              </span>
            </div>
          </aside>
        </div>
      </section>
    </div>
  );
}

function Research({ data }) {
  return (
    <div className="research-view">
      <div className="research-intro">
        <span className="eyebrow">
          RELATED WORK · {data?.checked_at || "November 1, 2026"}
        </span>
        <h2>Has anyone done this before?</h2>
        <p>{data?.conclusion || "Loading related work…"}</p>
      </div>
      <div className="research-grid">
        {data?.sources?.map((s, i) => (
          <article className="research-card" key={s.url}>
            <div className="research-card-top">
              <span className="research-number">0{i + 1}</span>
              <span className="research-type">{s.category}</span>
            </div>
            <h3>{s.title}</h3>
            <span className="research-author">
              {s.author} · {s.date}
            </span>
            <p>{s.summary}</p>
            <div className="research-relevance">
              <b>Relevance to this audit</b>
              <p>{s.relevance}</p>
            </div>
            <a href={s.url} target="_blank" rel="noreferrer">
              Open original source <ArrowUpRight size={16} />
            </a>
          </article>
        ))}
      </div>
      <p className="research-limit">
        <CircleHelp size={17} />
        {data?.limitation}
      </p>
    </div>
  );
}

function VolumeProgress({data, findings, onOpen, onFindings}) {
  if (!data) return <div className="loading-line">Loading volume coverage…</div>;
  return <section className="volume-progress-view">
    <div className="page-heading"><div>
      <div className="eyebrow">LIBRARY · {data.status === "active" ? "AUDIT ACTIVE" : "AUDIT RECORD"}</div>
      <h1>Every volume, one record.</h1>
      <p>Mathematics and facts first. Page coverage, findings, and the work still open.</p>
    </div></div>
    <p className="coverage-method">{data.methodology}</p>
    <PageAtlas volumes={data.volumes} findings={findings} onOpen={onOpen} />
    <div className="volume-progress-grid">
      {data.volumes.map((v) => {
        const m=v.page_map;
        return <article className="volume-progress-card" key={v.id} data-volume={v.id}>
          <header><span className="volume-icon">{v.label}</span><div><h2>{v.title}</h2><p>{v.edition}</p></div>
            <span className="volume-state">{{not_started:"Not started",active:"In progress",follow_up:"Open checks",queued:"Queued",paused:"Paused",reviewed:"Reviewed",not_reviewed:"Not reviewed"}[v.audit_status] || v.audit_status}</span></header>
          <div className="coverage-number"><strong>{count(m.counts.reviewed || 0)} <span>/ {count(m.total)}</span></strong><b>{Math.round(100*(m.counts.reviewed || 0)/m.total)}%</b></div>
          <p className="coverage-caption">file pages reviewed under the agreed scope</p>
          <div className="coverage-track" aria-label={`${m.counts.reviewed || 0} reviewed, ${m.counts.not_reviewed || 0} not reviewed`}>
            <i style={{width:`${(m.counts.reviewed || 0)/m.total*100}%`}}/>
          </div>
          <div className="coverage-legend"><span>{count(m.counts.reviewed || 0)} reviewed</span><span>{count(m.counts.not_reviewed || 0)} not reviewed</span></div>
          <p className="coverage-footnote">{v.review_summary || "The page map records the completed scope. Remaining pages are not reviewed."}</p>
          <div className="volume-findings-count"><span>{v.ledger_counts.confirmed || 0} audit supported</span><span>{v.ledger_counts.candidate || 0} candidates</span></div>
          {v.review_remaining && <p className="coverage-footnote">{v.review_remaining}</p>}
          {v.review_evidence && <a href={fileUrl(v.review_evidence)} target="_blank" rel="noreferrer">Review scope and exceptions <ExternalLink size={14}/></a>}
          <footer><button onClick={() => onFindings(v.id)}>Review findings <ArrowRight size={15}/></button>{v.book_available !== false ? <a href={fileUrl(v.book_path)} target="_blank" rel="noreferrer">Open book <ExternalLink size={14}/></a> : <span className="muted">Book not included</span>}</footer>
        </article>;
      })}
    </div>
  </section>;
}

function App() {
  const [data, setData] = useState(null),
    [error, setError] = useState(""),
    [research, setResearch] = useState(null),
    [refreshing, setRefreshing] = useState(false);
  const [nav, setNav] = useState("all"),
    [query, setQuery] = useState(""),
    [severity, setSeverity] = useState("all"),
    [audit, setAudit] = useState("confirmed"),
    [chapter, setChapter] = useState("all"),
    [volume, setVolume] = useState("all"),
    [sort, setSort] = useState("severity");
  const [mode, setMode] = useState(() => safeParse("knuth-view", "grid")),
    [focusIndex, setFocusIndex] = useState(0),
    [selected, setSelected] = useState(() => location.hash.slice(1)),
    [help, setHelp] = useState(false),
    [mobileNav, setMobileNav] = useState(false);
  const input = useRef(),
    touch = useRef(),
    helpRef = useRef(),
    notes = useAnnotations();
  useEffect(() => {
    if (!help) return;
    const previous = document.activeElement;
    document.body.style.overflow = "hidden";
    helpRef.current?.querySelector("button")?.focus();
    return () => {
      document.body.style.overflow = "";
      previous?.focus();
    };
  }, [help]);
  const currentRef = useRef({});
  async function refresh() {
    setRefreshing(true);
    try {
      const r = await fetch("/api/findings");
      if (!r.ok) throw new Error("Could not load the audit data.");
      const d = await r.json();
      notes.ingest(d.findings);
      setData(d);
      setError("");
    } catch (e) {
      setError(e.message);
    } finally {
      setRefreshing(false);
    }
  }
  useEffect(() => {
    refresh();
    fetch("/api/research")
      .then((r) => r.json())
      .then(setResearch)
      .catch(() => {});
    const timer = setInterval(() => refresh(), 60000);
    const hash = () => setSelected(location.hash.slice(1));
    window.addEventListener("hashchange", hash);
    return () => {
      clearInterval(timer);
      window.removeEventListener("hashchange", hash);
    };
  }, []);
  function open(id) {
    location.hash = id;
    setSelected(id);
  }
  function close() {
    history.replaceState(null, "", location.pathname + location.search);
    setSelected("");
  }
  const findings = useMemo(
    () =>
      (data?.findings || []).map((f) => ({
        ...f,
        annotation: notes.values[f.id] || f.annotation,
      })),
    [data, notes.values],
  );
  const filtered = useMemo(() => {
    const q = normalize(query);
    const list = findings.filter(
      (f) =>
        (volume === "all" || f.volume === volume) &&
        (audit === "all" || f.status === audit) &&
        (severity === "all" || severityOf(f) === severity) &&
        (chapter === "all" || f.chapter === chapter) &&
        (!q ||
          normalize(
            [f.id, f.title, f.summary, f.target, f.annotation.note].join(" "),
          ).includes(q)) &&
        (nav !== "pending" || f.annotation.review === "pending") &&
        (nav !== "notes" || f.annotation.note.trim()) &&
        (nav !== "starred" || f.annotation.starred),
    );
    return list.sort((a, b) =>
      sort === "page"
        ? (a.pages[0] ?? 9999) - (b.pages[0] ?? 9999) ||
          a.id.localeCompare(b.id)
        : sort === "newest"
          ? (b.updated_at || "").localeCompare(a.updated_at || "")
          : sort === "id"
            ? a.id.localeCompare(b.id)
            : Object.keys(SEVERITY).indexOf(severityOf(a)) -
                Object.keys(SEVERITY).indexOf(severityOf(b)) ||
              a.id.localeCompare(b.id),
    );
  }, [findings, volume, audit, severity, chapter, query, nav, sort]);
  const selectedFinding = findings.find((f) => f.id === selected),
    selectedIndex = filtered.findIndex((f) => f.id === selected);
  function next(delta) {
    if (!filtered.length) return;
    if (selected) {
      const idx =
        selectedIndex < 0
          ? 0
          : (selectedIndex + delta + filtered.length) % filtered.length;
      open(filtered[idx].id);
    } else
      setFocusIndex((i) => (i + delta + filtered.length) % filtered.length);
  }
  currentRef.current = { next, selected, mode, close, help };
  useEffect(() => {
    const handler = (e) => {
      if (e.key === "Escape") {
        if (currentRef.current.help) setHelp(false);
        else currentRef.current.close();
        return;
      }
      if (e.target.closest('input,textarea,select,[contenteditable="true"]'))
        return;
      if (
        e.key === "/" &&
        !currentRef.current.selected &&
        !currentRef.current.help
      ) {
        e.preventDefault();
        input.current?.focus();
      }
      if (e.key === "?" && !currentRef.current.selected) setHelp((x) => !x);
      if (
        ["ArrowRight", "j", "ArrowLeft", "k"].includes(e.key) &&
        !currentRef.current.help &&
        (currentRef.current.selected || currentRef.current.mode === "focus")
      ) {
        e.preventDefault();
        currentRef.current.next(["ArrowRight", "j"].includes(e.key) ? 1 : -1);
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, []);
  useEffect(() => {
    setFocusIndex(0);
  }, [query, severity, audit, chapter, nav, sort, volume]);
  useEffect(() => {
    localStorage.setItem("knuth-view", JSON.stringify(mode));
  }, [mode]);
  function navigate(value) {
    setNav(value);
    setMobileNav(false);
    close();
    if (["notes", "starred"].includes(value)) setAudit("all");
    else if (value === "pending") setAudit("confirmed");
    window.scrollTo(0, 0);
  }
  const volumeFindings = findings.filter((f) => volume === "all" || f.volume === volume);
  const activeVolume = data?.volumes?.find((v) => v.id === volume);
  const volumeLabel = activeVolume ? `Volume ${activeVolume.label}` : "All volumes";
  const chapters = [...new Set(volumeFindings.map((f) => f.chapter))].sort();
  const confirmed = volumeFindings.filter((f) => f.status === "confirmed"),
    verified = confirmed.filter(
      (f) => f.annotation.review === "verified",
    ).length;
  const counts = Object.fromEntries(
    Object.keys(SEVERITY).map((s) => [
      s,
      confirmed.filter((f) => severityOf(f) === s).length,
    ]),
  );
  const navItems = [
    [
      "all",
      "All findings",
      Layers3,
      confirmed.length,
    ],
    [
      "pending",
      "Awaiting review",
      Clock3,
      confirmed.filter((f) => f.annotation.review === "pending").length,
    ],
    [
      "starred",
      "Bookmarks",
      Star,
      volumeFindings.filter((f) => f.annotation.starred).length,
    ],
    [
      "notes",
      "My notes",
      MessageSquare,
      volumeFindings.filter((f) => f.annotation.note.trim()).length,
    ],
  ];
  const activeFilters =
    severity !== "all" || chapter !== "all" || audit !== "confirmed" || query;
  if (!data) {
    return <main className="loading-line" role="status" aria-live="polite">
      {error ? <><AlertCircle size={22} /> {error} <button onClick={refresh}>Try again</button></>
        : <><LoaderCircle size={22} className="spin" /> Loading findings…</>}
    </main>;
  }
  return (
    <>
      <div className="app-layout" inert={!!(selectedFinding || help)}>
        {mobileNav && (
          <div className="nav-shade" onClick={() => setMobileNav(false)} />
        )}
        <aside className={"sidebar " + (mobileNav ? "open" : "")}>
          <a
            className="brand"
            href="#"
            onClick={(e) => {
              e.preventDefault();
              navigate("all");
            }}
          >
            <div className="brand-mark">
              <BookOpen size={25} />
            </div>
            <span>
              knuth<span className="brand-dot">.</span>
              <small>REVIEW NOTEBOOK</small>
            </span>
          </a>
          <div className="workspace">
            <div className="volume-icon">{activeVolume?.label || "ALL"}</div>
            <div>
              <b>
                The Art of Computer
                <br />
                Programming
              </b>
              <small>{activeVolume?.title || "Seven volumes and fascicles"}</small>
            </div>
          </div>
          <label className="volume-selector">VOLUME
            <select aria-label="Volume" value={volume} onChange={(e) => {setVolume(e.target.value); setChapter("all"); setFocusIndex(0);}}>
              <option value="all">All volumes</option>
              {data?.volumes?.map((v) => <option value={v.id} key={v.id}>Volume {v.label}</option>)}
            </select>
          </label>
          <div className="nav-label">PERSONAL REVIEW</div>
          <nav>
            {navItems.map(([key, label, Icon, n]) => (
              <button
                key={key}
                className={nav === key ? "selected" : ""}
                onClick={() => navigate(key)}
              >
                <Icon size={18} />
                <span>{label}</span>
                <small>{n}</small>
              </button>
            ))}
          </nav>
          <div className="nav-label severity-nav-label">
            SEVERITY{" "}
            <button
              title="About severity ratings"
              onClick={() => setHelp(true)}
            >
              <CircleHelp size={14} />
            </button>
          </div>
          <div className="severity-nav">
            {Object.entries(SEVERITY)
              .filter(([k]) => k !== "unclassified")
              .map(([key, s]) => (
                <button
                  key={key}
                  className={
                    severity === key && !(["research", "progress"].includes(nav)) ? "selected" : ""
                  }
                  onClick={() => {
                    if (["research", "progress"].includes(nav)) navigate("all");
                    setSeverity(severity === key ? "all" : key);
                    setMobileNav(false);
                  }}
                >
                  <i className={"severity-dot " + key} />
                  <span>{s.label}</span>
                  <small>{counts[key]}</small>
                </button>
              ))}
          </div>
          <div className="sidebar-rule" />
          <nav>
            <button className={nav === "progress" ? "selected" : ""} onClick={() => navigate("progress")}>
              <LibraryBig size={18} /><span>Volume progress</span>
            </button>
            <button
              className={nav === "research" ? "selected" : ""}
              onClick={() => navigate("research")}
            >
              <Globe2 size={18} />
              <span>Related projects</span>
              <ArrowUpRight size={15} />
            </button>
          </nav>
          <div className="sidebar-bottom">
            <div className="personal-progress">
              <div>
                <span>My review</span>
                <b>
                  {verified}
                  <span> / {confirmed.length}</span>
                </b>
              </div>
              <div className="progress-track">
                <i
                  style={{
                    width: confirmed.length
                      ? `${(verified / confirmed.length) * 100}%`
                      : 0,
                  }}
                />
              </div>
              <p>Your personal review progress</p>
            </div>
            <div className="local-status">
              <i /> Private local notebook
            </div>
          </div>
        </aside>
        <main className="main">
          <header className="topbar">
            <div>
              <IconButton
                title="Open navigation"
                className="mobile-menu icon-button"
                onClick={() => setMobileNav(true)}
              >
                <Menu size={20} />
              </IconButton>
              <span className="breadcrumb-root">Library</span>
              <ChevronRight size={14} />
              <span>TAOCP · {volumeLabel}</span>
              <span className="topbar-pill">Local audit</span>
            </div>
            <div>
              <IconButton
                title="Refresh audit data"
                onClick={refresh}
                disabled={refreshing}
              >
                <RefreshCw size={16} className={refreshing ? "spin" : ""} />
              </IconButton>
              <a className="export-button" href="/api/export">
                <Download size={15} />
                <span>Export notes</span>
              </a>
              <span className="avatar" title="Personal review notebook">
                V
              </span>
            </div>
          </header>
          <div className="main-inner">
            {nav === "research" ? (
              <Research data={research} />
            ) : nav === "progress" ? (
              <VolumeProgress data={data?.progress} findings={findings} onOpen={open} onFindings={(id) => {setVolume(id); setChapter("all"); setSeverity("all"); setAudit("confirmed"); setQuery(""); navigate("all");}} />
            ) : (
              <>
                <div className="page-heading">
                  <div>
                    <div className="eyebrow">
                      <span className="eyebrow-line" /> INDEPENDENT REVIEW ·
                      {volumeLabel.toUpperCase()}
                    </div>
                    <h1>
                      {nav === "notes"
                        ? "Your notes."
                        : nav === "starred"
                          ? "Saved for later."
                          : nav === "pending"
                            ? "Ready for review."
                            : "Findings under review."}
                    </h1>
                    <p>
                      {nav === "notes"
                        ? "Your calculations, questions, and conclusions in one place."
                        : "From claim to proof. Choose a finding, examine the evidence, and add your conclusion."}
                    </p>
                  </div>
                  <div className="heading-illustration" aria-hidden="true">
                    <span>TAOCP</span>
                    <b>{activeVolume?.label || "1–4B"}</b>
                    <i>notes & proofs</i>
                  </div>
                </div>
                <div className="summary-strip">
                  <div className="summary-main">
                    <strong>{count(confirmed.length)}</strong>
                    <span>
                      audit-supported findings
                      <small>
                        {volumeLabel} · book, errata and companion sources
                      </small>
                    </span>
                  </div>
                  <button
                    className={severity === "critical" ? "selected" : ""}
                    onClick={() =>
                      setSeverity(severity === "critical" ? "all" : "critical")
                    }
                  >
                    <span className="severity-dot critical" />
                    <strong>{counts.critical}</strong>
                    <span>critical</span>
                    <ArrowUpRight size={15} />
                  </button>
                  <button
                    className={severity === "high" ? "selected" : ""}
                    onClick={() =>
                      setSeverity(severity === "high" ? "all" : "high")
                    }
                  >
                    <span className="severity-dot high" />
                    <strong>{counts.high}</strong>
                    <span>high impact</span>
                    <ArrowUpRight size={15} />
                  </button>
                  <div className="summary-reviewed">
                    <CheckCheck size={21} />
                    <strong>{verified}</strong>
                    <span>verified by you</span>
                  </div>
                </div>
                {activeVolume?.page_map && <div className="selected-volume-map"><PageLegend /><PageStrip key={activeVolume.id} volume={activeVolume} findings={findings} onOpen={open} /></div>}
                <div className="review-intro">
                  <span>
                    <span className="mini-dot" /> Findings are sorted by their
                    impact on correctness.
                  </span>
                  <button onClick={() => setHelp(true)}>
                    Understanding the ratings <CircleHelp size={14} />
                  </button>
                </div>
                <section className="findings-section">
                  <div className="filter-bar">
                    <label className="search">
                      <Search size={18} />
                      <input
                        ref={input}
                        aria-label="Search findings"
                        placeholder="Search findings, exercises, or notes…"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                      />
                      {query ? (
                        <IconButton
                          title="Clear search"
                          onClick={() => setQuery("")}
                        >
                          <X size={15} />
                        </IconButton>
                      ) : (
                        <kbd>/</kbd>
                      )}
                    </label>
                    <select
                      aria-label="Book section"
                      value={chapter}
                      onChange={(e) => setChapter(e.target.value)}
                    >
                      <option value="all">All sections</option>
                      {chapters.map((k) => (
                        <option key={k} value={k}>{CHAPTER[k] || k}</option>
                      ))}
                    </select>
                    <select
                      aria-label="Audit status"
                      value={audit}
                      onChange={(e) => setAudit(e.target.value)}
                    >
                      <option value="all">All audit statuses</option>
                      {Object.entries(AUDIT).map(([k, v]) => (
                        <option key={k} value={k}>
                          {v}
                        </option>
                      ))}
                    </select>
                  </div>
                  <div className="results-toolbar">
                    <div className="results-count">
                      <b>{filtered.length}</b>{" "}
                      {filtered.length === 1 ? "finding" : "findings"}
                      {severity !== "all" && (
                        <button
                          className="filter-chip"
                          onClick={() => setSeverity("all")}
                        >
                          {SEVERITY[severity].label}
                          <X size={12} />
                        </button>
                      )}
                      {activeFilters && (
                        <button
                          className="reset-filters"
                          onClick={() => {
                            setSeverity("all");
                            setChapter("all");
                            setAudit("confirmed");
                            setQuery("");
                          }}
                        >
                          Clear filters
                        </button>
                      )}
                    </div>
                    <div className="view-controls">
                      <label className="sort-label">
                        Sort{" "}
                        <select
                          aria-label="Sort order"
                          value={sort}
                          onChange={(e) => setSort(e.target.value)}
                        >
                          <option value="severity">By severity</option>
                          <option value="page">By page</option>
                          <option value="newest">Newest first</option>
                          <option value="id">By ID</option>
                        </select>
                      </label>
                      <div className="view-toggle" aria-label="View mode">
                        {[
                          ["grid", LayoutGrid, "Cards"],
                          ["list", List, "List"],
                          ["focus", PanelTop, "One at a time"],
                        ].map(([k, Icon, title]) => (
                          <IconButton
                            key={k}
                            title={title}
                            active={mode === k}
                            onClick={() => setMode(k)}
                          >
                            <Icon size={17} />
                          </IconButton>
                        ))}
                      </div>
                    </div>
                  </div>
                  {error && (
                    <div className="error-banner">
                      <AlertCircle size={18} />
                      {error}
                      <button onClick={refresh}>Try again</button>
                    </div>
                  )}
                  {!data ? (
                    <div className="loading-line">
                      <LoaderCircle size={22} className="spin" /> Loading
                      findings…
                    </div>
                  ) : filtered.length === 0 ? (
                    <Empty title="Nothing here yet">
                      {nav === "notes"
                        ? "Open a finding and add your first note."
                        : nav === "starred"
                          ? "Bookmark findings using the star button."
                          : "Try a different search or clear the filters."}
                    </Empty>
                  ) : mode === "focus" ? (
                    <div
                      className="focus-view"
                      onTouchStart={(e) => {
                        touch.current = [
                          e.touches[0].clientX,
                          e.touches[0].clientY,
                        ];
                      }}
                      onTouchEnd={(e) => {
                        if (!touch.current) return;
                        const dx =
                            e.changedTouches[0].clientX - touch.current[0],
                          dy = e.changedTouches[0].clientY - touch.current[1];
                        if (
                          Math.abs(dx) > 80 &&
                          Math.abs(dx) > Math.abs(dy) * 1.5
                        )
                          next(dx < 0 ? 1 : -1);
                        touch.current = null;
                      }}
                    >
                      <div className="focus-navigation">
                        <button onClick={() => next(-1)}>
                          <ArrowLeft size={18} /> Previous
                        </button>
                        <span>
                          {Math.min(focusIndex, filtered.length - 1) + 1}{" "}
                          <span>/ {filtered.length}</span>
                        </span>
                        <button onClick={() => next(1)}>
                          Next <ArrowRight size={18} />
                        </button>
                      </div>
                      <FindingCard
                        finding={
                          filtered[Math.min(focusIndex, filtered.length - 1)]
                        }
                        mode="focus"
                        onOpen={open}
                        onStar={(id, starred) => notes.change(id, { starred })}
                      />
                      <p className="focus-tip">
                        <Keyboard size={16} /> Browse with ← → or J / K. Click a
                        card to open it.
                      </p>
                    </div>
                  ) : (
                    <div className={"cards " + mode}>
                      {filtered.map((f, i) => (
                        <FindingCard
                          key={f.id}
                          finding={f}
                          index={i}
                          mode={mode}
                          onOpen={open}
                          onStar={(id, starred) =>
                            notes.change(id, { starred })
                          }
                        />
                      ))}
                    </div>
                  )}
                </section>
                <footer className="main-footer">
                  <span>
                    <BookOpen size={14} /> Digital copy · 1st edition, 2nd
                    printing (2022)
                  </span>
                  <button onClick={() => setHelp(true)}>
                    <Keyboard size={15} /> Keyboard shortcuts
                  </button>
                </footer>
              </>
            )}
          </div>
        </main>
      </div>
      {selectedFinding && (
        <ReviewPanel
          key="review"
          finding={selectedFinding}
          bookPath={selectedFinding.book_path}
          onClose={close}
          onNext={() => next(1)}
          onPrevious={() => next(-1)}
          position={selectedIndex + 1}
          total={filtered.length}
          save={notes.saving[selectedFinding.id]}
          onChange={notes.change}
          onRetry={notes.retry}
          onFlush={notes.flush}
        />
      )}
      {help && (
        <div
          className="help-backdrop"
          onClick={(e) => {
            if (e.target === e.currentTarget) setHelp(false);
          }}
        >
          <section
            className="help-dialog"
            ref={helpRef}
            onKeyDown={(e) => {
              if (e.key === "Tab") {
                e.preventDefault();
                helpRef.current?.querySelector("button")?.focus();
              }
            }}
            role="dialog"
            aria-modal="true"
            aria-label="Ratings and controls"
          >
            <IconButton title="Close help" onClick={() => setHelp(false)}>
              <X size={20} />
            </IconButton>
            <h2>Using this notebook</h2>
            <p>
              Severity describes the impact of an error. It does not measure
              confidence in a finding or promise a reward.
            </p>
            <div className="severity-legend">
              {Object.entries(SEVERITY)
                .filter(([k]) => k !== "unclassified")
                .map(([k, v]) => (
                  <div key={k}>
                    <Severity value={k} />
                    <span>{v.hint}</span>
                  </div>
                ))}
            </div>
            <p>
              “Audit supported” and “Verified by me” are independent statuses.
              You can change the severity rating on each card.
            </p>
            <p>
              Corrections already published in Knuth’s errata are excluded from
              findings, error counts, and page colors. The audit notes retain
              the record that these corrections were checked.
            </p>
            <h3>Quick navigation</h3>
            <div className="shortcuts">
              <span>
                <kbd>/</kbd> Search
              </span>
              <span>
                <kbd>←</kbd>
                <kbd>→</kbd> Previous / next finding
              </span>
              <span>
                <kbd>J</kbd>
                <kbd>K</kbd> Same action in detail or single-card view
              </span>
              <span>
                <kbd>Esc</kbd> Close detail
              </span>
            </div>
          </section>
        </div>
      )}
    </>
  );
}
createRoot(document.getElementById("root")).render(<App />);
