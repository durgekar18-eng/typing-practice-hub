#!/usr/bin/env python3
"""
Generate 6 professional diagrams for B.Tech mini project report:
"Typer's Club - A Web-Based Typing Tutor"
"""

import asyncio
import os
from playwright.async_api import async_playwright

OUTPUT_DIR = "/home/z/my-project/report-diagrams"


def get_base_css(w, h):
    return """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  background: #FFFFFF;
  color: #1E293B;
  overflow: hidden;
}
.diagram {
  width: """ + str(w) + """px;
  height: """ + str(h) + """px;
  padding: 40px;
  background: #FFFFFF;
  position: relative;
}
.title {
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  color: #0F172A;
  margin-bottom: 8px;
  letter-spacing: 0.01em;
}
.subtitle {
  text-align: center;
  font-size: 13px;
  color: #64748B;
  margin-bottom: 32px;
}
.layer-box {
  border: 2px solid #CBD5E1;
  border-radius: 12px;
  padding: 20px 24px;
  background: #F8FAFC;
  position: relative;
}
.layer-label {
  font-size: 15px;
  font-weight: 700;
  color: #0F172A;
  margin-bottom: 12px;
}
.layer-sub {
  font-size: 12px;
  color: #64748B;
  margin-bottom: 14px;
}
.chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 500;
  color: #1E293B;
  margin: 3px 4px;
}
.flow-box {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 18px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  border: 2px solid;
  text-align: center;
  line-height: 1.4;
}
.flow-blue { background: #DBEAFE; border-color: #93C5FD; color: #1E40AF; }
.flow-green { background: #DCFCE7; border-color: #86EFAC; color: #166534; }
.flow-red { background: #FEE2E2; border-color: #FCA5A5; color: #991B1B; }
.flow-gray { background: #F1F5F9; border-color: #CBD5E1; color: #334155; }
.flow-start { background: #FEF3C7; border-color: #FCD34D; color: #92400E; }
.flow-end { background: #E0E7FF; border-color: #A5B4FC; color: #3730A3; }
"""


def diagram1_system_architecture():
    w, h = 1200, 700
    css = get_base_css(w, h)
    lesson_badges = " ".join(
        [f'<span style="width:18px;height:18px;display:inline-flex;align-items:center;justify-content:center;background:#DCFCE7;border-radius:4px;font-size:9px;color:#166534;">{i}</span>' for i in range(1, 16)]
    )
    return """<!DOCTYPE html>
<html><head><style>""" + css + """</style></head>
<body>
<div class="diagram" style="width:""" + str(w) + """px;height:""" + str(h) + """px;">
  <div class="title">Fig. 1.1: System Architecture of Typer's Club</div>
  <div class="subtitle">Three-tier layered architecture with client-side rendering and local persistence</div>

  <!-- Top Layer: Client (Browser) -->
  <div class="layer-box" style="background:#EBF5FF; border-color:#93C5FD; min-height:165px;">
    <div class="layer-label">&#128187; Client (Browser)</div>
    <div class="layer-sub">Frontend layer running entirely in the user's browser</div>
    <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center;">
      <div class="chip" style="background:#DBEAFE; border:1px solid #93C5FD;">
        <span style="font-size:16px;">&#9883;</span> React UI Components
      </div>
      <div class="chip" style="background:#DBEAFE; border:1px solid #93C5FD;">
        <span style="font-size:16px;">&#9733;</span> Framer Motion Animations
      </div>
      <div class="chip" style="background:#DBEAFE; border:1px solid #93C5FD;">
        <span style="font-size:16px;">&#9998;</span> Tailwind CSS Styling
      </div>
      <div class="chip" style="background:#DBEAFE; border:1px solid #93C5FD;">
        <span style="font-size:16px;">&#9638;</span> shadcn/ui Components
      </div>
      <div class="chip" style="background:#DBEAFE; border:1px solid #93C5FD;">
        <span style="font-size:16px;">&#9881;</span> Zustand State Management
      </div>
    </div>
  </div>

  <!-- Arrow 1 -->
  <div style="text-align:center; padding:6px 0;">
    <svg width="1200" height="36"><line x1="600" y1="0" x2="600" y2="26" stroke="#94A3B8" stroke-width="2" stroke-dasharray="6,3"/><polygon points="600,30 594,20 606,20" fill="#94A3B8"/><text x="680" y="16" font-family="system-ui,sans-serif" font-size="11" fill="#94A3B8">HTTP Requests / Static Assets</text></svg>
  </div>

  <!-- Middle Layer: Next.js Server -->
  <div class="layer-box" style="background:#FFF7ED; border-color:#FDBA74; min-height:165px;">
    <div class="layer-label">&#9881; Next.js 16 Server</div>
    <div class="layer-sub">Server-side rendering engine and API layer</div>
    <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center;">
      <div class="chip" style="background:#FEF3C7; border:1px solid #FCD34D;">
        <span style="font-size:16px;">&#128204;</span> App Router
      </div>
      <div class="chip" style="background:#FEF3C7; border:1px solid #FCD34D;">
        <span style="font-size:16px;">&#128268;</span> API Routes
      </div>
      <div class="chip" style="background:#FEF3C7; border:1px solid #FCD34D;">
        <span style="font-size:16px;">&#128640;</span> SSR / CSR Hybrid
      </div>
      <div class="chip" style="background:#FEF3C7; border:1px solid #FCD34D;">
        <span style="font-size:16px;">&#128274;</span> Server-Side Validation
      </div>
      <div class="chip" style="background:#FEF3C7; border:1px solid #FCD34D;">
        <span style="font-size:16px;">&#128230;</span> Static Export
      </div>
    </div>
  </div>

  <!-- Arrow 2 -->
  <div style="text-align:center; padding:6px 0;">
    <svg width="1200" height="36"><line x1="600" y1="0" x2="600" y2="26" stroke="#94A3B8" stroke-width="2" stroke-dasharray="6,3"/><polygon points="600,30 594,20 606,20" fill="#94A3B8"/><text x="680" y="16" font-family="system-ui,sans-serif" font-size="11" fill="#94A3B8">Data Persistence</text></svg>
  </div>

  <!-- Bottom Layer: Client Storage -->
  <div class="layer-box" style="background:#F0FDF4; border-color:#86EFAC; min-height:115px;">
    <div class="layer-label">&#128451; Client Storage (Browser localStorage)</div>
    <div class="layer-sub">All user data persisted locally for offline access and privacy</div>
    <div style="display:flex; gap:16px; justify-content:center;">
      <div class="chip" style="background:#DCFCE7; border:1px solid #86EFAC; padding:12px 24px;">
        <span style="font-size:18px;">&#128274;</span>
        <div>
          <div style="font-weight:700;">localStorage (Auth)</div>
          <div style="font-size:11px; color:#166534; font-weight:400;">Credentials &amp; Session</div>
        </div>
      </div>
      <div class="chip" style="background:#DCFCE7; border:1px solid #86EFAC; padding:12px 24px;">
        <span style="font-size:18px;">&#128200;</span>
        <div>
          <div style="font-weight:700;">localStorage (Progress)</div>
          <div style="font-size:11px; color:#166534; font-weight:400;">WPM, Accuracy &amp; History</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Side annotations -->
  <div style="position:absolute; right:50px; top:230px;">
    <div style="font-size:11px; color:#94A3B8; writing-mode:vertical-lr; text-orientation:mixed; letter-spacing:1px;">NO DATABASE SERVER</div>
  </div>
  <div style="position:absolute; left:50px; top:230px;">
    <div style="font-size:11px; color:#94A3B8; writing-mode:vertical-lr; text-orientation:mixed; letter-spacing:1px;">CLIENT-SIDE APP</div>
  </div>

</div>
</body></html>"""


