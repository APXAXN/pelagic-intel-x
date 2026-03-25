import { lazy, Suspense } from 'react'
import { ChapterWrapper } from '@/components/layout/ChapterWrapper'
import { RevealOnScroll } from '@/components/ui/RevealOnScroll'
import { StatCard } from '@/components/ui/StatCard'
import { DownloadPanel } from '@/components/ui/DownloadPanel'
import { OceanDensityMap } from '@/components/map/OceanDensityMap'
import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'

const PlasticDepthModel = lazy(() => import('@/components/PlasticDepthModel'))

function SocialMockup({ platform, content, engagement }) {
  const { ref, isInView } = useInView({ threshold: 0.2 })
  const isX = platform === 'x'

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 20 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6 }}
      className="bg-ocean-surface border border-ocean-border rounded-lg p-5"
    >
      <div className="flex items-center gap-3 mb-3">
        <div className={`w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold ${
          isX ? 'bg-white/10 text-white' : 'bg-[#0A66C2]/20 text-[#0A66C2]'
        }`}>
          {isX ? 'X' : 'in'}
        </div>
        <div>
          <div className="font-body text-sm font-semibold text-text-primary">
            Pelagic IntelX
          </div>
          <div className="font-mono text-xs text-text-dim">
            {isX ? '@pelagicintelx' : 'Pelagic IntelX'}
          </div>
        </div>
      </div>
      <p className="text-sm text-text-secondary leading-relaxed mb-3">
        {content}
      </p>
      <div className="flex gap-4 font-mono text-xs text-text-dim">
        {engagement.map(({ label, value }) => (
          <span key={label}>{value} {label}</span>
        ))}
      </div>
    </motion.div>
  )
}

