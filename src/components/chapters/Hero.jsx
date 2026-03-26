import { motion } from 'framer-motion'
import { useEffect, useRef } from 'react'

function OceanScanAnimation() {
  const canvasRef = useRef(null)

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext('2d')
    let animationId
    let time = 0

    const resize = () => {
      canvas.width = canvas.offsetWidth * window.devicePixelRatio
      canvas.height = canvas.offsetHeight * window.devicePixelRatio
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio)
    }
    resize()
    window.addEventListener('resize', resize)

    const draw = () => {
      const w = canvas.offsetWidth
      const h = canvas.offsetHeight
      time += 0.008

      // Clear
      ctx.fillStyle = '#0D2B35'
      ctx.fillRect(0, 0, w, h)

      // Ocean depth gradient
      const gradient = ctx.createLinearGradient(0, 0, 0, h)
      gradient.addColorStop(0, 'rgba(13, 43, 53, 0.3)')
      gradient.addColorStop(0.5, 'rgba(20, 53, 69, 0.15)')
      gradient.addColorStop(1, 'rgba(10, 32, 48, 0.4)')
      ctx.fillStyle = gradient
      ctx.fillRect(0, 0, w, h)

      // Subtle wave lines
      for (let i = 0; i < 8; i++) {
        ctx.beginPath()
        ctx.strokeStyle = `rgba(232, 91, 138, ${0.03 + i * 0.008})`
        ctx.lineWidth = 0.5
        const yBase = h * 0.2 + i * (h * 0.08)
        for (let x = 0; x < w; x += 2) {
          const y = yBase + Math.sin(x * 0.005 + time + i * 0.7) * (15 + i * 3)
            + Math.sin(x * 0.012 + time * 1.3 + i) * 8
          if (x === 0) ctx.moveTo(x, y)
          else ctx.lineTo(x, y)
        }
        ctx.stroke()
      }

      // Scan line sweep — ping-pong across visible width
      // Use a linear ping-pong so speed feels consistent regardless of viewport width
      const scanSpeed = 120 // pixels per second at 60fps → ~120px/frame-set
      const scanCycle = (2 * w) / scanSpeed // time for one full back-and-forth
      const scanProgress = (time % scanCycle) / scanCycle
      const scanX = scanProgress < 0.5
        ? (scanProgress * 2) * w        // left → right
        : (1 - (scanProgress - 0.5) * 2) * w  // right → left
      const scanGradient = ctx.createLinearGradient(scanX - 100, 0, scanX + 100, 0)
      scanGradient.addColorStop(0, 'rgba(232, 91, 138, 0)')
      scanGradient.addColorStop(0.5, 'rgba(232, 91, 138, 0.08)')
      scanGradient.addColorStop(1, 'rgba(232, 91, 138, 0)')
      ctx.fillStyle = scanGradient
      ctx.fillRect(scanX - 100, 0, 200, h)

      // Scan line
      ctx.beginPath()
      ctx.strokeStyle = 'rgba(232, 91, 138, 0.25)'
      ctx.lineWidth = 1
      ctx.moveTo(scanX, 0)
      ctx.lineTo(scanX, h)
      ctx.stroke()

      // Floating particles (plastic detection points)
      for (let i = 0; i < 40; i++) {
        const px = (Math.sin(i * 3.7 + time * 0.3) + 1) / 2 * w
        const py = (Math.cos(i * 2.3 + time * 0.2) + 1) / 2 * h
        const distFromScan = Math.abs(px - scanX)
        const alpha = distFromScan < 150 ? 0.6 * (1 - distFromScan / 150) : 0.05

        ctx.beginPath()
        ctx.arc(px, py, 1.5 + Math.sin(i + time) * 0.5, 0, Math.PI * 2)
        ctx.fillStyle = `rgba(232, 91, 138, ${alpha})`
        ctx.fill()

        // Detection ring near scan line
        if (distFromScan < 80) {
          ctx.beginPath()
          ctx.arc(px, py, 6 + Math.sin(time * 2 + i) * 2, 0, Math.PI * 2)
          ctx.strokeStyle = `rgba(232, 91, 138, ${alpha * 0.3})`
          ctx.lineWidth = 0.5
          ctx.stroke()
        }
      }

      // Grid overlay
      ctx.strokeStyle = 'rgba(232, 91, 138, 0.03)'
      ctx.lineWidth = 0.5
      for (let x = 0; x < w; x += 60) {
        ctx.beginPath()
        ctx.moveTo(x, 0)
        ctx.lineTo(x, h)
        ctx.stroke()
      }
      for (let y = 0; y < h; y += 60) {
        ctx.beginPath()
        ctx.moveTo(0, y)
        ctx.lineTo(w, y)
        ctx.stroke()
      }

      animationId = requestAnimationFrame(draw)
    }

    draw()

    return () => {
      cancelAnimationFrame(animationId)
      window.removeEventListener('resize', resize)
    }
  }, [])

  return (
    <canvas
      ref={canvasRef}
      className="absolute inset-0 w-full h-full"
      style={{ opacity: 0.7 }}
    />
  )
}

export function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Subtle depth gradient — shallow surface → deep */}
      <div
        className="absolute inset-0 z-[1] pointer-events-none"
        style={{ background: 'linear-gradient(to bottom, rgba(42,96,112,0.3) 0%, transparent 50%)' }}
      />
      <OceanScanAnimation />

      {/* Content */}
      <div className="relative z-10 text-center px-6 max-w-4xl mx-auto">
        {/* Wordmark */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 0.3 }}
          className="mb-2"
        >
          <span className="font-mono text-xs tracking-[0.3em] text-cyan uppercase">
            Pelagic IntelX
          </span>
        </motion.div>

        {/* Tagline */}
        <motion.h1
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 0.6 }}
          className="font-display text-5xl md:text-7xl lg:text-8xl text-text-primary mb-6"
          style={{ fontWeight: 300, fontStyle: 'italic', letterSpacing: '-0.02em', lineHeight: 1.06 }}
        >
          Mapping the
          <br />
          <span className="text-cyan" style={{ fontWeight: 700, fontStyle: 'normal' }}>Invisible</span>
        </motion.h1>

        {/* Subtitle */}
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.9 }}
          className="font-body text-lg md:text-xl text-text-secondary max-w-2xl mx-auto mb-4"
        >
          AI-powered ocean plastic intelligence at planetary scale.
        </motion.p>

        {/* Case study label */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 1.2 }}
          className="font-mono text-xs text-text-dim tracking-wider mb-24"
        >
          A communications intelligence case study
        </motion.p>
      </div>

      {/* Scroll prompt — positioned from section, not content div */}
      <div className="absolute bottom-12 left-1/2 -translate-x-1/2 z-10">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 1.8 }}
        >
          <motion.div
            animate={{ y: [0, 8, 0] }}
            transition={{ duration: 2, repeat: Infinity, ease: 'easeInOut' }}
            className="flex flex-col items-center gap-2"
          >
            <span className="font-mono text-xs text-text-dim tracking-wider">SCROLL</span>
            <svg
              className="w-4 h-4 text-text-dim"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth={1.5}
            >
              <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 13.5L12 21m0 0l-7.5-7.5M12 21V3" />
            </svg>
          </motion.div>
        </motion.div>
      </div>

      {/* Bottom fade */}
      <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-ocean-bg to-transparent" />
    </section>
  )
}
