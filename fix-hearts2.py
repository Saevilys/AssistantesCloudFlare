#!/usr/bin/env python3
"""Replace hearts with SVG in nour, suyin, and finish zineb."""
import re

# ---- CSS replacements ----
CSS_NOUR_SUYIN_FIND = """.flirt-hearts{font-size:0.85rem;line-height:1;letter-spacing:1px;font-family:'Times New Roman',Georgia,serif;font-variant-emoji:text;text-shadow:1px 1px 0 #1a1020,-1px -1px 0 #1a1020,1px -1px 0 #1a1020,-1px 1px 0 #1a1020,0 0 2px #1a1020}
.flirt-hearts .on{color:#e8c878}
.flirt-hearts .off{color:#807868}
.flirt-lvl4{font-size:1.15rem;line-height:1;font-family:'Times New Roman',Georgia,serif;font-variant-emoji:text;animation:glowPulse 1.8s ease-in-out infinite;text-shadow:0 0 6px #ff3366,0 0 12px #ff3366,0 0 18px #ff336680}
.flirt-lvl5{font-size:1.3rem;line-height:1;font-family:'Times New Roman',Georgia,serif;font-variant-emoji:text;animation:glowPulseRed 1.8s ease-in-out infinite;text-shadow:0 0 6px #ff0033,0 0 12px #ff0033,0 0 18px #ff003380}
.flirt-lvl6{font-size:1.5rem;line-height:1;animation:rainbowGlow 1.5s ease-in-out infinite}
.flirt-lvl6 .heart{font-family:'Times New Roman',Georgia,serif;background:linear-gradient(90deg,#ff0044,#ff8800,#ffdd00,#44ff44,#00ccff,#6644ff,#ff00cc,#ff0044);background-size:300% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:rainbowShift 2s linear infinite;filter:drop-shadow(0 0 3px #ff3366) drop-shadow(0 0 6px #6644ff)}
.flirt-lvl6 .s-mark{font-size:1rem;font-weight:900;font-style:italic;vertical-align:baseline;background:linear-gradient(90deg,#ffd700,#ff8800,#ffd700,#ff3366,#ffd700);background-size:200% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:rainbowShift 2.5s linear infinite reverse;filter:drop-shadow(0 0 4px #ffd700) drop-shadow(0 0 8px #ff8800)}"""

CSS_REPLACE_DARK = """.flirt svg{display:block}
.flirt-lvl4 svg{animation:glowPulse 1.8s ease-in-out infinite;filter:drop-shadow(0 0 4px #ff3366) drop-shadow(0 0 8px #ff3366)}
.flirt-lvl5 svg{animation:glowPulseRed 1.8s ease-in-out infinite;filter:drop-shadow(0 0 4px #ff0033) drop-shadow(0 0 8px #ff0033)}
.flirt-lvl6 svg{animation:rainbowGlow 1.5s ease-in-out infinite}
.flirt-lvl6 .s-mark{font-size:0.85rem;font-weight:900;font-style:italic;color:#ffd700;filter:drop-shadow(0 0 4px #ffd700) drop-shadow(0 0 8px #ff8800)}"""

# ---- JS functions (same for both, uses \n indentation) ----
JS_FUNCS_FIND = """function flirtBannerLabel(lvl){
  if(lvl>=6) return '♥\\uFE0E S — Rang S';
  if(lvl>=5) return '☠\\uFE0E♥\\uFE0E LVL 5 — Succubus';
  if(lvl>=4) return '♥\\uFE0E! LVL 4 — Passionné';
  if(lvl>=1) return '♥\\uFE0E'.repeat(lvl)+'♡\\uFE0E'.repeat(3-lvl)+' Flirt L'+lvl;
  return '';
}"""

