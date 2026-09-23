import { useEffect, useMemo, useState } from 'react'
import type { ReactNode } from 'react'
import { loadAppData, searchAppData } from './api'
import type { AppData, Course, Lab, Lesson } from './api'

type View = 'home' | 'learn' | 'practice' | 'search' | 'progress'

const nav: Array<{ id: View; label: string }> = [
  { id: 'home', label: 'Home' },
  { id: 'learn', label: 'Learn' },
  { id: 'practice', label: 'Practice' },
  { id: 'search', label: 'Search' },
  { id: 'progress', label: 'Progress' },
]

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
      {view === 'learn' && <Learn data={data} progress={progress} onToggle={toggleProgress} />} 
      {view === 'practice' && <Practice data={data} progress={progress} onToggle={toggleProgress} />} 
      {view === 'search' && (
        <Search data={data} query={query} onQueryChange={setQuery} />
      )}
      {view === 'progress' && <Progress data={data} progress={progress} completedCount={completedCount} />} 
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

function Learn({ data, progress, onToggle }: { data: AppData; progress: Record<string, boolean>; onToggle: (key: string) => void }) {
  const courses = [...data.courses].sort((a, b) => a.level - b.level)
  return (
    <Card title="Learn" subtitle="Course and lesson overview.">
      <ul>
        {courses.map((course: Course) => (
          <ItemRow key={course.id} title={course.title} meta={`L${course.level}`}>
            <input type="checkbox" checked={!!progress[`course:${course.id}`]} onChange={() => onToggle(`course:${course.id}`)} />
            {course.summary}
          </ItemRow>
        ))}
      </ul>
      <details>
        <summary>Lessons</summary>
        <ul>
          {data.lessons.slice(0, 20).map((lesson: Lesson) => (
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

function Practice({ data, progress, onToggle }: { data: AppData; progress: Record<string, boolean>; onToggle: (key: string) => void }) {
  return (
    <Card title="Practice" subtitle="Lab workspace overview.">
      <ul>
        {data.labs.slice(0, 20).map((lab: Lab) => (
          <ItemRow key={lab.id} title={lab.title} meta={lab.sourcePath}>
            <input type="checkbox" checked={!!progress[`lab:${lab.id}`]} onChange={() => onToggle(`lab:${lab.id}`)} />
            {lab.objective}
          </ItemRow>
        ))}
      </ul>
    </Card>
  )
}

function Search({ data, query, onQueryChange }: { data: AppData; query: string; onQueryChange: (value: string) => void }) {
  const results = searchAppData(data, query)
  return (
    <Card title="Search" subtitle="Search repository-derived app content.">
      <input
        type="search"
        value={query}
        onChange={(event) => onQueryChange(event.target.value)}
        placeholder="Search courses, lessons, labs..."
      />
      <ul>
        {results.map((item) => (
          <ItemRow key={`${item.kind}-${item.title}-${item.path}`} title={item.title} meta={`${item.kind} · ${item.path}`}>{item.summary}</ItemRow>
        ))}
      </ul>
    </Card>
  )
}

function Progress({ data, progress, completedCount }: { data: AppData; progress: Record<string, boolean>; completedCount: number }) {
  const total = data.lessons.length + data.labs.length
  return (
    <Card title="Progress" subtitle="Local progress tracking.">
      <p>{completedCount} of {total} items completed</p>
      <ul>
        <li>Progress persists in localStorage.</li>
        <li>Submission drafts will be added after course browsing is wired.</li>
      </ul>
    </Card>
  )
}