def diagram2_authentication_flow():
    w, h = 1200, 900
    css = get_base_css(w, h)
    return """<!DOCTYPE html>
<html><head><style>""" + css + """</style></head>
<body>
<div class="diagram" style="width:""" + str(w) + """px;height:""" + str(h) + """px;">
  <div class="title">Fig. 1.2: Authentication System Flow</div>
  <div class="subtitle">Token-based authentication with multi-step account recovery</div>

  <!-- SVG for arrows -->
  <svg width="1200" height="780" style="position:absolute;top:75px;left:0;overflow:visible;">
    <!-- Create Account flow arrows -->
    <line x1="240" y1="25" x2="240" y2="60" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="240,64 234,54 246,54" fill="#93C5FD"/>
    <line x1="240" y1="108" x2="240" y2="140" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="240,144 234,134 246,134" fill="#93C5FD"/>
    <line x1="240" y1="192" x2="240" y2="224" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="240,228 234,218 246,218" fill="#93C5FD"/>
    <line x1="240" y1="276" x2="240" y2="308" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="240,312 234,302 246,302" fill="#93C5FD"/>
    <line x1="240" y1="360" x2="240" y2="392" stroke="#86EFAC" stroke-width="2"/>
    <polygon points="240,396 234,386 246,386" fill="#86EFAC"/>

    <!-- Login flow arrows -->
    <line x1="600" y1="25" x2="600" y2="60" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="600,64 594,54 606,54" fill="#93C5FD"/>
    <line x1="600" y1="108" x2="600" y2="140" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="600,144 594,134 606,134" fill="#93C5FD"/>
    <line x1="545" y1="170" x2="440" y2="170" stroke="#FCA5A5" stroke-width="2"/>
    <polygon points="436,170 446,164 446,176" fill="#FCA5A5"/>
    <text x="490" y="163" font-family="system-ui,sans-serif" font-size="11" fill="#DC2626">Invalid</text>
    <line x1="655" y1="170" x2="760" y2="170" stroke="#86EFAC" stroke-width="2"/>
    <polygon points="764,170 754,164 754,176" fill="#86EFAC"/>
    <text x="705" y="163" font-family="system-ui,sans-serif" font-size="11" fill="#16A34A">Valid</text>

    <!-- Forgot Token flow -->
    <line x1="960" y1="25" x2="960" y2="60" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="960,64 954,54 966,54" fill="#93C5FD"/>
    <line x1="960" y1="108" x2="960" y2="140" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="960,144 954,134 966,134" fill="#93C5FD"/>
    <line x1="960" y1="192" x2="960" y2="224" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="960,228 954,218 966,218" fill="#93C5FD"/>
    <line x1="960" y1="276" x2="960" y2="308" stroke="#86EFAC" stroke-width="2"/>
    <polygon points="960,312 954,302 966,302" fill="#86EFAC"/>

    <!-- Forgot Both flow -->
    <line x1="960" y1="360" x2="960" y2="392" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="960,396 954,386 966,386" fill="#93C5FD"/>
    <line x1="960" y1="444" x2="960" y2="476" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="960,480 954,470 966,470" fill="#93C5FD"/>
    <line x1="960" y1="528" x2="960" y2="560" stroke="#93C5FD" stroke-width="2"/>
    <polygon points="960,564 954,554 966,554" fill="#93C5FD"/>
    <line x1="960" y1="612" x2="960" y2="644" stroke="#86EFAC" stroke-width="2"/>
    <polygon points="960,648 954,638 966,638" fill="#86EFAC"/>
  </svg>

  <!-- Column labels -->
  <div style="display:flex; gap:20px; justify-content:center; margin-bottom:14px;">
    <div style="width:280px; text-align:center;">
      <div style="font-size:14px; font-weight:700; color:#1E40AF; padding:6px 0; border-bottom:2px solid #93C5FD;">Create Account Flow</div>
    </div>
    <div style="width:280px; text-align:center;">
      <div style="font-size:14px; font-weight:700; color:#1E40AF; padding:6px 0; border-bottom:2px solid #93C5FD;">Login Flow</div>
    </div>
    <div style="width:360px; text-align:center;">
      <div style="font-size:14px; font-weight:700; color:#1E40AF; padding:6px 0; border-bottom:2px solid #93C5FD;">Recovery Flows</div>
    </div>
  </div>

  <!-- Content columns -->
  <div style="display:flex; gap:20px; justify-content:center;">
    <!-- Create Account Column -->
    <div style="width:280px; display:flex; flex-direction:column; gap:18px; align-items:center;">
      <div class="flow-box flow-start" style="width:200px;">Create Account</div>
      <div class="flow-box flow-blue" style="width:200px;">Enter Display Name</div>
      <div class="flow-box flow-blue" style="width:200px;">Generate Unique Token</div>
      <div class="flow-box flow-blue" style="width:200px;">Set Password</div>
      <div class="flow-box flow-blue" style="width:200px;">Set Security Question<br/><span style="font-size:10px; font-weight:400;">+ Answer</span></div>
      <div class="flow-box flow-green" style="width:200px;">&#10003; Account Created<br/><span style="font-size:10px; font-weight:400;">Redirect to Dashboard</span></div>
    </div>

    <!-- Login Column -->
    <div style="width:280px; display:flex; flex-direction:column; gap:18px; align-items:center;">
      <div class="flow-box flow-start" style="width:200px;">Login</div>
      <div class="flow-box flow-blue" style="width:200px;">Enter Token + Password</div>
      <div class="flow-box flow-blue" style="width:200px;">Verify Credentials</div>
      <div style="display:flex; gap:30px;">
        <div class="flow-box flow-red" style="width:90px; font-size:11px;">&#10007; Error<br/>Try Again</div>
        <div class="flow-box flow-green" style="width:90px; font-size:11px;">&#10003; Success<br/>Dashboard</div>
      </div>
    </div>

    <!-- Recovery Column -->
    <div style="width:360px; display:flex; flex-direction:column; gap:10px; align-items:center;">
      <div style="text-align:center; font-size:12px; font-weight:600; color:#475569; margin-bottom:4px;">Forgot Token?</div>
      <div class="flow-box flow-start" style="width:200px; font-size:12px;">Enter Username + Password</div>
      <div class="flow-box flow-blue" style="width:200px; font-size:12px;">Verify Password</div>
      <div class="flow-box flow-green" style="width:200px; font-size:12px;">&#10003; Show Token</div>

      <div style="text-align:center; font-size:12px; font-weight:600; color:#475569; margin-top:16px; margin-bottom:4px;">Forgot Both?</div>
      <div class="flow-box flow-start" style="width:200px; font-size:12px;">Enter Username</div>
      <div class="flow-box flow-blue" style="width:200px; font-size:12px;">Show Security Question</div>
      <div class="flow-box flow-blue" style="width:200px; font-size:12px;">Verify Answer</div>
      <div class="flow-box flow-green" style="width:200px; font-size:12px;">&#10003; Reset Password<br/><span style="font-size:10px; font-weight:400;">+ Show Token</span></div>
    </div>
  </div>

  <!-- Legend -->
  <div style="position:absolute; bottom:20px; left:40px; display:flex; gap:20px; align-items:center;">
    <div style="display:flex; align-items:center; gap:5px;">
      <div style="width:16px; height:16px; background:#FEF3C7; border:1.5px solid #FCD34D; border-radius:4px;"></div>
      <span style="font-size:10px; color:#64748B;">Start/Action</span>
    </div>
    <div style="display:flex; align-items:center; gap:5px;">
      <div style="width:16px; height:16px; background:#DBEAFE; border:1.5px solid #93C5FD; border-radius:4px;"></div>
      <span style="font-size:10px; color:#64748B;">Process</span>
    </div>
    <div style="display:flex; align-items:center; gap:5px;">
      <div style="width:16px; height:16px; background:#DCFCE7; border:1.5px solid #86EFAC; border-radius:4px;"></div>
      <span style="font-size:10px; color:#64748B;">Success</span>
    </div>
    <div style="display:flex; align-items:center; gap:5px;">
      <div style="width:16px; height:16px; background:#FEE2E2; border:1.5px solid #FCA5A5; border-radius:4px;"></div>
      <span style="font-size:10px; color:#64748B;">Error</span>
    </div>
  </div>
</div>
</body></html>"""


