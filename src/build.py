"""요가 노트 GitHub 사이트 빌드: data/snap.json(시퀀스·일지·요가훈 스냅숏) → index.html
사용: python3 src/build.py   (저장소 최상위에서)"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from poses import POSES, TERMS, QUOTES
from kr import KR
from roots import ROOTS
ids = {p['id'] for p in POSES}
for r in ROOTS:
    for e in r[6]: assert e in ids, (r[1], e)
for p in POSES: p['kr'] = KR[p['id']]
snap = json.load(open(os.path.join(ROOT, 'data', 'snap.json'), encoding='utf-8'))
t = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
t = t.replace("""  try{ db = window.claude && typeof window.claude.use==="function" ? await window.claude.use("db") : null; }catch(e){ db=null; }""",
"""  const t0=Date.now();
  while(!(window.claude && typeof window.claude.use==="function") && Date.now()-t0<8000) await new Promise(r=>setTimeout(r,100));
  try{ db = window.claude && typeof window.claude.use==="function" ? await window.claude.use("db") : null; }catch(e){ db=null; }""")
t = t.replace('<title>요가 노트 — 시퀀스 & 아사나 용어집</title>', '<title>요가 노트</title>')
t = t.replace('<!--ICON-->', '<link rel="apple-touch-icon" href="icon.png">\n<link rel="icon" type="image/png" href="icon.png">')
for k, v in (('__POSES__', POSES), ('__TERMS__', TERMS), ('__QUOTES__', QUOTES), ('__ROOTS__', ROOTS), ('__PUBLIC__', True), ('__SNAP__', snap)):
    t = t.replace(k, json.dumps(v, ensure_ascii=False))
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(t)
print('built index.html:', len(snap.get('seqs', [])), 'sequences,', len(snap.get('journal', [])), 'journal entries')