function CampaignStrategy() {
  const { ref, isInView } = useInView({ threshold: 0.2 })

  const phases = [
    { phase: 'Pre-Launch', timeline: 'Week 1-2', items: ['Embargo briefings to tier-1 science journalists', 'Academic pre-print distribution', 'Coalition partner coordination'] },
    { phase: 'Launch Day', timeline: 'Day 1', items: ['Press release wire distribution', 'X thread + LinkedIn post sequence', 'Map goes live — public access URL', 'Dataset published — open access'] },
    { phase: 'Amplification', timeline: 'Week 2-4', items: ['Follow-up interviews with embargoing outlets', 'Reddit AMA in r/environment', 'Research newsletter features', 'Policy brief distribution'] },
  ]

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.7 }}
      className="mt-16"
    >
      <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-8">
        Campaign Strategy — Mapping the Invisible
      </h3>
      <div className="grid md:grid-cols-3 gap-6">
        {phases.map((p, i) => (
          <motion.div
            key={p.phase}
            initial={{ opacity: 0, y: 20 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5, delay: i * 0.15 }}
            className="bg-ocean-surface border border-ocean-border rounded-lg p-6"
          >
            <span className="font-mono text-xs text-cyan tracking-wider uppercase">{p.timeline}</span>
            <h4 className="font-body text-lg font-semibold text-text-primary mt-1 mb-4">{p.phase}</h4>
            <ul className="space-y-2">
              {p.items.map((item) => (
                <li key={item} className="text-sm text-text-secondary flex gap-2">
                  <span className="text-cyan mt-1 shrink-0">&#8250;</span>
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

const CHAPTER3_DOWNLOADS = [
  {
    title: 'Press Release',
    description: '"Pelagic IntelX Publishes First Real-Time AI Map of Pacific Ocean Plastic Density"',
    filename: 'pelagicintelx-press-release.pdf',
  },
  {
    title: 'Media One-Pager',
    description: 'At-a-glance brief for journalists — key stats, quotes, embed links',
    filename: 'pelagicintelx-media-one-pager.pdf',
  },
  {
    title: 'Social Content Brief',
    description: 'X thread (7 posts) + LinkedIn post — launch day content sequence',
    filename: 'pelagicintelx-social-content-brief.pdf',
  },
  {
    title: 'Depth Model — Methodology Note',
    description: 'Technical methodology for sub-surface volumetric plastic density modeling',
    filename: 'pelagicintelx-depth-model-methodology.pdf',
  },
]

export function Chapter3() {
  return (
    <ChapterWrapper
      id="the-launch"
      label="Chapter 3"
      title="The Launch"
      subtitle={'"Mapping the Invisible — the research launch campaign"'}
    >
      <RevealOnScroll className="mb-12 max-w-3xl">
        <p className="text-text-secondary leading-relaxed">
          The centerpiece: Pelagic IntelX releases its first publicly available
          ocean plastic density map — a real-time, AI-generated visualization of
          microplastic concentration across the Pacific. This is the
          credibility-building moment that transforms the company from one making
          claims into one that shows its work at planetary scale.
        </p>
      </RevealOnScroll>

      {/* Stats */}
      <RevealOnScroll className="mb-12">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <StatCard value={3844} label="Data Points" delay={0} />
          <StatCard value={16} label="Accumulation Zones" delay={0.1} />
          <StatCard value={580000} label="Max Particles/km²" delay={0.2} />
          <StatCard value={40} label="% Above Predictions" suffix="%" delay={0.3} />
        </div>
      </RevealOnScroll>

      {/* THE MAP — emotional centerpiece */}
      <RevealOnScroll className="mb-16">
        <OceanDensityMap />
      </RevealOnScroll>

      {/* ── Narrative bridge: surface → depth ── */}
      <RevealOnScroll className="mb-6">
        <div className="flex items-center gap-4 my-12">
          <div className="h-px flex-1 bg-gradient-to-r from-transparent via-[#E85B8A]/30 to-transparent" />
          <span className="font-mono text-[10px] tracking-[0.2em] text-[#E85B8A] uppercase whitespace-nowrap px-3 py-1 rounded-full border border-[#E85B8A]/20 bg-[#E85B8A]/5">
            New — Depth Profile Data
          </span>
          <div className="h-px flex-1 bg-gradient-to-r from-transparent via-[#E85B8A]/30 to-transparent" />
        </div>
      </RevealOnScroll>

      <RevealOnScroll className="mb-12 max-w-3xl">
        <h3 className="font-display text-2xl md:text-3xl text-text-primary mb-4 leading-snug">
          Every map before this one was looking at the surface.
        </h3>
        <p className="text-text-secondary leading-relaxed">
          Pelagic IntelX's satellite-AI pipeline doesn't stop at the waterline.
          By fusing multispectral imagery with sub-surface acoustic sensor data,
          we've modeled microplastic concentration through the full water column
          — for the first time at Pacific scale.
        </p>
      </RevealOnScroll>

      {/* 3D Depth Model */}
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        viewport={{ once: true, amount: 0.15 }}
        className="mb-16"
      >
        <Suspense
          fallback={
            <div
              className="w-full rounded-xl flex items-center justify-center"
              style={{ background: '#0D2B35', aspectRatio: '16/9' }}
            >
              <span className="font-mono text-sm text-[#7AA8B8] animate-pulse">
                Loading 3D depth model…
              </span>
            </div>
          }
        >
          <PlasticDepthModel />
        </Suspense>
      </motion.div>

      {/* Campaign strategy */}
      <CampaignStrategy />

      {/* Social content previews */}
      <RevealOnScroll className="mt-16">
        <h3 className="font-mono text-xs tracking-widest text-gold uppercase mb-8">
          Social Content Previews
        </h3>
        <div className="grid md:grid-cols-2 gap-6">
          <SocialMockup
            platform="x"
            content="We just published the most detailed map of ocean plastic ever made. The picture is not what we expected. 🧵"
            engagement={[
              { label: 'reposts', value: '12.4K' },
              { label: 'likes', value: '45.2K' },
              { label: 'views', value: '2.1M' },
            ]}
          />
          <SocialMockup
            platform="linkedin"
            content="Today, Pelagic IntelX releases its ocean plastic density map — the first real-time, AI-generated visualization of microplastic concentration across the Pacific. The dataset is open. The methodology is published. Here's what the data shows, and why it matters for policy."
            engagement={[
              { label: 'reactions', value: '3.2K' },
              { label: 'comments', value: '284' },
              { label: 'reposts', value: '891' },
            ]}
          />
        </div>
      </RevealOnScroll>

      {/* Downloads */}
      <DownloadPanel
        title="Campaign Collateral — Download"
        documents={CHAPTER3_DOWNLOADS}
      />
    </ChapterWrapper>
  )
}
