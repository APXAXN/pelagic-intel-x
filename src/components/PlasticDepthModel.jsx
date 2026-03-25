import { useRef, useEffect, useState, useCallback, useMemo } from 'react'

/* ------------------------------------------------------------------ */
/*  Particle generation                                                */
/* ------------------------------------------------------------------ */

function generateParticles(count = 4200) {
  const clusters = [
    { name: 'North Pacific Gyre',   cx: -40, cz: -20 },
    { name: 'Western Pacific Drift', cx:  30, cz:  15 },
    { name: 'Equatorial Scatter',    cx: -10, cz:  50 },
  ]

  const positions = new Float32Array(count * 3)
  const colors    = new Float32Array(count * 3)
  const depths    = new Float32Array(count)
  const clusterIds = new Uint8Array(count)

  const gauss = () => {
    let u = 0, v = 0
    while (u === 0) u = Math.random()
    while (v === 0) v = Math.random()
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v)
  }

  // Colors — Ai2 Dark palette
  const pink = [232 / 255, 91 / 255, 138 / 255]   // #E85B8A surface
  const deep = [20 / 255, 53 / 255, 69 / 255]      // #143545 depth
  const teal = [42 / 255, 96 / 255, 112 / 255]      // #2A6070 peak density core

  for (let i = 0; i < count; i++) {
    const ci = i % clusters.length
    const cluster = clusters[ci]
    clusterIds[i] = ci

    // Depth distribution
    const r = Math.random()
    let depth
    if (r < 0.55) depth = Math.random() * 50          // 0-50m neuston
    else if (r < 0.80) depth = 60 + Math.random() * 70 // 60-130m pycnocline
    else depth = 130 + Math.random() * 70               // 130-200m deep

    depths[i] = depth

    const spread = 30 + depth * 0.6
    const x = cluster.cx + gauss() * spread * 0.5
    const z = cluster.cz + gauss() * spread * 0.5
    const y = -(depth * 0.6)

    positions[i * 3]     = x
    positions[i * 3 + 1] = y
    positions[i * 3 + 2] = z

    // Color by depth
    const t = Math.min(depth / 200, 1)

    // Teal tint for core cluster 0, surface
    const distToC0 = Math.sqrt((x - clusters[0].cx) ** 2 + (z - clusters[0].cz) ** 2)
    const isCore = ci === 0 && distToC0 < 25 && depth < 60

    if (isCore) {
      const gt = 0.5 + t * 0.5
      colors[i * 3]     = teal[0] * (1 - gt) + deep[0] * gt
      colors[i * 3 + 1] = teal[1] * (1 - gt) + deep[1] * gt
      colors[i * 3 + 2] = teal[2] * (1 - gt) + deep[2] * gt
    } else {
      colors[i * 3]     = pink[0] * (1 - t) + deep[0] * t
      colors[i * 3 + 1] = pink[1] * (1 - t) + deep[1] * t
      colors[i * 3 + 2] = pink[2] * (1 - t) + deep[2] * t
    }
  }

  return { positions, colors, depths, clusterIds, clusters, count }
}

/* ------------------------------------------------------------------ */
/*  Component                                                          */
/* ------------------------------------------------------------------ */

