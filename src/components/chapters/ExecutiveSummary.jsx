import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'

export function ExecutiveSummary() {
  const { ref, isInView } = useInView({ threshold: 0.3 })

  return (
    <section ref={ref} className="py-24 px-6">
      <div className="max-w-3xl mx-auto">
        {/* Label */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="mb-8"
        >
          <span className="font-mono text-xs tracking-[0.2em] text-cyan uppercase">
            Executive Summary
          </span>
          <div className="h-px w-16 bg-cyan/30 mt-3" />
        </motion.div>

        {/* Body */}
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.7, delay: 0.15 }}
          className="font-body text-base md:text-lg text-text-secondary leading-relaxed"
        >
          Pelagic IntelX is a fictional AI ocean-monitoring company created as a
          portfolio case study. This microsite presents a full-cycle communications
          strategy — from data intelligence and audience segmentation through
          campaign launch, policy advocacy, and measurement — built to demonstrate
          senior-level communications competency. Every data visualization, message
          architecture, and stakeholder framework was informed by a real analytics
          pipeline: Google Trends, SerpApi keyword mapping, Reddit NLP, simulated
          social listening, and a novel framing fidelity analysis. The work is
          original. The methodology is documented. The company is invented; the
          communications thinking is not.
        </motion.p>
      </div>
    </section>
  )
}
