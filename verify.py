import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

opens  = content.count('<div')
closes = content.count('</div>')
print(f'div 태그: open={opens}, close={closes}, 짝맞음={opens == closes}')

checks = [
    # 1. 도면 전체 보이기 (JS 기반 크기 계산)
    ('1-1. requestAnimationFrame 사용',         'requestAnimationFrame' in content),
    ('1-2. container.clientWidth 실측',          'container.clientWidth' in content),
    ('1-3. container.clientHeight 실측',         'container.clientHeight' in content),
    ('1-4. gridW/gridH 정확한 크기 계산',          'const gridW = cH' in content),
    ('1-5. fitScale 계산',                        'const fitScale' in content),
    ('1-6. wrapper px 단위 위치',                 'wrapper.style.width  = gridW' in content),

    # 2. road-zone 테두리/레이블 복구
    ('2-1. zone-road 배경색 추가',               'rgba(200,210,230,0.25)' in content),
    ('2-2. zone-road dashed border',             'dashed rgba(100,120,160' in content),
    ('2-3. road-label 13px',                     'font-size: 13px; color: rgba(80,100,140' in content),

    # 3. 차량마커 이름 + 강조
    ('3-1. 희수 car-name span',                  'car-name">희수</span>' in content),
    ('3-2. 차미 car-name span',                  'car-name">차미</span>' in content),
    ('3-3. car-name CSS 8px',                    '.car-name {\r\n        font-size: 8px' in content),
    ('3-4. parked-heesoo box-shadow',            '#12C2E9' in content),
    ('3-5. parked-chami box-shadow',             '#42E695' in content),

    # 4&5. Pointer Events 핀치줌/패닝
    ('4-1. Pointer Events API 사용',             "addEventListener('pointerdown'" in content),
    ('4-2. setPointerCapture 사용',              'setPointerCapture' in content),
    ('4-3. activePointers Map',                  'const activePointers = new Map()' in content),
    ('4-4. pointermove 리스너',                  "addEventListener('pointermove'" in content),
    ('4-5. pointerup 리스너',                    "addEventListener('pointerup'" in content),
    ('4-6. baseScale 기준 최소 스케일',           'baseScale * 1.05' in content),
    ('5-1. initState 전달 구조',                  'initState ? initState.fitScale' in content),
    ('5-2. applyTransform 함수',                 'function applyTransform()' in content),
    ('5-3. isMobile 분기',                       'if (isMobile && initState)' in content),
]

all_ok = True
for name, ok in checks:
    status = 'OK' if ok else 'FAIL'
    if not ok:
        all_ok = False
    print(f'  [{status}] {name}')

print(f'\n전체 검증: {"✅ 모두 통과" if all_ok else "❌ 일부 실패"}')
print(f'파일: {len(content):,} bytes, {content.count(chr(10))+1} 줄')
