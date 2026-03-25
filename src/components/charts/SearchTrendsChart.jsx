import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts'
import searchTrends from '@/data/search_trends.json'

const COLORS = {
  'ocean plastic': '#00D4FF',
  'microplastics': '#E8C547',
  'plastic pollution': '#8899AA',
  'ocean cleanup': '#4ECDC4',
  'marine debris': '#6B7280',
}

function CustomTooltip({ active, payload, label }) {
  if (!active || !payload) return null
  return (
    <div className="bg-ocean-surface border border-ocean-border rounded-lg p-3 shadow-lg">
      <p className="font-mono text-xs text-text-secondary mb-2">{label}</p>
      {payload.map((entry) => (
        <p key={entry.name} className="font-mono text-xs" style={{ color: entry.color }}>
          {entry.name}: {entry.value}
        </p>
      ))}
    </div>
  )
}

export function SearchTrendsChart() {
  const data = searchTrends.interest_over_time
  const keywords = Object.keys(data).filter(k => COLORS[k])

  // Merge all keywords into a single array of {date, keyword1, keyword2, ...}
  const merged = data[keywords[0]]?.map((point, i) => {
    const entry = { date: point.date.slice(0, 7) } // YYYY-MM
    keywords.forEach(kw => {
      entry[kw] = data[kw]?.[i]?.value ?? 0
    })
    return entry
  }) ?? []

  // Sample every 4th point to avoid overcrowding
  const sampled = merged.filter((_, i) => i % 4 === 0)

  return (
    <div>
      <h4 className="font-mono text-xs tracking-widest text-text-secondary uppercase mb-4">
        Google Trends — Search Interest Over Time (5 Years)
      </h4>
      <ResponsiveContainer width="100%" height={320}>
        <LineChart data={sampled} margin={{ top: 5, right: 10, left: -10, bottom: 5 }}>
          <CartesianGrid stroke="#1a2535" strokeDasharray="3 3" />
          <XAxis
            dataKey="date"
            tick={{ fill: '#5A6A7A', fontSize: 11, fontFamily: 'IBM Plex Mono' }}
            tickLine={false}
            axisLine={{ stroke: '#1a2535' }}
            interval="preserveStartEnd"
          />
          <YAxis
            tick={{ fill: '#5A6A7A', fontSize: 11, fontFamily: 'IBM Plex Mono' }}
            tickLine={false}
            axisLine={false}
            domain={[0, 100]}
          />
          <Tooltip content={<CustomTooltip />} />
          {keywords.map(kw => (
            <Line
              key={kw}
              type="monotone"
              dataKey={kw}
              stroke={COLORS[kw]}
              strokeWidth={kw === 'microplastics' ? 2.5 : 1.5}
              dot={false}
              opacity={kw === 'microplastics' || kw === 'ocean plastic' ? 1 : 0.6}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
      <div className="flex flex-wrap gap-4 mt-4 justify-center">
        {keywords.map(kw => (
          <div key={kw} className="flex items-center gap-2">
            <div className="w-3 h-0.5 rounded" style={{ backgroundColor: COLORS[kw] }} />
            <span className="font-mono text-xs text-text-secondary">{kw}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
