import { createContext, useContext, useState, useEffect } from 'react'

const AccessibilityContext = createContext()

export function AccessibilityProvider({ children }) {
  const [highContrast, setHighContrast] = useState(false)

  useEffect(() => {
    document.documentElement.setAttribute(
      'data-theme',
      highContrast ? 'high-contrast' : 'branded'
    )
  }, [highContrast])

  return (
    <AccessibilityContext.Provider value={{ highContrast, setHighContrast }}>
      {children}
    </AccessibilityContext.Provider>
  )
}

export function useAccessibility() {
  return useContext(AccessibilityContext)
}
