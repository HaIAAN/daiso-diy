<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>다이소 DIY 조합기</title>
<style>
  :root {
    --primary: #e60012;
    --primary-dark: #b3000e;
    --bg: #f5f6f8;
    --card: #ffffff;
    --text: #1a1a1a;
    --muted: #6b7280;
    --border: #e5e7eb;
    --radius: 14px;
    --shadow: 0 4px 20px rgba(0,0,0,0.06);
  }
  * { box-sizing: border-box; margin:0; padding:0; }
  body {
    font-family: 'Pretendard', 'Noto Sans KR', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.5;
  }
  header {
    background: var(--primary);
    color: #fff;
    padding: 1rem 1.5rem;
    display: flex; align-items: center; justify-content: space-between;
    position: sticky; top:0; z-index: 100;
    box-shadow: 0 2px 10px rgba(230,0,18,0.3);
  }
  header h1 { font-size: 1.25rem; font-weight: 800; letter-spacing: -0.5px; }
  nav { display: flex; gap: .5rem; }
  nav button {
    background: rgba(255,255,255,0.15);
    border: none; color: #fff;
    padding: .45rem .9rem; border-radius: 999px;
    font-size: .85rem; cursor: pointer; transition: .2s;
  }
  nav button.active, nav button:hover { background: rgba(255,255,255,0.35); }

  main { max-width: 1100px; margin: 0 auto; padding: 1.5rem; }
  .section-title { font-size: 1.1rem; font-weight: 700; margin-bottom: .75rem; display: flex; align-items: center; gap: .5rem; }
  .section-title span { width: 6px; height: 6px; border-radius: 50%; background: var(--primary); }

  /* Product Grid */
  .filters { display: flex; gap: .5rem; margin-bottom: 1rem; flex-wrap: wrap; }
  .chip {
    padding: .35rem .8rem; border-radius: 999px; border: 1px solid var(--border);
    background: var(--card); font-size: .8rem; cursor: pointer; transition: .2s;
  }
  .chip.active { background: var(--primary); color: #fff; border-color: var(--primary); }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 1rem; }
  .card {
    background: var(--card); border-radius: var(--radius); overflow: hidden;
    box-shadow: var(--shadow); transition: .2s; cursor: pointer;
    border: 2px solid transparent;
  }
  .card:hover { transform: translateY(-3px); }
  .card.selected { border-color: var(--primary); }
  .card img { width:100%; height:150px; object-fit: cover; display:block; background:#f0f0f0; }
  .card-body { padding: .75rem; }
  .card-body .name { font-size: .85rem; font-weight: 700; }
  .card-body .meta { font-size: .75rem; color: var(--muted); margin-top: .25rem; }
  .card-body .price { font-size: .9rem; font-weight: 800; color: var(--primary); margin-top: .3rem; }

  /* Cart / Selection bar */
  .selection-bar {
    position: sticky; bottom: 0; background: var(--card); border-top: 1px solid var(--border);
    padding: .75rem 1rem; display: flex; gap: .75rem; align-items: center; justify-content: center;
    box-shadow: 0 -4px 20px rgba(0,0,0,0.06); z-index: 90;
  }
  .selection-bar .slot {
    width: 56px; height: 56px; border-radius: var(--radius); border: 2px dashed var(--border);
    display: grid; place-items: center; font-size: .7rem; color: var(--muted); overflow: hidden;
    position: relative; background: #fafafa;
  }
  .selection-bar .slot img { width:100%; height:100%; object-fit: cover; }
  .selection-bar .slot .remove {
    position: absolute; top:2px; right:2px; background:rgba(0,0,0,0.5); color:#fff; border:none;
    width:18px; height:18px; border-radius:50%; font-size:10px; cursor:pointer; display:none;
  }
  .selection-bar .slot.filled .remove { display:block; }
  .btn-primary {
    background: var(--primary); color:#fff; border:none; padding: .75rem 1.4rem;
    border-radius: var(--radius); font-weight: 700; font-size: .9rem; cursor: pointer; transition: .2s;
  }
  .btn-primary:disabled { background: #ccc; cursor: not-allowed; }
  .btn-primary:hover:not(:disabled) { background: var(--primary-dark); }

  /* Recipe / Result */
  .recipe-card {
    background: var(--card); border-radius: var(--radius); box-shadow: var(--shadow);
    padding: 1.25rem; margin-top: 1rem;
  }
  .recipe-card h3 { font-size: 1.1rem; margin-bottom: .5rem; }
  .recipe-card p { font-size: .9rem; color: var(--muted); margin-bottom: .5rem; }
  .recipe-card .final-image {
    width: 100%; max-height: 380px; object-fit: cover; border-radius: var(--radius); margin: .75rem 0;
    background: #f0f0f0; min-height: 200px;
  }
  .recipe-card .materials { display: flex; gap: .75rem; flex-wrap: wrap; margin-top: .5rem; }
  .recipe-card .materials .mini-card {
    display: flex; align-items: center; gap: .5rem; background: var(--bg); padding: .5rem .75rem; border-radius: 10px;
  }
  .recipe-card .materials .mini-card img { width:40px; height:40px; object-fit:cover; border-radius: 6px; background:#ddd; }
  .recipe-card .materials .mini-card div { font-size: .75rem; }
  .recipe-card .total { font-size: 1rem; font-weight: 800; color: var(--primary); margin-top: .75rem; }
  .badge { display:inline-block; padding: .2rem .55rem; border-radius: 6px; background: #fff0f1; color: var(--primary); font-size: .75rem; font-weight:700; margin-bottom: .75rem; }

  /* Target Input */
  .target-input {
    display: flex; gap: .5rem; margin-bottom: 1rem;
  }
  .target-input input {
    flex:1; padding: .7rem 1rem; border: 1px solid var(--border); border-radius: 999px; font-size: .9rem; outline:none;
  }
  .target-input button { border-radius: 999px; padding: .7rem 1.2rem; }

  .hidden { display: none !important; }
  .center { text-align: center; padding: 3rem 1rem; }

  @media (max-width: 600px) {
    .grid { grid-template-columns: repeat(2, 1fr); }
    header h1 { font-size: 1rem; }
    nav button { font-size: .75rem; padding: .35rem .6rem; }
  }
</style>
</head>
<body>
<header>
  <h1>DAISO DIY COMBINER</h1>
  <nav>
    <button id="nav-products" class="active" onclick="showPage('products')">제품 탐색</button>
    <button id="nav-combine" onclick="showPage('combine')">조합하기</button>
    <button id="nav-recipe" onclick="showPage('recipe')">레시피 창작</button>
  </nav>
</header>

<main>
  <!-- 제품 탐색 -->
  <section id="page-products">
    <div class="filters" id="product-filters">
      <button class="chip active" onclick="filterProducts('all', this)">전체</button>
      <button class="chip" onclick="filterProducts('조명', this)">조명</button>
      <button class="chip" onclick="filterProducts('리빙', this)">리빙</button>
      <button class="chip" onclick="filterProducts('공구/자동차', this)">공구</button>
      <button class="chip" onclick="filterProducts('가구/수납', this)">가구/수납</button>
      <button class="chip" onclick="filterProducts('주방/리빙', this)">주방</button>
      <button class="chip" onclick="filterProducts('문구/오피스', this)">문구</button>
    </div>
    <div class="grid" id="product-grid"></div>
  </section>

  <!-- 조합 결과 -->
  <section id="page-combine" class="hidden">
    <div class="section-title"><span></span> 조합 결과</div>
    <div id="combine-result"></div>
    <div class="center" id="combine-empty" style="padding:4rem 1rem;">
      <p style="color:var(--muted)">아래 선택 바에서 3가지 제품을 선택한 뒤 "조합하기"를 눌러보세요!</p>
    </div>
  </section>

  <!-- 레시피 창작 -->
  <section id="page-recipe" class="hidden">
    <div class="section-title"><span></span> 원하는 완성품을 적어주세요</div>
    <div class="target-input">
      <input type="text" id="target-input" placeholder="예: 무드등, 미니 화분 스탠드, 조명 오브제..." onkeydown="if(event.key==='Enter') generateRecipe()" />
      <button class="btn-primary" onclick="generateRecipe()">레시피 생성</button>
    </div>
    <div id="recipe-result"></div>
    <div class="center" id="recipe-empty" style="padding:3rem 1rem;">
      <p style="color:var(--muted)">원하는 DIY 완성품 이름을 입력하면 맞춤 레시피를 추천해드립니다.</p>
    </div>
  </section>
</main>

<!-- 하단 선택 바 -->
<div class="selection-bar" id="selection-bar">
  <div class="slot" id="slot-0" onclick="removeSlot(0)"><span>1</span><button class="remove">×</button></div>
  <div class="slot" id="slot-1" onclick="removeSlot(1)"><span>2</span><button class="remove">×</button></div>
  <div class="slot" id="slot-2" onclick="removeSlot(2)"><span>3</span><button class="remove">×</button></div>
  <button class="btn-primary" id="combine-btn" onclick="doCombine()" disabled>조합하기</button>
</div>

<script>
// GitHub Pages에서는 같은 도메인의 products.json을 fetch로 불러옵니다.
// GitHub Actions 크롤러가 매일 자동으로 products.json을 업데이트합니다.
let PRODUCTS = [];
let selected = [null, null, null];
let currentFilter = 'all';

// 로딩 표시
document.getElementById('product-grid').innerHTML = `
  <div style="grid-column:1/-1;text-align:center;padding:3rem;color:var(--muted)">
    <div style="font-size:2rem;margin-bottom:.5rem">⏳</div>
    <div>다이소 제품 데이터 불러오는 중...</div>
  </div>`;

fetch('./products.json?t=' + Date.now())
  .then(r => { if (!r.ok) throw new Error('load fail'); return r.json(); })
  .then(data => { PRODUCTS = data; renderProducts('all'); })
  .catch(() => { PRODUCTS = FALLBACK; renderProducts('all'); });

// 크롤링 실패 시 사용할 샘플 데이터 (폴백)
const FALLBACK = [
  {"id":"P001","name":"LED램프 (건전지식)","price":1000,"category":"조명","image":"https://image.pollinations.ai/prompt/daiso%20battery%20LED%20lamp%20product%20photo%20white%20background?width=200&height=200&seed=1&nologo=true"},
  {"id":"P002","name":"투명 유리병 (500ml)","price":1000,"category":"주방/리빙","image":"https://image.pollinations.ai/prompt/daiso%20clear%20glass%20bottle%20500ml%20product%20photo%20white%20background?width=200&height=200&seed=2&nologo=true"},
  {"id":"P003","name":"황동색 철사 (3m)","price":1000,"category":"공구/자동차","image":"https://image.pollinations.ai/prompt/daiso%20brass%20wire%203m%20product%20photo%20white%20background?width=200&height=200&seed=3&nologo=true"},
  {"id":"P004","name":"모래시계 (3분)","price":1000,"category":"문구/오피스","image":"https://image.pollinations.ai/prompt/daiso%20sand%20timer%203%20minutes%20product%20photo%20white%20background?width=200&height=200&seed=4&nologo=true"},
  {"id":"P005","name":"원목 미니 스탠드","price":2000,"category":"가구/수납","image":"https://image.pollinations.ai/prompt/daiso%20wooden%20mini%20stand%20product%20photo%20white%20background?width=200&height=200&seed=5&nologo=true"},
  {"id":"P006","name":"무드등 필름 (반투명)","price":1000,"category":"조명","image":"https://image.pollinations.ai/prompt/daiso%20translucent%20film%20sheet%20product%20photo%20white%20background?width=200&height=200&seed=6&nologo=true"},
  {"id":"P007","name":"미니 팬 (USB)","price":1000,"category":"생활/계절","image":"https://image.pollinations.ai/prompt/daiso%20mini%20USB%20fan%20product%20photo%20white%20background?width=200&height=200&seed=7&nologo=true"},
  {"id":"P008","name":"아크릴 물감 12색","price":2000,"category":"문구/오피스","image":"https://image.pollinations.ai/prompt/daiso%20acrylic%20paint%2012%20colors%20product%20photo%20white%20background?width=200&height=200&seed=8&nologo=true"},
  {"id":"P009","name":"수국 조화 (1묶음)","price":1000,"category":"리빙","image":"https://image.pollinations.ai/prompt/daiso%20hydrangea%20artificial%20flowers%20product%20photo%20white%20background?width=200&height=200&seed=9&nologo=true"},
  {"id":"P010","name":"LED 줄조명 2m","price":2000,"category":"조명","image":"https://image.pollinations.ai/prompt/daiso%20LED%20strip%20light%202m%20product%20photo%20white%20background?width=200&height=200&seed=10&nologo=true"},
  {"id":"P011","name":"플라스틱 바구니 (소)","price":1000,"category":"가구/수납","image":"https://image.pollinations.ai/prompt/daiso%20small%20plastic%20basket%20product%20photo%20white%20background?width=200&height=200&seed=11&nologo=true"},
  {"id":"P012","name":"빈티지 스티커 세트","price":1000,"category":"문구/오피스","image":"https://image.pollinations.ai/prompt/daiso%20vintage%20sticker%20set%20product%20photo%20white%20background?width=200&height=200&seed=12&nologo=true"},
  {"id":"P013","name":"청테이프 (방청)","price":1000,"category":"공구/자동차","image":"https://image.pollinations.ai/prompt/daiso%20rust%20prevention%20blue%20tape%20product%20photo%20white%20background?width=200&height=200&seed=13&nologo=true"},
  {"id":"P014","name":"미니 화분 (화이트)","price":1000,"category":"리빙","image":"https://image.pollinations.ai/prompt/daiso%20mini%20white%20pot%20product%20photo%20white%20background?width=200&height=200&seed=14&nologo=true"},
  {"id":"P015","name":"실리콘 글루건","price":2000,"category":"공구/자동차","image":"https://image.pollinations.ai/prompt/daiso%20silicone%20glue%20gun%20product%20photo%20white%20background?width=200&height=200&seed=15&nologo=true"},
  {"id":"P016","name":"금속 후크 (4개입)","price":1000,"category":"공구/자동차","image":"https://image.pollinations.ai/prompt/daiso%20metal%20hooks%204pcs%20product%20photo%20white%20background?width=200&height=200&seed=16&nologo=true"},
  {"id":"P017","name":"투명 아크릴판 A5","price":1000,"category":"문구/오피스","image":"https://image.pollinations.ai/prompt/daiso%20transparent%20acrylic%20board%20A5%20product%20photo%20white%20background?width=200&height=200&seed=17&nologo=true"},
  {"id":"P018","name":"원목 막대기 (30cm)","price":1000,"category":"가구/수납","image":"https://image.pollinations.ai/prompt/daiso%20wooden%20stick%2030cm%20product%20photo%20white%20background?width=200&height=200&seed=18&nologo=true"},
  {"id":"P019","name":"전구 모양 유리병","price":2000,"category":"주방/리빙","image":"https://image.pollinations.ai/prompt/daiso%20bulb%20shaped%20glass%20bottle%20product%20photo%20white%20background?width=200&height=200&seed=19&nologo=true"},
  {"id":"P020","name":"빈티지 로프 (3m)","price":1000,"category":"리빙","image":"https://image.pollinations.ai/prompt/daiso%20vintage%20rope%203m%20product%20photo%20white%20background?width=200&height=200&seed=20&nologo=true"}
];

function renderProducts(category) {
  const grid = document.getElementById('product-grid');
  grid.innerHTML = '';
  const items = category === 'all' ? PRODUCTS : PRODUCTS.filter(p => p.category === category);
  items.forEach(p => {
    const selIndex = selected.findIndex(s => s && s.id === p.id);
    const div = document.createElement('div');
    div.className = 'card' + (selIndex !== -1 ? ' selected' : '');
    div.onclick = () => toggleSelect(p);
    div.innerHTML = `
      <img src="${p.image}" alt="${p.name}" loading="lazy" />
      <div class="card-body">
        <div class="name">${p.name}</div>
        <div class="meta">${p.id} / ${p.category}</div>
        <div class="price">${p.price.toLocaleString()}원</div>
      </div>
    `;
    grid.appendChild(div);
  });
}

function filterProducts(cat, btnEl) {
  currentFilter = cat;
  document.querySelectorAll('#product-filters .chip').forEach(b => b.classList.remove('active'));
  if (btnEl) btnEl.classList.add('active');
  renderProducts(cat);
}

function toggleSelect(product) {
  const idx = selected.findIndex(s => s && s.id === product.id);
  if (idx !== -1) {
    selected[idx] = null;
  } else {
    const empty = selected.findIndex(s => s === null);
    if (empty === -1) { alert('3개까지만 선택할 수 있습니다.'); return; }
    selected[empty] = product;
  }
  updateSlots();
  renderProducts(currentFilter);
}

function updateSlots() {
  [0,1,2].forEach(i => {
    const slot = document.getElementById('slot-'+i);
    const product = selected[i];
    if (product) {
      slot.innerHTML = `<img src="${product.image}" alt=""><button class="remove">×</button>`;
      slot.classList.add('filled');
    } else {
      slot.innerHTML = `<span>${i+1}</span><button class="remove">×</button>`;
      slot.classList.remove('filled');
    }
  });
  const filled = selected.filter(Boolean).length;
  document.getElementById('combine-btn').disabled = filled !== 3;
}

function removeSlot(i) {
  selected[i] = null;
  updateSlots();
  renderProducts(currentFilter);
}

function showPage(page) {
  document.querySelectorAll('main > section').forEach(s => s.classList.add('hidden'));
  document.getElementById('page-'+page).classList.remove('hidden');
  document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
  document.getElementById('nav-'+page).classList.add('active');
}

function doCombine() {
  const items = selected.filter(Boolean);
  if (items.length !== 3) return;

  const names = items.map(p => p.name.split(' ')[0]);
  const total = items.reduce((s, p) => s + p.price, 0);
  const title = generateIdeaTitle(names);
  const desc = generateIdeaDesc(items, title);
  const seed = Math.floor(Math.random()*9000)+1000;
  const imageUrl = `https://image.pollinations.ai/prompt/diy%20handmade%20${encodeURIComponent(title)}%20made%20with%20${encodeURIComponent(names.join('%20and%20'))}%20aesthetic%20studio%20photo%20soft%20lighting?width=600&height=400&seed=${seed}&nologo=true`;

  const el = document.getElementById('combine-result');
  document.getElementById('combine-empty').classList.add('hidden');
  el.innerHTML = `
    <div class="recipe-card">
      <div class="badge">NEW DIY</div>
      <h3>${title}</h3>
      <p>${desc}</p>
      <img class="final-image" src="${imageUrl}" alt="${title}" loading="lazy">
      <div class="materials">
        ${items.map(p => `
          <div class="mini-card">
            <img src="${p.image}" alt="${p.name}">
            <div>
              <div style="font-weight:700">${p.name}</div>
              <div style="color:var(--muted)">${p.id}</div>
              <div style="color:var(--primary);font-weight:700">${p.price.toLocaleString()}원</div>
            </div>
          </div>
        `).join('')}
      </div>
      <div class="total">총 예상 비용: ${total.toLocaleString()}원</div>
      <button class="btn-primary" style="margin-top:1rem;width:100%" onclick="doCombine()">🔄 같은 재료로 다른 아이디어 보기</button>
    </div>
  `;
  showPage('combine');
}

function generateIdeaTitle(names) {
  const templates = [
    `${names[0]} ${names[1]} ${names[2]} 오브제`,
    `감성 ${names[0]} ${names[2]}`,
    `${names[1]} 활용 ${names[0]}`,
    `미니 ${names[2]} 스탠드`,
    `${names[0]} & ${names[2]} 조합품`,
    `DIY ${names[1]} 데코`,
    `${names[0]}를 이용한 ${names[2]}`,
  ];
  return templates[Math.floor(Math.random()*templates.length)];
}

function generateIdeaDesc(items, title) {
  const verbs = ['붙여서', '감싸서', '꽂아서', '조립해서', '덧씌워서'];
  const effects = ['따뜻한 무드 연출', '실용적인 수납 공간', '감성 인테리어 포인트', '독특한 오브제 완성', '유용한 데코 소품'];
  const v1 = verbs[Math.floor(Math.random()*verbs.length)];
  const v2 = verbs[Math.floor(Math.random()*verbs.length)];
  const e = effects[Math.floor(Math.random()*effects.length)];
  return `${items[0].name}와(과) ${items[1].name}를(을) ${v1} 거기에 ${items[2].name}를(을) ${v2} ${e}을(를) 만들어 보세요.`;
}

/* ---------- 레시피 창작 ---------- */
// 키워드 → 관련 카테고리(우선순위) 매핑. 매칭된 카테고리 풀에서 매번 다르게 3개를 뽑습니다.
const RECIPE_KEYWORDS = {
  '무드등': ['조명', '리빙', '주방/리빙'],
  '램프':   ['조명', '리빙', '주방/리빙'],
  '조명':   ['조명', '가구/수납'],
  '화분':   ['리빙', '가구/수납'],
  '스탠드': ['가구/수납', '조명'],
  '오브제': ['리빙', '주방/리빙', '문구/오피스'],
  '바구니': ['가구/수납', '공구/자동차'],
  '수납':   ['가구/수납', '공구/자동차'],
  '팬':     ['생활/계절', '공구/자동차', '문구/오피스'],
  '액자':   ['문구/오피스', '리빙'],
  '소품':   ['리빙', '문구/오피스', '조명'],
};

function pickRandom3(pool) {
  const shuffled = [...pool].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, 3);
}

function generateRecipe() {
  const keyword = document.getElementById('target-input').value.trim();
  if (!keyword) return alert('완성품 이름을 입력해주세요!');

  let matchedCats = null;
  for (const k in RECIPE_KEYWORDS) {
    if (keyword.includes(k)) { matchedCats = RECIPE_KEYWORDS[k]; break; }
  }

  let pool;
  if (matchedCats) {
    pool = PRODUCTS.filter(p => matchedCats.includes(p.category));
    if (pool.length < 3) pool = PRODUCTS; // 후보가 부족하면 전체에서 보충
  } else {
    pool = PRODUCTS; // 매칭 안되면 전체 풀에서 랜덤
  }

  const items = pickRandom3(pool);
  const names = items.map(p => p.name.split(' ')[0]);
  const total = items.reduce((s, p) => s + p.price, 0);
  const seed = Math.floor(Math.random()*9000)+1000;
  const safeKeyword = encodeURIComponent(keyword);
  const imageUrl = `https://image.pollinations.ai/prompt/diy%20handmade%20${safeKeyword}%20${encodeURIComponent(names.join('%20'))}%20aesthetic%20studio%20photo%20soft%20lighting%20korean%20interior?width=600&height=400&seed=${seed}&nologo=true`;

  const steps = [
    `① ${items[0].name}를(을) 준비하고 원하는 위치에 배치합니다.`,
    `② ${items[1].name}를(을) 활용해 기본 구조를 잡습니다.`,
    `③ ${items[2].name}로(으로) 마무리 디테일을 추가합니다.`,
    `④ 완성된 "${keyword}"를(을) 인테리어 공간에 배치해보세요.`
  ];

  document.getElementById('recipe-empty').classList.add('hidden');
  document.getElementById('recipe-result').innerHTML = `
    <div class="recipe-card">
      <div class="badge">맞춤 레시피</div>
      <h3>"${keyword}" 만들기</h3>
      <img class="final-image" src="${imageUrl}" alt="${keyword}" loading="lazy">
      <p style="font-weight:700; margin:.5rem 0">재료</p>
      <div class="materials">
        ${items.map(p => `
          <div class="mini-card">
            <img src="${p.image}" alt="${p.name}">
            <div>
              <div style="font-weight:700">${p.name}</div>
              <div style="color:var(--muted)">${p.id}</div>
              <div style="color:var(--primary);font-weight:700">${p.price.toLocaleString()}원</div>
            </div>
          </div>
        `).join('')}
      </div>
      <div class="total">총 예상 비용: ${total.toLocaleString()}원</div>
      <p style="font-weight:700; margin-top:1rem">만드는 방법</p>
      <ol style="padding-left:1.2rem; color:var(--muted); font-size:.9rem; line-height:1.8; margin-top:.4rem;">
        ${steps.map(s => `<li>${s}</li>`).join('')}
      </ol>
      <button class="btn-primary" style="margin-top:1rem;width:100%" onclick="generateRecipe()">🔄 다른 레시피 다시 추천받기</button>
    </div>
  `;
}
</script>
</body>
</html>
