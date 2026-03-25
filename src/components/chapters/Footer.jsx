import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'

export function Footer() {
  const { ref, isInView } = useInView({ threshold: 0.3 })

  return (
    <footer ref={ref} className="border-t border-ocean-border py-16 px-6 md:px-12">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={isInView ? { opacity: 1, y: 0 } : {}}
        transition={{ duration: 0.6 }}
        className="max-w-4xl mx-auto text-center"
      >
        {/* Brand note */}
        <div className="mb-8">
          <span className="font-mono text-xs tracking-[0.3em] text-cyan uppercase">
            Pelagic IntelX
          </span>
          <p className="text-sm text-text-dim mt-3 max-w-lg mx-auto">
            Pelagic IntelX is a fictional company created for portfolio
            purposes. All communications strategy, campaign concepts, and
            collateral are original work demonstrating senior-level
            communications competency.
          </p>
        </div>

        {/* Divider */}
        <div className="w-16 h-px bg-ocean-border mx-auto mb-8" />

        {/* Nathan's info */}
        <div className="mb-6">
          <p className="font-body text-sm text-text-secondary mb-1">
            Built by <span className="text-text-primary font-semibold">Nathan Fitzgerald</span>
          </p>
          <p className="font-mono text-xs text-text-dim">
            Senior Communications Specialist Application — Allen Institute for AI (Ai2)
          </p>
        </div>

        {/* Links */}
        <div className="flex justify-center gap-6">
          <a
            href="https://linkedin.com"
            target="_blank"
            rel="noopener noreferrer"
            className="font-mono text-xs text-text-dim hover:text-cyan transition-colors"
          >
            LinkedIn
          </a>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="font-mono text-xs text-text-dim hover:text-cyan transition-colors"
          >
            GitHub
          </a>
          <a
            href="mailto:nathan@example.com"
            className="font-mono text-xs text-text-dim hover:text-cyan transition-colors"
          >
            Contact
          </a>
        </div>

        {/* Tech credit */}
        <p className="font-mono text-xs text-text-dim/40 mt-10">
          React + Vite · Scrollama · Framer Motion · Mapbox GL JS · Recharts · Tailwind CSS
        </p>
      </motion.div>
    </footer>
  )
}
