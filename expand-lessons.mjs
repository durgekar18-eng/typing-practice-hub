import fs from 'fs';

const filePath = './src/lib/lessons.ts';
let content = fs.readFileSync(filePath, 'utf-8');

// New sub-chapters for each lesson (by phase and lesson index)
// Each entry is an array of {title, text, difficulty} objects
const newSubChapters = {
  // Phase 1: Home Row keys
  phase1: [
    // Lesson 1: Home Row A S D F
    [
      { title: "Fun Facts A", text: "a sad lad had a dad. add a fad. as a lad, dad had a sad fad. a dad had a fall. all dads add ads.", difficulty: "easy" },
      { title: "Keyboard Shortcut Hint", text: "add fads as sad lads fall. a dad adds a salad. salad adds flavor. fall adds glad feelings.", difficulty: "easy" },
      { title: "Mixed Review", text: "sad dad add fad as ads sad fads adds dad sad fad adds as ads dad sad adds fads.", difficulty: "medium" },
      { title: "Focus Accuracy", text: "asdf fdsa asdf fdsa ads fads sad dad adds lads salad falls dads glad half gash flash.", difficulty: "medium" },
    ],
    // Lesson 2: Home Row J K L ;
    [
      { title: "Fun Facts J", text: "jkl; jkl; ;lkj ;lkj all kids like jelly. just keep looking. jolly kids like juice.", difficulty: "easy" },
      { title: "Right Hand Flow", text: "jk l; jk l; kj ;l kj ;l jl jl k; k; jl jl k; k; just keep looking local.", difficulty: "easy" },
      { title: "Mixed Practice", text: "jkl; ;lkj asdf fdsa jkl; ;lkj jkl; fdsa asdf ;lkj jkl; asdf fdsa jkl; ;lkj.", difficulty: "medium" },
      { title: "Endurance Plus", text: "jkl; jkl; asdf fdsa ;lkj ;lkj asdf fdsa jkl; jkl; fdsa fdsa asdf jkl; ;lkj jkl.", difficulty: "medium" },
    ],
    // Lesson 3: Home Row Full
    [
      { title: "Sentence Fun", text: "all shall fall. a lad asks a lass. dad had a flask. glad lads add salad.", difficulty: "easy" },
      { title: "Home Row Story", text: "ask a glad lad. fall shall add a dash. flash a hall glass. lash a glass dash.", difficulty: "easy" },
      { title: "Speed Builder", text: "asdf jkl; fdsa ;lkj ask fall hall shall flask glad lash dash flash asdf jkl; fdsa.", difficulty: "medium" },
      { title: "Full Row Challenge", text: "all glad lads ask shall flask hall dash flash fall salad lads glass ash glad half staff.", difficulty: "medium" },
    ],
    // Lesson 4: G and H Keys
    [
      { title: "Fun Facts G", text: "a glad lad had a high goal. half a glass of hash. a hag had a giggle. dig a hedge.", difficulty: "easy" },
      { title: "G and H Words", text: "glad high hash half gash flash hedge haggle shield lodge badge dodge fudge", difficulty: "easy" },
      { title: "Mixed Drill", text: "fg jh fg jh glad high hash lash dash half gash flash hedge fg jh fg jh glad.", difficulty: "medium" },
      { title: "Speed Challenge", text: "glad hash half gash flash hedge haggle high lash dash glad hash half gash shield lodge.", difficulty: "medium" },
    ],
    // Lesson 5: R and T Keys
    [
      { title: "Fun Facts R", text: "a rat ate a tart. a star fell far. the start was a great draft. treat art right.", difficulty: "easy" },
      { title: "R and T Words", text: "raft tart treat great draft street trait start arrest grat trait rat tar rot tot", difficulty: "easy" },
      { title: "Mixed Sentences", text: "raft tart treat great draft street trait start arrest grat trait rat tar rot tot art.", difficulty: "medium" },
      { title: "Full Drill", text: "rf tg rf tg raft tart treat great draft street trait start rf tg rf tg arrest grat.", difficulty: "medium" },
    ],
    // Lesson 6: U and Y Keys
    [
      { title: "Fun Facts U", text: "you used your youth. yet you yield a juicy yam. yummy yogurt is good. young guys gym.", difficulty: "easy" },
      { title: "U and Y Words", text: "youth young yield your yule juice usage undue value guy gym you yet use your yak.", difficulty: "easy" },
      { title: "Mixed Review", text: "ju yk ju yk youth young yield your yule juice usage undue value guy gym ju yk ju yk.", difficulty: "medium" },
      { title: "Speed Plus", text: "you yet use your youth young juice gym yak yam yum yet guy gym yield value undue usage.", difficulty: "medium" },
    ],
    // Lesson 7: E and I Keys
    [
      { title: "Fun Facts E", text: "deep fire hides in the tree. fine kids line the street. elite fires slide free. tire a line.", difficulty: "easy" },
      { title: "E and I Words", text: "elite lion crime spider tire ride fire slide glide stride red fed see tree free deep.", difficulty: "easy" },
      { title: "Sentence Drill", text: "fe ji fe ji fire tire fine line dine kind hide side ride elite lion crime spider.", difficulty: "medium" },
      { title: "Advanced Mix", text: "red fed see tree free three seed feed feel feet deep kid lid dig big fig gig fire.", difficulty: "medium" },
    ],
    // Lesson 8: W and O Keys
    [
      { title: "Fun Facts W", text: "good old work goes on. gold grew cold. world work won gold. a wolf woke near town.", difficulty: "easy" },
      { title: "W and O Words", text: "window orange outcome overlook workflow overcome onboard went work wolf word wore woke world.", difficulty: "easy" },
      { title: "Mixed Sentences", text: "fw go fw go word work wolf glow gold golf world worse worth went window orange outcome.", difficulty: "medium" },
      { title: "Speed Drill", text: "went work wolf word wore worn woke world worse worth gold golf good grew glow gone goal.", difficulty: "medium" },
    ],
    // Lesson 9: Q and P Keys
    [
      { title: "Fun Facts Q", text: "quiet people pick pecks. a queen packed a quilt. quick picks play parts. quit playing.", difficulty: "easy" },
      { title: "Q and P Words", text: "picture puzzle people popular practice purpose purple quit quite queen quiet quote quest quiz.", difficulty: "easy" },
      { title: "Mixed Review", text: "fq jp fq jp quit pack quite pass queen path peace quiet peak quote picture puzzle.", difficulty: "medium" },
      { title: "Challenge Plus", text: "quit quite queen quiet quote quest quiz quill quick pack pass path peace peak pick pile.", difficulty: "medium" },
    ],
    // Lesson 10: V and B Keys
    [
      { title: "Fun Facts V", text: "vibrant birds build big nests. brave bears visit vast lands. bold voices blend vibes.", difficulty: "easy" },
      { title: "V and B Words", text: "vibrant brave brilliant volume visible valuable brother very verb vest vast view void vice.", difficulty: "easy" },
      { title: "Mixed Drill", text: "fv gb fv gb very best verb bear bold vest vast burn view void vibrant brave.", difficulty: "medium" },
      { title: "Speed Plus", text: "very verb vest vast view void vice visit vowel value best bear bold burn big bank.", difficulty: "medium" },
    ],
    // Lesson 11: C and M Keys
    [
      { title: "Fun Facts C", text: "clever monkeys climb. many came home. call me, come see my club. comic mix, magic.", difficulty: "easy" },
      { title: "C and M Words", text: "computer comment market member music complex company came mind call made cold move camp much.", difficulty: "easy" },
      { title: "Mixed Practice", text: "fc jm fc jm came mind call made cold move camp much card care computer comment.", difficulty: "medium" },
      { title: "Challenge Run", text: "came call came cold camp card care case cell city club mind made move much more.", difficulty: "medium" },
    ],
    // Lesson 12: X and N Keys
    [
      { title: "Fun Facts X", text: "next exam is on nine. nice extra news. new text needs fixing. mix nine nice zones.", difficulty: "easy" },
      { title: "X and N Words", text: "experience extension nineteen nothing mixture next name nine text nice noon exam extra express.", difficulty: "easy" },
      { title: "Mixed Review", text: "fx jn fx jn exit name next nine text nice noon exam extra need experience extension.", difficulty: "medium" },
      { title: "Speed Plus", text: "exit next text exam extra expand express extreme mix name nine nice noon none next nest.", difficulty: "medium" },
    ],
    // Lesson 13: Z and Comma/Period
    [
      { title: "Fun Facts Z", text: "zero jazz buzzed. zip, zoom, zap. a puzzle, a freeze. jazz, buzz, zero, zone, zoo.", difficulty: "easy" },
      { title: "Z Punctuation", text: "hello, world. this is fun. type fast, type well. zero, one, two, three. jazz is cool.", difficulty: "easy" },
      { title: "Mixed Sentences", text: "jazz buzz zero zone zoo zip zest freeze breeze puzzle hello, world. this is a test.", difficulty: "medium" },
      { title: "Speed Drill", text: "fz j, fz j, hello, world. this is a test. zero, one, two. jazz buzz zero zone zoo zip.", difficulty: "medium" },
    ],
    // Lesson 14: Numbers Row
    [
      { title: "Temperature", text: "98.6F 72.3F 45.1F 0.0F -12.5C 37.0C 100.0C 212.0F -40.0C 32.0F", difficulty: "hard" },
      { title: "Measurements", text: "5ft 10in 175cm 65kg 150lbs 3.5mi 5.6km 24oz 750ml 2.5in 6.35cm", difficulty: "hard" },
      { title: "License Plates", text: "ABC-1234 XYZ-5678 TYP-9012 KEY-3456 SPD-7890 WPM-1357 4QZ-2860", difficulty: "hard" },
      { title: "Mixed Numeric", text: "Room 404 Floor 13 Apt 2B Gate 7C Seat 14A Row 22 Box 88 Lot 5 Spot 99", difficulty: "hard" },
    ],
    // Lesson 15: Symbols
    [
      { title: "Social Media", text: "RT @user: This is amazing! #trending #viral 100% agree!!! (see link below) -> bit.ly/abc", difficulty: "hard" },
      { title: "Code Review", text: "if (x !== null && y > 0) { return x * y; } else { throw new Error('Invalid!'); }", difficulty: "hard" },
      { title: "Math Formula", text: "E = mc^2 (a + b)^2 = a^2 + 2ab + b^2 100% = (50% + 50%) (3 * 4) / 2 = 6", difficulty: "hard" },
      { title: "Special Chars", text: "price: $49.99 (was $79.99)! discount: 37.5% ~save $30.00 @store *limited* &free ship^", difficulty: "hard" },
    ],
  ],

  // Phase 2: Intermediate
  phase2: [
    // Lesson 1: Simple Words
    [
      { title: "Famous Quote", text: "To be or not to be that is the question. Whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune.", difficulty: "medium" },
      { title: "Recipe Steps", text: "First crack two eggs into a bowl. Add a pinch of salt and a dash of pepper. Beat well until smooth. Heat butter in a pan and pour in the mixture.", difficulty: "medium" },
      { title: "Song Lyrics", text: "Twinkle twinkle little star how I wonder what you are. Up above the world so high like a diamond in the sky.", difficulty: "medium" },
      { title: "Movie Dialogue", text: "Here is looking at you kid. Of all the gin joints in all the towns in all the world she walks into mine. Play it Sam.", difficulty: "medium" },
    ],
    // Lesson 2: Shift Keys: Capitals
    [
      { title: "Famous Quotes", text: "The only thing we have to fear is fear itself. Ask not what your country can do for you. I have a dream that one day all men will be equal.", difficulty: "medium" },
      { title: "Landmarks", text: "Eiffel Tower Statue of Liberty Great Wall of China Taj Mahal Colosseum Machu Picchu Sydney Opera House Big Ben Petra Christ the Redeemer", difficulty: "medium" },
      { title: "Brands", text: "Google Apple Microsoft Amazon Tesla Netflix Spotify Adobe Oracle Intel Samsung Sony Nike BMW Mercedes Boeing Airbus Pfizer", difficulty: "medium" },
      { title: "Historical Figures", text: "Albert Einstein Marie Curie Leonardo da Vinci Isaac Newton Nikola Tesla Ada Lovelace Charles Darwin Galileo Galilei Confucius Aristotle Plato Socrates", difficulty: "medium" },
    ],
    // Lesson 3: Common Phrases
    [
      { title: "Recipe Phrases", text: "Preheat the oven to three hundred and fifty degrees. Combine the dry ingredients in a large mixing bowl. Gradually fold in the wet ingredients until just combined. Bake for twenty five minutes or until golden brown.", difficulty: "medium" },
      { title: "Social Media Post", text: "Just finished an amazing hike up the mountain trail today. The views were absolutely breathtaking. Nothing beats being out in nature and clearing your mind. Who else loves outdoor adventures?", difficulty: "medium" },
      { title: "Movie Quotes", text: "May the Force be with you. I will be back. You talking to me? Here is looking at you kid. Frankly my dear I do not give a damn. Life is like a box of chocolates.", difficulty: "medium" },
      { title: "Song Fragments", text: "Imagine all the people living life in peace. We will rock you we will rock you. Is this the real life or is this just fantasy. Bohemian Rhapsody is a classic rock masterpiece.", difficulty: "medium" },
    ],
    // Lesson 4: Programming Keywords
    [
      { title: "Rust Keywords", text: "fn main let mut impl struct enum match trait pub use mod crate super self Self where async move loop break continue return yield dyn box const static unsafe extern ref type", difficulty: "medium" },
      { title: "Go Keywords", text: "func main package import var const type struct interface map chan go select defer range fallthrough break continue return switch case default if else for goto", difficulty: "medium" },
      { title: "Java Keywords", text: "public private protected static final abstract class interface extends implements new this super void int long double float boolean char byte short package import return try catch finally throw throws instanceof synchronized volatile transient native enum assert", difficulty: "medium" },
      { title: "CSS at Rules", text: "@media @keyframes @import @font-face @supports @layer @container @property @charset @namespace @page @counter-style @document @viewport", difficulty: "medium" },
    ],
    // Lesson 5: Punctuation Practice
    [
      { title: "News Headline", text: "Breaking News: Global Summit Reaches Historic Agreement on Climate Change! Leaders from 195 nations committed to reducing emissions by 50% before 2035. \"This is a turning point,\" said the UN Secretary-General.", difficulty: "medium" },
      { title: "Product Review", text: "Rating: 4.5/5 stars. This product exceeded my expectations! The build quality is excellent, and the battery lasts all day. My only complaint? The screen could be brighter. Overall, I would definitely recommend it to anyone looking for a reliable device.", difficulty: "medium" },
      { title: "Travel Blog", text: "Day 3 in Tokyo: We visited the Senso-ji temple, explored Akihabara, and ate the best ramen of our lives. The bullet train to Kyoto was incredible (300 km/h!). Can not wait to see what tomorrow brings.", difficulty: "medium" },
      { title: "Technical Docs", text: "Note: This API is deprecated as of v3.2.0. Please use the new endpoint: /api/v2/users. Required headers: Authorization: Bearer <token>, Content-Type: application/json. See migration guide (Ref. #4521) for details.", difficulty: "medium" },
    ],
    // Lesson 6: Speed Building: Short
    [
      { title: "Famous Speech", text: "Four score and seven years ago our fathers brought forth on this continent a new nation conceived in liberty and dedicated to the proposition that all men are created equal. We are now engaged in a great civil war testing whether that nation can long endure.", difficulty: "hard" },
      { title: "Science Fact", text: "The speed of light is approximately 299,792 kilometers per second. Water boils at 100 degrees Celsius at sea level. The human body contains about 60 percent water. Earth orbits the Sun at roughly 107,000 kilometers per hour.", difficulty: "hard" },
      { title: "History Passage", text: "The Industrial Revolution transformed society in profound ways. Steam engines powered factories, railroads connected cities, and mass production made goods affordable. Urbanization accelerated as people migrated from farms to cities seeking employment in the growing manufacturing sector.", difficulty: "hard" },
      { title: "Poetry Excerpt", text: "Two roads diverged in a yellow wood and sorry I could not travel both and be one traveler long I stood and looked down one as far as I could to where it bent in the undergrowth. I took the one less traveled by and that has made all the difference.", difficulty: "hard" },
    ],
  ],

  // Phase 3: Advanced
  phase3: [
    // Lesson 1: Code Snippets
    [
      { title: "GraphQL Schema", "text": "type User { id: ID! name: String! email: String! posts: [Post!]! createdAt: DateTime! } type Query { user(id: ID!): User users(limit: Int, offset: Int): [User!]! } type Mutation { createUser(input: CreateUserInput!): User! updateUser(id: ID!, input: UpdateUserInput!): User! } input CreateUserInput { name: String! email: String! password: String! }", difficulty: "hard" },
      { title: "Tailwind Classes", "text": "className='flex items-center justify-between px-6 py-4 bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700'", difficulty: "hard" },
      { title: "Bash Script", "text": "#!/bin/bash\nset -euo pipefail\nDEPLOY_ENV=${1:-staging}\nBRANCH=$(git branch --show-current)\necho \"Deploying $BRANCH to $DEPLOY_ENV\"\nnpm ci --production\nnpm run build\nrsync -avz ./dist/ server:/var/www/app/\necho \"Deploy complete!\"", difficulty: "hard" },
      { title: "Regex Patterns", "text": "const validators = {\n  ipv4: /^(?:(?:25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d\\d?)$/,\n  hex: /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/,\n  uuid: /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i\n};", difficulty: "hard" },
    ],
    // Lesson 2: JSON Data
    [
      { title: "OpenAPI Spec", "text": '{\n  "openapi": "3.0.3",\n  "info": {\n    "title": "Typer Club API",\n    "version": "2.0.0",\n    "description": "REST API for the typing tutor application"\n  },\n  "servers": [\n    { "url": "https://api.typers-club.com/v2" }\n  ],\n  "paths": {\n    "/users/{id}/stats": {\n      "get": {\n        "summary": "Get user typing statistics",\n        "parameters": [\n          { "name": "id", "in": "path", "required": true, "schema": { "type": "string" } }\n        ]\n      }\n    }\n  }\n}', difficulty: "hard" },
      { title: "ESLint Config", "text": '{\n  "env": { "browser": true, "es2024": true, "node": true },\n  "extends": ["next/core-web-vitals", "plugin:@typescript-eslint/recommended"],\n  "rules": {\n    "no-unused-vars": "warn",\n    "prefer-const": "error",\n    "no-console": ["warn", { "allow": ["warn", "error"] }],\n    "@typescript-eslint/no-explicit-any": "warn"\n  }\n}', difficulty: "hard" },
      { title: "Package Lock Entry", "text": '{\n  "name": "typers-club",\n  "lockfileVersion": 3,\n  "packages": {\n    "": { "name": "typers-club", "dependencies": { "react": "^18.2.0", "framer-motion": "^10.16.0" } },\n    "node_modules/react": { "version": "18.2.0", "resolved": "https://registry.npmjs.org/react/-/react-18.2.0.tgz" }\n  }\n}', difficulty: "hard" },
      { title: "GitHub Actions", "text": '{\n  "name": "CI Pipeline",\n  "on": { "push": { "branches": ["main"] }, "pull_request": { "branches": ["main"] } },\n  "jobs": {\n    "test": {\n      "runs-on": "ubuntu-latest",\n      "steps": [\n        { "uses": "actions/checkout@v4" },\n        { "run": "npm ci && npm run lint && npm run test && npm run build" }\n      ]\n    }\n  }\n}', difficulty: "hard" },
    ],
    // Lesson 3: HTML Markup
    [
      { title: "React JSX", "text": "function LessonCard({ lesson, isCompleted, isActive, onClick }) {\n  return (\n    <button\n      className={`lesson-card ${isCompleted ? 'completed' : ''} ${isActive ? 'active' : ''}`}\n      onClick={onClick}\n      aria-label={`Lesson: ${lesson.title}`}\n    >\n      <span className='lesson-id'>{lesson.id}</span>\n      <h3 className='lesson-title'>{lesson.title}</h3>\n      <span className='difficulty-badge'>{lesson.difficulty}</span>\n    </button>\n  );\n}", difficulty: "hard" },
      { title: "CSS Grid Layout", "text": ".dashboard {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n  grid-template-rows: auto 1fr auto;\n  grid-template-areas:\n    'header header header'\n    'sidebar main main'\n    'footer footer footer';\n  gap: 1.5rem;\n  min-height: 100vh;\n}", difficulty: "hard" },
      { title: "Tailwind Component", "text": "<div class='relative overflow-hidden rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 p-[1px] shadow-xl'>\n  <div class='rounded-2xl bg-white dark:bg-gray-900 p-6'>\n    <h3 class='text-xl font-bold text-gray-900 dark:text-white'>Typing Stats</h3>\n    <div class='mt-4 grid grid-cols-3 gap-4'>\n      <div class='text-center'>\n        <p class='text-3xl font-extrabold text-indigo-600'>72</p>\n        <p class='text-sm text-gray-500'>WPM</p>\n      </div>\n    </div>\n  </div>\n</div>", difficulty: "hard" },
      { title: "Responsive Breakpoints", "text": "/* Mobile First Responsive Design */\n.container { padding: 1rem; }\n@media (min-width: 640px) { .container { padding: 1.5rem; max-width: 640px; margin: 0 auto; } }\n@media (min-width: 768px) { .container { max-width: 768px; } }\n@media (min-width: 1024px) { .container { max-width: 1024px; } }\n@media (min-width: 1280px) { .container { max-width: 1280px; } }", difficulty: "hard" },
    ],
    // Lesson 4: SQL Queries
    [
      { title: "Recursive CTE", "text": "WITH RECURSIVE lesson_hierarchy AS (\n  SELECT id, title, phase_id, 1 AS depth\n  FROM lessons WHERE parent_id IS NULL\n  UNION ALL\n  SELECT l.id, l.title, l.phase_id, h.depth + 1\n  FROM lessons l\n  JOIN lesson_hierarchy h ON l.parent_id = h.id\n)\nSELECT * FROM lesson_hierarchy ORDER BY phase_id, depth;", difficulty: "hard" },
      { title: "Full Text Search", "text": "SELECT id, title, difficulty,\n  ts_rank(text_search_vector, query) AS rank\nFROM lessons,\n  plainto_tsquery('english', 'home row keys typing') AS query\nWHERE text_search_vector @@ query\nORDER BY rank DESC\nLIMIT 10;", difficulty: "hard" },
      { title: "Array Operations", "text": "SELECT id, title, focus_keys,\n  array_length(focus_keys, 1) AS key_count,\n  array_position(focus_keys, 'a') AS a_position\nFROM lessons\nWHERE 'shift' = ANY(focus_keys)\n   OR array_contains(focus_keys, 'a');\n\nUPDATE lessons\nSET focus_keys = array_append(focus_keys, 'shift')\nWHERE id = 2 AND NOT 'shift' = ANY(focus_keys);", difficulty: "hard" },
      { title: "Materialized View", "text": "CREATE MATERIALIZED VIEW user_leaderboard AS\nSELECT\n  u.id,\n  u.username,\n  COUNT(DISTINCT up.lesson_id) AS lessons_completed,\n  ROUND(AVG(up.wpm), 1) AS avg_wpm,\n  ROUND(AVG(up.accuracy), 1) AS avg_accuracy,\n  RANK() OVER (ORDER BY AVG(up.wpm) DESC) AS global_rank\nFROM users u\nJOIN user_progress up ON u.id = up.user_id\nWHERE up.completed_at IS NOT NULL\nGROUP BY u.id, u.username\nWITH DATA;\n\nREFRESH MATERIALIZED VIEW CONCURRENTLY user_leaderboard;", difficulty: "hard" },
    ],
    // Lesson 5: Markdown Content
    [
      { title: "GitHub Issue", "text": "## Bug: Sub-chapter progress not persisting after refresh\n\n### Steps to Reproduce\n1. Navigate to Learn page\n2. Complete sub-chapter 3 of Lesson 5\n3. Refresh the page\n4. Observe that progress is lost\n\n### Expected Behavior\nSub-chapter completion should persist in localStorage.\n\n### Environment\n- Browser: Chrome 122\n- OS: macOS Sonoma\n- Version: 2.0.0\n\n### Screenshots\nProgress resets from `completedSubChapters: [0,1,2,3]` to `[0,1,2]` after refresh.\n\n/cc @backend-team", difficulty: "hard" },
      { title: "API Reference", "text": "## Update User Profile\n\n### `PATCH /api/users/:id`\n\nUpdates the authenticated user's profile information.\n\n#### Request Headers\n| Header | Value |\n|--------|-------|\n| Authorization | Bearer {token} |\n| Content-Type | application/json |\n\n#### Request Body\n```json\n{\n  \"name\": \"string (max 100)\",\n  \"bio\": \"string (max 500, optional)\",\n  \"theme\": \"light\" | \"dark\",\n  \"soundEnabled\": \"boolean\"\n}\n```\n\n#### Response `200 OK`\n```json\n{ \"success\": true, \"user\": { \"id\": 42, \"name\": \"Updated Name\" } }\n```", difficulty: "hard" },
      { title: "Pull Request", "text": "## feat: Add sub-chapter progress tracking\n\n### Changes\n- Added `SubChapter` interface with id, title, text, and difficulty\n- Updated `Lesson` interface to include subChapters array\n- Implemented `getSubChapterText()` helper function\n- Added per-sub-chapter completion tracking in progress engine\n\n### Testing\n- [x] Unit tests for new helper functions\n- [x] Integration tests with progress engine\n- [x] Manual testing on Chrome, Firefox, Safari\n\n### Breaking Changes\nNone. This is a backward-compatible addition.\n\n### Related Issues\nCloses #142, #158", difficulty: "hard" },
      { title: "Architecture Doc", "text": "# System Architecture\n\n## Frontend\n```\nsrc/\n  app/\n    layout.tsx          Root layout with providers\n    page.tsx            Home / Landing page\n    learn/\n      page.tsx          Phase selection\n      [phaseId]/\n        page.tsx        Lesson overview\n    practice/\n      [subChapterId]/\n        page.tsx        Typing session\n  components/\n    ui/                 Shared components\n    features/           Feature-specific components\n  lib/\n    engine.ts           Typing engine\n    store.ts            State management\n    lessons.ts          Lesson data\n```\n\n## Data Flow\n1. User selects a lesson from the path map\n2. Lesson data loaded from `lessons.ts`\n3. Sub-chapter text displayed in typing interface\n4. Engine tracks WPM, accuracy, errors in real-time\n5. On completion, progress saved to localStorage", difficulty: "hard" },
    ],
    // Lesson 6: Technical Paragraph
    [
      { title: "WebSocket Protocol", "text": "WebSocket provides full-duplex communication channels over a single TCP connection. Unlike HTTP's request-response model, WebSocket enables persistent connections where both client and server can send messages independently. This makes it ideal for real-time applications like chat systems, live notifications, collaborative editing, and multiplayer games. The protocol starts with an HTTP handshake that upgrades the connection to WebSocket.", difficulty: "hard" },
      { title: "Graph Databases", "text": "Graph databases store data as nodes and edges, representing entities and their relationships. Neo4j, the most popular graph database, uses Cypher query language for pattern matching. Unlike relational databases requiring expensive JOINs for connected data, graph databases traverse relationships in constant time. They excel in social networks, recommendation engines, fraud detection, and knowledge graphs where relationship queries are the primary access pattern.", difficulty: "hard" },
      { title: "Functional Programming", "text": "Functional programming treats computation as the evaluation of mathematical functions, avoiding mutable state and side effects. Core concepts include pure functions that always return the same output for given inputs, immutability that prevents data modification after creation, and higher-order functions that accept or return other functions. Languages like Haskell enforce these principles, while JavaScript and TypeScript support them optionally through map, filter, and reduce.", difficulty: "hard" },
      { title: "Edge Computing", "text": "Edge computing processes data closer to the source of generation rather than relying on centralized cloud servers. By deploying compute resources at network edges near end users, latency drops significantly from hundreds of milliseconds to single digits. Content delivery networks were early adopters, caching static assets at edge locations. Modern edge platforms like Cloudflare Workers and Vercel Edge Functions now run serverless code at the edge, enabling personalized and dynamic responses globally.", difficulty: "hard" },
    ],
  ],

  // Phase 4: Practitioner
  phase4: [
    // Lesson 1: Endless Mode: Speed Run
    [
      { title: "Keyboard History", "text": "The QWERTY keyboard layout was invented by Christopher Latham Sholes in 1873 for the Sholes and Glidden typewriter. Contrary to popular belief, it was not designed to slow down typists but to prevent adjacent typebars from jamming by separating commonly paired letters. Despite the availability of more efficient layouts like Dvorak and Colemak, QWERTY remains the dominant standard worldwide due to network effects and established muscle memory.", difficulty: "hard" },
      { title: "Touch Typing Origins", "text": "Touch typing was pioneered by Frank Edward McGurrin, a court stenographer from Salt Lake City, who won a widely publicized typing contest in 1888. Unlike his competitors who used the hunt-and-peck method, McGurrin typed without looking at the keys. His victory demonstrated that touch typing was not only possible but superior in speed, and it sparked a revolution in typing education that continues to this day.", difficulty: "hard" },
      { title: "Speed Records", "text": "The official Guinness World Record for typing speed belongs to Stella Pajunas-Garnand, who reached 216 words per minute on an IBM electric typewriter in 1946. Modern computer keyboards have enabled even higher speeds, with competitive typists regularly exceeding 150 WPM on platforms like TypeRacer and Monkeytype. However, sustained speed over long sessions typically averages much lower, around 75 to 100 WPM for professional typists.", difficulty: "hard" },
      { title: "Ergonomic Evolution", "text": "Ergonomic keyboard design has evolved significantly since the flat typewriter keyboard. Split keyboards like the Microsoft Sculpt and Kinesis Advantage separate the hands to reduce ulnar deviation. Columnar layouts align keys with natural finger movement. Some models like the ErgoDox and Moonlander offer fully programmable layers, allowing users to customize every key position. These innovations aim to prevent repetitive strain injuries while maintaining or even improving typing speed.", difficulty: "hard" },
    ],
    // Lesson 2: Endless Mode: Technical
    [
      { title: "WebAssembly", "text": "WebAssembly (Wasm) enables high-performance code execution in web browsers by compiling languages like C++, Rust, and Go to a portable binary format. It runs at near-native speed, making it suitable for computationally intensive tasks like image processing, game engines, and scientific simulations. WebAssembly complements JavaScript rather than replacing it, allowing developers to choose the right tool for each component of their application.", difficulty: "hard" },
      { title: "Event Sourcing", "text": "Event sourcing stores all changes to application state as a sequence of immutable events. Instead of updating records in place, each action produces an event that is appended to an event log. The current state is reconstructed by replaying events from the beginning. This approach provides a complete audit trail, enables temporal queries, and simplifies debugging by revealing exactly how the system reached its current state.", difficulty: "hard" },
      { title: "Container Security", "text": "Container security requires a multi-layered approach spanning the entire lifecycle. Base images should be minimal and scanned for vulnerabilities using tools like Trivy or Snyk. Runtime security monitors container behavior for anomalous activity such as unexpected network connections or file system modifications. Network policies restrict communication between containers following the principle of least privilege. Secrets management through vault systems prevents credential exposure.", difficulty: "hard" },
      { title: "Serverless Architecture", "text": "Serverless computing abstracts infrastructure management, allowing developers to focus purely on business logic. Functions execute in response to events like HTTP requests, database changes, or message queue entries. While the name suggests no servers exist, the model eliminates server provisioning, scaling, and maintenance. Cold start latency remains a challenge, but innovations like provisioned concurrency and smaller function packages have significantly reduced response times.", difficulty: "hard" },
    ],
    // Lesson 3: Endless Mode: Literary
    [
      { title: "Technology and Nature", "text": "In the quiet hours before dawn, when the digital world sleeps and servers hum their low lullabies, there exists a moment of pure possibility. The cursor blinks on empty screens like a heartbeat, waiting for the first keystroke of a new day. Each tap is a small act of creation, transforming thought into reality one character at a time. This is the poetry of programming, where logic meets imagination at the intersection of human ingenuity and machine precision.", difficulty: "hard" },
      { title: "The Silent Language", "text": "Words are the building blocks of civilization. From clay tablets in ancient Mesopotamia to glowing screens in modern cafes, the act of writing has defined what it means to be human. Each generation inherits a language shaped by its predecessors and reshapes it for its children. The keyboard, for all its mechanical simplicity, is the latest chapter in this ancient story of expression, connecting minds across time and space through the simple power of typed words.", difficulty: "hard" },
      { title: "Digital Gardens", "text": "A digital garden is not a portfolio of finished works but a living collection of growing ideas. Unlike a blog presented in reverse chronological order, a digital garden allows ideas to evolve publicly, shifting from seedlings to budding notes to evergreen articles. This metaphor of cultivation reminds us that learning is not linear but organic. The best digital gardens are tended with care, weeded of outdated notions, and fertilized with new connections between concepts.", difficulty: "hard" },
      { title: "The Art of Code", "text": "There is a certain beauty in well-written code that transcends its functional purpose. Like a well-crafted sentence, elegant code communicates intent with clarity and economy. Variable names are chosen with the precision of a poet selecting words. Function structures mirror the narrative arcs of stories, with clear beginnings, logical progressions, and satisfying conclusions. The best code is not merely correct but graceful, not just efficient but expressive, transforming the mundane task of instructing machines into an art form.", difficulty: "hard" },
    ],
    // Lesson 4: Endless Mode: Philosophy
    [
      { title: "The Beginner Mind", "text": "In Zen Buddhism, the concept of shoshin, or beginner's mind, encourages approaching every situation with openness and eagerness, free from preconceptions. In typing practice, this means treating each session as if it were your first, maintaining curiosity about the craft and avoiding the complacency that comes with familiarity. The expert who retains a beginner's mind continues to grow, while the expert who believes they have nothing left to learn has already stopped improving.", difficulty: "hard" },
      { title: "Deliberate Practice", "text": "Anders Ericsson's research on deliberate practice revealed that the key differentiator between experts and novices is not innate talent but the quality of practice. Deliberate practice involves identifying specific weaknesses, designing targeted exercises to address them, seeking immediate feedback, and pushing beyond comfort zones. In typing, this means analyzing error patterns, focusing on problem keys, and gradually increasing difficulty rather than simply repeating comfortable exercises.", difficulty: "hard" },
      { title: "The Pomodoro Principle", "text": "The Pomodoro Technique, developed by Francesco Cirillo in the late 1980s, breaks work into focused intervals separated by short breaks. Typically, 25 minutes of concentrated effort is followed by a 5-minute rest. This rhythm prevents mental fatigue and maintains high-quality output throughout extended practice sessions. Applied to typing, regular Pomodoro sessions build endurance while ensuring each practice period benefits from full concentration.", difficulty: "hard" },
      { title: "Compound Interest of Skills", "text": "Albert Einstein reportedly called compound interest the eighth wonder of the world. The same principle applies to skill development. Improving by just one percent each day results in being thirty-seven times better after a year. In typing, daily practice that yields even marginal improvements in speed or accuracy compounds into dramatic progress over months and years. The gap between those who practice daily and those who practice occasionally grows exponentially, not linearly.", difficulty: "hard" },
    ],
    // Lesson 5: Endless Mode: Science
    [
      { title: "Cognitive Load Theory", "text": "Cognitive load theory, developed by John Sweller, explains how the limited capacity of working memory affects learning. In typing, intrinsic load comes from the complexity of the text being typed, extraneous load from distractions or poor interface design, and germane load from the effort of building schemas. Effective typing practice minimizes extraneous load through clean interfaces while optimizing germane load through progressively challenging exercises that strengthen motor patterns.", difficulty: "hard" },
      { title: "Interleaving Effect", "text": "Research in motor learning has demonstrated that interleaving different types of practice, rather than focusing on one skill at a time, leads to better long-term retention. In typing, this means alternating between different key combinations, text types, and difficulty levels within a single session. Although blocked practice feels easier in the moment, interleaved practice forces the brain to constantly retrieve and apply different motor programs, strengthening the neural pathways responsible for flexible, adaptable typing performance.", difficulty: "hard" },
      { title: "Visual Feedback Loop", "text": "The visual feedback loop in typing involves perceiving the target text, planning the motor sequence, executing keystrokes, and comparing the output against the target. This cycle repeats hundreds of times per minute during fluent typing. Research shows that even brief disruptions to this loop, such as looking away from the screen or encountering an unexpected error, significantly impact both speed and accuracy. Minimizing interruptions to the feedback loop is essential for maintaining optimal typing performance.", difficulty: "hard" },
      { title: "Metacognition in Practice", "text": "Metacognition, or thinking about thinking, plays a crucial role in skill development. Expert typists monitor their own performance in real-time, detecting errors before conscious recognition and adjusting their technique subconsciously. Developing metacognitive awareness involves regularly reflecting on your typing patterns, identifying recurring mistakes, understanding why they occur, and consciously addressing them. This self-awareness accelerates improvement by making practice more targeted and intentional.", difficulty: "hard" },
    ],
    // Lesson 6: Endless Mode: Code
    [
      { title: "Binary Tree Traversal", "text": "class TreeNode<T> {\n  value: T;\n  left: TreeNode<T> | null;\n  right: TreeNode<T> | null;\n  constructor(value: T) {\n    this.value = value;\n    this.left = null;\n    this.right = null;\n  }\n}\n\nfunction inorderTraversal<T>(root: TreeNode<T> | null): T[] {\n  const result: T[] = [];\n  function traverse(node: TreeNode<T> | null) {\n    if (!node) return;\n    traverse(node.left);\n    result.push(node.value);\n    traverse(node.right);\n  }\n  traverse(root);\n  return result;\n}", difficulty: "hard" },
      { title: "Observable Pattern", "text": "class Observable<T> {\n  private subscribers: Set<(value: T) => void> = new Set();\n  private _value: T;\n\n  constructor(initialValue: T) {\n    this._value = initialValue;\n  }\n\n  get value(): T {\n    return this._value;\n  }\n\n  subscribe(callback: (value: T) => void): () => void {\n    this.subscribers.add(callback);\n    callback(this._value);\n    return () => this.subscribers.delete(callback);\n  }\n\n  next(value: T): void {\n    this._value = value;\n    this.subscribers.forEach(fn => fn(value));\n  }\n}", difficulty: "hard" },
      { title: "Generic Stack", "text": "class Stack<T> {\n  private items: T[] = [];\n\n  push(item: T): void {\n    this.items.push(item);\n  }\n\n  pop(): T | undefined {\n    if (this.items.length === 0) {\n      throw new Error('Stack is empty');\n    }\n    return this.items.pop();\n  }\n\n  peek(): T | undefined {\n    return this.items[this.items.length - 1];\n  }\n\n  get size(): number {\n    return this.items.length;\n  }\n\n  isEmpty(): boolean {\n    return this.items.length === 0;\n  }\n\n  clear(): void {\n    this.items = [];\n  }\n}", difficulty: "hard" },
      { title: "Rate Limiter", "text": "class RateLimiter {\n  private requests: Map<string, number[]> = new Map();\n  private maxRequests: number;\n  private windowMs: number;\n\n  constructor(maxRequests: number, windowMs: number) {\n    this.maxRequests = maxRequests;\n    this.windowMs = windowMs;\n  }\n\n  isAllowed(key: string): boolean {\n    const now = Date.now();\n    const windowStart = now - this.windowMs;\n    const timestamps = this.requests.get(key) || [];\n    const recentRequests = timestamps.filter(t => t > windowStart);\n\n    if (recentRequests.length >= this.maxRequests) {\n      this.requests.set(key, recentRequests);\n      return false;\n    }\n\n    recentRequests.push(now);\n    this.requests.set(key, recentRequests);\n    return true;\n  }\n}", difficulty: "hard" },
    ],
  ],
};

