import { motion } from 'framer-motion'
import { ChapterWrapper } from '@/components/layout/ChapterWrapper'
import { RevealOnScroll } from '@/components/ui/RevealOnScroll'
import { StatCard } from '@/components/ui/StatCard'
import { useInView } from '@/hooks/useInView'
import { FramingFidelitySection } from '@/components/charts/FramingFidelityChart'

const KPIS = [
  { metric: 'Press Pickups', target: '15+', baseline: '0', source: 'Media monitoring', timeframe: '30 days' },
  { metric: 'Map Unique Visitors', target: '50,000', baseline: '—', source: 'Vercel analytics', timeframe: '30 days' },
  { metric: 'Dataset Downloads', target: '2,000', baseline: '—', source: 'Download tracker', timeframe: '30 days' },
  { metric: 'X Thread Impressions', target: '500K', baseline: '—', source: 'X Analytics', timeframe: '30 days' },
  { metric: 'Joint Report Downloads', target: '5,000', baseline: '—', source: 'Download tracker', timeframe: '60 days' },
  { metric: 'Policy Briefing Requests', target: '8+', baseline: '—', source: 'CRM', timeframe: '60 days' },
]

function KPICards() {
  const { ref, isInView } = useInView({ threshold: 0.1 })

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0 }}
      animate={isInView ? { opacity: 1 } : {}}
      transition={{ duration: 0.5 }}
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-6">
        KPI Framework — What We Measure
      </h3>
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
        {KPIS.map((kpi, i) => (
          <motion.div
            key={kpi.metric}
            initial={{ opacity: 0, y: 20 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5, delay: i * 0.08 }}
            className="bg-ocean-surface border border-ocean-border rounded-lg p-5"
          >
            <div className="font-mono text-2xl font-bold text-cyan mb-1">{kpi.target}</div>
            <div className="font-body text-sm font-semibold text-text-primary mb-2">{kpi.metric}</div>
            <div className="flex justify-between text-xs">
              <span className="text-text-dim">{kpi.source}</span>
              <span className="font-mono text-text-dim">{kpi.timeframe}</span>
            </div>
          </motion.div>
        ))}
      </div>
    </motion.div>
  )
}

const TIMELINE_PHASES = [
  {
    phase: 'Phase 1',
    title: 'Intelligence & Prep',
    weeks: 'Week 1–2',
    items: ['Social listening analysis', 'Audience segmentation', 'Message architecture', 'Collateral drafting'],
    color: '#E85B8A',
  },
  {
    phase: 'Phase 2',
    title: 'Research Launch',
    weeks: 'Week 3–4',
    items: ['Map release + press embargo', 'Social content deployment', 'Dataset publication', 'Journalist outreach'],
    color: '#2A6070',
  },
  {
    phase: 'Phase 3',
    title: 'Amplification',
    weeks: 'Week 5–8',
    items: ['Follow-up media coverage', 'Research newsletter features', 'Conference presentations', 'Reddit AMA'],
    color: '#7AA8B8',
  },
  {
    phase: 'Phase 4',
    title: 'Policy Impact',
    weeks: 'Week 9–12',
    items: ['Joint report release', 'Policy briefings', 'Op-ed placements', 'Google Ads campaign'],
    color: '#E85B8A',
  },
]

function Timeline() {
  const { ref, isInView } = useInView({ threshold: 0.1 })

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0 }}
      animate={isInView ? { opacity: 1 } : {}}
      transition={{ duration: 0.5 }}
      className="mt-20"
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-8">
        90-Day Campaign Roadmap
      </h3>

      {/* Horizontal timeline bar */}
      <div className="relative mb-8">
        <div className="h-1 bg-ocean-border rounded-full" />
        <div className="flex justify-between absolute inset-x-0 -top-1">
          {TIMELINE_PHASES.map((p, i) => (
            <motion.div
              key={p.phase}
              initial={{ scale: 0 }}
              animate={isInView ? { scale: 1 } : {}}
              transition={{ duration: 0.4, delay: 0.3 + i * 0.15 }}
              className="w-3 h-3 rounded-full"
              style={{ backgroundColor: p.color }}
            />
          ))}
        </div>
      </div>

      {/* Phase cards */}
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
        {TIMELINE_PHASES.map((p, i) => (
          <motion.div
            key={p.phase}
            initial={{ opacity: 0, y: 20 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5, delay: 0.2 + i * 0.1 }}
            className="bg-ocean-surface border border-ocean-border rounded-lg p-5"
            style={{ borderTopColor: p.color, borderTopWidth: 2 }}
          >
            <span className="font-mono text-xs tracking-wider" style={{ color: p.color }}>
              {p.weeks}
            </span>
            <h4 className="font-body text-sm font-semibold text-text-primary mt-1 mb-3">{p.title}</h4>
            <ul className="space-y-1.5">
              {p.items.map(item => (
                <li key={item} className="text-xs text-text-secondary flex gap-2">
                  <span style={{ color: p.color }} className="mt-0.5 shrink-0">&#8250;</span>
                  {item}
                </li>
              ))}
            </ul>
          </motion.div>
        ))}
      </div>
    </motion.div>
  )
}

function ToolsPanel() {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  const tools = [
    { category: 'Data Collection', items: ['Pytrends', 'PRAW (Reddit API)', 'SerpApi', 'Brandwatch'] },
    { category: 'Analysis', items: ['NLTK / spaCy', 'pandas', 'Jupyter'] },
    { category: 'Visualization', items: ['Recharts', 'Mapbox GL JS', 'Plotly'] },
    { category: 'Frontend', items: ['React + Vite', 'Scrollama.js', 'Framer Motion', 'Tailwind CSS'] },
  ]

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.7 }}
      className="mt-20"
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-6">
        Tools & Methodology
      </h3>
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
        {tools.map(t => (
          <div key={t.category} className="bg-ocean-surface border border-ocean-border rounded-lg p-5">
            <span className="font-mono text-xs text-cyan tracking-wider uppercase block mb-3">
              {t.category}
            </span>
            <div className="space-y-1.5">
              {t.items.map(item => (
                <div key={item} className="font-mono text-sm text-text-secondary">{item}</div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </motion.div>
  )
}

export function Chapter5() {
  return (
    <ChapterWrapper
      id="the-playbook"
      label="Chapter 5"
      title="The Playbook"
      subtitle={'"What we\'d measure. What success looks like."'}
    >
      <RevealOnScroll className="mb-16 max-w-3xl">
        <p className="text-text-secondary leading-relaxed">
          Every communications strategy needs a measurement framework.
          These are the metrics that prove the work mattered — and the
          90-day roadmap that sequences intelligence, launch, amplification,
          and policy impact into a coherent campaign arc.
        </p>
      </RevealOnScroll>

      {/* KPI cards */}
      <RevealOnScroll className="mb-8">
        <KPICards />
      </RevealOnScroll>

      {/* Framing fidelity analysis */}
      <FramingFidelitySection />

      {/* 90-day timeline */}
      <Timeline />

      {/* Tools panel */}
      <ToolsPanel />

      {/* Closing statement */}
      <RevealOnScroll className="mt-20">
        <div className="text-center max-w-2xl mx-auto">
          <p className="font-display text-2xl md:text-3xl text-text-primary italic leading-relaxed mb-6">
            "The ocean has been waiting for this map. Now we build on it."
          </p>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 font-mono text-sm text-cyan hover:text-text-primary transition-colors"
          >
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            View Data Pipeline on GitHub
          </a>
        </div>
      </RevealOnScroll>
    </ChapterWrapper>
  )
}
