import { useEffect, useRef, useState } from 'react'
import scrollama from 'scrollama'

export function useScrollama({ offset = 0.5, once = false } = {}) {
  const containerRef = useRef(null)
  const [activeIndex, setActiveIndex] = useState(-1)
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    if (!containerRef.current) return

    const scroller = scrollama()

    scroller
      .setup({
        step: containerRef.current.querySelectorAll('[data-step]'),
        offset,
        progress: true,
      })
      .onStepEnter(({ index }) => {
        setActiveIndex(index)
      })
      .onStepProgress(({ progress: p }) => {
        setProgress(p)
      })

    const handleResize = () => scroller.resize()
    window.addEventListener('resize', handleResize)

    return () => {
      scroller.destroy()
      window.removeEventListener('resize', handleResize)
    }
  }, [offset, once])

  return { containerRef, activeIndex, progress }
}
