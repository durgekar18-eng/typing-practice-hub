# Typer's Club — Complete Technical Specification v1.2
## Pixel-Perfect Recreation Blueprint

---

## TABLE OF CONTENTS

1. [Project Architecture](#1-project-architecture)
2. [Technology Stack](#2-technology-stack)
3. [Design System — Colors](#3-design-system--colors)
4. [Design System — Typography](#4-design-system--typography)
5. [Design System — Spacing & Layout](#5-design-system--spacing--layout)
6. [Design System — Borders, Radius, Shadows](#6-design-system--borders-radius-shadows)
7. [Design System — CSS Custom Properties (Complete Map)](#7-design-system--css-custom-properties)
8. [Theme System (5 Themes)](#8-theme-system-5-themes)
9. [CSS Animations & Keyframes](#9-css-animations--keyframes)
10. [Framer Motion Animations](#10-framer-motion-animations)
11. [WebGL Neural Vortex Background](#11-webgl-neural-vortex-background)
12. [SVG Wave Background](#12-svg-wave-background)
13. [Component Architecture](#13-component-architecture)
14. [Page Views (11 SPA Views)](#14-page-views)
15. [Navigation System — Animated Dock](#15-navigation-system--animated-dock)
16. [Typing Engine — Core Logic](#16-typing-engine--core-logic)
17. [Lesson Content — 33 Lessons × ~15 Sub-Chapters](#17-lesson-content)
18. [Authentication System](#18-authentication-system)
19. [Data Persistence — localStorage Schema](#19-data-persistence--localstorage-schema)
20. [API Routes](#20-api-routes)
21. [PWA Configuration](#21-pwa-configuration)
22. [SEO & Meta Tags](#22-seo--meta-tags)
23. [Responsive Breakpoints](#23-responsive-breakpoints)
24. [All Lucide Icons Used](#24-all-lucide-icons-used)
25. [File Structure](#25-file-structure)
26. [Dependencies — Exact Versions](#26-dependencies--exact-versions)

---

## 1. PROJECT ARCHITECTURE

- **Framework**: Next.js 16.1.3 with App Router
- **Pattern**: Single-Page Application (SPA) inside a single route (`/`)
- **Routing**: Client-side state-based (`AppView` union type), NO URL-based routing
- **Rendering**: All components are `'use client'` — zero server-side rendering of UI
- **Output**: `standalone` (Docker-ready)
- **Language**: TypeScript 5, strict mode disabled (`noImplicitAny: false`)
- **React**: v19.0.0
- **React Strict Mode**: DISABLED (`reactStrictMode: false`)
- **Port**: 3000 (development), 81 (Caddy gateway)

### SPA View State Machine

```typescript
type AppView = 
  | 'calibrating'    // Initial splash screen (3 seconds)
  | 'home'           // Hero + CurriculumGrid + StatsSection + PerformanceGraph + Footer
  | 'typing'         // Full-screen typing practice
  | 'learn'          // Phase/lesson/sub-chapter navigation
  | 'speedtest'      // Timed speed test
  | 'profile'        // Auth (login/signup/OTP) + profile card + stats
  | 'settings'       // Theme picker + reset data
  | 'leaderboard'    // Mock leaderboard with user insertion
  | 'progress'       // Full performance graph
  | 'download'       // PWA download/install page
  | 'custompractice' // User-pasted text practice
```

---

## 2. TECHNOLOGY STACK

| Category | Technology | Version |
|----------|-----------|---------|
| Framework | Next.js | ^16.1.1 |
| Language | TypeScript | ^5 |
| React | React | ^19.0.0 |
| Styling | Tailwind CSS | ^4 (v4-native PostCSS plugin) |
| UI Components | shadcn/ui (New York style) | — |
| Icons | lucide-react | ^0.525.0 |
| Animation | framer-motion | ^12.23.2 |
| GSAP | gsap | ^3.14.2 |
| Noise | simplex-noise | ^4.0.3 |
| State | React useState/useCallback | — |
| Database | Prisma + SQLite | ^6.11.1 (UNUSED in app) |
| Auth (Google) | Firebase | ^12.12.0 |
| Email (OTP) | nodemailer | ^8.0.5 |
| PDF | pdf-parse | ^2.4.5 |
| DOCX | mammoth | ^1.12.0 |
| Toast | sonner | ^2.0.6 |
| Mobile Detection | Custom hook (768px) | — |

---

## 3. DESIGN SYSTEM — COLORS

### Base Color Palette (Dark Theme Default)

| Token | Value | Usage |
|-------|-------|-------|
| `--tc-bg` | `hsl(0 0% 4%)` | Page background (~#0a0a0a) |
| `--tc-surface` | `hsl(0 0% 8%)` | Card/panel background (~#141414) |
| `--tc-text` | `hsl(0 0% 96%)` | Primary text (~#f5f5f5) |
| `--tc-muted` | `hsl(0 0% 53%)` | Secondary/muted text (~#878787) |
| `--tc-stroke` | `hsl(0 0% 12%)` | Borders/dividers (~#1f1f1f) |
| `--tc-accent` | `#89AACC` | Primary accent (steel blue) |
| `--tc-accent-from` | `#89AACC` | Gradient start |
| `--tc-accent-to` | `#4E85BF` | Gradient end (deeper blue) |
| `--tc-accent-rgb` | `137, 170, 204` | For rgba() calculations |

### Accent Opacity Variants (Derived)

| Token | Value | Usage |
|-------|-------|-------|
| `--tc-accent-08` | `rgba(137, 170, 204, 0.08)` | Subtle backgrounds |
| `--tc-accent-10` | `rgba(137, 170, 204, 0.10)` | Hover states |
| `--tc-accent-15` | `rgba(137, 170, 204, 0.15)` | Active indicators, badge bg |
| `--tc-accent-20` | `rgba(137, 170, 204, 0.20)` | Border highlights |
| `--tc-accent-30` | `rgba(137, 170, 204, 0.30)` | Strong accents, glows |
| `--tc-accent-33` | `rgba(137, 170, 204, 0.33)` | Borders |
| `--tc-accent-44` | `rgba(137, 170, 204, 0.44)` | Completed line fill |

### Typing-Specific Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--tc-correct-past` | `hsl(0 0% 40%)` | Correctly typed characters |
| `--tc-incorrect-past` | `hsl(0 85% 60%)` | Incorrectly typed characters (red) |
| `--tc-future-text` | `hsl(0 0% 60%)` | Untyped characters |
| `--tc-current-text` | `hsl(0 0% 96%)` | Current active character |
| `--tc-cursor` | `linear-gradient(90deg, #89AACC, #4E85BF)` | Cursor highlight |

### Keyboard Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--tc-keyboard-bg` | `hsl(0 0% 6%)` | Keyboard container |
| `--tc-keyboard-key-bg` | `hsl(0 0% 10%)` | Individual key |
| `--tc-keyboard-key-border` | `hsl(0 0% 18%)` | Key border |
| `--tc-keyboard-active-bg` | `rgba(137, 170, 204, 0.25)` | Active key highlight |

### Gradient Definitions

| Name | Value | Usage |
|------|-------|-------|
| Hero gradient | `linear-gradient(to bottom, #0a0e1a, #0d1117, hsl(0 0% 4%))` | Hero section background |
| Footer gradient | `linear-gradient(to top, #0a0e1a, hsl(0 0% 4%))` | Footer background |
| Accent gradient | `linear-gradient(90deg, var(--tc-accent-from), var(--tc-accent-to))` | Buttons, progress bars |
| Cursor gradient | `linear-gradient(90deg, var(--tc-accent-from), var(--tc-accent-to))` | Typing cursor |
| Selection | `background: var(--tc-accent-30); color: white` | Text selection |

### shadcn/ui Semantic Colors (Dark Theme)

| Token | Value |
|-------|-------|
| `--background` | `oklch(0.145 0 0)` |
| `--foreground` | `oklch(0.985 0 0)` |
| `--primary` | `hsl(var(--tc-text))` |
| `--primary-foreground` | `hsl(var(--tc-bg))` |
| `--secondary` | `hsl(var(--tc-surface))` |
| `--destructive` | `oklch(0.704 0.191 22.216)` |
| `--border` | `hsl(var(--tc-stroke))` |
| `--ring` | `hsl(var(--tc-muted))` |

---

## 4. DESIGN SYSTEM — TYPOGRAPHY

### Font Families

| Font | Source | Weights | Usage |
|------|--------|---------|-------|
| Inter | Google Fonts | 300, 400, 500, 600, 700 | Body text, buttons, labels, UI |
| Instrument Serif | Google Fonts | italic (ital@0;1) | Display headings, decorative text |

### Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet" />
```

### Typography Scale (by Component)

| Element | Class | Size | Weight | Letter-Spacing |
|---------|-------|------|--------|----------------|
| Hero h1 | `text-5xl md:text-7xl lg:text-8xl font-light` | 48/72/96px | 300 | — |
| Hero italic word | Inline style `fontFamily: 'Instrument Serif'` | Same | 300 | — |
| Hero eyebrow | `text-xs tracking-[0.3em] uppercase` | 12px | 400 | 0.3em |
| Hero subheading | `text-base md:text-lg` | 16/18px | 400 | — |
| Section h2 | `text-3xl md:text-5xl font-light` | 30/48px | 300 | — |
| Section italic word | `fontFamily: 'Instrument Serif', italic` | Same | 300 | — |
| Section description | `text-base md:text-lg` | 16/18px | 400 | — |
| Card title | `text-lg md:text-xl font-semibold` | 18/20px | 600 | — |
| Card subtitle | `text-sm` | 14px | 400 | — |
| Card stat | `text-4xl md:text-6xl font-light` | 36/60px | 300 | — |
| Body text | `text-base` | 16px | 400 | — |
| Small text | `text-sm` | 14px | 400 | — |
| Caption | `text-xs` | 12px | 400 | — |
| Badge/label | `text-[10px] tracking-[0.2em] uppercase font-semibold` | 10px | 600 | 0.2em |
| Button primary | `text-sm font-medium` | 14px | 500 | — |
| Button nav | — | 22px (icon size) | — | — |
| Typing text | `text-xl sm:text-2xl md:text-3xl` | 20/24/30px | 400 | — |
| Typing text line-height | `md:leading-loose` | — | — | 2 (loose) |
| Marquee text | `text-6xl md:text-8xl font-light` | 60/96px | 300 | — |
| Counter display | `text-sm tabular-nums monospace` | 14px | 400 | — |
| OTP digits | `text-4xl md:text-5xl font-mono font-bold tracking-[0.25em]` | 36/48px | 700 | 0.25em |
| Keyboard labels | SVG text | — | — | — |
| Tooltip text | `text-[11px] font-medium tracking-wide` | 11px | 500 | wide |
| Toast text | `text-sm` | 14px | — | — |

---

## 5. DESIGN SYSTEM — SPACING & LAYOUT

### Base Spacing

- **Base unit**: 4px (Tailwind default)
- **Body**: `antialiased` font smoothing
- **Theme transition**: `background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease`

### Page Layout

- Min height: `min-h-screen`
- Content wrapper: `relative z-10`
- Navbar clearance: `pb-28` (112px bottom padding for dock)
- Top padding for pages: `pt-8` (32px)
- Section padding: `py-32 px-4 md:px-8` (128px vertical, 16/32px horizontal)
- Content max-width: `max-w-3xl mx-auto` (768px) or `max-w-5xl mx-auto` (1024px)

### Card Padding

- Standard: `p-5 md:p-6` (20/24px)
- Compact: `p-4` (16px)
- Large: `p-6 md:p-8` (24/32px)
- Modal: `p-8` (32px)

### Gap Values

- Between sections: Inherent via `py-32`
- Between cards: `space-y-3` (12px) or `space-y-6` (24px)
- Between elements in cards: `gap-3` or `gap-4` (12/16px)
- Dock items: `gap-2` (8px)

---

## 6. DESIGN SYSTEM — BORDERS, RADIUS, SHADOWS

### Border Radius

| Element | Radius |
|---------|--------|
| Base radius (CSS var) | `--radius: 0.625rem` (10px) |
| Cards | `rounded-2xl` (16px) |
| Buttons (primary) | `rounded-full` (9999px) |
| Inputs | `rounded-xl` (12px) |
| Badges | `rounded-full` |
| Modal | `rounded-2xl` (16px) |
| Keyboard keys | `rx={6} ry={6}` |
| Dock container | `rounded-full` |
| Toast | `rounded-xl` |

### Border Widths

| Element | Width | Color |
|---------|-------|-------|
| Card default | 1px | `var(--tc-stroke)` |
| Card hover | 1px | `var(--tc-accent-33)` |
| Input default | 1px | `var(--tc-stroke)` |
| Input focus | 2px | `var(--tc-accent)` |
| Divider | 1px | `var(--tc-stroke)` |
| Active state | 2px | `var(--tc-accent)` |

### Box Shadows

| Context | Shadow |
|---------|--------|
| Dock glass (dark) | `0 8px 40px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.1), inset 0 -1px 0 rgba(255,255,255,0.02)` |
| Dock glass (light) | Complex with `inset 0 1px 0 rgba(255,255,255,0.6)` |
| Card hover | `0 12px 32px var(--tc-accent-08)` |
| Active node | `0 0 12px var(--tc-accent-30), 0 0 24px var(--tc-accent-08)` |
| Completed node glow | `0 0 8px var(--tc-accent-30), 0 0 16px var(--tc-accent-08)` |
| Install button glow | `0 0 30px var(--tc-accent-30)` |
| Toast shadow | `0 4px 16px rgba(0,0,0,0.15)` |
| Modal backdrop | `bg-black/60 backdrop-blur-sm` |

---

## 7. DESIGN SYSTEM — CSS CUSTOM PROPERTIES

### Complete `--tc-*` Variable Map

```css
/* Core */
--tc-bg              → Page background color
--tc-surface         → Card/panel background
--tc-text            → Primary text color
--tc-muted           → Secondary text color
--tc-stroke          → Border/divider color
--tc-accent          → Primary accent (hex)
--tc-accent-rgb      → Accent RGB values (for rgba)
--tc-accent-from     → Gradient start (hex)
--tc-accent-to       → Gradient end (hex)

/* Gradients */
--tc-hero-gradient   → Hero section bg gradient
--tc-footer-gradient → Footer bg gradient
--tc-cursor          → Typing cursor gradient
--tc-card-bg         → Card background (alias for surface)

/* Typing */
--tc-correct-past    → Correctly typed character color
--tc-incorrect-past  → Incorrectly typed character color
--tc-future-text     → Untyped character color
--tc-current-text    → Active/current character color

/* Keyboard */
--tc-keyboard-bg         → Keyboard container bg
--tc-keyboard-key-bg     → Individual key bg
--tc-keyboard-key-border → Key border color
--tc-keyboard-active-bg  → Active key bg

/* Accent opacity variants */
--tc-accent-08, --tc-accent-10, --tc-accent-15, --tc-accent-20,
--tc-accent-30, --tc-accent-33, --tc-accent-44

/* Dynamic (set by Navbar) */
--dock-glass-bg      → Dock background
--dock-glass-border  → Dock border color
--dock-glass-shadow  → Dock box-shadow

/* Dynamic (set by VortexBackground) */
--vortex-opacity     → WebGL canvas opacity (0=off, 0.55=on)
```

### shadcn/ui Variables (Dark Theme Defaults)

```css
--radius: 0.625rem;
--background: oklch(0.145 0 0);
--foreground: oklch(0.985 0 0);
--card: hsl(var(--tc-surface));
--card-foreground: hsl(var(--tc-text));
--popover: hsl(var(--tc-surface));
--popover-foreground: hsl(var(--tc-text));
--primary: hsl(var(--tc-text));
--primary-foreground: hsl(var(--tc-bg));
--secondary: hsl(var(--tc-surface));
--secondary-foreground: hsl(var(--tc-text));
--accent: hsl(var(--tc-surface));
--accent-foreground: hsl(var(--tc-text));
--destructive: oklch(0.704 0.191 22.216);
--border: hsl(var(--tc-stroke));
--input: hsl(var(--tc-stroke));
--ring: hsl(var(--tc-muted));
```

---

## 8. THEME SYSTEM (5 THEMES)

### Theme: Dark (Default)
- **ID**: `dark`
- **Name**: "Dark"
- **Emoji**: 🌑
- **Background**: `hsl(0 0% 4%)` (#0a0a0a)
- **Accent**: `#89AACC` → `#4E85BF` (steel blue gradient)
- **Vortex**: visible (opacity 0.55)
- **Hero gradient**: `#0a0e1a → #0d1117 → #0a0a0a`
- **Footer gradient**: `#0a0e1a → #0a0a0a`

### Theme: Daylight
- **ID**: `light`
- **Name**: "Daylight"
- **Emoji**: ☀️
- **Background**: `hsl(0 0% 97%)` (#f8f8f8)
- **Accent**: `#3B7EBF` → `#2563EB` (deeper blue)
- **Vortex**: HIDDEN (opacity 0), body bg set to solid
- **Hero gradient**: `#f0f4f8 → #f8fafc → #f8f8f8`
- **Footer gradient**: `#e8edf2 → #f8f8f8`
- **Correct past**: `hsl(0 0% 70%)` (lighter gray)
- **Incorrect past**: `hsl(0 75% 45%)` (darker red for contrast)

### Theme: Deep Ocean
- **ID**: `ocean`
- **Name**: "Deep Ocean"
- **Emoji**: 🌊
- **Background**: `hsl(215 50% 7%)` (#0d1520)
- **Accent**: `#38BDF8` → `#0EA5E9` (sky blue)
- **Vortex**: visible
- **Hero gradient**: `#071525 → #0c1e30 → #0d1520`
- **Incorrect past**: `hsl(350 80% 65%)` (warm red for contrast)

### Theme: Sunset
- **ID**: `sunset`
- **Name**: "Sunset"
- **Emoji**: 🌅
- **Background**: `hsl(20 40% 6%)` (#1a0f0a)
- **Accent**: `#F97316` → `#EF4444` (orange → red)
- **Vortex**: visible
- **Hero gradient**: `#1a0f0a → #1f1510 → #1a0f0a`

### Theme: Forest
- **ID**: `nature`
- **Name**: "Forest"
- **Emoji**: 🌿
- **Background**: `hsl(155 28% 5%)` (#0a1a12)
- **Accent**: `#22C55E` → `#16A34A` (green)
- **Vortex**: visible
- **Hero gradient**: `#071a12 → #0a1f16 → #0a1a12`

### Theme Storage & Switching
- **localStorage key**: `typers-club-theme`
- **Default**: `dark` (SSR hydration-safe — always starts dark)
- **Switching**: Applied via `document.documentElement.style.setProperty()` in `useEffect`
- **Transition**: `background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease` on `body.theme-transition`

---

## 9. CSS ANIMATIONS & KEYFRAMES

### Defined in `globals.css`

| Name | Duration | Easing | Purpose |
|------|----------|--------|---------|
| `float-up` | 0.6s | ease-out | Element floats up and fades out |
| `error-shake` | 0.4s | ease-in-out | Wrong keystroke shake (±4px X) |
| `gradient-shift` | 6s | ease, infinite | Background gradient movement (200% size) |
| `pulse-cursor` | 1.2s | ease-in-out, infinite | Cursor blinking |
| `spin-slow` | 8s | linear, infinite | Loading spinners |
| `marquee` | 20s | linear, infinite | Footer text scroll (-50% X) |
| `roadmap-node-glow` | 3s | ease-in-out, infinite | Completed timeline node glow |
| `roadmap-node-ring` | 2.4s | — | Active node pulsing ring (scale 1→1.45, fade) |
| `roadmap-traveling-dot` | 3s | ease-in-out, infinite | Energy dot traveling down completed segment |
| `roadmap-line-fill` | — | — | Completed line fill (scaleY 0→1) |
| `roadmap-connector-draw` | — | — | Horizontal connector draw (scaleX 0→1) |

### Defined in `SubChapterMap.tsx` (inline SVG `<style>`)

| Name | Duration | Purpose |
|------|----------|---------|
| `tc-pulse-ring` | 3s ease-in-out infinite | Active node outer pulse |
| `tc-pulse-ring-2` | 3s ease-in-out 0.8s infinite | Active node inner pulse (delayed) |
| `tc-dash-flow` | — | Connection line dash animation |
| `tc-node-appear` | 0.6s cubic-bezier(0.22,1,0.36,1) both | Node entrance |
| `tc-glow-pulse` | 3s ease-in-out infinite | Static glow pulse |

### Custom Scrollbar

```css
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--tc-surface); }
::-webkit-scrollbar-thumb { background: var(--tc-stroke); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: color-mix(in srgb, var(--tc-muted) 40%, transparent); }
```

---

## 10. FRAMER MOTION ANIMATIONS

### Universal `fadeUp` Variant (Used in 10+ Components)

```ts
const fadeUp = {
  hidden: { opacity: 0, y: 24 },
  visible: (delay: number) => ({
    opacity: 1, y: 0,
    transition: { duration: 0.7, ease: 'easeOut', delay },
  }),
};
```

### Variants by Component

| Component | Variant | Values |
|-----------|---------|--------|
| CalibrationScreen | Word cycle | `initial: {opacity:0, y:12}`, `animate: {opacity:1, y:0}`, `exit: {opacity:0, y:-12}`, 0.35s easeInOut |
| CurriculumGrid | Container | `staggerChildren: 0.18` |
| CurriculumGrid | Node | `opacity:0, scale:0.3 → 1,1`, spring stiffness:260, damping:20, mass:0.8 |
| CurriculumGrid | Card | `opacity:0, x:48, filter:'blur(4px)' → 0,0,'blur(0)'`, 0.65s, ease:[0.16,1,0.3,1] |
| CurriculumGrid | Connector | `scaleX: 0 → 1`, 0.5s, ease:[0.16,1,0.3,1] |
| LearnPage | fadeUp | `hidden: {opacity:0, y:20}`, visible with 0.5s, ease:[0.19,1,0.22,1] |
| TypingInterface | Overlay | `opacity:0 → 1`, 0.3s easeOut |
| TypingInterface | Modal | `opacity:0, y:30, scale:0.95 → 1,0,1`, 0.4s, ease:[0.19,1,0.22,1] |
| SpeedTest | Results modal | Same as TypingInterface |
| AnimatedStat | Number change | `scale: 1.12 → 1`, 0.2s |
| SubChapterMap | Header | `opacity:0, y:-16 → 0`, 0.35s |
| DownloadPage | staggerContainer | `staggerChildren: 0.1, delayChildren: 0.2` |
| WarningGraphic | Triangle draw | `pathLength: 0 → 1`, 0.8s |
| WarningGraphic | Stripes | `scaleX: 0 → 1`, spring stiffness:400, damping:30 |
| WarningGraphic | Exclamation | `scale: [0, 1.3, 1]`, spring stiffness:500, damping:20 |

### whileInView Triggers

- CurriculumGrid cards: `viewport={{ once: true, margin: '-60px' }}`
- Footer marquee: `viewport={{ once: true, amount: 0.2 }}`
- Phase goal progress bar: `whileInView` width animation

### whileHover Effects

- Phase cards: `y: -4, borderColor: 'var(--tc-accent-33)', boxShadow: '0 12px 32px var(--tc-accent-08)'`
- Phase cards: `whileTap: { scale: 0.98 }`
- Dock icons: Magnification via spring physics (42px → 64px base width)

---

## 11. WEBGL NEURAL VORTEX BACKGROUND

### Component: `InteractiveNeuralVortex`

- **File**: `src/components/ui/interactive-neural-vortex-background.tsx`
- **Technology**: Raw WebGL with custom GLSL shaders
- **Canvas**: `fixed inset-0 w-full h-full pointer-events-none`
- **DPR**: Capped at 2x for performance
- **Opacity**: 0.55 (dark themes) / 0 (light theme)

### Fragment Shader Algorithm

1. **`neuro_shape(uv, t, p)`**: 15-iteration nested loop with rotation + sin accumulation
2. **Color mixing**: Base `vec3(0.5, 0.15, 0.65)` (purple) mixed with `vec3(0.02, 0.7, 0.9)` (cyan) based on scroll progress
3. **Pointer interaction**: Distance-based falloff, `p = 0.5 * pow(1-d, 2)`
4. **Noise post-processing**: Cubed + 10th power, max clamped, edge fade

### Uniforms

| Uniform | Type | Source |
|---------|------|--------|
| `u_time` | float | `performance.now()` |
| `u_ratio` | float | canvas width / height |
| `u_pointer_position` | vec2 | Mouse position normalized to 0-1 |
| `u_scroll_progress` | float | `pageYOffset / (2 * innerHeight)` |

### Pointer Tracking

- Mouse: `pointermove` event
- Touch: `touchmove` event
- Smoothing: `current += (target - current) * 0.2` (lerp)

---

## 12. SVG WAVE BACKGROUND

### Component: `Waves`

- **File**: `src/components/ui/wave-background.tsx`
- **Technology**: SVG with simplex-noise generated lines
- **Grid**: 8px spacing (both X and Y)
- **Lines**: `stroke-width: 1`, filled `none`
- **Noise**: `createNoise2D()` from simplex-noise
- **Wave amplitude**: `cos(move) * 12` (X), `sin(move) * 6` (Y)
- **Mouse influence**: Lines deform based on proximity (175px radius), velocity, angle
- **Mouse smoothing**: `sx += (x - sx) * 0.1`
- **Damping**: velocity * 0.95
- **Clamping**: ±50px max displacement

### Hero Section Configuration

- `strokeColor`: `rgba(${accentRgb}, 0.15)` (dark) / `rgba(59, 126, 191, 0.2)` (light)
- `backgroundColor`: `transparent`
- `pointerSize`: `0` (dot disabled)

---

## 13. COMPONENT ARCHITECTURE

### Component Tree

```
<html class="dark">
  <body class="antialiased theme-transition" style="font-family: Inter">
    <ThemeProvider>          ← Manages --tc-* CSS variables
      <VortexBackground>     ← WebGL canvas + children
        <InteractiveNeuralVortex opacity={0.55/0} />
        {children}           ← App content
        <Toaster />          ← shadcn/ui toast notifications
        <InstallPWAButton /> ← PWA install prompt (fixed bottom-right)
        <OfflineIndicator /> ← Network status banner (fixed top)
      </VortexBackground>
    </ThemeProvider>
    <script>SW cleanup</script>
  </body>
</html>
```

### All 18 Application Components

| # | Component | Lines | Props | State Vars | Refs |
|---|-----------|-------|-------|------------|------|
| 1 | CalibrationScreen | ~80 | `onComplete` | 4 | 1 |
| 2 | Navbar | ~80 | `onNavigate, activeSection` | 0 | 0 |
| 3 | HeroSection | ~80 | `onStartTraining, onLogin, account` | 0 | 0 |
| 4 | CurriculumGrid | ~664 | `phasesProgress, sessionHistory, onSelectPhase` | 1 | 1 |
| 5 | LearnPage | ~625 | `phasesProgress, onSelectSubChapter, onBack` | 3 | 0 |
| 6 | SubChapterMap | ~733 | `subChapters, completedIds, activeId, onSelectSubChapter, onBack, lessonTitle, phaseTitle` | 1 | 3 |
| 7 | TypingInterface | ~678 | 11 props | 11 | 8 |
| 8 | KeyboardDiagram | ~275 | `activeKey, pressedKey` | 0 | 0 |
| 9 | SpeedTestPage | ~579 | `onBack` | 12 | 0 |
| 10 | ProfilePage | ~1556 | 8 props | 27 | 0 |
| 11 | SettingsPage | ~288 | `onBack, onResetAll` | 3 | 0 |
| 12 | LeaderboardPage | ~300 | `onBack, userWpm, userAccuracy, account` | 0 | 0 |
| 13 | PerformanceGraph | ~1084 | `records, compact` | 3 | 2 |
| 14 | StatsSection | ~198 | `totalKeystrokes, averageWpm, totalTimeSpent, onGoToProfile, account` | 3 | 1 |
| 15 | Footer | ~62 | (none) | 0 | 0 |
| 16 | CustomPracticePage | ~300 | `onStartPractice, onBack` | 2 | 0 |
| 17 | DownloadPage | ~664 | `onBack` | 4 | 0 |
| 18 | PhaseVideoInstruction | ~299 | `phaseId, isUnlocked` | 2 | 0 |

### Supporting Components

| Component | File | Purpose |
|-----------|------|---------|
| AnimatedDock | `ui/animated-dock.tsx` | macOS-style bottom nav with spring magnification |
| VortexBackground | `VortexBackground.tsx` | WebGL background wrapper with theme opacity control |
| GoogleLoginButton | `typers-club/GoogleLoginButton.tsx` | Firebase Google Auth button |
| InstallPWAButton | `typers-club/InstallPWAButton.tsx` | PWA install prompt popup |
| OfflineIndicator | `typers-club/OfflineIndicator.tsx` | Red offline banner |
| WarningGraphic | `ui/warning-graphic.tsx` | Animated warning triangle SVG |
| Waves | `ui/wave-background.tsx` | Interactive SVG wave field |
| InteractiveNeuralVortex | `ui/interactive-neural-vortex-background.tsx` | WebGL neural background |

---

## 14. PAGE VIEWS

### View 1: Calibration (3-second splash)

- Full-screen overlay, `z-[9999]`, `fixed inset-0`
- WarningGraphic SVG (280×91px, accent color, animated)
- Word cycling: `['Initialize', 'Calibrate', 'Focus', 'Type']` every 900ms
- AnimatePresence `mode="wait"` for smooth word transitions
- Progress counter: `000` → `100` in bottom-right, monospace
- Progress bar: 2px height at bottom, gradient fill
- Auto-fades at 3 seconds → calls `onComplete()`

### View 2: Home (Default)

Structure:
```
min-h-screen flex flex-col
├── Navbar (fixed bottom dock)
├── main.flex-1
│   ├── HeroSection (min-h-screen)
│   ├── CurriculumGrid (4 phase cards with roadmap timeline)
│   ├── StatsSection (3 animated counters + optional CTA banner)
│   └── PerformanceGraph (canvas chart + stat badges)
└── Footer (pb-28)
```

### View 3: Typing (Full-screen)

Structure:
```
relative z-10
├── Top bar (sticky): Back button, lesson title, WPM, accuracy, timer, reset, keyboard toggle, home, map
├── Stats bar (when started): WPM, Accuracy, Time, Mistakes
├── Text display area:
│   ├── Each character rendered individually as <span>
│   ├── Past correct: var(--tc-correct-past)
│   ├── Past incorrect: var(--tc-incorrect-past) + animate-error-shake
│   ├── Current: var(--tc-current-text) + animate-pulse-cursor + cursor underline
│   └── Future: var(--tc-future-text)
├── KeyboardDiagram (toggleable, SVG, 5-row QWERTY)
└── Completion modal (AnimatePresence overlay):
    ├── Trophy icon in accent circle
    ├── AnimatedStat: WPM, Accuracy, Duration, Mistakes
    ├── Threshold status (if applicable)
    ├── Error analysis
    └── Action buttons: Next Practice, Go to Phases, Go Home
```

### View 4: Learn (Phase/Lesson/Sub-chapter navigation)

3 sub-views:
- **phases**: 4 PhaseCards with progress bars + PhaseVideoInstruction per phase
- **chapters**: LessonChapterCard list for selected phase with video
- **subchapters**: SubChapterMap (snake-pattern SVG nodes with canvas particles)

### View 5: Speed Test

- Config screen: Difficulty pills (easy/medium/hard), time limit pills (30/60/120s)
- Timer bar: gradient fill, red at ≤10s
- Text display: Same character-by-character rendering as TypingInterface
- Keyboard diagram below text
- Results modal: Trophy, stats grid, WPM rating, action buttons

### View 6: Profile (7 auth states)

- Login: Email/phone + password, forgot link, Google button, signup link
- Signup: Name + email + phone + password, gradient submit button
- Verify-signup: OTP input (6 digits), timer, email status banner
- Forgot: Email input → OTP → account details reveal
- Profile: Avatar circle, name, account details, stats grid, PerformanceGraph (compact)

### Views 7-11: Settings, Leaderboard, Progress, Download, Custom Practice

(Each has specific layout documented in component audit)

---

## 15. NAVIGATION SYSTEM — ANIMATED DOCK

### Dock Component: `AnimatedDock`

- **Position**: `fixed bottom-5 left-1/2 -translate-x-1/2 z-50`
- **Style**: Liquid glass — `backdrop-filter: blur(40px) saturate(1.8)`
- **Border**: 1px solid `var(--dock-glass-border)`
- **Padding**: `px-3 py-2`
- **Item gap**: `gap-2`

### Magnification Physics

```ts
const widthSync = useTransform(distance, [-120, 0, 120], [42, 64, 42]);
const width = useSpring(widthSync, { mass: 0.1, stiffness: 200, damping: 15 });
```

- **Rest size**: 42px
- **Hovered size**: 64px
- **Influence radius**: 120px from center
- **Spring**: mass 0.1, stiffness 200, damping 15

### Dock Items (9 total)

| Icon | Name | ID |
|------|------|----|
| Home | Home | `home` |
| BookOpen | Learn | `learn` |
| Gauge | Speed Test | `speedtest` |
| PenLine | Custom Practice | `custompractice` |
| Trophy | Leaderboard | `leaderboard` |
| Activity | Progress | `progress` |
| User | Profile | `profile` |
| Settings | Settings | `settings` |
| MonitorDown | Download | `download` |

- Icon size: 22px, strokeWidth: 1.8
- Inactive opacity: 0.45
- Active indicator: 4px accent dot at bottom center
- Tooltip: 11px text, rounded-lg, appears 10px above with 0.2s fade

---

## 16. TYPING ENGINE — CORE LOGIC

### WPM Calculation

```typescript
export function calculateWPM(correctChars: number, timeSeconds: number): number {
  if (timeSeconds <= 0) return 0;
  return Math.round((correctChars / 5) / (timeSeconds / 60));
}
```

- **Formula**: Standard = (characters / 5) / (minutes)
- **5 characters = 1 "word"**

### Accuracy Calculation

```typescript
export function calculateAccuracy(correct: number, total: number): number {
  if (total <= 0) return 100;
  return Math.round((correct / total) * 100);
}
```

### Phase System

```typescript
export const PHASES = [
  { id: 1, title: "The Foundation", requiredWpm: 20, requiredAccuracy: 90, color: "#89AACC" },
  { id: 2, title: "Intermediate", requiredWpm: 40, requiredAccuracy: 95, color: "#6B9BD2" },
  { id: 3, title: "Advanced Prep", requiredWpm: 60, requiredAccuracy: 98, color: "#4E85BF" },
  { id: 4, title: "The Practitioner", requiredWpm: 0, requiredAccuracy: 0, color: "#3A6FA0" },
];
```

### Progress Data Structure

```typescript
interface UserProgress {
  totalKeystrokes: number;
  totalTimeSpent: number;
  averageWpm: number;
  phases: PhaseProgress[];
  currentLesson: { phaseId: number; lessonId: number } | null;
  sessionHistory: SessionHistory;
}

interface PhaseProgress {
  phaseId: number;
  bestWpm: number;
  bestAccuracy: number;
  unlocked: boolean;
  completed: boolean;
  totalLessonsCompleted: number;
  lessons: LessonProgress[];
}

interface LessonProgress {
  completedSubChapters: number[];
  bestWpm: number;
  bestAccuracy: number;
}

interface LessonRecord {
  lessonId: number;
  phaseId: number;
  title: string;
  wpm: number;
  accuracy: number;
  timestamp: number;
  subChapterId?: number;
  duration?: number;    // seconds
  mistakes?: number;
  totalChars?: number;
}
```

### Session History Limit
- Maximum **50 records** (FIFO — oldest removed when exceeded)
- `averageWpm` recalculated on every record addition

---

## 17. LESSON CONTENT

### 4 Phases, 33 Lessons, ~495 Sub-chapters

| Phase | Lessons | Sub-chapters per lesson | Focus |
|-------|---------|------------------------|-------|
| 1. Foundation | 15 (IDs 1-15) | 15 each | Home row, individual keys, numbers, symbols |
| 2. Intermediate | 6 (IDs 1-6) | 15 each | Words, shift keys, phrases, code keywords |
| 3. Advanced Prep | 6 (IDs 1-6) | 15 each | Code snippets, JSON, HTML, SQL, Markdown |
| 4. Practitioner | 6 (IDs 1-6) | 15 each | Speed, technical, literary, philosophy, science |

### Phase 1 Lesson Titles

1. Home Row: ASDF JKL;
2. Home Row: JKL;
3. Home Row: Full
4. G and H
5. R and T
6. U and Y
7. E and I
8. W and O
9. Q and P
10. V and B
11. C and M
12. X and N
13. Z and Comma/Period
14. Numbers Row
15. Symbols

### Sub-chapter difficulties: `easy`, `medium`, `hard`

### Random Endless Text
- `getRandomEndlessText()` picks a random sub-chapter text from all phases

---

## 18. AUTHENTICATION SYSTEM

### Dual Auth Model

1. **Email/Phone + Password** (localStorage)
2. **Google OAuth** (Firebase, graceful degradation)

### Account Data Structure

```typescript
interface AccountData {
  displayName: string;
  email: string;
  password: string;
  phone: string;
  joinDate: string;
  provider?: 'google';
  providerUserId?: string;
  photoURL?: string;
}
```

### Login Logic

- Accepts email OR phone as username
- Password: actual password OR phone number (alternative)
- Case: `(a.email === id || a.phone === id) && (a.password === pass || a.phone === pass)`

### Google Login Flow

1. `signInWithPopup(getFirebaseAuth(), new GoogleAuthProvider())`
2. Look up by `providerUserId` → direct login
3. Look up by `email` → link Google to existing account (non-destructive)
4. No match → create new Google account (empty password/phone)

### OTP Verification

- 6-digit random code
- 120-second expiry timer
- Stored client-side, compared locally
- Email delivery via `/api/send-otp` (SMTP or demo mode)

---

## 19. DATA PERSISTENCE — localStorage SCHEMA

### Keys

| Key | Type | Description |
|-----|------|-------------|
| `typers-club-accounts` | `AccountData[]` (JSON) | All registered accounts |
| `typers-club-session` | `AccountData` (JSON) | Currently logged-in account |
| `typers-club-progress:{userId}` | `UserProgress` (JSON) | User typing progress |
| `typers-club-progress:guest` | `UserProgress` (JSON) | Guest/anonymous progress |
| `typers-club-theme` | `ThemeId` (string) | Theme preference |
| `typers-club-install-dismissed` | `'true'` | PWA install prompt dismissed |

### User ID Derivation

```typescript
function getUserId(account: AccountData | null): string | null {
  return account?.providerUserId || account?.email || null;
}
```

### Storage Key Format

```
"typers-club-progress:guest"              → Unauthenticated users
"typers-club-progress:user:{lowercase-email-without-special-chars}" → Authenticated users
```

---

## 20. API ROUTES

### GET /api
- Returns: `{ message: "Hello, world!" }`
- Purpose: Health check

### POST /api/extract-text
- Content-Type: `multipart/form-data`
- Field: `file` (File)
- Supports: `.txt`, `.pdf`, `.docx`
- Returns: `{ text, fileName, charCount, originalLength }`
- Limits: Min 10 chars, max 5000 chars

### POST /api/send-otp
- Body: `{ email: string, otp: string, purpose: 'verification' | 'recovery' }`
- In-memory OTP store (2-minute TTL)
- SMTP via nodemailer (env: SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS)
- Demo mode fallback when SMTP not configured
- HTML email with dark theme, gradient header, OTP code box
- Returns: `{ success, emailSent, demoMode?, message }`

---

## 21. PWA CONFIGURATION

### manifest.json

```json
{
  "name": "Typer's Club — Master the Gravity of Keys",
  "short_name": "Typer's Club",
  "display": "standalone",
  "background_color": "#0a0a0a",
  "theme_color": "#89AACC",
  "orientation": "any",
  "categories": ["education", "utilities"],
  "icons": [
    { "src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable" },
    { "src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }
  ],
  "shortcuts": [
    { "name": "Speed Test", "url": "/?view=speed-test" }
  ]
}
```

### Service Worker: Self-Destructing

- On install: Deletes ALL caches
- On activate: Unregisters itself + deletes ALL remaining caches
- NO fetch handler — all requests go directly to network

### Install PWA Button

- Fixed bottom-right, z-50
- Captures `beforeinstallprompt` event
- Shows slide-in banner with install button
- Dismissible (saves to localStorage)

---

## 22. SEO & META TAGS

```html
<title>Typer's Club — Master the Gravity of Keys</title>
<meta name="description" content="A premium typing tutor designed to build muscle memory and elevate your typing speed through progressive phase-based training." />
<meta name="keywords" content="typing tutor, touch typing, WPM, typing speed, muscle memory, B.Tech mini project" />
<meta name="author" content="Ankush Durgekar" />
<meta name="theme-color" content="#89AACC" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
<meta name="apple-mobile-web-app-title" content="Typer's Club" />
<link rel="manifest" href="/manifest.json" />
<link rel="apple-touch-icon" href="/icons/icon-192.png" />
<link rel="icon" href="data:image/svg+xml,...⌨️..." />
```

### robots.txt
- All user agents allowed on `/`

---

## 23. RESPONSIVE BREAKPOINTS

| Breakpoint | Width | Usage |
|------------|-------|-------|
| Default | <640px | Mobile layout (single column, smaller text, hidden labels) |
| `sm:` | ≥640px | Tablet-ish (flex-row buttons, larger padding) |
| `md:` | ≥768px | Desktop (larger headings, grid columns, full labels) |
| `lg:` | ≥1024px | Wide desktop (extra-large headings, 3-col grids) |
| `xl:` | ≥1280px | Ultrawide (very large text) |

### Key Responsive Changes

| Element | Mobile | Tablet (md) | Desktop (lg) |
|---------|--------|-------------|--------------|
| Hero h1 | text-5xl (48px) | text-7xl (72px) | text-8xl (96px) |
| Section h2 | text-3xl (30px) | text-5xl (48px) | text-5xl (48px) |
| Typing text | text-xl (20px) | text-2xl (24px) | text-3xl (30px) |
| Marquee | text-6xl (60px) | text-8xl (96px) | text-8xl (96px) |
| Stats counter | text-4xl (36px) | text-6xl (60px) | text-6xl (60px) |
| Card padding | p-5 (20px) | p-6 (24px) | p-6 (24px) |
| Section padding | px-4 (16px) | px-8 (32px) | px-8 (32px) |
| CTA buttons | flex-col | sm:flex-row | sm:flex-row |
| Footer bottom | flex-col | sm:flex-row | sm:flex-row |
| Theme picker grid | 1 col | sm:2 col | lg:3 col |
| Benefits grid | 1 col | md:2 col | md:3 col |
| Dock items | Scrolling | Scrolling | All visible |

### Mobile-Specific Handling

- SubChapterMap: Snake layout with fewer columns, shorter title max length
- ProfilePage: Full-width on mobile, constrained form on larger screens
- SpeedTest: Back button text hidden on small screens
- PhaseVideoInstruction: Collapsed thumbnail smaller on mobile
- Leaderboard table: Reduced column widths on mobile

---

## 24. ALL LUCIDE ICONS USED

### Navigation
`Home`, `BookOpen`, `Gauge`, `PenLine`, `Trophy`, `Activity`, `User`, `Settings`, `MonitorDown`

### Typing Interface
`ArrowLeft`, `Target`, `Trophy`, `X`, `RotateCcw`, `ChevronRight`, `CornerDownLeft`, `Home`, `Map`, `Keyboard`

### Profile/Auth
`ArrowLeft`, `User`, `Mail`, `Calendar`, `Keyboard`, `Zap`, `Clock`, `LogOut`, `ShieldCheck`, `Lock`, `Phone`, `Eye`, `EyeOff`, `KeyRound`, `ArrowRight`, `CheckCircle`, `Copy`, `Check`, `RefreshCw`, `MailCheck`, `ShieldAlert`, `Timer`, `Send`, `Inbox`, `AlertTriangle`, `Loader2`

### Performance Graph
`TrendingUp`, `TrendingDown`, `Minus`, `Target`, `BarChart3`, `Activity`, `Zap`, `Clock`, `XCircle`, `Type`

### Curriculum/Learn
`Lock`, `CheckCircle2`, `ChevronRight`, `ArrowLeft`, `ChevronDown`, `ChevronUp`, `ExternalLink`, `X`, `Play`

### Speed Test
`ArrowLeft`, `RotateCcw`, `Zap`, `Target`, `Clock`, `Trophy`, `ChevronDown`, `Gauge`

### Other
`Palette`, `Download`, `Wifi`, `WifiOff`, `Smartphone`, `Monitor`, `HardDrive`, `Shield`, `ExternalLink`, `Sparkles`, `FileText`, `AlertCircle`, `Flame`, `Crown`, `Medal`, `Type`

**Total unique icons: ~65**

---

## 25. FILE STRUCTURE

```
src/
├── app/
│   ├── globals.css                 (231 lines — design system)
│   ├── layout.tsx                  (85 lines — root layout)
│   ├── page.tsx                    (615 lines — SPA router)
│   └── api/
│       ├── route.ts                (health check)
│       ├── extract-text/route.ts   (PDF/DOCX text extraction)
│       └── send-otp/route.ts       (OTP email)
├── components/
│   ├── VortexBackground.tsx        (WebGL wrapper)
│   ├── ui/                         (55 shadcn/ui components)
│   │   ├── animated-dock.tsx       (macOS dock)
│   │   ├── interactive-neural-vortex-background.tsx (WebGL shader)
│   │   ├── warning-graphic.tsx     (Animated SVG warning)
│   │   ├── wave-background.tsx     (SVG noise waves)
│   │   └── ... (50+ shadcn primitives)
│   └── typers-club/                (18 app components)
│       ├── CalibrationScreen.tsx
│       ├── Navbar.tsx
│       ├── HeroSection.tsx
│       ├── CurriculumGrid.tsx
│       ├── LearnPage.tsx
│       ├── SubChapterMap.tsx
│       ├── TypingInterface.tsx
│       ├── KeyboardDiagram.tsx
│       ├── SpeedTestPage.tsx
│       ├── ProfilePage.tsx
│       ├── SettingsPage.tsx
│       ├── LeaderboardPage.tsx
│       ├── PerformanceGraph.tsx
│       ├── StatsSection.tsx
│       ├── Footer.tsx
│       ├── CustomPracticePage.tsx
│       ├── DownloadPage.tsx
│       ├── PhaseVideoInstruction.tsx
│       ├── GoogleLoginButton.tsx
│       ├── InstallPWAButton.tsx
│       └── OfflineIndicator.tsx
├── hooks/
│   ├── use-mobile.ts               (768px breakpoint)
│   └── use-toast.ts                (toast notification system)
└── lib/
    ├── typing-engine.ts            (356 lines — WPM/accuracy/progress)
    ├── lessons.ts                  (852 lines — 33 lessons)
    ├── theme-context.tsx            (281 lines — 5 themes)
    ├── firebase.ts                 (156 lines — Google Auth)
    ├── db.ts                       (Prisma client)
    └── utils.ts                    (cn() utility)

public/
├── sw.js                           (self-destructing service worker)
├── manifest.json                   (PWA config)
├── robots.txt                      (allow all)
├── logo.svg                        (keyboard emoji favicon)
├── icons/
│   ├── icon-192.png                (76 KB)
│   ├── icon-512.png                (76 KB)
│   └── download-hero.png           (77 KB)
└── typers-club-source-v1.1.zip     (554 KB — source download)

prisma/
└── schema.prisma                   (SQLite, User + Post models — UNUSED)
```

---

## 26. DEPENDENCIES — EXACT VERSIONS

### Critical (Must Have)

| Package | Version | Purpose |
|---------|---------|---------|
| next | ^16.1.1 | Framework |
| react | ^19.0.0 | UI library |
| react-dom | ^19.0.0 | DOM rendering |
| framer-motion | ^12.23.2 | Animations |
| lucide-react | ^0.525.0 | Icons |
| tailwindcss | ^4 | Styling |
| @tailwindcss/postcss | ^4 | PostCSS plugin |
| tailwindcss-animate | ^1.0.7 | Animation utilities |
| simplex-noise | ^4.0.3 | Wave background |
| clsx | ^2.1.1 | Class merging |
| tailwind-merge | ^3.3.1 | Tailwind class merging |
| class-variance-authority | ^0.7.1 | Component variants |

### Auth & Email

| Package | Version | Purpose |
|---------|---------|---------|
| firebase | ^12.12.0 | Google OAuth |
| nodemailer | ^8.0.5 | Email delivery |
| pdf-parse | ^2.4.5 | PDF text extraction |
| mammoth | ^1.12.0 | DOCX text extraction |

### shadcn/ui (Radix Primitives)

All @radix-ui/* packages for: accordion, alert-dialog, avatar, checkbox, collapsible, context-menu, dialog, dropdown-menu, hover-card, label, menubar, navigation-menu, popover, progress, radio-group, scroll-area, select, separator, slider, switch, tabs, toast, toggle, toggle-group, tooltip

### Optional (Used by shadcn/ui but not directly)

@hookform/resolvers, @tanstack/react-query, @tanstack/react-table, cmdk, date-fns, embla-carousel-react, input-otp, react-day-picker, react-hook-form, react-resizable-panels, recharts, sonner, vaul, zod, zustand, gsap, hls.js, @mdxeditor/editor, @reactuses/core, @dnd-kit/*, uuid, z-ai-web-dev-sdk, next-intl, next-themes, next-auth, prisma, @prisma/client, sharp

---

## APPENDIX: KEY INTERACTION DETAILS

### Calibration Screen Timing
- Word cycle: 900ms per word
- Total duration: 3000ms
- Fade-out: 600ms opacity transition
- Progress bar: `width: ${progress * 100}%`, transition `width 0.1s linear`

### Typing Interface Key Handling
- Ignores: Shift, Control, Alt, Meta, CapsLock, Tab, Escape
- Backspace: Removes last typed character, decrements correctCount if was 'correct'
- Regular char: Compares to expected, marks 'correct' or 'incorrect'
- Timer starts on first character typed
- 200ms timer interval for elapsed seconds
- Completion: All characters typed → triggers onComplete callback

### Keyboard Diagram
- 5 rows: Number, QWERTY, Home, Shift, Bottom
- 60+ keys with QWERTY layout
- Key width: 46px base (Space = 6.5x)
- Key height: 36px
- Row gap: 4px
- Row offsets: [0, 18, 36, 52, 0]px
- SVG viewBox: 800 × ~200
- Active key: gradient fill + accent border + 1.2px stroke
- Pressed key: stronger gradient + 1.5px stroke
- Home row indicators: small circles (r=1.5) on A,S,D,F,J,K,L

### Performance Graph Canvas
- Dimensions: left=48, right=52, top=16, bottom=36
- Grid: horizontal dashed lines at "nice" step intervals
- WPM line: 2.5px gradient stroke with smooth bezier curves
- WPM area: gradient fill (0.35→0.02 alpha)
- Accuracy line: 1.5px dashed muted stroke
- Drop zones: red tint + vertical dashed lines
- Moving average: 5-period, dashed white line
- Hover: crosshair lines + enlarged dot within 40px proximity
- DPR-aware rendering

### SubChapterMap Snake Layout
- Desktop: 5 columns, 32px node radius, 130px row height
- Mobile: 3 columns, smaller radius
- Organic wobble: `sin(i*0.8)*6` horizontal, `cos(i*0.6)*4` vertical
- Canvas particle system: 1 particle per completed connection
- Particles: core + glow, 80-frame lifecycle, respawn at random completed connection

---

*Document generated from exhaustive code audit. Every value, class, color, animation, and structure documented above exists exactly as specified in the source code at `/home/z/my-project/`.*

*Version: v1.2 — Last updated: April 26, 2026*
