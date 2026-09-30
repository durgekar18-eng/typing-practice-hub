# Typer's Club — Complete Project Guide (For Presentation)

> Written like you're a newborn learning everything from scratch.
> Read this top-to-bottom and you'll understand every single thing about your project.

---

## 📖 CHAPTER 1: WHAT IS THIS PROJECT? (Elevator Pitch)

**Typer's Club** is a **typing tutor website** — like a gym for your fingers.

Think of it this way: Just like a gym has exercises that build your muscles step by step, Typer's Club has typing exercises that build your **finger muscle memory** step by step. You start with easy keys (A, S, D, F) and slowly progress to full-speed typing.

**In one line for your presentation:**
> "Typer's Club is a progressive typing tutor web application that teaches touch typing through structured phases, real-time performance tracking, speed tests, and an offline-capable Progressive Web App experience."

---

## 📖 CHAPTER 2: WHAT FEATURES DOES IT HAVE?

Imagine the app as a house with many rooms. Each room is a feature:

### Room 1: 🏠 Home Page
- **Hero section** — The landing page with a cool wave animation and "Start Training" button
- **Journey map** — A visual roadmap showing your 4 phases of learning (like a game map with levels)
- **Stats section** — Shows your total keystrokes, average WPM (words per minute), and time spent
- **Performance graph** — A chart that shows your WPM and accuracy over time

### Room 2: 📚 Learn Page (The Core Feature)
- Shows all **33 lessons** organized as a vertical timeline/roadmap
- Each lesson has **10-15 sub-chapters** (individual practice exercises)
- Lessons are grouped into **4 phases**:
  - **Phase 1 — The Foundation** (15 lessons): Home row keys, basic letters
  - **Phase 2 — Intermediate** (6 lessons): Words, capital letters, phrases
  - **Phase 3 — Advanced Prep** (6 lessons): Complex formatting, numbers, code
  - **Phase 4 — The Practitioner** (6 lessons): Endless mastery mode
- Each lesson has a **YouTube video tutorial** you can watch before practicing
- A **sub-chapter map** shows all exercises within a lesson with progress dots

### Room 3: ⌨️ Typing Interface (The Practice Screen)
- Full-screen typing area with large, easy-to-read text
- **Real-time WPM and accuracy** counter at the top
- **Visual keyboard** at the bottom that highlights which key to press next
- **Color-coded feedback**: correct letters turn gray, wrong letters turn red, current letter is white
- **Collapsible keyboard** — you can hide it once you're confident
- After completing: Shows results (WPM, accuracy, time) with options to go Home, back to Phases, Retry, or go to Next sub-chapter

### Room 4: ⚡ Speed Test
- **3 difficulty levels**: Easy (simple prose), Medium (technical), Hard (complex)
- **3 time limits**: 30 seconds, 60 seconds, 120 seconds
- **15 unique paragraphs** that are randomly selected
- Countdown timer with progress bar (turns red when ≤10 seconds)
- **Auto-completes** when you finish all text before time runs out
- Results modal shows WPM, accuracy, characters typed, and performance rating

### Room 5: 👤 Profile Page
- **Create Account** form (name, email, phone, password)
- **Login** with email/phone + password
- **Google Sign-In** via Firebase
- **Email OTP verification** — sends a real email with a 6-digit code
- **Forgot Password** — recover account via email OTP
- Shows your stats: total keystrokes, average WPM, time spent
- Performance graph (compact mode)
- Logout functionality

### Room 6: 🏆 Leaderboard
- Shows 15 mock users with their WPM, accuracy, and rank
- Gold 🥇, Silver 🥈, Bronze 🥉 icons for top 3
- Current user highlighted if logged in

### Room 7: 📈 Progress Page
- Full-width performance graph
- Shows WPM and accuracy over your last 50 typing sessions
- Trend analysis: "Improving" / "Declining" / "Steady"
- Moving average line and performance drop detection

### Room 8: ⚙️ Settings Page
- **Theme picker**: 5 themes — Dark, Daylight, Deep Ocean, Sunset, Forest
- Each theme changes ALL colors: background, text, accent, keyboard, cards
- **Reset All** button with confirmation dialog (clears account + progress)

