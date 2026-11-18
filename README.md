# 요가 노트

개인 요가 시퀀스 · 아사나 용어집 · 어근 사전 · 수련 일지 (보기 전용 사이트)

- 사이트: https://hatae0216.github.io/Yoga/
- 편집: Claude 요가 노트 페이지 https://claude.ai/artifact/LA5gxJWufsE2MY231BtGBR (slug 9b2237d3-f957-4706-a52e-ec72cd036a10)

## 갱신 방법
1. 편집 페이지의 데이터베이스에서 `sequences`, `journal` 컬렉션과 `settings/main` 문서를 읽어 JSON으로 저장
2. `python3 src/make_snap.py seqs.json journal.json settings.json` → `data/snap.json`
3. `python3 src/build.py` → `index.html`
4. 바뀐 게 있으면 커밋·푸시 (GitHub Pages: main 브랜치 / root)