// Process the file
const lines = content.split('\n');

// Find all lines with sc(10, - these are the last sub-chapters
// We need to track which lesson we're in to know which new sub-chapters to add
let lessonIndex = -1;
let currentPhase = '';

const newLines = [];

for (let i = 0; i < lines.length; i++) {
  newLines.push(lines[i]);

  // Track phase
  if (lines[i].includes('PHASE_1_LESSONS')) {
    currentPhase = 'phase1';
    lessonIndex = -1;
  } else if (lines[i].includes('PHASE_2_LESSONS')) {
    currentPhase = 'phase2';
    lessonIndex = -1;
  } else if (lines[i].includes('PHASE_3_LESSONS')) {
    currentPhase = 'phase3';
    lessonIndex = -1;
  } else if (lines[i].includes('PHASE_4_LESSONS')) {
    currentPhase = 'phase4';
    lessonIndex = -1;
  }

  // Track lesson starts (id: N, within a lesson object)
  if (lines[i].match(/^\s+id:\s+\d+,$/) && currentPhase) {
    lessonIndex++;
  }

  // Find sc(10, lines - these are the last sub-chapters
  if (lines[i].match(/^\s+sc\(10,/) && currentPhase && lessonIndex >= 0) {
    const phaseData = newSubChapters[currentPhase];
    if (phaseData && phaseData[lessonIndex]) {
      // Add 4 new sub-chapters (ids 11-14)
      for (let j = 0; j < 4; j++) {
        const sub = phaseData[lessonIndex][j];
        const id = 11 + j;
        const indent = lines[i].match(/^(\s+)/)[1]; // Get the indentation
        // Escape any single quotes in text
        const escapedText = sub.text.replace(/'/g, "\\'");
        newLines.push(`${indent}sc(${id}, "${sub.title}", '${escapedText}', '${sub.difficulty}'),`);
      }
    }
  }
}

const newContent = newLines.join('\n');

// Also update the comment
const updatedContent = newContent.replace(
  '// Each lesson (chapter) now contains 10–15 sub-chapters.',
  '// Each lesson (chapter) now contains 15 sub-chapters.'
);

fs.writeFileSync(filePath, updatedContent, 'utf-8');
console.log('Done! File updated successfully.');

// Verify counts
const p1 = (updatedContent.match(/sc\(10,/g) || []).length;
const p2 = (updatedContent.match(/sc\(11,/g) || []).length;
const p3 = (updatedContent.match(/sc\(12,/g) || []).length;
const p4 = (updatedContent.match(/sc\(13,/g) || []).length;
const p5 = (updatedContent.match(/sc\(14,/g) || []).length;
console.log(`sc(10,) count: ${p1} (should be 33)`);
console.log(`sc(11,) count: ${p2} (should be 33)`);
console.log(`sc(12,) count: ${p3} (should be 33)`);
console.log(`sc(13,) count: ${p4} (should be 33)`);
console.log(`sc(14,) count: ${p5} (should be 33)`);