### Room 9: 📥 Download Page
- Explains PWA (Progressive Web App) install feature
- Shows "How It Works" — 3 step guide
- 6 benefit cards (Works Offline, Lightning Fast, Native Desktop Feel, etc.)
- Platform support badges (Chrome, Edge, Firefox, Safari)
- Install button triggers native browser install dialog

### Room 10: 🎨 Global Features
- **macOS-style animated dock** at the bottom with 8 icons (magnification on hover)
- **Calibration loading screen** on first visit (fancy word cycling animation)
- **Vortex animated background** (WebGL-based, always running behind content)
- **Offline indicator** — red banner appears when internet is lost: "You are offline — Core typing still works!"
- **PWA install button** — floating card in bottom-right corner when browser supports installation
- **Toast notifications** — for success/error messages
- **Framer Motion animations** — smooth page transitions and scroll-triggered reveals
- **Responsive design** — works on mobile, tablet, and desktop

---

## 📖 CHAPTER 3: WHAT TECHNOLOGY IS USED? (Tech Stack)

Think of this as the list of tools/ingredients used to build the project:

### The Big Three (The Foundation)

| Technology | What It Does | Simple Analogy |
|---|---|---|
| **Next.js 16** | The web framework — controls pages, routing, rendering | The **foundation/structure** of the house |
| **TypeScript** | Adds type safety to JavaScript — catches errors before they happen | A **spell-checker** for your code |
| **Tailwind CSS 4** | Utility-first CSS — style everything with class names | A **paintbrush** with pre-mixed colors |

### The UI Library

| Technology | What It Does |
|---|---|
| **shadcn/ui** | Pre-built UI components (buttons, cards, dialogs, etc.) — saves time |
| **Lucide React** | Icon library (Home, Settings, Trophy icons etc.) |
| **Framer Motion** | Animation library — smooth transitions, scroll reveals, hover effects |
| **GSAP** | Advanced animation library (used for subtle effects) |

### The Styling System

| Technology | What It Does |
|---|---|
| **CSS Variables** (`var(--tc-*)`) | Theme colors that change dynamically |
| **5 Theme Definitions** | Dark, Daylight, Deep Ocean, Sunset, Forest — each with 20+ color properties |
| **Theme Context (React)** | A React context that provides theme data to all components |

### Data & State Management

| Technology | What It Does |
|---|---|
| **localStorage** | Browser storage — saves progress, account data, theme preference |
| **Prisma ORM** | Database tool (SQLite) — schema definition, type-safe queries |
| **React useState/useEffect** | Component-level state management |
| **React useRef** | Holds mutable values that don't trigger re-renders |
| **React useCallback** | Memoizes functions to prevent unnecessary re-renders |

### Authentication

| Technology | What It Does |
|---|---|
| **Firebase Auth** | Google Sign-In (popup-based OAuth) |
| **Custom Auth System** | Email + password login, phone as alternative password |
| **Email OTP** | Nodemailer + SMTP for sending verification codes |
| **Per-user data isolation** | Each user's progress stored under their unique key |

### PWA (Offline Support)

| Technology | What It Does |
|---|---|
| **manifest.json** | Tells the browser "this is an installable app" |
| **Service Worker (sw.js)** | Caches files for offline use — stale-while-revalidate strategy |
| **BeforeInstallPromptEvent** | Browser API for showing native "Install App" dialog |

---

## 📖 CHAPTER 4: HOW IS THE CODE ORGANIZED? (Project Structure)

