import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'
import { useEffect, useState } from 'react'

export function StatCard({ value, label, suffix = '', prefix = '', delay = 0 }) {
  const { ref, isInView } = useInView({ threshold: 0.3 })
  const [displayValue, setDisplayValue] = useState(0)

  useEffect(() => {
    if (!isInView) return

    const numValue = typeof value === 'number' ? value : parseFloat(value)
    if (isNaN(numValue)) {
      setDisplayValue(value)
      return
    }

    const duration = 1500
    const steps = 60
    const stepDuration = duration / steps
    const increment = numValue / steps
    let current = 0
    let step = 0

    const timer = setInterval(() => {
      step++
      current = Math.min(numValue, increment * step)
      setDisplayValue(
        numValue >= 1000
          ? Math.round(current).toLocaleString()
          : numValue % 1 !== 0
          ? current.toFixed(1)
          : Math.round(current)
      )
      if (step >= steps) clearInterval(timer)
    }, stepDuration)

    return () => clearInterval(timer)
  }, [isInView, value])

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6, delay }}
      className="bg-ocean-surface border border-ocean-border rounded-lg p-6 text-center"
    >
      <div className="font-mono text-3xl md:text-4xl font-bold text-cyan mb-2">
        {prefix}{displayValue}{suffix}
      </div>
      <div className="text-sm text-text-secondary uppercase tracking-wider">
        {label}
      </div>
    </motion.div>
  )
}