def diagram3_data_flow():
    w, h = 1200, 700
    css = get_base_css(w, h)
    return """<!DOCTYPE html>
<html><head><style>""" + css + """</style></head>
<body>
<div class="diagram" style="width:""" + str(w) + """px;height:""" + str(h) + """px;">
  <div class="title">Fig. 3.1: Data Flow Diagram</div>
  <div class="subtitle">Data movement through the Typing Tutor system</div>

  <!-- SVG for arrows -->
  <svg width="1200" height="560" style="position:absolute;top:80px;left:0;">
    <!-- Row 1 arrows -->
    <line x1="165" y1="40" x2="240" y2="40" stroke="#64748B" stroke-width="2"/>
    <polygon points="244,40 234,34 234,46" fill="#64748B"/>
    <text x="200" y="33" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">Keystrokes</text>

    <line x1="440" y1="40" x2="530" y2="40" stroke="#64748B" stroke-width="2"/>
    <polygon points="534,40 524,34 524,46" fill="#64748B"/>
    <text x="485" y="33" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">Raw data</text>

    <line x1="730" y1="40" x2="820" y2="40" stroke="#64748B" stroke-width="2"/>
    <polygon points="824,40 814,34 814,46" fill="#64748B"/>
    <text x="775" y="33" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">WPM / Accuracy</text>

    <line x1="1020" y1="40" x2="1090" y2="40" stroke="#64748B" stroke-width="2"/>
    <polygon points="1094,40 1084,34 1084,46" fill="#64748B"/>
    <text x="1055" y="33" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">Store</text>

    <!-- Row 2 arrows -->
    <line x1="165" y1="160" x2="240" y2="160" stroke="#64748B" stroke-width="2"/>
    <polygon points="244,160 234,154 234,166" fill="#64748B"/>
    <text x="200" y="153" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">Selection</text>

    <line x1="440" y1="160" x2="530" y2="160" stroke="#64748B" stroke-width="2"/>
    <polygon points="534,160 524,154 524,166" fill="#64748B"/>
    <text x="485" y="153" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">Lesson config</text>

    <!-- Row 3 arrows -->
    <line x1="165" y1="290" x2="240" y2="290" stroke="#64748B" stroke-width="2"/>
    <polygon points="244,290 234,284 234,296" fill="#64748B"/>
    <text x="200" y="283" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">Results</text>

    <line x1="440" y1="290" x2="530" y2="290" stroke="#64748B" stroke-width="2"/>
    <polygon points="534,290 524,284 524,296" fill="#64748B"/>
    <text x="485" y="283" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">Records</text>

    <line x1="730" y1="290" x2="820" y2="290" stroke="#64748B" stroke-width="2"/>
    <polygon points="824,290 814,284 814,296" fill="#64748B"/>
    <text x="775" y="283" font-family="system-ui,sans-serif" font-size="10" fill="#64748B">History</text>

    <!-- Cross arrows -->
    <line x1="940" y1="65" x2="940" y2="135" stroke="#93C5FD" stroke-width="2" stroke-dasharray="5,3"/>
    <polygon points="940,139 934,129 946,129" fill="#93C5FD"/>
    <text x="955" y="108" font-family="system-ui,sans-serif" font-size="10" fill="#93C5FD">Fetch lessons</text>

    <line x1="940" y1="185" x2="940" y2="260" stroke="#93C5FD" stroke-width="2" stroke-dasharray="5,3"/>
    <polygon points="940,264 934,254 946,254" fill="#93C5FD"/>
    <text x="955" y="228" font-family="system-ui,sans-serif" font-size="10" fill="#93C5FD">Save session</text>

    <!-- localStorage feedback -->
    <line x1="1120" y1="65" x2="1120" y2="265" stroke="#86EFAC" stroke-width="2" stroke-dasharray="5,3"/>
    <polygon points="1120,269 1114,259 1126,259" fill="#86EFAC"/>
    <text x="1136" y="170" font-family="system-ui,sans-serif" font-size="10" fill="#86EFAC" transform="rotate(90,1136,170)">Load history</text>
  </svg>

  <!-- Row 1: Main Typing Flow -->
  <div style="display:flex; gap:12px; justify-content:center; margin-bottom:80px;">
    <div style="width:120px; text-align:center;">
      <div class="flow-box flow-start" style="width:120px; height:50px; font-size:12px;">User Input<br/><span style="font-size:10px; font-weight:400;">(Keystrokes)</span></div>
    </div>
    <div style="width:200px; text-align:center;">
      <div class="flow-box flow-blue" style="width:200px; height:50px; font-size:12px;">Typing Engine<br/><span style="font-size:10px; font-weight:400;">(Real-time Processing)</span></div>
    </div>
    <div style="width:200px; text-align:center;">
      <div class="flow-box flow-blue" style="width:200px; height:50px; font-size:12px;">WPM / Accuracy<br/>Calculator</div>
    </div>
    <div style="width:200px; text-align:center;">
      <div class="flow-box flow-blue" style="width:200px; height:50px; font-size:12px;">Progress Manager<br/><span style="font-size:10px; font-weight:400;">(Session Tracking)</span></div>
    </div>
    <div style="width:100px; text-align:center;">
      <div class="flow-box flow-green" style="width:100px; height:50px; font-size:12px;">localStorage</div>
    </div>
  </div>

  <!-- Row 2: Lesson Selection Flow -->
  <div style="display:flex; gap:12px; justify-content:center; margin-bottom:80px;">
    <div style="width:120px; text-align:center;">
      <div class="flow-box flow-start" style="width:120px; height:50px; font-size:12px;">Lesson Selector<br/><span style="font-size:10px; font-weight:400;">(Phase/Level)</span></div>
    </div>
    <div style="width:200px; text-align:center;">
      <div class="flow-box flow-blue" style="width:200px; height:50px; font-size:12px;">Lesson Data<br/><span style="font-size:10px; font-weight:400;">(Content &amp; Config)</span></div>
    </div>
    <div style="width:200px; text-align:center;">
      <div class="flow-box flow-blue" style="width:200px; height:50px; font-size:12px;">Typing Interface<br/><span style="font-size:10px; font-weight:400;">(Display + Input)</span></div>
    </div>
  </div>

  <!-- Row 3: Performance Tracking -->
  <div style="display:flex; gap:12px; justify-content:center;">
    <div style="width:120px; text-align:center;">
      <div class="flow-box flow-start" style="width:120px; height:50px; font-size:12px;">Performance<br/>Data</div>
    </div>
    <div style="width:200px; text-align:center;">
      <div class="flow-box flow-blue" style="width:200px; height:50px; font-size:12px;">Session History<br/><span style="font-size:10px; font-weight:400;">(Timestamped Records)</span></div>
    </div>
    <div style="width:200px; text-align:center;">
      <div class="flow-box flow-green" style="width:200px; height:50px; font-size:12px;">Performance Graph<br/><span style="font-size:10px; font-weight:400;">(Visual Analytics)</span></div>
    </div>
    <div style="width:100px; text-align:center;">
      <div class="flow-box flow-green" style="width:100px; height:50px; font-size:12px;">localStorage</div>
    </div>
  </div>

  <!-- Legend -->
  <div style="position:absolute; bottom:20px; left:40px; display:flex; gap:16px; align-items:center;">
    <span style="font-size:11px; color:#64748B; font-weight:600;">LEGEND:</span>
    <div style="display:flex; align-items:center; gap:4px;">
      <div style="width:24px; height:3px; background:#64748B;"></div>
      <span style="font-size:10px; color:#64748B;">Data Flow</span>
    </div>
    <div style="display:flex; align-items:center; gap:4px;">
      <div style="width:24px; height:3px; background:#93C5FD; border-top:2px dashed #93C5FD;"></div>
      <span style="font-size:10px; color:#64748B;">Cross Reference</span>
    </div>
    <div style="display:flex; align-items:center; gap:4px;">
      <div style="width:24px; height:3px; background:#86EFAC; border-top:2px dashed #86EFAC;"></div>
      <span style="font-size:10px; color:#64748B;">Feedback Loop</span>
    </div>
  </div>
</div>
</body></html>"""


