import { motion } from 'framer-motion'
import { ChapterWrapper } from '@/components/layout/ChapterWrapper'
import { RevealOnScroll } from '@/components/ui/RevealOnScroll'
import { DownloadPanel } from '@/components/ui/DownloadPanel'
import { useInView } from '@/hooks/useInView'

const STAKEHOLDERS = [
  {
    group: 'UNEP Officials',
    interest: 'Treaty evidence base',
    ask: 'Cite dataset in Global Plastics Treaty appendix',
    message: 'This data meets evidentiary standards for international law',
    channel: 'Direct briefing + white paper',
  },
  {
    group: 'National EPA Leads',
    interest: 'Domestic enforcement tools',
    ask: 'Pilot density monitoring in regulatory framework',
    message: 'Jurisdiction-level data available on request',
    channel: 'Targeted outreach + policy memo',
  },
  {
    group: 'Environmental NGOs',
    interest: 'Advocacy ammunition',
    ask: 'Embed map in campaign materials',
    message: 'The evidence is finally good enough to fight with',
    channel: 'Coalition emails + social co-posts',
  },
  {
    group: 'Policy Journalists',
    interest: 'News hook + access',
    ask: 'Cover joint report release',
    message: 'Three organizations. One dataset. Real regulatory consequences.',
    channel: 'Press release + embargo',
  },
  {
    group: 'University Partners',
    interest: 'Research validation + citation',
    ask: 'Co-author methodology paper',
    message: 'Peer-reviewed pipeline, open for replication',
    channel: 'Academic journals + research newsletters',
  },
]

function StakeholderMatrix() {
  const { ref, isInView } = useInView({ threshold: 0.1 })

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.7 }}
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-6">
        Stakeholder Communications Matrix
      </h3>
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-ocean-border">
              {['Stakeholder', 'Primary Interest', 'Ask / CTA', 'Key Message', 'Channel'].map(h => (
                <th key={h} className="font-mono text-xs text-text-dim tracking-wider uppercase text-left py-3 px-4">
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {STAKEHOLDERS.map((s, i) => (
              <motion.tr
                key={s.group}
                initial={{ opacity: 0, x: -20 }}
                animate={isInView ? { opacity: 1, x: 0 } : {}}
                transition={{ duration: 0.4, delay: i * 0.08 }}
                className="border-b border-ocean-border/50 hover:bg-ocean-surface/50 transition-colors"
              >
                <td className="py-3 px-4 font-body font-semibold text-text-primary">{s.group}</td>
                <td className="py-3 px-4 text-text-secondary">{s.interest}</td>
                <td className="py-3 px-4 text-cyan text-xs font-mono">{s.ask}</td>
                <td className="py-3 px-4 text-text-secondary italic">{s.message}</td>
                <td className="py-3 px-4 text-text-dim text-xs">{s.channel}</td>
              </motion.tr>
            ))}
          </tbody>
        </table>
      </div>
    </motion.div>
  )
}

function OpEdExcerpt() {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.7 }}
      className="mt-16"
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-6">
        Op-Ed Excerpt — "The Ocean Has a Memory"
      </h3>
      <div className="bg-ocean-surface border border-ocean-border rounded-xl p-8 md:p-10">
        <div className="max-w-2xl">
          <p className="font-display text-lg md:text-xl text-text-primary italic leading-relaxed mb-6">
            "The ocean doesn't forget what we put in it. Microplastics
            accumulate in the same current systems, year after year — but
            until now, we couldn't see where."
          </p>
          <p className="text-sm text-text-secondary leading-relaxed mb-6">
            International treaties on ocean plastic exist but lack the
            evidentiary standards to enforce. This data changes that.
            When a data company, a policy organization, and a university
            research lab agree that the evidence is finally ready — the
            question shifts from whether to act to how fast.
          </p>
          <p className="font-display text-lg text-text-primary italic leading-relaxed">
            "The ocean has a memory. Our governance frameworks are still
            suffering from amnesia. Not anymore."
          </p>
          <div className="mt-6 pt-4 border-t border-ocean-border">
            <p className="font-mono text-xs text-text-dim">
              Target outlets: Nature (Comment) · The Atlantic · Politico Pro · The Guardian
            </p>
          </div>
        </div>
      </div>
    </motion.div>
  )
}

