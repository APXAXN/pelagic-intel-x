import { useState } from 'react'
import {
  LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer,
  CartesianGrid, Legend, BarChart, Bar, Cell,
} from 'recharts'
import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'
import fidelityData from '@/data/framing_fidelity.json'

const CHANNEL_COLORS = {
  press: '#E85B8A',
  social: '#7AA8B8',
  policy: '#2A6070',
  academic: '#F5F0E8',
}

const CHANNEL_LABELS = {
  press: 'Press',
  social: 'Social',
  policy: 'Policy',
  academic: 'Academic',
}

function FidelityDecayChart() {
  const { metrics } = fidelityData
  const series = metrics.channel_period_series

  // Build unified data for the line chart
  const chartData = metrics.by_period.map((p) => {
    const point = { period: p.period.replace('Day ', 'D'), ffi: p.ffi }
    for (const ch of Object.keys(series)) {
      const match = series[ch].find((s) => s.period_idx === p.period_idx)
      if (match) point[ch] = match.ffi
    }
    return point
  })

  return (
    <div className="bg-ocean-surface border border-ocean-border rounded-xl p-5 md:p-6">
      <div className="flex items-center justify-between mb-4">
        <h4 className="font-mono text-xs tracking-widest text-cyan uppercase">
          Fidelity Decay — 90-Day Window
        </h4>
        <span className="font-mono text-[10px] text-text-dim">FFI by channel over time</span>
      </div>
      <ResponsiveContainer width="100%" height={260}>
        <LineChart data={chartData} margin={{ top: 5, right: 10, bottom: 5, left: -10 }}>
          <CartesianGrid stroke="#1a4050" strokeDasharray="3 3" />
          <XAxis
            dataKey="period"
            tick={{ fill: '#4A7080', fontSize: 10, fontFamily: 'IBM Plex Mono' }}
            axisLine={{ stroke: '#1a4050' }}
            tickLine={false}
          />
          <YAxis
            domain={[0, 1]}
            tick={{ fill: '#4A7080', fontSize: 10, fontFamily: 'IBM Plex Mono' }}
            axisLine={{ stroke: '#1a4050' }}
            tickLine={false}
            tickFormatter={(v) => `${(v * 100).toFixed(0)}%`}
          />
          <Tooltip
            contentStyle={{
              background: '#0D2B35',
              border: '1px solid #1a4050',
              borderRadius: 8,
              fontFamily: 'IBM Plex Mono',
              fontSize: 11,
            }}
            labelStyle={{ color: '#7AA8B8' }}
            formatter={(value, name) => [`${(value * 100).toFixed(1)}%`, CHANNEL_LABELS[name] || name]}
          />
          {Object.entries(CHANNEL_COLORS).map(([ch, color]) => (
            <Line
              key={ch}
              type="monotone"
              dataKey={ch}
              stroke={color}
              strokeWidth={2}
              dot={{ fill: color, r: 3 }}
              activeDot={{ r: 5, stroke: color }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
      <div className="flex flex-wrap gap-4 mt-3 justify-center">
        {Object.entries(CHANNEL_COLORS).map(([ch, color]) => (
          <div key={ch} className="flex items-center gap-1.5">
            <div className="w-3 h-0.5 rounded" style={{ background: color }} />
            <span className="font-mono text-[10px] text-text-dim">{CHANNEL_LABELS[ch]}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

function FramePerformanceBars() {
  const { metrics } = fidelityData
  const frameData = Object.values(metrics.by_frame)
    .sort((a, b) => b.ffi - a.ffi)
    .map((f) => ({
      ...f,
      short: f.frame.length > 30 ? f.frame.slice(0, 28) + '…' : f.frame,
      ffiPercent: Math.round(f.ffi * 100),
    }))

  const barColor = (category) => {
    const map = {
      novelty: '#E85B8A',
      scale: '#c4326a',
      technology: '#2A6070',
      urgency: '#E85B8A',
      narrative: '#7AA8B8',
      capability: '#2A6070',
      policy: '#7AA8B8',
      brand: '#E85B8A',
    }
    return map[category] || '#7AA8B8'
  }

  return (
    <div className="bg-ocean-surface border border-ocean-border rounded-xl p-5 md:p-6">
      <div className="flex items-center justify-between mb-4">
        <h4 className="font-mono text-xs tracking-widest text-cyan uppercase">
          Per-Frame Fidelity
        </h4>
        <span className="font-mono text-[10px] text-text-dim">FFI by source frame</span>
      </div>
      <ResponsiveContainer width="100%" height={280}>
        <BarChart data={frameData} layout="vertical" margin={{ top: 0, right: 10, bottom: 0, left: 0 }}>
          <CartesianGrid stroke="#1a4050" strokeDasharray="3 3" horizontal={false} />
          <XAxis
            type="number"
            domain={[0, 100]}
            tick={{ fill: '#4A7080', fontSize: 10, fontFamily: 'IBM Plex Mono' }}
            axisLine={{ stroke: '#1a4050' }}
            tickLine={false}
            tickFormatter={(v) => `${v}%`}
          />
          <YAxis
            type="category"
            dataKey="short"
            width={140}
            tick={{ fill: '#7AA8B8', fontSize: 10, fontFamily: 'IBM Plex Mono' }}
            axisLine={false}
            tickLine={false}
          />
          <Tooltip
            contentStyle={{
              background: '#0D2B35',
              border: '1px solid #1a4050',
              borderRadius: 8,
              fontFamily: 'IBM Plex Mono',
              fontSize: 11,
            }}
            formatter={(value, name, props) => [
              `${value}% FFI (${props.payload.mention_count} mentions)`,
              props.payload.frame,
            ]}
          />
          <Bar dataKey="ffiPercent" radius={[0, 4, 4, 0]}>
            {frameData.map((entry, i) => (
              <Cell key={i} fill={barColor(entry.category)} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

function DriftExamples() {
  const examples = fidelityData.metrics.top_drift_examples.slice(0, 5)

  return (
    <div className="bg-ocean-surface border border-ocean-border rounded-xl p-5 md:p-6">
      <h4 className="font-mono text-xs tracking-widest text-cyan uppercase mb-4">
        Frame Drift Examples — Highest Semantic Distance
      </h4>
      <div className="space-y-3">
        {examples.map((ex, i) => (
          <div key={i} className="border-l-2 border-ocean-border pl-3 py-1">
            <div className="flex items-center gap-2 mb-1">
              <span className="font-mono text-[10px] text-text-dim uppercase tracking-wider">
                {ex.channel}
              </span>
              <span className="font-mono text-[10px] text-text-dim">
                {ex.period}
              </span>
              <span className="font-mono text-[10px] text-cyan">
                J={ex.jaccard}
              </span>
            </div>
            <div className="text-xs text-text-secondary">
              <span className="text-text-dim">Source:</span>{' '}
              <span className="italic">"{ex.source_frame}"</span>
            </div>
            <div className="text-xs text-text-secondary mt-0.5">
              <span className="text-text-dim">Became:</span>{' '}
              <span className="text-cyan">"{ex.downstream_text}"</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export function FramingFidelitySection() {
  const { ref, isInView } = useInView({ threshold: 0.1 })
  const { metrics } = fidelityData
  const overall = metrics.overall

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0 }}
      animate={isInView ? { opacity: 1 } : {}}
      transition={{ duration: 0.6 }}
      className="mt-20"
    >
      <h3 className="font-mono text-xs tracking-widest text-cyan uppercase mb-2">
        Framing Fidelity Analysis
      </h3>
      <p className="text-sm text-text-secondary mb-8 max-w-2xl">
        Quantified downstream fidelity effect — how well campaign-intended message
        frames survive propagation through press, social, policy, and academic channels
        across a 90-day campaign window. Scored via token-level Jaccard similarity.
      </p>

      {/* Summary stat row */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-8">
        {[
          { value: `${(overall.ffi * 100).toFixed(1)}%`, label: 'Overall FFI' },
          { value: overall.total_mentions.toLocaleString(), label: 'Mentions Scored' },
          { value: `${(overall.exact_rate * 100).toFixed(1)}%`, label: 'Exact Match Rate' },
          { value: `${(overall.drift_rate * 100).toFixed(1)}%`, label: 'Drift Rate' },
        ].map((stat, i) => (
          <motion.div
            key={stat.label}
            initial={{ opacity: 0, y: 15 }}
            animate={isInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.4, delay: i * 0.08 }}
            className="bg-ocean-surface border border-ocean-border rounded-lg p-4 text-center"
          >
            <div className="font-mono text-xl md:text-2xl font-bold text-cyan mb-1">{stat.value}</div>
            <div className="font-mono text-[10px] text-text-dim uppercase tracking-wider">{stat.label}</div>
          </motion.div>
        ))}
      </div>

      {/* Charts grid */}
      <div className="grid md:grid-cols-2 gap-4 mb-4">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          <FidelityDecayChart />
        </motion.div>
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.5, delay: 0.3 }}
        >
          <FramePerformanceBars />
        </motion.div>
      </div>

      {/* Drift examples */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={isInView ? { opacity: 1, y: 0 } : {}}
        transition={{ duration: 0.5, delay: 0.4 }}
      >
        <DriftExamples />
      </motion.div>

      {/* Insight callout */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={isInView ? { opacity: 1, y: 0 } : {}}
        transition={{ duration: 0.5, delay: 0.5 }}
        className="mt-6 bg-ocean-surface/50 border border-cyan/20 rounded-lg p-5"
      >
        <div className="flex gap-3">
          <span className="text-cyan text-lg shrink-0">→</span>
          <div>
            <p className="text-sm text-text-primary font-body leading-relaxed">
              <strong>Key insight:</strong> Policy and academic channels maintain 3× higher
              fidelity than social ({(metrics.by_channel.policy?.ffi * 100).toFixed(0)}% vs{' '}
              {(metrics.by_channel.social?.ffi * 100).toFixed(0)}% FFI). Social volume
              compensates — {metrics.by_channel.social?.mention_count.toLocaleString()} mentions
              at lower fidelity still drive awareness. The strategic implication: invest in
              press embargo precision (high-fidelity seeding) while accepting social drift
              as amplification cost.
            </p>
          </div>
        </div>
      </motion.div>
    </motion.div>
  )
}
