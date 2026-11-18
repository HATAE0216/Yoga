"""db_list/db_get 결과(JSON)를 data/snap.json으로 변환.
사용: python3 src/make_snap.py seqs.json journal.json settings.json
 - seqs.json / journal.json: [{"id":..., "data":{...}}, ...] 형식의 배열 (db_list 결과의 각 문서)
 - settings.json: settings/main 문서의 data 객체, 없으면 {}"""
import json, sys, os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(p, d):
    try: return json.load(open(p, encoding='utf-8'))
    except Exception: return d
seqs = [{'id': d['id'], **d.get('data', {})} for d in load(sys.argv[1], [])]
jour = [{'id': d['id'], **d.get('data', {})} for d in load(sys.argv[2], [])]
sett = load(sys.argv[3], {}) if len(sys.argv) > 3 else {}
# data/pending.json: 아직 편집 페이지 DB에 저장되지 못한 시퀀스. DB에 같은 id가 생기면 DB 쪽을 사용.
have = {x['id'] for x in seqs}
seqs += [x for x in load(os.path.join(ROOT, 'data', 'pending.json'), []) if x.get('id') not in have]
kst = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)
snap = {'at': f"{kst.year}. {kst.month}. {kst.day}", 'motto': (sett or {}).get('motto', ''), 'journal': jour, 'seqs': seqs}
old = load(os.path.join(ROOT, 'data', 'snap.json'), {})
if old and all(old.get(k) == snap[k] for k in ('motto', 'journal', 'seqs')):
    snap['at'] = old.get('at', snap['at'])  # 내용이 같으면 날짜도 그대로 두어 불필요한 커밋을 막음
json.dump(snap, open(os.path.join(ROOT, 'data', 'snap.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('snap:', len(seqs), 'seqs,', len(jour), 'journal')
