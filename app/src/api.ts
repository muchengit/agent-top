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

export type SearchKind = 'Course' | 'Lesson' | 'Lab' | 'Search'

export type SearchResult = {
  kind: SearchKind
  title: string
  path: string
  summary: string
  language?: string
  level?: number | null
}

export type SearchFilter = {
  kind?: 'all' | SearchKind
  language?: 'all' | 'en' | 'zh'
}

export function searchAppData(data: AppData, query: string, filter: SearchFilter = {}): SearchResult[] {
  const q = query.trim().toLowerCase()
  if (!q) return []
  const matches: SearchResult[] = []
  const kindFilter = filter.kind ?? 'all'
  const languageFilter = filter.language ?? 'all'
  const includeKind = (kind: SearchKind) => kindFilter === 'all' || kindFilter === kind
  const includeLanguage = (language?: string) => languageFilter === 'all' || language === languageFilter

  for (const item of data.courses) {
    if (!includeKind('Course')) continue
    if ([item.title, item.summary, item.sourcePath].some((text) => text.toLowerCase().includes(q))) {
      matches.push({ kind: 'Course', title: item.title, path: item.sourcePath, summary: item.summary, level: item.level })
    }
  }
  for (const item of data.lessons) {
    if (!includeKind('Lesson')) continue
    if (!includeLanguage(item.language)) continue
    if ([item.title, item.summary, item.sourcePath].some((text) => text.toLowerCase().includes(q))) {
      matches.push({ kind: 'Lesson', title: item.title, path: item.sourcePath, summary: item.summary, language: item.language, level: item.level })
    }
  }
  for (const item of data.labs) {
    if (!includeKind('Lab')) continue
    if ([item.title, item.objective, item.sourcePath].some((text) => text.toLowerCase().includes(q))) {
      matches.push({ kind: 'Lab', title: item.title, path: item.sourcePath, summary: item.objective, level: item.level })
    }
  }
  for (const item of data.searchIndex) {
    if (!includeKind('Search')) continue
    if (!includeLanguage(item.language)) continue
    if ([item.title, item.summary, item.sourcePath].some((text) => text.toLowerCase().includes(q))) {
      matches.push({ kind: 'Search', title: item.title, path: item.sourcePath, summary: item.summary, language: item.language })
    }
  }
  return matches.slice(0, 50)
}
