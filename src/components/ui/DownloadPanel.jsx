import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'

// TODO: PDF collateral — recolor to Ai2 Dark palette

function DownloadCard({ title, description, filename, delay = 0 }) {
  const href = `/downloads/${filename}`

  return (
    <motion.a
      href={href}
      download
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay }}
      className="group block bg-ocean-surface border border-ocean-border rounded-lg p-5 hover:border-cyan/40 transition-colors duration-300"
    >
      <div className="flex items-start justify-between gap-4">
        <div>
          <h4 className="font-body text-sm font-semibold text-text-primary group-hover:text-cyan transition-colors">
            {title}
          </h4>
          <p className="text-xs text-text-secondary mt-1">{description}</p>
        </div>
        <div className="shrink-0 mt-0.5">
          <svg
            className="w-5 h-5 text-text-dim group-hover:text-cyan transition-colors"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            strokeWidth={1.5}
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3"
            />
          </svg>
        </div>
      </div>
      <div className="mt-3 flex items-center gap-2">
        <span className="font-mono text-xs text-text-dim">PDF</span>
        <span className="text-ocean-border">|</span>
        <span className="font-mono text-xs text-text-dim">{filename}</span>
      </div>
    </motion.a>
  )
}

export function DownloadPanel({ title, documents }) {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  return (
    <div ref={ref} className="mt-16">
      <h3 className="font-mono text-sm tracking-widest text-gold uppercase mb-6">
        {title}
      </h3>
      {isInView && (
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {documents.map((doc, i) => (
            <DownloadCard key={doc.filename} {...doc} delay={i * 0.1} />
          ))}
        </div>
      )}
    </div>
  )
}
