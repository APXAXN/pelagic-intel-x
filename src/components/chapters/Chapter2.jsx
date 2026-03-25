import { motion } from 'framer-motion'
import { ChapterWrapper } from '@/components/layout/ChapterWrapper'
import { RevealOnScroll } from '@/components/ui/RevealOnScroll'
import { useInView } from '@/hooks/useInView'

const AUDIENCES = [
  {
    id: 'journalists',
    label: 'Science & Environmental Journalists',
    icon: '01',
    coreNeed: 'First-look access, data credibility, visual assets they can embed',
    whereTheyLive: 'X (breaking news), email pitches, embargo lists, Substack newsletters',
    languageThatWorks: [
      '"First-of-its-kind"',
      '"Real-time"',
      '"Publicly available"',
      '"The map speaks for itself"',
    ],
    color: '#00D4FF',
  },
  {
    id: 'researchers',
    label: 'Environmental Researchers',
    icon: '02',
    coreNeed: 'Methodology transparency, data access, peer validity, reproducibility',
    whereTheyLive: 'Research newsletters, LinkedIn, Google Scholar alerts, academic Slack channels',
    languageThatWorks: [
      '"Open dataset"',
      '"Satellite + AI fusion"',
      '"Peer-reviewed pipeline"',
      '"Density model"',
    ],
    color: '#E8C547',
  },
  {
    id: 'policymakers',
    label: 'Policy Advocates & Regulators',
    icon: '03',
    coreNeed: 'Actionable evidence, scale of problem, regulatory hooks, enforcement tools',
    whereTheyLive: 'LinkedIn, coalition emails, policy briefings, conference side events',
    languageThatWorks: [
      '"Mapped for the first time"',
      '"The data regulators need"',
      '"Evidence base for enforcement"',
      '"Jurisdiction-level data"',
    ],
    color: '#4ECDC4',
  },
]

function AudienceCard({ audience, index }) {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 40 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.7, delay: index * 0.15 }}
      className="bg-ocean-surface border border-ocean-border rounded-xl p-6 md:p-8 hover:border-opacity-60 transition-colors duration-300"
      style={{ borderColor: `${audience.color}20` }}
    >
      {/* Header */}
      <div className="flex items-start gap-4 mb-6">
        <div
          className="font-mono text-2xl font-bold opacity-30"
          style={{ color: audience.color }}
        >
          {audience.icon}
        </div>
        <div>
          <h3
            className="font-body text-lg font-semibold"
            style={{ color: audience.color }}
          >
            {audience.label}
          </h3>
        </div>
      </div>

      {/* Core Need */}
      <div className="mb-5">
        <span className="font-mono text-xs text-text-dim tracking-wider uppercase block mb-2">
          What they care about
        </span>
        <p className="text-sm text-text-secondary leading-relaxed">
          {audience.coreNeed}
        </p>
      </div>

      {/* Where they live */}
      <div className="mb-5">
        <span className="font-mono text-xs text-text-dim tracking-wider uppercase block mb-2">
          Where they live online
        </span>
        <p className="text-sm text-text-secondary leading-relaxed">
          {audience.whereTheyLive}
        </p>
      </div>

      {/* Language that works */}
      <div>
        <span className="font-mono text-xs text-text-dim tracking-wider uppercase block mb-3">
          Language that resonates
        </span>
        <div className="flex flex-wrap gap-2">
          {audience.languageThatWorks.map((phrase) => (
            <span
              key={phrase}
              className="font-mono text-xs px-3 py-1.5 rounded-full border"
              style={{
                color: audience.color,
                borderColor: `${audience.color}30`,
                backgroundColor: `${audience.color}08`,
              }}
            >
              {phrase}
            </span>
          ))}
        </div>
      </div>
    </motion.div>
  )
}

function MessageArchitecture() {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.7 }}
      className="mt-20"
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-8">
        Message Architecture
      </h3>

      {/* Primary message */}
      <div className="bg-ocean-surface border border-ocean-border rounded-xl p-6 md:p-8 mb-6">
        <span className="font-mono text-xs text-cyan tracking-wider uppercase block mb-3">
          Primary Message — All Audiences
        </span>
        <p className="font-display text-xl md:text-2xl text-text-primary italic leading-relaxed">
          "For the first time, we can see exactly where ocean plastic
          accumulates — and the picture is worse than models predicted."
        </p>
      </div>

      {/* Per-audience messages */}
      <div className="grid md:grid-cols-3 gap-4">
        {AUDIENCES.map((aud, i) => (
          <motion.div
            key={aud.id}
            initial={{ opacity: 0, y: 20 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5, delay: 0.3 + i * 0.1 }}
            className="border border-ocean-border rounded-lg p-5"
            style={{ borderLeftColor: aud.color, borderLeftWidth: 2 }}
          >
            <span
              className="font-mono text-xs tracking-wider uppercase block mb-2"
              style={{ color: aud.color }}
            >
              {aud.label.split(' ').slice(0, 2).join(' ')}
            </span>
            <p className="text-sm text-text-secondary leading-relaxed">
              {aud.id === 'journalists' &&
                'The map gives reporters a visual story — not just statistics. Embeddable, shareable, updated in near-real-time.'}
              {aud.id === 'researchers' &&
                'The underlying dataset is open-access. Methodology is published. The satellite + CV pipeline is reproducible.'}
              {aud.id === 'policymakers' &&
                'This map makes the invisible visible. It gives regulators the evidence base to move from negotiation to enforcement.'}
            </p>
          </motion.div>
        ))}
      </div>
    </motion.div>
  )
}

