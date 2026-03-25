import { ChapterWrapper } from '@/components/layout/ChapterWrapper'
import { RevealOnScroll } from '@/components/ui/RevealOnScroll'
import { StatCard } from '@/components/ui/StatCard'
import { SearchTrendsChart } from '@/components/charts/SearchTrendsChart'
import { BrandwatchChart } from '@/components/charts/BrandwatchChart'
import { WordFrequencyChart } from '@/components/charts/WordFrequencyChart'
import { VocabularyGapChart } from '@/components/charts/VocabularyGapChart'

export function Chapter1() {
  return (
    <ChapterWrapper
      id="the-signal"
      label="Chapter 1"
      title="The Signal"
      subtitle={'"Before we wrote a single word, we listened."'}
    >
      {/* Intro text */}
      <RevealOnScroll className="mb-16 max-w-3xl">
        <p className="text-text-secondary leading-relaxed">
          Great communications strategy starts with intelligence, not instinct.
          We pulled social listening data, search trends, Reddit discourse, and
          keyword landscapes to understand how people actually talk about ocean
          plastic — and where the gaps are between scientific language and public
          understanding.
        </p>
      </RevealOnScroll>

      {/* Stats row */}
      <RevealOnScroll className="mb-20">
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
          <StatCard value={1053557} label="Social Mentions" suffix="+" delay={0} />
          <StatCard value={8} label="Keywords Tracked" delay={0.1} />
          <StatCard value={4} label="Subreddits Mined" delay={0.2} />
          <StatCard value={727} label="Unique Terms" delay={0.3} />
        </div>
      </RevealOnScroll>

      {/* Social Listening Chart */}
      <RevealOnScroll className="mb-20">
        <div className="bg-ocean-surface border border-ocean-border rounded-xl p-6 md:p-8">
          <BrandwatchChart />
        </div>
      </RevealOnScroll>

      {/* Search Trends Chart */}
      <RevealOnScroll className="mb-20">
        <div className="bg-ocean-surface border border-ocean-border rounded-xl p-6 md:p-8">
          <SearchTrendsChart />
        </div>
      </RevealOnScroll>

      {/* Word Frequency */}
      <RevealOnScroll className="mb-20">
        <div className="bg-ocean-surface border border-ocean-border rounded-xl p-6 md:p-8">
          <WordFrequencyChart />
        </div>
      </RevealOnScroll>

      {/* Vocabulary Gap Analysis */}
      <RevealOnScroll className="mb-12">
        <VocabularyGapChart />
      </RevealOnScroll>
    </ChapterWrapper>
  )
}