function GoogleAdsBrief() {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  const headlines = [
    'The Data Behind Global Plastics Policy',
    'AI Mapping Makes Ocean Plastic Regulation Possible',
    'Read the Report: Ocean Plastic, AI, and Enforcement',
  ]

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.7 }}
      className="mt-16"
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-6">
        Google Ads Brief — Policy Search Campaign
      </h3>
      <div className="grid md:grid-cols-2 gap-6">
        <div className="bg-ocean-surface border border-ocean-border rounded-lg p-6">
          <span className="font-mono text-xs text-cyan tracking-wider uppercase block mb-3">Headline Variants</span>
          <div className="space-y-2">
            {headlines.map((h, i) => (
              <div key={h} className="flex gap-3 items-start">
                <span className="font-mono text-xs text-text-dim mt-0.5">{i + 1}.</span>
                <span className="text-sm text-text-primary">{h}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="bg-ocean-surface border border-ocean-border rounded-lg p-6">
          <span className="font-mono text-xs text-cyan tracking-wider uppercase block mb-3">Campaign Details</span>
          <div className="space-y-3 text-sm">
            <div className="flex justify-between">
              <span className="text-text-dim">Budget</span>
              <span className="text-text-primary font-mono">$4,500/mo</span>
            </div>
            <div className="flex justify-between">
              <span className="text-text-dim">Window</span>
              <span className="text-text-primary font-mono">30-day release</span>
            </div>
            <div className="flex justify-between">
              <span className="text-text-dim">Target CTR</span>
              <span className="text-cyan font-mono">3.5%+</span>
            </div>
            <div className="flex justify-between">
              <span className="text-text-dim">Industry avg</span>
              <span className="text-text-dim font-mono">2.1%</span>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  )
}

const CHAPTER4_DOWNLOADS = [
  {
    title: 'Op-Ed — "The Ocean Has a Memory"',
    description: 'Full draft for Nature Comment, The Atlantic, Politico Pro, The Guardian',
    filename: 'pelagicintelx-op-ed.pdf',
  },
  {
    title: 'Stakeholder Communications Matrix',
    description: 'Per-stakeholder framing, language, asks, and channel strategy',
    filename: 'pelagicintelx-stakeholder-matrix.pdf',
  },
  {
    title: 'Campaign Strategy Memo',
    description: 'Full strategic communications plan — situation analysis through KPIs',
    filename: 'pelagicintelx-campaign-strategy-memo.pdf',
  },
  {
    title: 'Google Ads Brief',
    description: 'Policy search campaign — keywords, headlines, audience targeting, budget',
    filename: 'pelagicintelx-google-ads-brief.pdf',
  },
]

export function Chapter4() {
  return (
    <ChapterWrapper
      id="the-impact-play"
      label="Chapter 4"
      title="The Impact Play"
      subtitle={'"Plastic Doesn\'t Disappear — the policy campaign"'}
    >
      <RevealOnScroll className="mb-16 max-w-3xl">
        <p className="text-text-secondary leading-relaxed">
          The second campaign moves Pelagic IntelX from "interesting data
          company" to "essential infrastructure for environmental governance."
          In coalition with a policy organization and university research lab,
          the joint report argues that AI-mapped density data can — and
          should — inform international environmental regulation.
        </p>
      </RevealOnScroll>

      {/* Stakeholder matrix */}
      <RevealOnScroll className="mb-8">
        <StakeholderMatrix />
      </RevealOnScroll>

      {/* Op-Ed excerpt */}
      <OpEdExcerpt />

      {/* Google Ads brief */}
      <GoogleAdsBrief />

      {/* Downloads */}
      <DownloadPanel
        title="Policy Campaign Collateral — Download"
        documents={CHAPTER4_DOWNLOADS}
      />
    </ChapterWrapper>
  )
}
