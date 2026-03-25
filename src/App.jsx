import { ScrollContainer } from '@/components/layout/ScrollContainer'
import { Hero } from '@/components/chapters/Hero'
import { Chapter1 } from '@/components/chapters/Chapter1'
import { Chapter2 } from '@/components/chapters/Chapter2'
import { Chapter3 } from '@/components/chapters/Chapter3'
import { Chapter4 } from '@/components/chapters/Chapter4'
import { Chapter5 } from '@/components/chapters/Chapter5'
import { Footer } from '@/components/chapters/Footer'

function App() {
  return (
    <ScrollContainer>
      <Hero />
      <Chapter1 />
      <Chapter2 />
      <Chapter3 />
      <Chapter4 />
      <Chapter5 />
      <Footer />
    </ScrollContainer>
  )
}

export default App