export default function PlasticDepthModel() {
  const containerRef = useRef(null)
  const canvasRef    = useRef(null)
  const stateRef     = useRef({})      // mutable state for animation loop

  const [maxDepth, setMaxDepth]   = useState(200)
  const [opacity, setOpacity]     = useState(80)
  const [autoRot, setAutoRot]     = useState(true)
  const [visibleCount, setVisibleCount] = useState(4200)
  const [tooltip, setTooltip]     = useState(null)

  const particleData = useMemo(() => generateParticles(4200), [])

  /* ---- depth label ---- */
  const peakLabel = maxDepth <= 50
    ? 'Surface neuston'
    : maxDepth <= 120
      ? 'Pycnocline band'
      : 'Full column'

  /* ---- Three.js setup & loop ---- */
  useEffect(() => {
    let cancelled = false
    let animId

    async function init() {
      const THREE = await import('three')
      if (cancelled) return

      const container = containerRef.current
      const canvas    = canvasRef.current
      if (!container || !canvas) return

      const W = container.clientWidth
      const H = Math.round(W * 9 / 16)
      canvas.width  = W * devicePixelRatio
      canvas.height = H * devicePixelRatio
      canvas.style.width  = W + 'px'
      canvas.style.height = H + 'px'

      /* renderer */
      const renderer = new THREE.WebGLRenderer({
        canvas,
        antialias: true,
        alpha: false,
      })
      renderer.setSize(W, H)
      renderer.setPixelRatio(devicePixelRatio)
      renderer.setClearColor(0x0D2B35, 1)

      /* scene & camera */
      const scene  = new THREE.Scene()
      const camera = new THREE.PerspectiveCamera(45, W / H, 0.1, 2000)
      camera.position.set(0, 60, 280)
      camera.lookAt(0, -30, 0)

      /* wireframe grid at y=2 */
      const gridGeo  = new THREE.PlaneGeometry(220, 220, 30, 30)
      const gridMat  = new THREE.MeshBasicMaterial({
        color: 0x1a4050,
        wireframe: true,
        transparent: true,
        opacity: 0.3,
      })
      const gridMesh = new THREE.Mesh(gridGeo, gridMat)
      gridMesh.rotation.x = -Math.PI / 2
      gridMesh.position.y = 2
      scene.add(gridMesh)

      /* depth marker lines */
      const markerDepths = [0, 50, 100, 150, 200]
      markerDepths.forEach((d) => {
        const y = -(d * 0.6)
        const lineGeo = new THREE.BufferGeometry()
        const pts = new Float32Array([
          -110, y, -110,
           110, y, -110,
           110, y,  110,
          -110, y,  110,
          -110, y, -110,
        ])
        lineGeo.setAttribute('position', new THREE.BufferAttribute(pts, 3))
        const lineMat = new THREE.LineBasicMaterial({
          color: 0x1a4050,
          transparent: true,
          opacity: 0.5,
        })
        scene.add(new THREE.Line(lineGeo, lineMat))
      })

      /* particles */
      const geo = new THREE.BufferGeometry()
      const posBuf   = new Float32Array(particleData.positions)
      const colorBuf = new Float32Array(particleData.colors)
      geo.setAttribute('position', new THREE.BufferAttribute(posBuf, 3))
      geo.setAttribute('color',    new THREE.BufferAttribute(colorBuf, 3))

      const mat = new THREE.PointsMaterial({
        size: 2.2,
        vertexColors: true,
        transparent: true,
        opacity: 0.8,
        sizeAttenuation: true,
        depthWrite: false,
      })

      const points = new THREE.Points(geo, mat)
      scene.add(points)

      /* raycaster */
      const raycaster = new THREE.Raycaster()
      raycaster.params.Points.threshold = 4
      const mouse = new THREE.Vector2(9999, 9999)

      /* orbit state */
      const S = stateRef.current
      S.theta   = 0
      S.tilt    = 0.25
      S.radius  = 280
      S.autoRot = true
      S.maxDepth = 200
      S.opacity  = 0.8
      S.renderer = renderer
      S.dragging = false
      S.lastMouse = { x: 0, y: 0 }

      /* pointer events */
      const onPointerDown = (e) => {
        S.dragging = true
        S.lastMouse = { x: e.clientX, y: e.clientY }
        S.autoRot = false
      }
      const onPointerMove = (e) => {
        const rect = canvas.getBoundingClientRect()
        mouse.x =  ((e.clientX - rect.left) / rect.width)  * 2 - 1
        mouse.y = -((e.clientY - rect.top)  / rect.height) * 2 + 1

        if (S.dragging) {
          const dx = e.clientX - S.lastMouse.x
          const dy = e.clientY - S.lastMouse.y
          S.theta -= dx * 0.005
          S.tilt  = Math.max(-0.1, Math.min(0.6, S.tilt + dy * 0.003))
          S.lastMouse = { x: e.clientX, y: e.clientY }
        }
      }
      const onPointerUp = () => { S.dragging = false }
      const onPointerLeave = () => {
        S.dragging = false
        mouse.x = 9999
        mouse.y = 9999
      }

      canvas.addEventListener('pointerdown', onPointerDown)
      canvas.addEventListener('pointermove', onPointerMove)
      canvas.addEventListener('pointerup',   onPointerUp)
      canvas.addEventListener('pointerleave', onPointerLeave)

      /* resize */
      const onResize = () => {
        if (!container) return
        const w = container.clientWidth
        const h = Math.round(w * 9 / 16)
        renderer.setSize(w, h)
        canvas.style.width  = w + 'px'
        canvas.style.height = h + 'px'
        camera.aspect = w / h
        camera.updateProjectionMatrix()
      }
      window.addEventListener('resize', onResize)

      /* animation loop */
      let frameCount = 0
      const clusterNames = ['North Pacific Gyre', 'Western Pacific Drift', 'Equatorial Scatter']

      function animate() {
        if (cancelled) return
        animId = requestAnimationFrame(animate)

        // auto-rotate
        if (S.autoRot) S.theta += 0.004

        // orbit camera
        const cy = S.radius * Math.sin(S.tilt)
        const flatR = S.radius * Math.cos(S.tilt)
        camera.position.set(
          flatR * Math.sin(S.theta),
          60 + cy * 0.5,
          flatR * Math.cos(S.theta),
        )
        camera.lookAt(0, -30, 0)

        // depth filter
        const posAttr = geo.attributes.position
        let visible = 0
        for (let i = 0; i < particleData.count; i++) {
          if (particleData.depths[i] <= S.maxDepth) {
            posAttr.array[i * 3]     = particleData.positions[i * 3]
            posAttr.array[i * 3 + 1] = particleData.positions[i * 3 + 1]
            posAttr.array[i * 3 + 2] = particleData.positions[i * 3 + 2]
            visible++
          } else {
            posAttr.array[i * 3] = 9999
            posAttr.array[i * 3 + 1] = 9999
            posAttr.array[i * 3 + 2] = 9999
          }
        }
        posAttr.needsUpdate = true

        // opacity
        mat.opacity = S.opacity

        // raycasting (every 3rd frame)
        frameCount++
        if (frameCount % 3 === 0 && mouse.x < 900) {
          raycaster.setFromCamera(mouse, camera)
          const hits = raycaster.intersectObject(points)
          if (hits.length > 0) {
            const idx = hits[0].index
            const depth = particleData.depths[idx]
            const ci = particleData.clusterIds[idx]
            const rect = canvas.getBoundingClientRect()
            const sx = ((mouse.x + 1) / 2) * rect.width
            const sy = ((1 - mouse.y) / 2) * rect.height
            S.tooltip = {
              x: sx,
              y: sy,
              depth: Math.round(depth),
              zone: clusterNames[ci],
              density: (Math.random() * 400 + 50 + (200 - depth) * 2).toFixed(0),
            }
          } else {
            S.tooltip = null
          }
        }

        // batch React state updates (every 10th frame)
        if (frameCount % 10 === 0) {
          setVisibleCount(visible)
          setTooltip(S.tooltip || null)
        }

        renderer.render(scene, camera)
      }

      animate()

      S._cleanup = () => {
        cancelled = true
        cancelAnimationFrame(animId)
        canvas.removeEventListener('pointerdown', onPointerDown)
        canvas.removeEventListener('pointermove', onPointerMove)
        canvas.removeEventListener('pointerup',   onPointerUp)
        canvas.removeEventListener('pointerleave', onPointerLeave)
        window.removeEventListener('resize', onResize)
        geo.dispose()
        mat.dispose()
        gridGeo.dispose()
        gridMat.dispose()
        renderer.dispose()
      }
    }

    init()

    return () => {
      cancelled = true
      if (stateRef.current._cleanup) stateRef.current._cleanup()
    }
  }, [particleData])

  /* ---- sync React state → mutable ref ---- */
  useEffect(() => { stateRef.current.maxDepth = maxDepth }, [maxDepth])
  useEffect(() => { stateRef.current.opacity  = opacity / 100 }, [opacity])
  useEffect(() => { stateRef.current.autoRot  = autoRot }, [autoRot])

  /* ---- handlers ---- */
  const handleSurface  = useCallback(() => setMaxDepth(50),  [])
  const handleDeepCut  = useCallback(() => setMaxDepth(200), [])
  const toggleAutoRot  = useCallback(() => setAutoRot(p => !p), [])

  return (
    <div
      ref={containerRef}
      className="relative w-full rounded-xl overflow-hidden select-none"
      style={{ background: '#0D2B35', aspectRatio: '16/9' }}
    >
      <canvas ref={canvasRef} className="block w-full h-full" />

      {/* Badge top-left */}
      <div className="absolute top-3 left-3 px-2.5 py-1 rounded bg-black/50 backdrop-blur-sm">
        <span className="font-mono text-[10px] tracking-wider text-[#7AA8B8] uppercase">
          Central Pacific Gyre — Depth Profile
        </span>
      </div>

      {/* Badge top-right */}
      <div className="absolute top-3 right-3 px-2.5 py-1 rounded bg-black/50 backdrop-blur-sm">
        <span className="font-mono text-[10px] tracking-wider text-[#2A6070] uppercase">
          ⚠ Simulated Data — Portfolio
        </span>
      </div>

      {/* Stats panel */}
      <div className="absolute top-11 left-3 px-2.5 py-2 rounded bg-black/40 backdrop-blur-sm space-y-1">
        <div className="font-mono text-[11px] text-[#7AA8B8]">
          PARTICLES: <span className="text-[#E85B8A]">{visibleCount.toLocaleString()}</span>
        </div>
        <div className="font-mono text-[11px] text-[#7AA8B8]">
          DEPTH RANGE: <span className="text-[#E85B8A]">0–{maxDepth}m</span>
        </div>
        <div className="font-mono text-[11px] text-[#7AA8B8]">
          PEAK ZONE: <span className="text-[#E85B8A]">{peakLabel}</span>
        </div>
      </div>

      {/* Tooltip */}
      {tooltip && (
        <div
          className="absolute pointer-events-none px-3 py-2 rounded bg-black/80 backdrop-blur-sm border border-[#E85B8A]/30"
          style={{ left: tooltip.x + 12, top: tooltip.y - 20 }}
        >
          <div className="font-mono text-[10px] text-[#7AA8B8] uppercase mb-0.5">
            {tooltip.zone}
          </div>
          <div className="font-mono text-[11px] text-[#E85B8A]">
            DEPTH: {tooltip.depth}m
          </div>
          <div className="font-mono text-[11px] text-[#2A6070]">
            DENSITY: {tooltip.density} items/m³
          </div>
        </div>
      )}

      {/* Controls panel */}
      <div
        className="absolute bottom-0 left-0 right-0 px-5 pt-10 pb-4"
        style={{ background: 'linear-gradient(transparent, rgba(13,43,53,0.95))' }}
      >
        <div className="flex flex-wrap items-end gap-6">
          {/* Max Depth slider */}
          <label className="flex flex-col gap-1.5 flex-1 min-w-[140px]">
            <span className="font-mono text-[11px] text-[#7AA8B8] tracking-wider uppercase">
              Max Depth <span className="text-[#E85B8A]">{maxDepth}m</span>
            </span>
            <input
              type="range"
              min={20}
              max={200}
              step={10}
              value={maxDepth}
              onChange={(e) => setMaxDepth(Number(e.target.value))}
              className="accent-[#E85B8A] h-1 cursor-pointer"
            />
          </label>

          {/* Opacity slider */}
          <label className="flex flex-col gap-1.5 flex-1 min-w-[120px]">
            <span className="font-mono text-[11px] text-[#7AA8B8] tracking-wider uppercase">
              Opacity <span className="text-[#E85B8A]">{opacity}%</span>
            </span>
            <input
              type="range"
              min={20}
              max={100}
              step={5}
              value={opacity}
              onChange={(e) => setOpacity(Number(e.target.value))}
              className="accent-[#E85B8A] h-1 cursor-pointer"
            />
          </label>

          {/* Buttons */}
          <div className="flex gap-2">
            <button
              onClick={toggleAutoRot}
              className={`font-mono text-[11px] tracking-wider uppercase px-3 py-1.5 rounded border transition-colors cursor-pointer ${
                autoRot
                  ? 'border-[#E85B8A]/50 text-[#E85B8A] bg-[#E85B8A]/10'
                  : 'border-[#7AA8B8]/30 text-[#7AA8B8] bg-transparent'
              }`}
            >
              Auto Rot
            </button>
            <button
              onClick={handleSurface}
              className="font-mono text-[11px] tracking-wider uppercase px-3 py-1.5 rounded border border-[#7AA8B8]/30 text-[#7AA8B8] hover:text-[#E85B8A] hover:border-[#E85B8A]/50 transition-colors cursor-pointer"
            >
              Surface
            </button>
            <button
              onClick={handleDeepCut}
              className="font-mono text-[11px] tracking-wider uppercase px-3 py-1.5 rounded border border-[#7AA8B8]/30 text-[#7AA8B8] hover:text-[#E85B8A] hover:border-[#E85B8A]/50 transition-colors cursor-pointer"
            >
              Deep Cut
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