function StakeholderMap() {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  const nodes = [
    { label: 'Pelagic IntelX', x: 50, y: 50, size: 'lg', color: '#00D4FF' },
    { label: 'Journalists', x: 20, y: 20, size: 'md', color: '#00D4FF' },
    { label: 'Researchers', x: 80, y: 20, size: 'md', color: '#E8C547' },
    { label: 'Policymakers', x: 50, y: 85, size: 'md', color: '#4ECDC4' },
    { label: 'UNEP', x: 25, y: 75, size: 'sm', color: '#4ECDC4' },
    { label: 'NGOs', x: 75, y: 75, size: 'sm', color: '#4ECDC4' },
    { label: 'Science Media', x: 10, y: 45, size: 'sm', color: '#00D4FF' },
    { label: 'University Labs', x: 90, y: 45, size: 'sm', color: '#E8C547' },
  ]

  const connections = [
    [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
    [1, 6], [2, 7], [3, 4], [3, 5],
  ]

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0 }}
      animate={isInView ? { opacity: 1 } : {}}
      transition={{ duration: 0.8 }}
      className="mt-20"
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-8">
        Stakeholder Map
      </h3>
      <div className="bg-ocean-surface border border-ocean-border rounded-xl p-8 relative overflow-hidden">
        <svg viewBox="0 0 100 100" className="w-full max-w-2xl mx-auto" style={{ height: 400 }}>
          {/* Connections */}
          {connections.map(([from, to], i) => (
            <motion.line
              key={i}
              x1={nodes[from].x}
              y1={nodes[from].y}
              x2={nodes[to].x}
              y2={nodes[to].y}
              stroke="#1a2535"
              strokeWidth={0.3}
              initial={{ pathLength: 0, opacity: 0 }}
              animate={isInView ? { pathLength: 1, opacity: 1 } : {}}
              transition={{ duration: 0.8, delay: 0.5 + i * 0.05 }}
            />
          ))}

          {/* Nodes */}
          {nodes.map((node, i) => {
            const r = node.size === 'lg' ? 4 : node.size === 'md' ? 2.5 : 1.8
            return (
              <motion.g
                key={node.label}
                initial={{ opacity: 0, scale: 0 }}
                animate={isInView ? { opacity: 1, scale: 1 } : {}}
                transition={{ duration: 0.5, delay: 0.3 + i * 0.08 }}
              >
                <circle
                  cx={node.x}
                  cy={node.y}
                  r={r}
                  fill={node.color}
                  opacity={0.2}
                />
                <circle
                  cx={node.x}
                  cy={node.y}
                  r={r * 0.5}
                  fill={node.color}
                  opacity={0.8}
                />
                <text
                  x={node.x}
                  y={node.y + r + 3}
                  textAnchor="middle"
                  fill="#8899AA"
                  fontSize={2.5}
                  fontFamily="IBM Plex Mono"
                >
                  {node.label}
                </text>
              </motion.g>
            )
          })}
        </svg>
      </div>
    </motion.div>
  )
}

export function Chapter2() {
  return (
    <ChapterWrapper
      id="the-audience"
      label="Chapter 2"
      title="The Audience"
      subtitle={'"Three audiences. Three completely different conversations."'}
    >
      <RevealOnScroll className="mb-16 max-w-3xl">
        <p className="text-text-secondary leading-relaxed">
          The same data story told three different ways — because a journalist
          needs a visual hook, a researcher needs methodology transparency, and
          a policymaker needs an enforcement argument. The message architecture
          adapts language, channel, and ask to each audience.
        </p>
      </RevealOnScroll>

      {/* Audience cards */}
      <div className="grid lg:grid-cols-3 gap-6 mb-8">
        {AUDIENCES.map((audience, i) => (
          <AudienceCard key={audience.id} audience={audience} index={i} />
        ))}
      </div>

      {/* Stakeholder map */}
      <StakeholderMap />

      {/* Message architecture */}
      <MessageArchitecture />
    </ChapterWrapper>
  )
}