def diagram4_phase_progression():
    w, h = 1200, 600
    css = get_base_css(w, h)
    lesson15 = " ".join(
        [f'<span style="width:18px;height:18px;display:inline-flex;align-items:center;justify-content:center;background:#DCFCE7;border-radius:4px;font-size:9px;color:#166534;">{i}</span>' for i in range(1, 16)]
    )
    lesson6 = " ".join(
        [f'<span style="width:18px;height:18px;display:inline-flex;align-items:center;justify-content:center;background:#F1F5F9;border-radius:4px;font-size:9px;color:#475569;">{i}</span>' for i in range(1, 7)]
    )
    return """<!DOCTYPE html>
<html><head><style>""" + css + """</style></head>
<body>
<div class="diagram" style="width:""" + str(w) + """px;height:""" + str(h) + """px;">
  <div class="title">Fig. 3.2: Phase Progression Model</div>
  <div class="subtitle">Structured learning path with progressive difficulty and unlock requirements</div>

  <div style="display:flex; align-items:flex-end; gap:20px; justify-content:center; padding:10px 30px;">

    <!-- Phase 1 -->
    <div style="flex:1; max-width:250px;">
      <div style="border:2px solid #89AACC; border-radius:14px; padding:18px; background:#EBF5FF; height:350px; display:flex; flex-direction:column;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
          <span style="font-size:13px; font-weight:700; color:#89AACC;">PHASE 1</span>
          <span style="font-size:18px;">&#128275;</span>
        </div>
        <div style="font-size:17px; font-weight:800; color:#1E293B; margin-bottom:3px;">The Foundation</div>
        <div style="font-size:12px; color:#475569; margin-bottom:14px;">Home Row, Basic Keys</div>
        <div style="background:#FFFFFF; border-radius:10px; padding:12px; margin-bottom:10px; border:1px solid #E2E8F0;">
          <div style="font-size:10px; font-weight:600; color:#64748B; margin-bottom:5px;">REQUIREMENTS</div>
          <div style="display:flex; gap:12px;">
            <div><div style="font-size:22px; font-weight:800; color:#89AACC;">20+</div><div style="font-size:10px; color:#64748B;">WPM</div></div>
            <div><div style="font-size:22px; font-weight:800; color:#89AACC;">90%+</div><div style="font-size:10px; color:#64748B;">Accuracy</div></div>
          </div>
        </div>
        <div style="background:#FFFFFF; border-radius:10px; padding:12px; margin-bottom:10px; border:1px solid #E2E8F0;">
          <div style="font-size:10px; font-weight:600; color:#64748B; margin-bottom:5px;">15 LESSONS</div>
          <div style="display:flex; flex-wrap:wrap; gap:3px;">""" + lesson15 + """</div>
        </div>
        <div style="margin-top:auto; text-align:center; font-size:12px; font-weight:600; color:#16A34A; background:#DCFCE7; padding:8px; border-radius:8px;">
          &#10003; Always Unlocked
        </div>
      </div>
    </div>

    <!-- Arrow -->
    <div style="display:flex; align-items:center; padding-bottom:40px;">
      <svg width="36" height="24"><line x1="0" y1="10" x2="24" y2="10" stroke="#94A3B8" stroke-width="2"/><polygon points="26,10 18,5 18,15" fill="#94A3B8"/></svg>
    </div>

    <!-- Phase 2 -->
    <div style="flex:1; max-width:250px;">
      <div style="border:2px solid #6B9BD2; border-radius:14px; padding:18px; background:#EFF6FF; height:350px; display:flex; flex-direction:column;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
          <span style="font-size:13px; font-weight:700; color:#6B9BD2;">PHASE 2</span>
          <span style="font-size:18px;">&#128274;</span>
        </div>
        <div style="font-size:17px; font-weight:800; color:#1E293B; margin-bottom:3px;">Intermediate</div>
        <div style="font-size:12px; color:#475569; margin-bottom:14px;">Words, Shift Keys</div>
        <div style="background:#FFFFFF; border-radius:10px; padding:12px; margin-bottom:10px; border:1px solid #E2E8F0;">
          <div style="font-size:10px; font-weight:600; color:#64748B; margin-bottom:5px;">REQUIREMENTS</div>
          <div style="display:flex; gap:12px;">
            <div><div style="font-size:22px; font-weight:800; color:#6B9BD2;">40+</div><div style="font-size:10px; color:#64748B;">WPM</div></div>
            <div><div style="font-size:22px; font-weight:800; color:#6B9BD2;">95%+</div><div style="font-size:10px; color:#64748B;">Accuracy</div></div>
          </div>
        </div>
        <div style="background:#FFFFFF; border-radius:10px; padding:12px; margin-bottom:10px; border:1px solid #E2E8F0;">
          <div style="font-size:10px; font-weight:600; color:#64748B; margin-bottom:5px;">6 LESSONS</div>
          <div style="display:flex; flex-wrap:wrap; gap:3px;">""" + lesson6 + """</div>
        </div>
        <div style="margin-top:auto; text-align:center; font-size:11px; font-weight:600; color:#6B9BD2; background:#DBEAFE; padding:8px; border-radius:8px;">
          &#128274; Unlocked after Phase 1
        </div>
      </div>
    </div>

    <!-- Arrow -->
    <div style="display:flex; align-items:center; padding-bottom:40px;">
      <svg width="36" height="24"><line x1="0" y1="10" x2="24" y2="10" stroke="#94A3B8" stroke-width="2"/><polygon points="26,10 18,5 18,15" fill="#94A3B8"/></svg>
    </div>

    <!-- Phase 3 -->
    <div style="flex:1; max-width:250px;">
      <div style="border:2px solid #4E85BF; border-radius:14px; padding:18px; background:#F0F7FF; height:350px; display:flex; flex-direction:column;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
          <span style="font-size:13px; font-weight:700; color:#4E85BF;">PHASE 3</span>
          <span style="font-size:18px;">&#128274;</span>
        </div>
        <div style="font-size:17px; font-weight:800; color:#1E293B; margin-bottom:3px;">Advanced Prep</div>
        <div style="font-size:12px; color:#475569; margin-bottom:14px;">Complex Formatting</div>
        <div style="background:#FFFFFF; border-radius:10px; padding:12px; margin-bottom:10px; border:1px solid #E2E8F0;">
          <div style="font-size:10px; font-weight:600; color:#64748B; margin-bottom:5px;">REQUIREMENTS</div>
          <div style="display:flex; gap:12px;">
            <div><div style="font-size:22px; font-weight:800; color:#4E85BF;">60+</div><div style="font-size:10px; color:#64748B;">WPM</div></div>
            <div><div style="font-size:22px; font-weight:800; color:#4E85BF;">98%+</div><div style="font-size:10px; color:#64748B;">Accuracy</div></div>
          </div>
        </div>
        <div style="background:#FFFFFF; border-radius:10px; padding:12px; margin-bottom:10px; border:1px solid #E2E8F0;">
          <div style="font-size:10px; font-weight:600; color:#64748B; margin-bottom:5px;">6 LESSONS</div>
          <div style="display:flex; flex-wrap:wrap; gap:3px;">""" + lesson6 + """</div>
        </div>
        <div style="margin-top:auto; text-align:center; font-size:11px; font-weight:600; color:#4E85BF; background:#DBEAFE; padding:8px; border-radius:8px;">
          &#128274; Unlocked after Phase 2
        </div>
      </div>
    </div>

    <!-- Arrow -->
    <div style="display:flex; align-items:center; padding-bottom:40px;">
      <svg width="36" height="24"><line x1="0" y1="10" x2="24" y2="10" stroke="#94A3B8" stroke-width="2"/><polygon points="26,10 18,5 18,15" fill="#94A3B8"/></svg>
    </div>

    <!-- Phase 4 -->
    <div style="flex:1; max-width:250px;">
      <div style="border:2px solid #3A6FA0; border-radius:14px; padding:18px; background:#E8F0FE; height:350px; display:flex; flex-direction:column;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
          <span style="font-size:13px; font-weight:700; color:#3A6FA0;">PHASE 4</span>
          <span style="font-size:18px;">&#127775;</span>
        </div>
        <div style="font-size:17px; font-weight:800; color:#1E293B; margin-bottom:3px;">The Practitioner</div>
        <div style="font-size:12px; color:#475569; margin-bottom:14px;">Endless Mastery</div>
        <div style="background:#FFFFFF; border-radius:10px; padding:12px; margin-bottom:10px; border:1px solid #E2E8F0;">
          <div style="font-size:10px; font-weight:600; color:#64748B; margin-bottom:5px;">REQUIREMENTS</div>
          <div style="font-size:13px; color:#475569; text-align:center; padding:6px 0;">
            No minimum requirements<br/>
            <span style="font-size:10px;">Practice at your own pace</span>
          </div>
        </div>
        <div style="background:#FFFFFF; border-radius:10px; padding:12px; margin-bottom:10px; border:1px solid #E2E8F0;">
          <div style="font-size:10px; font-weight:600; color:#64748B; margin-bottom:5px;">6 LESSONS</div>
          <div style="display:flex; flex-wrap:wrap; gap:3px;">""" + lesson6 + """</div>
        </div>
        <div style="margin-top:auto; text-align:center; font-size:11px; font-weight:600; color:#3A6FA0; background:#DBEAFE; padding:8px; border-radius:8px;">
          &#128274; Unlocked after Phase 3
        </div>
      </div>
    </div>

  </div>

  <!-- Difficulty bar -->
  <div style="margin:16px 60px 0; display:flex; align-items:center; gap:12px;">
    <span style="font-size:11px; color:#64748B; font-weight:500;">BEGINNER</span>
    <div style="flex:1; height:6px; border-radius:3px; background:linear-gradient(to right, #89AACC, #6B9BD2, #4E85BF, #3A6FA0);"></div>
    <span style="font-size:11px; color:#64748B; font-weight:500;">MASTERY</span>
  </div>
</div>
</body></html>"""


