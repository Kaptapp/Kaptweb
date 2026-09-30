# -*- coding: utf-8 -*-
"""Shared site chrome: the header, footer, skip link and social labels that every
secondary page carries identically.

These lived only in the help table, which is why the privacy pages kept shipping
an English skip link, footer, navigation labels and og:image:alt. Both tables
merge this now, so the wording stays in step instead of drifting apart again.

Every value here is the wording the homepage and the privacy page already use,
so nothing on a live page changes meaning. Brand and contact details are never
translated: Kapture, Kapture Pro, Chrome, kaptapp.com and the support address.
"""

CHROME = {

'<a class="skip-link" href="#main">Skip to content</a>': {
 'es': '<a class="skip-link" href="#main">Saltar al contenido</a>',
 'zh': '<a class="skip-link" href="#main">跳到主要内容</a>',
 'ko': '<a class="skip-link" href="#main">본문으로 건너뛰기</a>',
 'ja': '<a class="skip-link" href="#main">本文へスキップ</a>'},

'<nav class="header-nav" aria-label="Primary">': {
 'es': '<nav class="header-nav" aria-label="Navegación principal">',
 'zh': '<nav class="header-nav" aria-label="主导航">',
 'ko': '<nav class="header-nav" aria-label="주요 메뉴">',
 'ja': '<nav class="header-nav" aria-label="メインナビゲーション">'},

'<nav class="footer-nav" aria-label="Footer">': {
 'es': '<nav class="footer-nav" aria-label="Pie de página">',
 'zh': '<nav class="footer-nav" aria-label="页脚">',
 'ko': '<nav class="footer-nav" aria-label="푸터">',
 'ja': '<nav class="footer-nav" aria-label="フッター">'},

'<a href="/#how">How it works</a>': {
 'es': '<a href="/#how">Cómo funciona</a>', 'zh': '<a href="/#how">使用方法</a>',
 'ko': '<a href="/#how">사용 방법</a>', 'ja': '<a href="/#how">使い方</a>'},

'<a href="/privacy/">Privacy</a>': {
 'es': '<a href="/privacy/">Privacidad</a>', 'zh': '<a href="/privacy/">隐私</a>',
 'ko': '<a href="/privacy/">개인정보</a>', 'ja': '<a href="/privacy/">プライバシー</a>'},

'<a href="mailto:pequelord@gmail.com">Contact</a>': {
 'es': '<a href="mailto:pequelord@gmail.com">Contacto</a>',
 'zh': '<a href="mailto:pequelord@gmail.com">联系</a>',
 'ko': '<a href="mailto:pequelord@gmail.com">문의</a>',
 'ja': '<a href="mailto:pequelord@gmail.com">お問い合わせ</a>'},

'<a class="btn btn-ghost btn-sm store-cta" href="/">Back to site</a>': {
 'es': '<a class="btn btn-ghost btn-sm store-cta" href="/">Volver al sitio</a>',
 'zh': '<a class="btn btn-ghost btn-sm store-cta" href="/">返回网站</a>',
 'ko': '<a class="btn btn-ghost btn-sm store-cta" href="/">사이트로 돌아가기</a>',
 'ja': '<a class="btn btn-ghost btn-sm store-cta" href="/">サイトに戻る</a>'},

'aria-label="Kapture on X"': {
 'es': 'aria-label="Kapture en X"', 'zh': 'aria-label="Kapture 的 X 主页"',
 'ko': 'aria-label="X에서 Kapture 보기"', 'ja': 'aria-label="X の Kapture"'},

'aria-label="Kapture on LinkedIn"': {
 'es': 'aria-label="Kapture en LinkedIn"', 'zh': 'aria-label="Kapture 的 LinkedIn 主页"',
 'ko': 'aria-label="LinkedIn에서 Kapture 보기"', 'ja': 'aria-label="LinkedIn の Kapture"'},

# og:image:alt and twitter:image:alt share this string
'content="Kapture, full page screenshots for Chrome."': {
 'es': 'content="Kapture, capturas de páginas completas para Chrome."',
 'zh': 'content="Kapture，Chrome 整页截图扩展。"',
 'ko': 'content="Kapture, Chrome용 전체 페이지 스크린샷."',
 'ja': 'content="Kapture、Chrome でページ全体をスクリーンショット。"'},

# JSON-LD breadcrumb. Search results show these, so they are translated too.
'"name": "Home"': {
 'es': '"name": "Inicio"', 'zh': '"name": "首页"',
 'ko': '"name": "홈"', 'ja': '"name": "ホーム"'},

'<p class="legal-foot">Kapture by Pequelord &middot; Screenshots stay on your device.</p>': {
 'es': '<p class="legal-foot">Kapture, de Pequelord &middot; Tus capturas se quedan en tu dispositivo.</p>',
 'zh': '<p class="legal-foot">Kapture by Pequelord &middot; 截图只留在你的设备上。</p>',
 'ko': '<p class="legal-foot">Kapture by Pequelord &middot; 스크린샷은 기기 안에만 남습니다.</p>',
 'ja': '<p class="legal-foot">Kapture by Pequelord &middot; スクリーンショットは端末の外に出ません。</p>'},

# Help was reachable only from inside the extension. It is in the footer of
# every page now, so the link text is shared chrome like the rest of the nav.
'<a href="/help/">Help</a>': {
 'es': '<a href="/help/">Ayuda</a>',
 'zh': '<a href="/help/">帮助</a>',
 'ko': '<a href="/help/">도움말</a>',
 'ja': '<a href="/help/">ヘルプ</a>'},

}