```
my-project/
├── 📁 src/                          ← ALL your source code lives here
│   ├── 📁 app/                      ← Next.js App Router (pages & API)
│   │   ├── layout.tsx               ← The MASTER layout (HTML wrapper for ALL pages)
│   │   ├── page.tsx                 ← The MAIN page (the single-page app controller)
│   │   ├── globals.css              ← Global styles (Tailwind, animations, scrollbar, etc.)
│   │   └── 📁 api/
│   │       ├── route.ts             ← Placeholder API route
│   │       └── 📁 send-otp/
│   │           └── route.ts         ← API route that sends OTP emails via Nodemailer
│   │
│   ├── 📁 components/               ← ALL UI components
│   │   ├── 📁 typers-club/          ← YOUR custom app components
│   │   │   ├── CalibrationScreen.tsx  ← Loading screen on first visit
│   │   │   ├── Navbar.tsx              ← Bottom dock navigation (8 icons)
│   │   │   ├── HeroSection.tsx         ← Landing hero with wave background
│   │   │   ├── CurriculumGrid.tsx      ← Home page phase roadmap (4 phase cards)
│   │   │   ├── LearnPage.tsx           ← Learn page (33 lessons timeline)
│   │   │   ├── SubChapterMap.tsx       ← Sub-chapter selection within a lesson
│   │   │   ├── TypingInterface.tsx     ← The main typing practice screen
│   │   │   ├── KeyboardDiagram.tsx     ← Visual QWERTY keyboard
│   │   │   ├── SpeedTestPage.tsx       ← Speed test feature
│   │   │   ├── ProfilePage.tsx         ← Account/login/signup page
│   │   │   ├── LeaderboardPage.tsx     ← Leaderboard with mock users
│   │   │   ├── SettingsPage.tsx        ← Theme picker + reset
│   │   │   ├── StatsSection.tsx        ← Stats counters (keystrokes/WPM/time)
│   │   │   ├── PerformanceGraph.tsx    ← Canvas-based WPM/accuracy chart
│   │   │   ├── PhaseVideoInstruction.tsx ← YouTube video embeds for each phase
│   │   │   ├── GoogleLoginButton.tsx   ← Google Sign-In button
│   │   │   ├── DownloadPage.tsx        ← PWA download/install page
│   │   │   ├── InstallPWAButton.tsx    ← Floating install prompt
│   │   │   ├── OfflineIndicator.tsx    ← Offline status banner
│   │   │   └── Footer.tsx              ← Footer with marquee text
│   │   ├── 📁 ui/                   ← shadcn/ui pre-built components (buttons, cards, etc.)
│   │   │   ├── animated-dock.tsx     ← macOS-style magnifying dock
│   │   │   ├── wave-background.tsx   ← Interactive SVG wave effect
│   │   │   ├── warning-graphic.tsx   ← SVG loading graphic
│   │   │   └── ... (50+ more UI components)
│   │   └── VortexBackground.tsx      ← WebGL vortex animation background
│   │
│   ├── 📁 hooks/                    ← Custom React hooks
│   │   ├── use-toast.ts             ← Toast notification hook
│   │   └── use-mobile.ts            ← Mobile detection hook
│   │
│   └── 📁 lib/                      ← Core logic libraries
│       ├── typing-engine.ts         ← THE BRAIN: WPM calc, progress tracking, phase unlock
│       ├── lessons.ts               ← ALL lesson content (33 lessons, 300+ sub-chapters)
│       ├── theme-context.tsx         ← Theme system (5 themes, CSS variable provider)
│       ├── firebase.ts               ← Firebase configuration & Google Sign-In
│       └── db.ts                     ← Prisma database client
│
├── 📁 public/                        ← Static files served directly
│   ├── manifest.json                 ← PWA manifest (app name, icons, theme)
│   ├── sw.js                         ← Service Worker (offline caching)
│   ├── logo.svg                      ← App logo (emoji-based)
│   └── 📁 icons/
│       ├── icon-192.png              ← PWA icon (192x192)
│       ├── icon-512.png              ← PWA icon (512x512)
│       └── download-hero.png         ← Download page hero image
│
├── 📁 prisma/
│   └── schema.prisma                 ← Database schema (User + Post models)
│
├── package.json                      ← Project config & dependencies list
├── tsconfig.json                     ← TypeScript configuration
├── tailwind.config.ts                ← Tailwind CSS configuration
├── next.config.ts                    ← Next.js configuration
├── eslint.config.mjs                 ← Code quality rules
├── bun.lock                          ← Locked dependency versions
└── .env                              ← Environment variables (Firebase config, DB URL)
```

---

## 📖 CHAPTER 5: HOW DOES THE APP WORK? (The Flow)

### When a User First Visits

```
1. Calibration Screen appears (loading animation with cycling words)
   ↓
2. User clicks "I'm Ready" 
   ↓
3. Home Page loads:
   - Hero section with "Start Training" button
   - Phase roadmap (4 phases, only Phase 1 unlocked)
   - Stats section (all zeros for new user)
   - Performance graph (empty state)
   ↓
4. Bottom dock shows: Home | Learn | Speed Test | Leaderboard | Progress | Profile | Settings | Download
```

