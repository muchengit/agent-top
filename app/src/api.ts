export type Course = {
  id: string
  level: number
  title: string
  summary: string
  sourcePath: string
  lessonIds: string[]
}

export type Lesson = {
  id: string
  courseId: string
  level: number | null
  title: string
  language: string
  sourcePath: string
  summary: string
  relatedLabId?: string
  validatedDate?: string | null
}

export type Lab = {
  id: string
  title: string
  level: number | null
  sourcePath: string
  objective: string
  selfCheck: string[]
  testedAgainst?: string | null
  validatedDate?: string | null
}

export type SearchHit = {
  id: string
  title: string
  sourcePath: string
  category: string
  language: string
  summary: string
}

export type AppData = {
  courses: Course[]
  lessons: Lesson[]
  labs: Lab[]
  searchIndex: SearchHit[]
}

export async function fetchJson<T>(path: string): Promise<T> {
  const res = await fetch(path)
  if (!res.ok) throw new Error(`${path} -> ${res.status}`)
  return res.json() as Promise<T>
}

export async function loadAppData(): Promise<AppData> {
  const [courses, lessons, labs, searchIndex] = await Promise.all([
    fetchJson<Course[]>('/courses.json'),
    fetchJson<Lesson[]>('/lessons.json'),
    fetchJson<Lab[]>('/labs.json'),
    fetchJson<SearchHit[]>('/search-index.json'),
  ])
  return { courses, lessons, labs, searchIndex }
}

export function searchAppData(data: AppData, query: string): Array<{ kind: string; title: string; path: string; summary: string }> {
  const q = query.trim().toLowerCase()
  if (!q) return []
  const matches: Array<{ kind: string; title: string; path: string; summary: string }> = []
  for (const item of data.courses) {
    if ([item.title, item.summary, item.sourcePath].some((text) => text.toLowerCase().includes(q))) {
      matches.push({ kind: 'Course', title: item.title, path: item.sourcePath, summary: item.summary })
    }
  }
  for (const item of data.lessons) {
    if ([item.title, item.summary, item.sourcePath].some((text) => text.toLowerCase().includes(q))) {
      matches.push({ kind: 'Lesson', title: item.title, path: item.sourcePath, summary: item.summary })
    }
  }
  for (const item of data.labs) {
    if ([item.title, item.objective, item.sourcePath].some((text) => text.toLowerCase().includes(q))) {
      matches.push({ kind: 'Lab', title: item.title, path: item.sourcePath, summary: item.objective })
    }
  }
  for (const item of data.searchIndex) {
    if ([item.title, item.summary, item.sourcePath].some((text) => text.toLowerCase().includes(q))) {
      matches.push({ kind: 'Search', title: item.title, path: item.sourcePath, summary: item.summary })
    }
  }
  return matches.slice(0, 50)
}
