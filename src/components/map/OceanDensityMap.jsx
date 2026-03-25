import { useEffect, useRef, useState } from 'react'
import { motion } from 'framer-motion'
import { useInView } from '@/hooks/useInView'
import mapboxgl from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
import densityData from '@/data/plastic_density.json'

const MAPBOX_TOKEN = import.meta.env.VITE_MAPBOX_TOKEN || ''

export function OceanDensityMap() {
  const mapContainer = useRef(null)
  const map = useRef(null)
  const { ref: wrapperRef, isInView } = useInView({ threshold: 0.3, once: true })
  const [phase, setPhase] = useState(0) // 0=hidden, 1=base, 2=scanning, 3=revealed, 4=interactive
  const [hasLoaded, setHasLoaded] = useState(false)

  useEffect(() => {
    if (!isInView || map.current || !MAPBOX_TOKEN) return

    mapboxgl.accessToken = MAPBOX_TOKEN

    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/mapbox/dark-v11',
      center: [-150, 20],
      zoom: 2.5,
      minZoom: 1.5,
      maxZoom: 8,
      projection: 'mercator',
      attributionControl: false,
      interactive: false, // Disabled until phase 4
    })

    map.current.on('load', () => {
      setHasLoaded(true)

      // Add density data source
      map.current.addSource('plastic-density', {
        type: 'geojson',
        data: densityData,
      })

      // Phase 1: Base layer loads
      setPhase(1)

      // Phase 2: Scan sweep (1.5s delay)
      setTimeout(() => setPhase(2), 1500)

      // Phase 3: Density layer reveals (3s delay)
      setTimeout(() => {
        map.current.addLayer({
          id: 'density-heat',
          type: 'heatmap',
          source: 'plastic-density',
          paint: {
            'heatmap-weight': ['interpolate', ['linear'], ['get', 'density'], 0, 0, 1, 1],
            'heatmap-intensity': 1.2,
            'heatmap-color': [
              'interpolate',
              ['linear'],
              ['heatmap-density'],
              0, 'rgba(0,0,0,0)',
              0.1, 'rgba(13,43,53,0.3)',
              0.3, 'rgba(42,96,112,0.5)',
              0.5, 'rgba(232,91,138,0.6)',
              0.7, 'rgba(232,91,138,0.8)',
              0.9, 'rgba(42,96,112,0.85)',
              1, 'rgba(42,96,112,1)',
            ],
            'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 1, 15, 5, 30, 8, 50],
            'heatmap-opacity': 0,
          },
        })

        // Animate opacity in
        let opacity = 0
        const fadeIn = setInterval(() => {
          opacity = Math.min(1, opacity + 0.02)
          if (map.current) {
            map.current.setPaintProperty('density-heat', 'heatmap-opacity', opacity)
          }
          if (opacity >= 1) clearInterval(fadeIn)
        }, 30)

        setPhase(3)
      }, 3000)

      // Phase 4: Interactive (5s)
      setTimeout(() => {
        if (map.current) {
          map.current.scrollZoom.enable()
          map.current.dragPan.enable()
          map.current.dragRotate.enable()
          map.current.touchZoomRotate.enable()

          // Add circle layer for hover interaction
          map.current.addLayer({
            id: 'density-points',
            type: 'circle',
            source: 'plastic-density',
            paint: {
              'circle-radius': ['interpolate', ['linear'], ['zoom'], 1, 2, 5, 4, 8, 8],
              'circle-color': 'transparent',
              'circle-stroke-width': 0,
            },
          })

          // Popup on hover
          const popup = new mapboxgl.Popup({
            closeButton: false,
            closeOnClick: false,
            className: 'density-popup',
          })

          map.current.on('mouseenter', 'density-points', (e) => {
            map.current.getCanvas().style.cursor = 'pointer'
            const props = e.features[0].properties
            popup
              .setLngLat(e.features[0].geometry.coordinates)
              .setHTML(
                `<div style="font-family: IBM Plex Mono; font-size: 11px; color: #F5F0E8; background: #143545; border: 1px solid #1a4050; padding: 8px 12px; border-radius: 6px;">
                  <div style="color: #E85B8A; margin-bottom: 4px;">${props.category.toUpperCase()}</div>
                  <div>${props.particles_per_km2?.toLocaleString()} particles/km²</div>
                </div>`
              )
              .addTo(map.current)
          })

          map.current.on('mouseleave', 'density-points', () => {
            map.current.getCanvas().style.cursor = ''
            popup.remove()
          })
        }
        setPhase(4)
      }, 5000)
    })

    return () => {
      if (map.current) {
        map.current.remove()
        map.current = null
      }
    }
  }, [isInView])

  if (!MAPBOX_TOKEN) {
    return (
      <div ref={wrapperRef} className="relative w-full rounded-xl overflow-hidden bg-ocean-surface border border-ocean-border" style={{ height: 500 }}>
        <div className="absolute inset-0 flex items-center justify-center">
          <p className="font-mono text-sm text-text-dim">
            Map requires VITE_MAPBOX_TOKEN in .env
          </p>
        </div>
      </div>
    )
  }

  return (
    <div ref={wrapperRef} className="relative">
      <div
        ref={mapContainer}
        className="w-full rounded-xl overflow-hidden"
        style={{ height: 500 }}
      />

      {/* Scan line overlay */}
      {phase === 2 && (
        <motion.div
          className="absolute top-0 bottom-0 w-px bg-cyan pointer-events-none"
          style={{ boxShadow: '0 0 30px 10px rgba(232,91,138,0.15)' }}
          initial={{ left: '0%' }}
          animate={{ left: '100%' }}
          transition={{ duration: 1.5, ease: 'linear' }}
        />
      )}

      {/* Phase indicator */}
      {phase > 0 && phase < 4 && (
        <div className="absolute top-4 left-4 font-mono text-xs text-cyan/60">
          {phase === 1 && 'LOADING BASE LAYER...'}
          {phase === 2 && 'SCANNING...'}
          {phase === 3 && 'RENDERING DENSITY DATA...'}
        </div>
      )}

      {/* Interactive badge */}
      {phase === 4 && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="absolute top-4 right-4 font-mono text-xs text-cyan/60 bg-ocean-bg/80 px-3 py-1 rounded"
        >
          INTERACTIVE — PAN & ZOOM
        </motion.div>
      )}

      {/* Simulated data badge */}
      <div
        className="absolute bottom-4 left-4 font-mono text-xs px-2 py-1 rounded"
        style={{ background: 'rgba(13,43,53,0.85)', color: '#7AA8B8', border: '0.5px solid #1a4050' }}
      >
        Simulated data for portfolio purposes
      </div>
    </div>
  )
}
