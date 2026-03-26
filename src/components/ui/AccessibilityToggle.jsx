import { useState, useEffect, useRef } from 'react'
import { useAccessibility } from '@/contexts/AccessibilityContext'

export function AccessibilityToggle() {
  const { highContrast, setHighContrast } = useAccessibility()
  const [visible, setVisible] = useState(true)
  const lastScrollY = useRef(0)
  const ticking = useRef(false)

  useEffect(() => {
    const onScroll = () => {
      if (ticking.current) return
      ticking.current = true
      requestAnimationFrame(() => {
        const y = window.scrollY
        if (y < 100) {
          // Always show near top
          setVisible(true)
        } else if (y < lastScrollY.current) {
          // Scrolling up → show
          setVisible(true)
        } else if (y > lastScrollY.current + 10) {
          // Scrolling down (with 10px deadzone) → hide
          setVisible(false)
        }
        lastScrollY.current = y
        ticking.current = false
      })
    }

    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  return (
    <button
      onClick={() => setHighContrast(prev => !prev)}
      aria-label={highContrast ? 'Switch to branded mode' : 'Switch to high contrast mode'}
      title={highContrast ? 'Branded mode' : 'High contrast mode'}
      style={{
        position: 'fixed',
        top: 20,
        right: 20,
        zIndex: 9999,
        display: 'flex',
        alignItems: 'center',
        gap: 8,
        padding: '8px 14px',
        borderRadius: 6,
        border: highContrast ? '1px solid #fff' : '1px solid rgba(122,168,184,0.3)',
        background: highContrast ? '#000' : 'rgba(13,43,53,0.85)',
        backdropFilter: 'blur(8px)',
        color: highContrast ? '#fff' : '#7AA8B8',
        fontFamily: "'IBM Plex Mono', monospace",
        fontSize: 10,
        letterSpacing: '0.08em',
        textTransform: 'uppercase',
        cursor: 'pointer',
        transition: 'all 0.3s ease, opacity 0.35s ease, transform 0.35s ease',
        opacity: visible ? 1 : 0,
        transform: visible ? 'translateY(0)' : 'translateY(-20px)',
        pointerEvents: visible ? 'auto' : 'none',
      }}
    >
      <svg
        width="14"
        height="14"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        {highContrast ? (
          <>
            <circle cx="12" cy="12" r="5" />
            <line x1="12" y1="1" x2="12" y2="3" />
            <line x1="12" y1="21" x2="12" y2="23" />
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" />
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" />
            <line x1="1" y1="12" x2="3" y2="12" />
            <line x1="21" y1="12" x2="23" y2="12" />
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" />
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" />
          </>
        ) : (
          <path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9z" />
        )}
      </svg>
      {highContrast ? 'Branded' : 'AccMode'}
    </button>
  )
}
