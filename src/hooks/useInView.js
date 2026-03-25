import { useEffect, useRef, useState } from 'react'

export function useInView({ threshold = 0.2, once = true } = {}) {
  const ref = useRef(null)
  const [isInView, setIsInView] = useState(false)

  useEffect(() => {
    if (!ref.current) return

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true)
          if (once) observer.disconnect()
        } else if (!once) {
          setIsInView(false)
        }
      },
      { threshold }
    )

    observer.observe(ref.current)
    return () => observer.disconnect()
  }, [threshold, once])

  return { ref, isInView }
}