def diagram5_component_hierarchy():
    w, h = 1200, 800
    css = get_base_css(w, h)
    return """<!DOCTYPE html>
<html><head><style>""" + css + """</style></head>
<body>
<div class="diagram" style="width:""" + str(w) + """px;height:""" + str(h) + """px;">
  <div class="title">Fig. 4.1: Component Hierarchy</div>
  <div class="subtitle">React component tree with state management hooks</div>

  <!-- SVG for connecting lines -->
  <svg width="1200" height="720" style="position:absolute;top:80px;left:0;overflow:visible;">
    <!-- App to horizontal bar -->
    <line x1="600" y1="50" x2="600" y2="80" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="80" y1="80" x2="1120" y2="80" stroke="#CBD5E1" stroke-width="1.5"/>
    <!-- Drops to level 1 row 1 -->
    <line x1="100" y1="80" x2="100" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="220" y1="80" x2="220" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="340" y1="80" x2="340" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="460" y1="80" x2="460" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="580" y1="80" x2="580" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="700" y1="80" x2="700" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="820" y1="80" x2="820" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="940" y1="80" x2="940" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="1060" y1="80" x2="1060" y2="105" stroke="#CBD5E1" stroke-width="1.5"/>

    <!-- Level 1 Row 2 drops -->
    <line x1="250" y1="160" x2="250" y2="195" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="550" y1="160" x2="550" y2="195" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="850" y1="160" x2="850" y2="195" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="1050" y1="160" x2="1050" y2="195" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="250" y1="175" x2="1050" y2="175" stroke="#CBD5E1" stroke-width="1.5"/>

    <!-- ProfilePage -> sub-children -->
    <line x1="580" y1="285" x2="580" y2="320" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="460" y1="320" x2="780" y2="320" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="460" y1="320" x2="460" y2="340" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="570" y1="320" x2="570" y2="340" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="680" y1="320" x2="680" y2="340" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="780" y1="320" x2="780" y2="340" stroke="#CBD5E1" stroke-width="1.5"/>

    <!-- TypingInterface -> sub-children -->
    <line x1="340" y1="285" x2="340" y2="320" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="240" y1="320" x2="440" y2="320" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="240" y1="320" x2="240" y2="340" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="340" y1="320" x2="340" y2="340" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="440" y1="320" x2="440" y2="340" stroke="#CBD5E1" stroke-width="1.5"/>
  </svg>

  <!-- Root: App -->
  <div style="text-align:center; margin-bottom:10px;">
    <div style="display:inline-flex; padding:12px 32px; background:#1E293B; color:#FFFFFF; border-radius:10px; font-size:15px; font-weight:700;">
      App <span style="font-weight:400; font-size:12px; opacity:0.7; margin-left:8px;">(page.tsx)</span>
    </div>
  </div>

  <!-- State management badges -->
  <div style="display:flex; gap:8px; justify-content:center; margin-bottom:16px;">
    <span style="padding:4px 12px; background:#FEF3C7; border:1px solid #FCD34D; border-radius:6px; font-size:11px; font-weight:600; color:#92400E;">useState</span>
    <span style="padding:4px 12px; background:#FEF3C7; border:1px solid #FCD34D; border-radius:6px; font-size:11px; font-weight:600; color:#92400E;">useCallback</span>
    <span style="padding:4px 12px; background:#FEF3C7; border:1px solid #FCD34D; border-radius:6px; font-size:11px; font-weight:600; color:#92400E;">useEffect</span>
    <span style="padding:4px 12px; background:#F3E8FF; border:1px solid #C084FC; border-radius:6px; font-size:11px; font-weight:600; color:#6B21A8;">useRouter</span>
  </div>

  <!-- Level 1 Row 1 -->
  <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center; margin-bottom:12px; padding:0 20px;">
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:90px;">Navbar</div>
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:115px;">CalibrationScreen</div>
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:95px;">HeroSection</div>
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:115px;">CurriculumGrid</div>
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:115px;">TypingInterface</div>
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:100px;">ProfilePage</div>
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:100px;">SettingsPage</div>
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:95px;">GamesPage</div>
    <div style="padding:8px 12px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:8px; font-size:12px; font-weight:600; color:#1E40AF; text-align:center; width:95px;">LearnPage</div>
  </div>

  <!-- Level 1 Row 2 -->
  <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center; margin-bottom:20px; padding:0 20px;">
    <div style="padding:8px 12px; background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:8px; font-size:12px; font-weight:600; color:#166534; text-align:center; width:115px;">SpeedTestPage</div>
    <div style="padding:8px 12px; background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:8px; font-size:12px; font-weight:600; color:#166534; text-align:center; width:115px;">DownloadPage</div>
    <div style="padding:8px 12px; background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:8px; font-size:12px; font-weight:600; color:#166534; text-align:center; width:140px;">PerformanceGraph</div>
    <div style="padding:8px 12px; background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:8px; font-size:12px; font-weight:600; color:#166534; text-align:center; width:150px;">CustomPracticePage</div>
  </div>

  <!-- Sub-components label -->
  <div style="text-align:center; margin-bottom:6px;">
    <span style="font-size:11px; font-weight:600; color:#94A3B8; letter-spacing:1px;">COMPONENT SUB-TREES</span>
  </div>

  <!-- Sub-components row -->
  <div style="display:flex; gap:60px; justify-content:center; margin-bottom:24px;">
    <!-- TypingInterface subs -->
    <div style="text-align:center;">
      <div style="font-size:11px; font-weight:600; color:#64748B; margin-bottom:8px;">TypingInterface</div>
      <div style="display:flex; gap:8px; justify-content:center;">
        <div style="padding:7px 12px; background:#F3E8FF; border:1.5px solid #C084FC; border-radius:8px; font-size:11px; font-weight:600; color:#6B21A8; text-align:center;">KeystrokeTracker</div>
        <div style="padding:7px 12px; background:#F3E8FF; border:1.5px solid #C084FC; border-radius:8px; font-size:11px; font-weight:600; color:#6B21A8; text-align:center;">WPMCalculator</div>
        <div style="padding:7px 12px; background:#F3E8FF; border:1.5px solid #C084FC; border-radius:8px; font-size:11px; font-weight:600; color:#6B21A8; text-align:center;">AccuracyTracker</div>
      </div>
    </div>

    <!-- ProfilePage subs -->
    <div style="text-align:center;">
      <div style="font-size:11px; font-weight:600; color:#64748B; margin-bottom:8px;">ProfilePage</div>
      <div style="display:flex; gap:8px; justify-content:center;">
        <div style="padding:7px 12px; background:#FEF3C7; border:1.5px solid #FCD34D; border-radius:8px; font-size:11px; font-weight:600; color:#92400E; text-align:center;">AuthCard</div>
        <div style="padding:7px 12px; background:#FEF3C7; border:1.5px solid #FCD34D; border-radius:8px; font-size:11px; font-weight:600; color:#92400E; text-align:center;">InputField</div>
        <div style="padding:7px 12px; background:#FEF3C7; border:1.5px solid #FCD34D; border-radius:8px; font-size:11px; font-weight:600; color:#92400E; text-align:center;">PasswordField</div>
        <div style="padding:7px 12px; background:#FEF3C7; border:1.5px solid #FCD34D; border-radius:8px; font-size:11px; font-weight:600; color:#92400E; text-align:center;">Toast</div>
      </div>
    </div>
  </div>

  <!-- Legend -->
  <div style="display:flex; gap:20px; justify-content:center; flex-wrap:wrap;">
    <div style="display:flex; align-items:center; gap:6px;">
      <div style="width:16px; height:16px; background:#1E293B; border-radius:4px;"></div>
      <span style="font-size:11px; color:#64748B;">Root Component</span>
    </div>
    <div style="display:flex; align-items:center; gap:6px;">
      <div style="width:16px; height:16px; background:#EBF5FF; border:1.5px solid #93C5FD; border-radius:4px;"></div>
      <span style="font-size:11px; color:#64748B;">Page Components</span>
    </div>
    <div style="display:flex; align-items:center; gap:6px;">
      <div style="width:16px; height:16px; background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:4px;"></div>
      <span style="font-size:11px; color:#64748B;">Feature Components</span>
    </div>
    <div style="display:flex; align-items:center; gap:6px;">
      <div style="width:16px; height:16px; background:#FEF3C7; border:1.5px solid #FCD34D; border-radius:4px;"></div>
      <span style="font-size:11px; color:#64748B;">Profile Sub-components</span>
    </div>
    <div style="display:flex; align-items:center; gap:6px;">
      <div style="width:16px; height:16px; background:#F3E8FF; border:1.5px solid #C084FC; border-radius:4px;"></div>
      <span style="font-size:11px; color:#64748B;">Engine Sub-components</span>
    </div>
  </div>
</div>
</body></html>"""


