import { useEffect, useMemo, useState } from 'react'
import type { ReactNode } from 'react'
import { loadAppData, searchAppData } from './api'
import type { AppData, Course, Lab, Lesson, SearchFilter, SearchKind } from './api'

type View = 'home' | 'learn' | 'practice' | 'search' | 'progress'

const nav: Array<{ id: View; label: string }> = [
  { id: 'home', label: 'Home' },
  { id: 'learn', label: 'Learn' },
  { id: 'practice', label: 'Practice' },
  { id: 'search', label: 'Search' },
  { id: 'progress', label: 'Progress' },
]


function DetailCard({ title, meta, children }: { title: string; meta?: string; children?: ReactNode }) {
  return (
    <section className="detail-card">
      <h2>{title}</h2>
      {meta ? <p>{meta}</p> : null}
      {children}
    </section>
  )
}
function Shell({ view, onNavigate, children }: { view: View; onNavigate: (view: View) => void; children: ReactNode }) {
  return (
    <div className="shell">
      <header className="topbar">
        <div className="brand">Agent-Top</div>
        <nav>
          {nav.map((item) => (
            <button
              key={item.id}
              className={item.id === view ? 'active' : undefined}
              onClick={() => onNavigate(item.id)}
              type="button"
            >
              {item.label}
            </button>
          ))}
        </nav>
      </header>
      <main>{children}</main>
    </div>
  )
}

function Card({ title, subtitle, children }: { title: string; subtitle?: string; children?: ReactNode }) {
  return (
    <section className="panel">
      <h1>{title}</h1>
      {subtitle ? <p>{subtitle}</p> : null}
      {children}
    </section>
  )
}

function ItemRow({ title, meta, children }: { title: string; meta?: string; children?: ReactNode }) {
  return (
    <li className="row">
      <strong>{title}</strong>
      {meta ? <span>{meta}</span> : null}
      {children}
    </li>
  )
}

export default function App() {
  const [view, setView] = useState<View>('home')
  const [data, setData] = useState<AppData | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [query, setQuery] = useState('')
  const [searchFilter, setSearchFilter] = useState<SearchFilter>({ kind: 'all', language: 'all' })
  const [selectedCourseId, setSelectedCourseId] = useState<string | null>(null)
  const [selectedLabId, setSelectedLabId] = useState<string | null>(null)
  const [progress, setProgress] = useState<Record<string, boolean>>(() => {
    try {
      return JSON.parse(localStorage.getItem('agent-top-progress') ?? '{}') as Record<string, boolean>
    } catch {
      return {}
    }
  })

  useEffect(() => {
    loadAppData()
      .then(setData)
      .catch((err) => setError(err instanceof Error ? err.message : String(err)))
  }, [])

  useEffect(() => {
    localStorage.setItem('agent-top-progress', JSON.stringify(progress))
  }, [progress])

  const completedCount = useMemo(() => Object.values(progress).filter(Boolean).length, [progress])

  const toggleProgress = (key: string) => {
    setProgress((prev) => ({ ...prev, [key]: !prev[key] }))
  }

  const resetProgress = () => {
    setProgress({})
  }

  if (error) {
    return (
      <Card title="App content unavailable" subtitle="Could not load generated app content.">{error}</Card>
    )
  }

  if (!data) {
    return <Card title="Agent-Top learning app" subtitle="Loading generated content..." />
  }

  return (
    <Shell view={view} onNavigate={setView}>
      {view === 'home' && <Home data={data} />} 
      {view === 'learn' && <Learn data={data} progress={progress} onToggle={toggleProgress} selectedCourseId={selectedCourseId} onSelectCourse={setSelectedCourseId} />} 
      {view === 'practice' && <Practice data={data} progress={progress} onToggle={toggleProgress} selectedLabId={selectedLabId} onSelectLab={setSelectedLabId} />} 
      {view === 'search' && (
        <Search data={data} query={query} onQueryChange={setQuery} filter={searchFilter} onFilterChange={setSearchFilter} />
      )}
      {view === 'progress' && <Progress data={data} progress={progress} completedCount={completedCount} onReset={resetProgress} />}
    </Shell>
  )
}

function Home({ data }: { data: AppData }) {
  return (
    <Card
      title="Agent-Top learning app"
      subtitle={`Loaded ${data.courses.length} courses, ${data.lessons.length} lessons, and ${data.labs.length} labs.`}
    >
      <ul>
        <li>L0-L5 learning path</li>
        <li>Bilingual content</li>
        <li>Local-first browsing</li>
      </ul>
    </Card>
  )
}

function Learn({ data, progress, onToggle, selectedCourseId, onSelectCourse }: { data: AppData; progress: Record<string, boolean>; onToggle: (key: string) => void; selectedCourseId: string | null; onSelectCourse: (id: string | null) => void }) {
  const courses = [...data.courses].sort((a, b) => a.level - b.level)
  const selectedCourse = selectedCourseId ? data.courses.find((course) => course.id === selectedCourseId) ?? null : null
  const lessons = selectedCourse ? data.lessons.filter((lesson) => selectedCourse.lessonIds.includes(lesson.id)) : data.lessons.slice(0, 20)
  return (
    <Card title="Learn" subtitle="Course and lesson overview.">
      {selectedCourse ? <button type="button" className="link-button" onClick={() => onSelectCourse(null)}>Back to all lessons</button> : null}
      {selectedCourse ? <DetailCard title={selectedCourse.title} meta={`L${selectedCourse.level} · ${selectedCourse.sourcePath}`}>{selectedCourse.summary}</DetailCard> : null}
      <ul>
        {courses.map((course: Course) => (
          <ItemRow key={course.id} title={course.title} meta={"L" + course.level}>
            <button type="button" className={`pill ${course.id === selectedCourseId ? 'active' : ''}`} onClick={() => onSelectCourse(course.id === selectedCourseId ? null : course.id)}>Select</button>
            <input type="checkbox" checked={!!progress[`course:${course.id}`]} onChange={() => onToggle(`course:${course.id}`)} />
            {course.summary}
          </ItemRow>
        ))}
      </ul>
      <details open={!!selectedCourse}>
        <summary>Lessons</summary>
        <ul>
          {lessons.map((lesson: Lesson) => (
            <ItemRow key={lesson.id} title={lesson.title} meta={lesson.sourcePath}>
              <input type="checkbox" checked={!!progress[`lesson:${lesson.id}`]} onChange={() => onToggle(`lesson:${lesson.id}`)} />
              {lesson.summary}
            </ItemRow>
          ))}
        </ul>
      </details>
    </Card>
  )
}

