import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'
import wordFreqData from '@/data/reddit_word_freq.json'

export function WordFrequencyChart() {
  const { ref, isInView } = useInView({ threshold: 0.2 })
  const words = wordFreqData.top_words.slice(0, 30)
  const maxCount = words[0]?.count || 1

  return (
    <div ref={ref}>
      <h4 className="font-mono text-xs tracking-widest text-text-secondary uppercase mb-4">
        Reddit Corpus — Word Frequency Analysis
      </h4>
      <p className="text-sm text-text-secondary mb-6">
        Top 30 terms across r/environment, r/Futurology, r/collapse, r/MachineLearning
      </p>
      <div className="flex flex-wrap gap-2 justify-center">
        {words.map((item, i) => {
          const scale = 0.6 + (item.count / maxCount) * 0.8
          const opacity = 0.4 + (item.count / maxCount) * 0.6
          const isHighlight = ['plastic', 'ocean', 'data', 'satellite', 'density', 'monitoring', 'cleanup'].includes(item.word)

          return (
            <motion.span
              key={item.word}
              initial={{ opacity: 0, scale: 0.5 }}
              animate={isInView ? { opacity, scale } : {}}
              transition={{ duration: 0.5, delay: i * 0.03 }}
              className={`font-mono inline-block px-2 py-1 rounded cursor-default transition-colors ${
                isHighlight
                  ? 'text-cyan hover:bg-cyan/10'
                  : 'text-text-secondary hover:bg-ocean-surface'
              }`}
              style={{
                fontSize: `${Math.max(11, 11 + (item.count / maxCount) * 18)}px`,
              }}
              title={`${item.word}: ${item.count} occurrences`}
            >
              {item.word}
            </motion.span>
          )
        })}
      </div>
    </div>
  )
}