def diagram6_data_model():
    w, h = 1200, 700
    css = get_base_css(w, h)
    return """<!DOCTYPE html>
<html><head><style>""" + css + """</style></head>
<body>
<div class="diagram" style="width:""" + str(w) + """px;height:""" + str(h) + """px;">
  <div class="title">Fig. 4.2: Data Model</div>
  <div class="subtitle">Client-side data structures stored in localStorage</div>

  <!-- SVG for relationship arrows -->
  <svg width="1200" height="600" style="position:absolute;top:80px;left:0;overflow:visible;">
    <!-- UserProgress -> PhaseProgress -->
    <line x1="280" y1="110" x2="280" y2="185" stroke="#64748B" stroke-width="2"/>
    <polygon points="280,189 274,179 286,179" fill="#64748B"/>
    <text x="295" y="155" font-family="system-ui,sans-serif" font-size="11" fill="#64748B">contains</text>
    <text x="295" y="168" font-family="system-ui,sans-serif" font-size="10" fill="#94A3B8">phases[]</text>

    <!-- PhaseProgress -> LessonProgress -->
    <line x1="280" y1="330" x2="280" y2="395" stroke="#64748B" stroke-width="2"/>
    <polygon points="280,399 274,389 286,389" fill="#64748B"/>
    <text x="295" y="370" font-family="system-ui,sans-serif" font-size="11" fill="#64748B">contains</text>
    <text x="295" y="383" font-family="system-ui,sans-serif" font-size="10" fill="#94A3B8">lessons[]</text>

    <!-- UserProgress -> LessonRecord -->
    <line x1="380" y1="80" x2="620" y2="80" stroke="#94A3B8" stroke-width="2" stroke-dasharray="5,3"/>
    <polygon points="624,80 614,74 614,86" fill="#94A3B8"/>
    <text x="500" y="73" font-family="system-ui,sans-serif" font-size="11" fill="#94A3B8">sessionHistory[]</text>

    <!-- UserProgress -> AccountData -->
    <line x1="380" y1="110" x2="620" y2="260" stroke="#94A3B8" stroke-width="2" stroke-dasharray="5,3"/>
    <polygon points="620,260 626,250 614,252" fill="#94A3B8"/>
    <text x="520" y="195" font-family="system-ui,sans-serif" font-size="11" fill="#94A3B8">references</text>

    <!-- AccountData -> LessonRecord -->
    <line x1="830" y1="170" x2="830" y2="220" stroke="#64748B" stroke-width="2"/>
    <polygon points="830,224 824,214 836,214" fill="#64748B"/>
    <text x="845" y="200" font-family="system-ui,sans-serif" font-size="11" fill="#64748B">generates</text>
  </svg>

  <div style="display:flex; gap:30px; justify-content:center; padding:0 30px;">
    <!-- Left Column -->
    <div style="display:flex; flex-direction:column; gap:24px; width:380px;">
      <!-- UserProgress -->
      <div style="border:2px solid #3B82F6; border-radius:12px; padding:14px 18px; background:#EFF6FF;">
        <div style="font-size:14px; font-weight:800; color:#1E40AF; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
          <span style="background:#3B82F6; color:white; width:22px; height:22px; display:inline-flex; align-items:center; justify-content:center; border-radius:6px; font-size:11px;">U</span>
          UserProgress
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:3px 14px;">
          <div style="font-size:12px;"><span style="color:#64748B;">totalKeystrokes</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">totalTimeSpent</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">averageWpm</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">currentLesson</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">phases[]</span> <span style="color:#3B82F6;">PhaseProgress</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">sessionHistory[]</span> <span style="color:#3B82F6;">LessonRecord</span></div>
        </div>
      </div>

      <!-- PhaseProgress -->
      <div style="border:2px solid #10B981; border-radius:12px; padding:14px 18px; background:#ECFDF5;">
        <div style="font-size:14px; font-weight:800; color:#065F46; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
          <span style="background:#10B981; color:white; width:22px; height:22px; display:inline-flex; align-items:center; justify-content:center; border-radius:6px; font-size:11px;">P</span>
          PhaseProgress
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:3px 14px;">
          <div style="font-size:12px;"><span style="color:#64748B;">phaseId</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">bestWpm</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">bestAccuracy</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">unlocked</span> <span style="color:#94A3B8;">boolean</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">completed</span> <span style="color:#94A3B8;">boolean</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">lessons[]</span> <span style="color:#10B981;">LessonProgress</span></div>
        </div>
      </div>

      <!-- LessonProgress -->
      <div style="border:2px solid #F59E0B; border-radius:12px; padding:14px 18px; background:#FFFBEB;">
        <div style="font-size:14px; font-weight:800; color:#92400E; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
          <span style="background:#F59E0B; color:white; width:22px; height:22px; display:inline-flex; align-items:center; justify-content:center; border-radius:6px; font-size:11px;">L</span>
          LessonProgress
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:3px 14px;">
          <div style="font-size:12px;"><span style="color:#64748B;">completedSubChapters[]</span> <span style="color:#94A3B8;">string[]</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">bestWpm</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">bestAccuracy</span> <span style="color:#94A3B8;">number</span></div>
        </div>
      </div>
    </div>

    <!-- Right Column -->
    <div style="display:flex; flex-direction:column; gap:24px; width:380px;">
      <!-- AccountData -->
      <div style="border:2px solid #8B5CF6; border-radius:12px; padding:14px 18px; background:#F5F3FF;">
        <div style="font-size:14px; font-weight:800; color:#5B21B6; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
          <span style="background:#8B5CF6; color:white; width:22px; height:22px; display:inline-flex; align-items:center; justify-content:center; border-radius:6px; font-size:11px;">A</span>
          AccountData
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:3px 14px;">
          <div style="font-size:12px;"><span style="color:#64748B;">displayName</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">password</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">token</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">securityQuestion</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">securityAnswer</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">joinDate</span> <span style="color:#94A3B8;">string</span></div>
        </div>
      </div>

      <!-- LessonRecord -->
      <div style="border:2px solid #EF4444; border-radius:12px; padding:14px 18px; background:#FEF2F2;">
        <div style="font-size:14px; font-weight:800; color:#991B1B; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
          <span style="background:#EF4444; color:white; width:22px; height:22px; display:inline-flex; align-items:center; justify-content:center; border-radius:6px; font-size:11px;">R</span>
          LessonRecord
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:3px 14px;">
          <div style="font-size:12px;"><span style="color:#64748B;">lessonId</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">phaseId</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">title</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">wpm</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">accuracy</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">timestamp</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">subChapterId</span> <span style="color:#94A3B8;">string</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">duration</span> <span style="color:#94A3B8;">number</span></div>
          <div style="font-size:12px;"><span style="color:#64748B;">mistakes</span> <span style="color:#94A3B8;">number</span></div>
        </div>
      </div>

      <!-- Storage info -->
      <div style="border:2px solid #CBD5E1; border-radius:12px; padding:14px 18px; background:#F8FAFC;">
        <div style="font-size:13px; font-weight:700; color:#334155; margin-bottom:8px;">&#128451; Storage Keys</div>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <div style="font-size:12px; color:#475569;"><code style="background:#E2E8F0; padding:2px 6px; border-radius:4px; font-size:11px;">tc-auth</code> &rarr; AccountData</div>
          <div style="font-size:12px; color:#475569;"><code style="background:#E2E8F0; padding:2px 6px; border-radius:4px; font-size:11px;">tc-progress</code> &rarr; UserProgress</div>
        </div>
      </div>
    </div>
  </div>
</div>
</body></html>"""