JS_FUNCS_REPLACE = """function heartSVG(filled,size){
  size=size||16;
  var fill=filled?'#e8c878':'none';
  var stroke=filled?'#1a1020':'#807868';
  return '<svg viewBox="0 0 24 24" width="'+size+'" height="'+size+'" fill="'+fill+'" stroke="'+stroke+'" stroke-width="1.5" stroke-linejoin="round"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
}
function heartGlowSVG(size){
  size=size||18;
  return '<svg viewBox="0 0 24 24" width="'+size+'" height="'+size+'" fill="#ff3366" stroke="#1a1020" stroke-width="1.5" stroke-linejoin="round"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
}
function skullHeartSVG(size){
  size=size||18;
  return '<svg viewBox="0 0 28 24" width="'+size+'" height="'+Math.round(size*24/28)+'" fill="none" stroke="#ff0033" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"><path d="M10 12c0-3 2-5 4-5s4 2 4 5c0 1.5-.5 2.5-1 3v3h-6v-3c-.5-.5-1-1.5-1-3z"/><circle cx="11" cy="12" r="1.3" fill="#ff0033"/><circle cx="16" cy="12" r="1.3" fill="#ff0033"/><path d="M12 17v2M14 17v2"/></svg>';
}
function rainbowHeartSVG(size){
  size=size||20;
  var gid='rh'+Math.random().toString(36).slice(2);
  return '<svg viewBox="0 0 24 24" width="'+size+'" height="'+size+'" stroke-width="1.5" stroke-linejoin="round"><defs><linearGradient id="'+gid+'" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ff0044"/><stop offset="20%" stop-color="#ff8800"/><stop offset="40%" stop-color="#ffdd00"/><stop offset="60%" stop-color="#44ff44"/><stop offset="80%" stop-color="#00ccff"/><stop offset="100%" stop-color="#6644ff"/></linearGradient></defs><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="url(#'+gid+')"/></svg>';
}
function flirtBannerLabel(lvl){
  if(lvl>=6) return 'S — Rang S';
  if(lvl>=5) return 'LVL 5 — Succubus';
  if(lvl>=4) return 'LVL 4 — Passionné';
  if(lvl>=1) return 'Flirt L'+lvl;
  return '';
}"""

# ---- flirtDots (template literal, backtick) ----
FLIRT_DOTS_FIND = """const flirtDots=a.flirty>=6
      ? `<span class="flirt-lvl6"><span class="heart">♥\\uFE0E</span><span class="s-mark">S</span></span>`
      : a.flirty>=5
      ? `<span class="flirt-lvl5">☠\\uFE0E♥\\uFE0E</span>`
      : a.flirty>=4
      ? `<span class="flirt-lvl4">♥\\uFE0E!</span>`
      : `<span class="flirt-hearts">${[1,2,3].map(i=>`<span class="${i<=a.flirty?'on':'off'}">♥\\uFE0E</span>`).join('')}</span>`;"""

FLIRT_DOTS_REPLACE = """const flirtDots=a.flirty>=6
      ? `<span class="flirt-lvl6">${rainbowHeartSVG(20)}<span class="s-mark">S</span></span>`
      : a.flirty>=5
      ? `<span class="flirt-lvl5">${skullHeartSVG(18)}</span>`
      : a.flirty>=4
      ? `<span class="flirt-lvl4">${heartGlowSVG(18)}<span style="color:#ff3366;font-weight:700;font-size:0.8rem">!</span></span>`
      : `<span class="flirt-hearts">${[1,2,3].map(i=>heartSVG(i<=a.flirty,16)).join('')}</span>`;"""

# ---- Profile badge (template literal) ----
PROFILE_FIND = """${a.flirty>=6
        ? `<span class="profile-badge badge-flirt flirt-lvl6" style="font-size:0.9rem;padding:4px 12px"><span class="heart">♥\\uFE0E</span><span class="s-mark">S</span> — Rang S</span>`
        : a.flirty>=5
        ? `<span class="profile-badge badge-flirt flirt-lvl5" style="font-size:0.9rem;padding:4px 12px">☠\\uFE0E♥\\uFE0E LVL 5 — Succubus</span>`
        : a.flirty>=4
        ? `<span class="profile-badge badge-flirt flirt-lvl4" style="font-size:0.8rem;padding:4px 12px">♥\\uFE0E! LVL 4</span>`
        : `<span class="profile-badge badge-flirt flirt-hearts" style="font-size:0.85rem;padding:4px 12px">${'♥\\uFE0E'.repeat(a.flirty)}${'♡\\uFE0E'.repeat(3-a.flirty)} Flirt L${a.flirty}</span>`}"""

