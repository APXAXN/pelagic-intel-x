import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, Cell } from 'recharts'
import brandwatchData from '@/data/brandwatch_mentions.json'

const TOPIC_COLORS = {
  'ocean plastic pollution': '#00D4FF',
  'microplastics': '#E8C547',
  'ocean cleanup technology': '#4ECDC4',
  'plastic pollution regulation': '#FF6B6B',
  'marine debris': '#8899AA',
  'AI environmental monitoring': '#A78BFA',
}

const SHORT_LABELS = {
  'ocean plastic pollution': 'Ocean Plastic',
  'microplastics': 'Microplastics',
  'ocean cleanup technology': 'Cleanup Tech',
  'plastic pollution regulation': 'Regulation',
  'marine debris': 'Marine Debris',
  'AI environmental monitoring': 'AI Monitoring',
}

function CustomTooltip({ active, payload }) {
  if (!active || !payload?.[0]) return null
  const d = payload[0].payload
  return (
    <div className="bg-ocean-surface border border-ocean-border rounded-lg p-3 shadow-lg">
      <p className="font-mono text-xs text-text-primary mb-1">{d.topic}</p>
      <p className="font-mono text-xs text-cyan">{d.mentions.toLocaleString()} mentions</p>
    </div>
  )
}

export function BrandwatchChart() {
  const { topic_totals } = brandwatchData.summary

  const data = Object.entries(topic_totals).map(([topic, mentions]) => ({
    topic,
    label: SHORT_LABELS[topic] || topic,
    mentions,
    color: TOPIC_COLORS[topic] || '#8899AA',
  }))

  return (
    <div>
      <h4 className="font-mono text-xs tracking-widest text-text-secondary uppercase mb-4">
        Social Listening — Mention Volume by Topic (12 Months)
      </h4>
      <ResponsiveContainer width="100%" height={320}>
        <BarChart data={data} layout="vertical" margin={{ top: 5, right: 30, left: 10, bottom: 5 }}>
          <CartesianGrid stroke="#1a2535" strokeDasharray="3 3" horizontal={false} />
          <XAxis
            type="number"
            tick={{ fill: '#5A6A7A', fontSize: 11, fontFamily: 'IBM Plex Mono' }}
            tickLine={false}
            axisLine={{ stroke: '#1a2535' }}
            tickFormatter={(v) => `${(v / 1000).toFixed(0)}k`}
          />
          <YAxis
            type="category"
            dataKey="label"
            tick={{ fill: '#8899AA', fontSize: 11, fontFamily: 'IBM Plex Mono' }}
            tickLine={false}
            axisLine={false}
            width={110}
          />
          <Tooltip content={<CustomTooltip />} cursor={{ fill: 'rgba(0,212,255,0.05)' }} />
          <Bar dataKey="mentions" radius={[0, 4, 4, 0]} barSize={24}>
            {data.map((entry, i) => (
              <Cell key={i} fill={entry.color} fillOpacity={0.85} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