# ============================================================
# MAIN
# ============================================================
async def render_diagram(html_content, html_file, output_file, width, height):
    """Write HTML and render to PNG using Playwright."""
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={'width': width, 'height': height},
            device_scale_factor=2
        )
        await page.goto(f'file://{html_file}')
        await page.wait_for_load_state('networkidle')
        await page.screenshot(path=output_file, full_page=False)
        await browser.close()


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    diagrams = [
        {
            'name': 'System Architecture',
            'filename': 'system_architecture',
            'size': (1200, 700),
            'func': diagram1_system_architecture,
        },
        {
            'name': 'Authentication Flow',
            'filename': 'authentication_flow',
            'size': (1200, 900),
            'func': diagram2_authentication_flow,
        },
        {
            'name': 'Data Flow Diagram',
            'filename': 'data_flow_diagram',
            'size': (1200, 700),
            'func': diagram3_data_flow,
        },
        {
            'name': 'Phase Progression Model',
            'filename': 'phase_progression',
            'size': (1200, 600),
            'func': diagram4_phase_progression,
        },
        {
            'name': 'Component Hierarchy',
            'filename': 'component_hierarchy',
            'size': (1200, 800),
            'func': diagram5_component_hierarchy,
        },
        {
            'name': 'Data Model',
            'filename': 'typing_engine_data_model',
            'size': (1200, 700),
            'func': diagram6_data_model,
        },
    ]

    for i, diag in enumerate(diagrams, 1):
        w, h = diag['size']
        html_file = os.path.join(OUTPUT_DIR, f"{diag['filename']}.html")
        png_file = os.path.join(OUTPUT_DIR, f"{diag['filename']}.png")

        print(f"[{i}/{len(diagrams)}] Generating: {diag['name']} ({w}x{h})")
        html_content = diag['func']()
        await render_diagram(html_content, html_file, png_file, w, h)

        size_kb = os.path.getsize(png_file) / 1024
        print(f"  Done: {png_file} ({size_kb:.1f} KB)")

    print(f"\n{'='*50}")
    print(f"All {len(diagrams)} diagrams generated successfully!")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == '__main__':
    asyncio.run(main())