### When a User Practices Typing

```
1. User clicks "Learn" in dock → Learn Page appears
   ↓
2. Learn Page shows 33 lessons as a vertical timeline
   - Completed lessons have green glow + checkmark
   - Current lesson has pulsing animation
   - Locked lessons are grayed out
   ↓
3. User clicks a lesson → SubChapterMap appears
   - Shows all sub-chapters (10-15 per lesson)
   - Completed sub-chapters have green dots
   - User clicks a sub-chapter
   ↓
4. Typing Interface appears (full screen):
   - Large text to type at the top
   - WPM + Accuracy counter at top
   - Visual keyboard at bottom
   ↓
5. User types character by character:
   - Correct → letter turns gray
   - Wrong → letter turns red, error counter increases
   - Keyboard highlights the next key to press
   ↓
6. User finishes typing:
   - Results modal appears (WPM, Accuracy, Time)
   - Options: Home | Phases | Retry | Next
   - Progress is saved to localStorage
   - Session record added for performance graph
   - If performance meets threshold → next phase unlocks
```

### How Progress Works (The Math)

**WPM (Words Per Minute):**
```
WPM = (correct characters / 5) / (time in minutes)
```
- Standard formula: 1 "word" = 5 characters
- Example: 250 correct chars in 60 seconds = 50 WPM

**Accuracy:**
```
Accuracy = (correct keystrokes / total keystrokes) × 100
```

**Phase Unlocking:**
- Phase 1: Always unlocked (starting phase)
- Phase 2: Unlocks when you hit 20 WPM + 90% accuracy in Phase 1
- Phase 3: Unlocks when you hit 40 WPM + 95% accuracy in Phase 2
- Phase 4: Unlocks when you hit 60 WPM + 98% accuracy in Phase 3

**Data Storage (localStorage):**
- Each user has a unique storage key: `typers-club-progress:user:email@example.com`
- Stores: total keystrokes, time spent, average WPM, per-phase progress, per-lesson sub-chapter completion, session history (last 50 records)
- Guests use: `typers-club-progress:guest`

---

## 📖 CHAPTER 6: KEY CONCEPTS EXPLAINED (Like You're 5)

### What is Next.js?
Next.js is a **framework for building websites**. It handles the hard stuff so you don't have to:
- **Routing** — which page shows when you click what
- **Server rendering** — generates HTML on the server for faster loading
- **API routes** — backend endpoints right inside your frontend project

Our app uses **App Router** — everything lives in `src/app/` folder. `page.tsx` is the main page.

### What is React?
React is a **library for building user interfaces with components**. Think of components as LEGO blocks:
- Each block is a self-contained piece of UI
- Blocks can be nested inside other blocks
- When data changes, React automatically updates only the affected blocks

Our app is a **Single Page Application (SPA)** — there's only ONE page (`page.tsx`) that swaps different views based on `appView` state.

### What is TypeScript?
TypeScript is **JavaScript with types**. Normal JavaScript lets you do anything:
```javascript
let x = "hello";     // string
x = 42;              // oops, now it's a number — no error!
```
TypeScript catches this:
```typescript
let x: string = "hello";
x = 42;  // ❌ ERROR! TypeScript says: "42 is not a string"
```

### What is Tailwind CSS?
Instead of writing separate CSS files, you add **classes directly in HTML**:
```html
<!-- Old way -->
<button class="my-button">Click</button>

<!-- Tailwind way -->
<button class="bg-blue-500 text-white rounded-lg px-4 py-2 hover:bg-blue-600">
  Click
</button>
```
Each class is a utility: `bg-blue-500` = blue background, `text-white` = white text, etc.

### What is the Service Worker (PWA)?
A Service Worker is a **background script** that runs in your browser. It can:
- **Cache files** — save app files to your device
- **Intercept network requests** — serve cached files when offline
- **Enable installation** — make the browser show "Install App" prompt

Our `sw.js` uses **stale-while-revalidate**: show cached file instantly, update cache in background.

