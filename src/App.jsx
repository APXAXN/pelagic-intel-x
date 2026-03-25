import { lazy, Suspense } from 'react'
import { ScrollContainer } from '@/components/layout/ScrollContainer'
import { Hero } from '@/components/chapters/Hero'
import { Footer } from '@/components/chapters/Footer'

// Lazy-load heavy chapters to keep initial bundle lean
const Chapter1 = lazy(() => import('@/components/chapters/Chapter1').then(m => ({ default: m.Chapter1 })))
const Chapter2 = lazy(() => import('@/components/chapters/Chapter2').then(m => ({ default: m.Chapter2 })))
const Chapter3 = lazy(() => import('@/components/chapters/Chapter3').then(m => ({ default: m.Chapter3 })))
const Chapter4 = lazy(() => import('@/components/chapters/Chapter4').then(m => ({ default: m.Chapter4 })))
const Chapter5 = lazy(() => import('@/components/chapters/Chapter5').then(m => ({ default: m.Chapter5 })))

function ChapterFallback() {
  return <div className="min-h-screen" />
}

function App() {
  return (
    <ScrollContainer>
      <Hero />
      <Suspense fallback={<ChapterFallback />}>
        <Chapter1 />
      </Suspense>
      <Suspense fallback={<ChapterFallback />}>
        <Chapter2 />
      </Suspense>
      <Suspense fallback={<ChapterFallback />}>
        <Chapter3 />
      </Suspense>
      <Suspense fallback={<ChapterFallback />}>
        <Chapter4 />
      </Suspense>
      <Suspense fallback={<ChapterFallback />}>
        <Chapter5 />
      </Suspense>
      <Footer />
    </ScrollContainer>
  )
}

export default App