function Practice({ data, progress, onToggle, selectedLabId, onSelectLab }: { data: AppData; progress: Record<string, boolean>; onToggle: (key: string) => void; selectedLabId: string | null; onSelectLab: (id: string | null) => void }) {
  const labs = data.labs.slice(0, 20)
  const selectedLab = selectedLabId ? data.labs.find((lab) => lab.id === selectedLabId) ?? null : null
  const [drafts, setDrafts] = useState<Record<string, string>>(() => {
    try {
      return JSON.parse(localStorage.getItem('agent-top-lab-drafts') ?? '{}') as Record<string, string>
    } catch {
      return {}
    }
  })

  useEffect(() => {
    localStorage.setItem('agent-top-lab-drafts', JSON.stringify(drafts))
  }, [drafts])

  const draftText = selectedLabId ? drafts[selectedLabId] ?? '' : ''
  return (
    <Card title="Practice" subtitle="Lab workspace overview.">
      {selectedLab ? <button type="button" className="link-button" onClick={() => onSelectLab(null)}>Back to all labs</button> : null}
      {selectedLab ? <DetailCard title={selectedLab.title} meta={`${selectedLab.sourcePath}${selectedLab.testedAgainst ? ` · ${selectedLab.testedAgainst}` : ''}`}>
        <p>{selectedLab.objective}</p>
        {selectedLab.selfCheck.length ? <ul>{selectedLab.selfCheck.map((check) => <li key={check}>{check}</li>)}</ul> : null}
        <label>
          Submission draft
          <textarea
            value={draftText}
            onChange={(event) => setDrafts((prev) => ({ ...prev, [selectedLab.id]: event.target.value }))}
            placeholder="Paste your submission, notes, or JSONL here."
            rows={6}
          />
        </label>
      </DetailCard> : null}
      <ul>
        {labs.map((lab: Lab) => (
          <ItemRow key={lab.id} title={lab.title} meta={lab.sourcePath}>
            <button type="button" className={`pill ${lab.id === selectedLabId ? 'active' : ''}`} onClick={() => onSelectLab(lab.id === selectedLabId ? null : lab.id)}>Select</button>
            <input type="checkbox" checked={!!progress[`lab:${lab.id}`]} onChange={() => onToggle(`lab:${lab.id}`)} />
            {lab.objective}
          </ItemRow>
        ))}
      </ul>
    </Card>
  )
}

function Search({ data, query, onQueryChange, filter, onFilterChange }: { data: AppData; query: string; onQueryChange: (value: string) => void; filter: SearchFilter; onFilterChange: (value: SearchFilter) => void }) {
  const results = searchAppData(data, query, filter)
  return (
    <Card title="Search" subtitle="Search repository-derived app content.">
      <div className="filters">
        <input
          type="search"
          value={query}
          onChange={(event) => onQueryChange(event.target.value)}
          placeholder="Search courses, lessons, labs..."
        />
        <select value={filter.kind ?? 'all'} onChange={(event) => onFilterChange({ ...filter, kind: event.target.value as 'all' | SearchKind })}>
          <option value="all">All types</option>
          <option value="Course">Courses</option>
          <option value="Lesson">Lessons</option>
          <option value="Lab">Labs</option>
          <option value="Search">Search index</option>
        </select>
        <select value={filter.language ?? 'all'} onChange={(event) => onFilterChange({ ...filter, language: event.target.value as 'all' | 'en' | 'zh' })}>
          <option value="all">All languages</option>
          <option value="en">English</option>
          <option value="zh">中文</option>
        </select>
      </div>
      <ul>
        {results.map((item) => (
          <ItemRow key={`${item.kind}-${item.title}-${item.path}`} title={item.title} meta={`${item.kind}${item.level !== undefined ? ` · L${item.level}` : ''} · ${item.path}`}>{item.summary}</ItemRow>
        ))}
      </ul>
    </Card>
  )
}

function Progress({ data, progress, completedCount, onReset }: { data: AppData; progress: Record<string, boolean>; completedCount: number; onReset: () => void }) {
  const total = data.lessons.length + data.labs.length
  const percentage = total === 0 ? 0 : Math.round((completedCount / total) * 100)
  return (
    <Card title="Progress" subtitle="Local progress tracking.">
      <p>{completedCount} of {total} items completed</p>
      <div className="progress-bar">
        <div className="progress-fill" style={{ width: `${percentage}%` }} />
      </div>
      <div className="filters">
        <button type="button" className="pill" onClick={onReset} disabled={completedCount === 0}>Reset progress</button>
      </div>
      <ul>
        <li>Progress persists in localStorage.</li>
        <li>Submission drafts will be added after course browsing is wired.</li>
      </ul>
    </Card>
  )
}
