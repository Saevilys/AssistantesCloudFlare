#!/usr/bin/env python3
"""Find profile badge flirt rendering in nour and suyin."""
import re

for fname in ['station-nour.html', 'station-suyin.html']:
    with open(fname) as f:
        content = f.read()
    
    print(f"\n=== {fname} ===")
    
    # Find all occurrences of "badge-flirt" in the JS part (after first <script>)
    script_start = content.find('<script>')
    if script_start < 0:
        script_start = content.find('<script')
    
    js = content[script_start:]
    offset = script_start
    
    for m in re.finditer(r'badge-flirt', js):
        pos = m.start() + offset
        start = max(0, pos - 100)
        end = min(len(content), pos + 500)
        print(f"\n--- badge-flirt at {pos} ---")
        print(repr(content[start:end]))