PROFILE_REPLACE = """${a.flirty>=6
        ? `<span class="profile-badge badge-flirt flirt-lvl6" style="font-size:0.9rem;padding:4px 12px;display:inline-flex;align-items:center;gap:4px">${rainbowHeartSVG(20)}<span class="s-mark">S</span> — Rang S</span>`
        : a.flirty>=5
        ? `<span class="profile-badge badge-flirt flirt-lvl5" style="font-size:0.9rem;padding:4px 12px;display:inline-flex;align-items:center;gap:4px">${skullHeartSVG(18)} LVL 5 — Succubus</span>`
        : a.flirty>=4
        ? `<span class="profile-badge badge-flirt flirt-lvl4" style="font-size:0.8rem;padding:4px 12px;display:inline-flex;align-items:center;gap:2px">${heartGlowSVG(18)}<span style="color:#ff3366;font-weight:700;font-size:0.8rem">!</span> LVL 4</span>`
        : `<span class="profile-badge badge-flirt flirt-hearts" style="font-size:0.85rem;padding:4px 12px;display:inline-flex;align-items:center;gap:3px">${[1,2,3].map(i=>heartSVG(i<=a.flirty,16)).join('')} Flirt L${a.flirty}</span>`}"""

# ---- Also handle zineb (already had CSS replaced, needs JS) ----
# Zineb flirtBannerLabel uses same format as nour/suyin
JS_FUNCS_FIND_ZINEB = """function flirtBannerLabel(lvl){
if(lvl>=6)return '♥\\uFE0E S — Rang S';
if(lvl>=5)return '☠\\uFE0E♥\\uFE0E LVL 5 — Succubus';
if(lvl>=4)return '♥\\uFE0E! LVL 4 — Passionné';
if(lvl>=1)return '♥\\uFE0E'.repeat(lvl)+'♡\\uFE0E'.repeat(3-lvl)+' Flirt L'+lvl;
return '';
}"""

JS_FUNCS_REPLACE_ZINEB = """function heartSVG(filled,size){
size=size||16;
var fill=filled?'#e8c878':'none';
var stroke=filled?'#0e1828':'#807868';
return '<svg viewBox="0 0 24 24" width="'+size+'" height="'+size+'" fill="'+fill+'" stroke="'+stroke+'" stroke-width="1.5" stroke-linejoin="round"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
}
function heartGlowSVG(size){
size=size||18;
return '<svg viewBox="0 0 24 24" width="'+size+'" height="'+size+'" fill="#ff3366" stroke="#0e1828" stroke-width="1.5" stroke-linejoin="round"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
}
function skullHeartSVG(size){
size=size||18;
return '<svg viewBox="0 0 28 24" width="'+size+'" height="'+Math.round(size*24/28)+'" fill="none" stroke="#ff0033" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"><path d="M10 12c0-3 2-5 4-5s4 2 4 5c0 1.5-.5 2.5-1 3v3h-6v-3c-.5-.5-1-1.5-1-3z"/><circle cx="11" cy="12" r="1.3" fill="#ff0033"/><circle cx="16" cy="12" r="1.3" fill="#ff0033"/><path d="M12 17v2M14 17v2"/></svg>';
}
function rainbowHeartSVG(size){
size=size||20;
var gid='rh'+Math.random().toString(36).slice(2);
return '<svg viewBox="0 0 24 24" width="'+size+'" height="'+size+'" stroke-width="1.5" stroke-linejoin="round"><defs><linearGradient id="'+gid+'" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ff0044"/><stop offset="20%" stop-color="#ff8800"/><stop offset="40%" stop-color="#ffdd00"/><stop offset="60%" stop-color="#44ff44"/><stop offset="80%" stop-color="#00ccff"/><stop offset="100%" stop-color="#6644ff"/></linearGradient></defs><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="url(#'+gid+')"/></svg>';
}
function flirtBannerLabel(lvl){
if(lvl>=6)return 'S — Rang S';
if(lvl>=5)return 'LVL 5 — Succubus';
if(lvl>=4)return 'LVL 4 — Passionné';
if(lvl>=1)return 'Flirt L'+lvl;
return '';
}"""

