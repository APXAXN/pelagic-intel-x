import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'
import vocabData from '@/data/vocabulary_gap.json'

export function VocabularyGapChart() {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  return (
    <div ref={ref}>
      <h4 className="font-mono text-xs tracking-widest text-text-secondary uppercase mb-6">
        The Vocabulary Gap — Scientific vs. Public Language
      </h4>

      <div className="grid md:grid-cols-2 gap-8">
        {/* Scientific language */}
        <motion.div
          initial={{ opacity: 0, x: -30 }}
          animate={isInView ? { opacity: 1, x: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="bg-ocean-surface border border-ocean-border rounded-lg p-6"
        >
          <div className="flex items-center gap-2 mb-4">
            <div className="w-2 h-2 rounded-full bg-cyan" />
            <span className="font-mono text-xs tracking-widest text-cyan uppercase">
              Scientific Register
            </span>
          </div>
          <p className="text-xs text-text-dim mb-4">How researchers talk about ocean plastic</p>
          <div className="space-y-2">
            {vocabData.scientific_term_counts.map((item, i) => (
              <motion.div
                key={item.term}
                initial={{ opacity: 0, x: -20 }}
                animate={isInView ? { opacity: 1, x: 0 } : {}}
                transition={{ duration: 0.4, delay: 0.2 + i * 0.1 }}
                className="flex items-center justify-between"
              >
                <span className="font-mono text-sm text-text-primary">{item.term}</span>
                <span className="font-mono text-xs text-text-dim">{item.count}x</span>
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Public language */}
        <motion.div
          initial={{ opacity: 0, x: 30 }}
          animate={isInView ? { opacity: 1, x: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="bg-ocean-surface border border-ocean-border rounded-lg p-6"
        >
          <div className="flex items-center gap-2 mb-4">
            <div className="w-2 h-2 rounded-full bg-gold" />
            <span className="font-mono text-xs tracking-widest text-gold uppercase">
              Public Register
            </span>
          </div>
          <p className="text-xs text-text-dim mb-4">How people actually talk about ocean plastic</p>
          <div className="space-y-2">
            {vocabData.public_term_counts.map((item, i) => (
              <motion.div
                key={item.term}
                initial={{ opacity: 0, x: 20 }}
                animate={isInView ? { opacity: 1, x: 0 } : {}}
                transition={{ duration: 0.4, delay: 0.2 + i * 0.1 }}
                className="flex items-center justify-between"
              >
                <span className="font-mono text-sm text-text-primary">{item.term}</span>
                <span className="font-mono text-xs text-text-dim">{item.count}x</span>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </div>

      {/* Insight callout */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={isInView ? { opacity: 1, y: 0 } : {}}
        transition={{ duration: 0.6, delay: 0.6 }}
        className="mt-8 border-l-2 border-gold pl-6 py-2"
      >
        <p className="font-mono text-xs text-gold uppercase tracking-widest mb-2">Key Insight</p>
        <p className="text-sm text-text-secondary leading-relaxed max-w-3xl">
          {vocabData.gap_insight}
        </p>
      </motion.div>
    </div>
  )
}
