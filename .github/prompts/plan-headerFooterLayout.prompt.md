# Plan: 헤더/푸터 공백 제거
# (Remove Header/Footer Gaps)

현재 헤더는 이미 브라우저 최상단에 올바르게 고정되어 있습니다. 푸터만 Flexbox를 사용하여 브라우저 최하단에 붙도록 수정하면 됩니다.

## Steps

1. **`html` 요소 초기화** - `default.html`의 CSS에서 `html { margin: 0; padding: 0; height: 100%; }` 추가

2. **`body`에 Flexbox 레이아웃 적용** - `body` 스타일에 `min-height: 100vh; display: flex; flex-direction: column;` 추가하여 전체 높이 확보

3. **`.wrapper`가 가용 공간 차지하도록 설정** - `.wrapper` 스타일에 `flex: 1 0 auto;` 추가하여 헤더와 푸터 사이 공간 모두 차지

4. **푸터 고정 및 상단 마진 제거** - `.site-footer` 스타일에 `flex-shrink: 0;` 추가하고 `margin-top: 60px`을 `0`으로 변경

5. **콘텐츠와 푸터 간격 조정** - `section` 스타일의 `min-height` 제거하고 `margin-bottom: 40px` 추가로 적절한 간격 유지

## Further Considerations

1. **모바일 반응형 테스트** - 모바일에서 `body { padding-top: 180px }` 설정과 Flexbox 레이아웃이 충돌하지 않는지 확인 필요?: Yes

2. **콘텐츠 길이 테스트** - 짧은 페이지와 긴 페이지 모두에서 푸터가 올바르게 하단에 위치하는지 검증 필요?: Yes
