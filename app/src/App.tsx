import { useState } from 'react'
import type { ReactNode } from 'react'

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

export default function App() {
  const [view, setView] = useState<View>('home')

  return (
    <Shell view={view} onNavigate={setView}>
      {view === 'home' && <Home />}
      {view === 'learn' && <Learn />}
      {view === 'practice' && <Practice />}
      {view === 'search' && <Search />}
      {view === 'progress' && <Progress />}
    </Shell>
  )
}

function Home() {
  return (
    <section className="panel">
      <h1>Agent-Top learning app</h1>
      <p>A local-first shell for courses, labs, search, and progress.</p>
      <ul>
        <li>L0-L5 learning path</li>
        <li>Bilingual content</li>
        <li>Local-first browsing</li>
      </ul>
    </section>
  )
}

function Learn() {
  return (
    <section className="panel">
      <h1>Learn</h1>
      <p>Course and lesson browsing will live here.</p>
    </section>
  )
}

function Practice() {
  return (
    <section className="panel">
      <h1>Practice</h1>
      <p>Lab workspace and submission drafts will live here.</p>
    </section>
  )
}

function Search() {
  return (
    <section className="panel">
      <h1>Search</h1>
      <p>Repository search will live here.</p>
    </section>
  )
}

function Progress() {
  return (
    <section className="panel">
      <h1>Progress</h1>
      <p>Local progress tracking will live here.</p>
    </section>
  )
}