# Zineb flirtDots (template literal)
FLIRT_DOTS_FIND_ZINEB = """const flirtDots=a.flirty>=6
      ? `<span class="flirt-lvl6"><span class="heart">♥\\uFE0E</span><span class="s-mark">S</span></span>`
      : a.flirty>=5
      ? `<span class="flirt-lvl5">☠\\uFE0E♥\\uFE0E</span>`
      : a.flirty>=4
      ? `<span class="flirt-lvl4">♥\\uFE0E!</span>`
      : `<span class="flirt-hearts">${[1,2,3].map(i=>`<span class="${i<=a.flirty?'on':'off'}">♥\\uFE0E</span>`).join('')}</span>`;"""

# Zineb profile badge (template literal)
PROFILE_FIND_ZINEB = """${a.flirty>=6
        ? `<span class="profile-badge badge-flirt flirt-lvl6" style="font-size:0.9rem;padding:4px 12px"><span class="heart">♥\\uFE0E</span><span class="s-mark">S</span> — Rang S</span>`
        : a.flirty>=5
        ? `<span class="profile-badge badge-flirt flirt-lvl5" style="font-size:0.9rem;padding:4px 12px">☠\\uFE0E♥\\uFE0E LVL 5 — Succubus</span>`
        : a.flirty>=4
        ? `<span class="profile-badge badge-flirt flirt-lvl4" style="font-size:0.8rem;padding:4px 12px">♥\\uFE0E! LVL 4</span>`
        : `<span class="profile-badge badge-flirt flirt-hearts" style="font-size:0.85rem;padding:4px 12px">${'♥\\uFE0E'.repeat(a.flirty)}${'♡\\uFE0E'.repeat(3-a.flirty)} Flirt L${a.flirty}</span>`}"""

def process_file(fname, css_find, css_replace, js_find, js_replace, dots_find, dots_replace, prof_find, prof_replace):
    print(f"\n=== {fname} ===")
    with open(fname) as f:
        content = f.read()
    
    if css_find and css_find in content:
        content = content.replace(css_find, css_replace)
        print("  CSS: replaced")
    elif css_find:
        print("  CSS: NOT FOUND")
    
    if js_find and js_find in content:
        content = content.replace(js_find, js_replace)
        print("  JS funcs: replaced")
    elif js_find:
        print("  JS funcs: NOT FOUND")
    
    if dots_find and dots_find in content:
        content = content.replace(dots_find, dots_replace)
        print("  flirtDots: replaced")
    elif dots_find:
        print("  flirtDots: NOT FOUND")
    
    if prof_find and prof_find in content:
        content = content.replace(prof_find, prof_replace)
        print("  profile badge: replaced")
    elif prof_find:
        print("  profile badge: NOT FOUND")
    
    with open(fname, 'w') as f:
        f.write(content)

# nour and suyin: same patterns
for fname in ['station-nour.html', 'station-suyin.html']:
    process_file(fname, CSS_NOUR_SUYIN_FIND, CSS_REPLACE_DARK,
                 JS_FUNCS_FIND, JS_FUNCS_REPLACE,
                 FLIRT_DOTS_FIND, FLIRT_DOTS_REPLACE,
                 PROFILE_FIND, PROFILE_REPLACE)

# zineb: CSS already done, just JS
process_file('station-zineb.html', None, None,
             JS_FUNCS_FIND_ZINEB, JS_FUNCS_REPLACE_ZINEB,
             FLIRT_DOTS_FIND_ZINEB, FLIRT_DOTS_REPLACE,
             PROFILE_FIND_ZINEB, PROFILE_REPLACE)

print("\nDone!")
