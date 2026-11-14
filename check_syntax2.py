import re, subprocess, os
for page in ['station-suyin.html','station-zineb.html','station-nour.html','station-minorea.html']:
    with open(page) as f:
        html = f.read()
    scripts = re.findall(r'<script>(.*?)</script>', html, re.S)
    for i, s in enumerate(scripts):
        tmp = f'/tmp/check_{page}_{i}.js'
        with open(tmp,'w') as g:
            g.write(s)
        p = subprocess.run(['node','--check',tmp], capture_output=True)
        if p.returncode != 0:
            print(f'{page} script {i}: SYNTAX ERROR')
            print(p.stderr.decode()[:400])
        else:
            print(f'{page} script {i}: OK')