### What is localStorage?
A **browser storage** that saves data as key-value pairs:
```javascript
localStorage.setItem('my-key', 'my-value');  // Save
localStorage.getItem('my-key');                // Read → 'my-value'
```
- Data persists even after closing the browser
- Limited to ~5MB per domain
- Our app stores progress, account data, and theme preference here

### What is Firebase?
Firebase is **Google's backend-as-a-service**. We use only **Firebase Auth** for Google Sign-In:
```
User clicks "Sign in with Google"
    ↓
Google popup appears
    ↓
User selects their Google account
    ↓
Firebase returns user data (name, email, photo)
    ↓
We create/link an account in localStorage
```

### What is Prisma?
Prisma is a **database ORM** (Object-Relational Mapper). Instead of writing raw SQL:
```sql
SELECT * FROM User WHERE email = 'test@example.com'
```
You write TypeScript:
```typescript
const user = await db.user.findUnique({ where: { email: 'test@example.com' } });
```
Our schema has User and Post models, though the main app uses localStorage for progress.

---

## 📖 CHAPTER 7: THE THEME SYSTEM (How Colors Work)

The app has **5 themes**. Each theme defines 20+ color properties:

| Property | What It Controls | Dark Theme Value |
|---|---|---|
| `--tc-bg` | Main background | `hsl(0 0% 4%)` (near black) |
| `--tc-surface` | Card/panel background | `hsl(0 0% 8%)` (dark gray) |
| `--tc-text` | Main text color | `hsl(0 0% 96%)` (near white) |
| `--tc-accent` | Primary accent color | `#89AACC` (steel blue) |
| `--tc-accent-from/to` | Gradient start/end | `#89AACC → #4E85BF` |
| `--tc-cursor` | Typing cursor gradient | `linear-gradient(90deg, #89AACC, #4E85BF)` |
| `--tc-keyboard-bg` | Keyboard background | `hsl(0 0% 6%)` |
| ...and 15+ more | | |

**How it works:**
1. `ThemeProvider` (in `theme-context.tsx`) reads the saved theme from localStorage
2. It applies all colors as CSS variables to `document.documentElement`
3. Every component uses `var(--tc-xxx)` to reference these colors
4. When user switches theme → all CSS variables update → entire app changes color instantly

---

## 📖 CHAPTER 8: THE LESSON CONTENT

The app contains **33 lessons** across **4 phases** with **300+ sub-chapters total**:

### Phase 1: The Foundation (15 lessons, 225 sub-chapters)
| Lesson | Keys | Example |
|---|---|---|
| 1 | A S D F | `asdf asdf asdf` |
| 2 | J K L ; | `jkl; jkl; jkl;` |
| 3 | Full Home Row | `asdf jkl; fdsa ;lkj` |
| 4 | G and H | `fg jh fg jh` |
| 5 | R and T | `rf tg rf tg` |
| 6 | U and Y | `ju yk ju yk` |
| 7 | E and I | `fe ji fe ji` |
| 8 | W and O | `fw go fw go` |
| 9 | Q and P | `fq jp fq jp` |
| 10 | V and B | `fv gb fv gb` |
| 11 | C and M | `fc jm fc jm` |
| 12 | X and N | `fx jn fx jn` |
| 13 | Z and , . | `fz j, fz j.` |
| 14 | Numbers Row | `1234567890` |
| 15 | Symbols | `!@#$%^&*()` |

### Phase 2: Intermediate (6 lessons, ~84 sub-chapters)
Simple words, shift keys (capitals), common phrases, programming keywords

### Phase 3: Advanced Prep (6 lessons, ~84 sub-chapters)
Full paragraphs, technical text, code snippets, complex formatting

### Phase 4: The Practitioner (6 lessons, ~84 sub-chapters)
Endless mode — mixed content for mastery

---

## 📖 CHAPTER 9: PRESENTATION TALKING POINTS

### Opening (30 seconds)
> "Today I'd like to present Typer's Club — a progressive typing tutor web application built with modern web technologies. It teaches touch typing through structured phases, real-time performance tracking, and speed tests."

