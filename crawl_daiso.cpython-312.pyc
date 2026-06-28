name: 🛒 다이소 제품 크롤링 & 배포

on:
  # ① 매일 오전 6시(KST) = UTC 21:00 자동 실행
  schedule:
    - cron: "0 21 * * *"

  # ② GitHub Actions 탭에서 수동으로 실행 가능
  workflow_dispatch:

  # ③ main 브랜치에 push할 때마다 Pages 재배포
  push:
    branches: [main]

permissions:
  contents: write        # products.json 커밋을 위해 필요
  pages: write           # GitHub Pages 배포를 위해 필요
  id-token: write        # Pages OIDC 인증

jobs:
  # ────────────────────────────────────────────────────────────────────────────
  crawl:
    name: 크롤링 & products.json 업데이트
    runs-on: ubuntu-latest
    # push 이벤트는 크롤링 건너뜀 (코드 변경만 배포)
    if: github.event_name != 'push'

    steps:
      - name: 📥 저장소 체크아웃
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: 🐍 Python 설정
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: 📦 의존성 설치
        run: |
          pip install requests beautifulsoup4 lxml

      - name: 🕷️ 크롤러 실행
        id: crawl
        run: |
          python scripts/crawl_daiso.py
          echo "product_count=$(python -c "import json; d=json.load(open('products.json')); print(len(d))")" >> $GITHUB_OUTPUT

      - name: 📊 크롤링 결과 확인
        run: |
          echo "수집된 제품 수: ${{ steps.crawl.outputs.product_count }}개"
          python -c "
          import json
          data = json.load(open('products.json', encoding='utf-8'))
          cats = {}
          for p in data:
              cats[p.get('category','미분류')] = cats.get(p.get('category','미분류'), 0) + 1
          for cat, cnt in sorted(cats.items()):
              print(f'  {cat}: {cnt}개')
          "

      - name: 💾 products.json 자동 커밋
        run: |
          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add products.json
          # 변경이 있을 때만 커밋
          git diff --staged --quiet || git commit -m "🔄 제품 데이터 자동 업데이트 ($(date '+%Y-%m-%d %H:%M KST'))"
          git push

  # ────────────────────────────────────────────────────────────────────────────
  deploy:
    name: GitHub Pages 배포
    runs-on: ubuntu-latest
    needs: [crawl]
    # crawl 성공 시 또는 push 이벤트일 때 실행
    if: always() && (needs.crawl.result == 'success' || github.event_name == 'push')

    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: 📥 저장소 체크아웃
        uses: actions/checkout@v4

      - name: ⚙️ GitHub Pages 설정
        uses: actions/configure-pages@v4

      - name: 📁 아티팩트 업로드
        uses: actions/upload-pages-artifact@v3
        with:
          # 루트 디렉토리 전체를 Pages로 배포
          path: "."

      - name: 🚀 GitHub Pages 배포
        id: deployment
        uses: actions/deploy-pages@v4
