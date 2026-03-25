import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'

export function ChapterWrapper({ id, label, title, subtitle, children, className = '' }) {
  const { ref, isInView } = useInView({ threshold: 0.1 })

  return (
    <section
      id={id}
      ref={ref}
      className={`relative min-h-screen py-24 px-6 md:px-12 lg:px-24 ${className}`}
    >
      <div className="max-w-6xl mx-auto">
        {label && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.6 }}
            className="mb-4"
          >
            <span className="font-mono text-sm tracking-widest text-cyan uppercase">
              {label}
            </span>
          </motion.div>
        )}

        {title && (
          <motion.h2
            initial={{ opacity: 0, y: 30 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.8, delay: 0.1 }}
            className="font-display text-4xl md:text-5xl lg:text-6xl text-text-primary mb-4"
            style={{ fontWeight: 300, fontStyle: 'italic', letterSpacing: '-0.02em', lineHeight: 1.06 }}
          >
            {title}
          </motion.h2>
        )}

        {subtitle && (
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="font-display text-xl md:text-2xl text-text-secondary italic mb-16 max-w-3xl"
          >
            {subtitle}
          </motion.p>
        )}

        {children}
      </div>
    </section>
  )
}