### Key Features to Highlight (2 minutes each)
1. **Progressive Learning System** — 4 phases, 33 lessons, 300+ exercises
2. **Real-Time Feedback** — Live WPM, accuracy, visual keyboard highlighting
3. **Performance Analytics** — Canvas-based graphs, trend analysis, session history
4. **Authentication System** — Email/password login, Google Sign-In, OTP verification
5. **5 Custom Themes** — Dynamic color system using CSS variables
6. **Progressive Web App** — Install on any device, works offline
7. **Responsive Design** — Works on mobile, tablet, and desktop

### Technical Highlights (if asked)
- **Frontend**: Next.js 16, React 19, TypeScript, Tailwind CSS 4, shadcn/ui
- **Animations**: Framer Motion, GSAP, WebGL vortex background
- **Authentication**: Firebase Google Auth + custom email/phone auth with Nodemailer OTP
- **Data Storage**: localStorage (per-user isolation) + Prisma ORM (SQLite)
- **Offline Support**: Service Worker with stale-while-revalidate caching strategy
- **UI**: macOS-style animated dock, SVG wave background, canvas performance graph

### Common Questions & Answers

**Q: How is data stored?**
> "User progress and account data are stored in the browser's localStorage, scoped per user via their email. This means each user's data is completely isolated. For unauthenticated guests, a shared guest key is used."

**Q: How does the typing engine work?**
> "The engine tracks every keystroke with timestamps. WPM is calculated as (correct characters / 5) / minutes elapsed. Accuracy is correct keystrokes divided by total keystrokes. Phase unlocking is based on meeting both WPM and accuracy thresholds."

**Q: How does authentication work?**
> "We support two methods: Google Sign-In via Firebase Auth, and a custom email/password system with phone as an alternative password. For account creation, we send a 6-digit OTP via Nodemailer SMTP. The API route at /api/send-otp handles email delivery."

**Q: How does offline support work?**
> "A Service Worker (sw.js) intercepts all network requests. Static assets use stale-while-revalidate — serving cached versions instantly while updating in the background. API routes use network-first. A manifest.json file makes the app installable on any device."

**Q: How does theming work?**
> "Five theme definitions, each with 20+ color properties, are defined in theme-context.tsx. Colors are applied as CSS variables to the document root. Every component references these variables using var(--tc-xxx), so switching themes instantly updates the entire app."

---

## 📖 CHAPTER 10: IMPORTANT FILES TO KNOW

For your presentation, if someone asks "where is X?":

| Question | File |
|---|---|
| "Where is the main page?" | `src/app/page.tsx` |
| "Where is the typing logic?" | `src/lib/typing-engine.ts` |
| "Where are the lessons?" | `src/lib/lessons.ts` |
| "Where are the themes?" | `src/lib/theme-context.tsx` |
| "Where is the navigation?" | `src/components/typers-club/Navbar.tsx` |
| "Where is the typing screen?" | `src/components/typers-club/TypingInterface.tsx` |
| "Where is the login system?" | `src/components/typers-club/ProfilePage.tsx` |
| "Where is the speed test?" | `src/components/typers-club/SpeedTestPage.tsx` |
| "Where is the offline support?" | `public/sw.js` + `public/manifest.json` |
| "Where are the styles?" | `src/app/globals.css` |
| "Where is the layout wrapper?" | `src/app/layout.tsx` |
| "Where is the email OTP?" | `src/app/api/send-otp/route.ts` |
| "Where is Firebase config?" | `src/lib/firebase.ts` + `.env` |

---

## 📖 CHAPTER 11: ONE-MINUTE DEMO SCRIPT

1. **Open the app** → Calibration screen appears (mention it's a loading animation)
2. **Home page** → Point out the animated dock, hero section, phase roadmap
3. **Click Learn** → Show the lesson timeline with YouTube videos
4. **Click a lesson** → Show sub-chapter map
5. **Start typing** → Demonstrate real-time WPM/accuracy, keyboard highlighting, color feedback
6. **Complete a lesson** → Show results modal with WPM/accuracy
7. **Check Progress page** → Show the performance graph
8. **Switch theme** → Go to Settings, pick a theme, show entire app color change
9. **Show Speed Test** → Configure difficulty/time, start a test
10. **Show Download page** → Mention offline install capability

---

**Good luck with your presentation! You've got this. 🎯**
