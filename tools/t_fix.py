# -*- coding: utf-8 -*-
"""Correction pass: one Chrome composition, the real Kapture Pro window.

The Kapture Pro interface inside `.kp-demo` and the side-panel screenshots stay
in English on every page. Neither product is localised, so translating their
interface would show software that does not exist. Only the site's own copy and
the alternative text around them are translated here.
"""

FIX = {

# ---------------------------------------------------------------- hero
'<a class="btn btn-ghost" href="#capture">See it capture</a>': {
 'es': '<a class="btn btn-ghost" href="#capture">Ver cómo captura</a>',
 'zh': '<a class="btn btn-ghost" href="#capture">看它如何截图</a>',
 'ko': '<a class="btn btn-ghost" href="#capture">캡처하는 모습 보기</a>',
 'ja': '<a class="btn btn-ghost" href="#capture">撮るところを見る</a>'},

# ---------------------------------------------------------------- Chrome composition
'''               alt="A webpage open in Chrome, being captured by Kapture."''': {
 'es': '''               alt="Una página web abierta en Chrome mientras Kapture la captura."''',
 'zh': '''               alt="Chrome 中打开的网页，Kapture 正在截取它。"''',
 'ko': '''               alt="Chrome에 열린 웹페이지를 Kapture가 캡처하는 모습."''',
 'ja': '''               alt="Chrome で開いた Web ページを Kapture が撮っているところ。"'''},

'''                   alt="The Kapture side panel set to Full page."''': {
 'es': '''                   alt="El panel lateral de Kapture en modo Full page."''',
 'zh': '''                   alt="Kapture 侧边栏处于 Full page 模式。"''',
 'ko': '''                   alt="Full page 모드로 설정된 Kapture 사이드 패널."''',
 'ja': '''                   alt="Full page に設定された Kapture のサイドパネル。"'''},

'''                   alt="The Kapture side panel set to Select area."''': {
 'es': '''                   alt="El panel lateral de Kapture en modo Select area."''',
 'zh': '''                   alt="Kapture 侧边栏处于 Select area 模式。"''',
 'ko': '''                   alt="Select area 모드로 설정된 Kapture 사이드 패널."''',
 'ja': '''                   alt="Select area に設定された Kapture のサイドパネル。"'''},

# ---------------------------------------------------------------- Kapture Pro intro
'''          Kapture Pro indexes the screenshots already on your Mac and turns them into a
          searchable visual library. The files never move, never upload, never leave the disk.''': {
 'es': '''          Kapture Pro indexa las capturas que ya tienes en el Mac y las convierte en una
          biblioteca visual con búsqueda. Los archivos no se mueven, no se suben, no salen del disco.''',
 'zh': '''          Kapture Pro 会索引你 Mac 上已有的截图，把它们变成一个可搜索的可视化图库。
          文件不会被移动，不会被上传，也不会离开硬盘。''',
 'ko': '''          Kapture Pro는 Mac에 이미 있는 스크린샷을 색인해 검색 가능한 시각적 라이브러리로
          만듭니다. 파일은 옮겨지지도, 업로드되지도, 디스크를 벗어나지도 않습니다.''',
 'ja': '''          Kapture Pro は Mac にすでにあるスクリーンショットを索引化し、検索できる
          ビジュアルライブラリにします。ファイルは移動せず、アップロードもされず、ディスクから出ません。'''},

# ---------------------------------------------------------------- two products
'<p class="plan-note">Pricing is not final. One payment, no subscription.</p>': {
 'es': '<p class="plan-note">El precio no es definitivo. Un solo pago, sin suscripción.</p>',
 'zh': '<p class="plan-note">价格尚未最终确定。一次付费，无订阅。</p>',
 'ko': '<p class="plan-note">가격은 아직 확정되지 않았습니다. 1회 결제, 구독 없음.</p>',
 'ja': '<p class="plan-note">価格は未確定です。買い切りで、サブスクリプションはありません。</p>'},

# ---------------------------------------------------------------- copy pass
'''        Kapture saves full webpages or selected areas straight from Chrome.
        Kapture Pro turns them into an organised, searchable visual library on your Mac.''': {
 'es': '''        Kapture guarda páginas web completas o el área que elijas, directamente desde Chrome.
        Kapture Pro las convierte en una biblioteca visual ordenada y con búsqueda en tu Mac.''',
 'zh': '''        Kapture 直接在 Chrome 里保存整张网页或你框选的区域。
        Kapture Pro 把它们变成 Mac 上一个井井有条、可搜索的可视化图库。''',
 'ko': '''        Kapture는 Chrome에서 바로 전체 웹페이지나 선택한 영역을 저장합니다.
        Kapture Pro는 그것들을 Mac 안에서 정돈되고 검색 가능한 시각적 라이브러리로 만듭니다.''',
 'ja': '''        Kapture は Chrome から直接、Web ページ全体や選んだ範囲を保存します。
        Kapture Pro はそれらを Mac 上の整理された、検索できるビジュアルライブラリにします。'''},

'<p class="section-lead">Capture a complete webpage or select exactly the area you need. Save it locally as PNG, JPEG or PDF.</p>': {
 'es': '<p class="section-lead">Captura una página web completa o selecciona justo el área que necesitas. Guárdala en local como PNG, JPEG o PDF.</p>',
 'zh': '<p class="section-lead">截取整张网页，或只框选你需要的那块区域。以 PNG、JPEG 或 PDF 保存在本地。</p>',
 'ko': '<p class="section-lead">웹페이지 전체를 캡처하거나 필요한 영역만 정확히 선택하세요. PNG, JPEG, PDF로 로컬에 저장됩니다.</p>',
 'ja': '<p class="section-lead">Web ページ全体を撮るか、必要な範囲だけを選びます。PNG、JPEG、PDF でローカルに保存できます。</p>'},

'<li data-mode="full"><h3>Full page</h3><p>Save the whole page to your project. Long pages split at 8,000&nbsp;pixels.</p></li>': {
 'es': '<li data-mode="full"><h3>Página completa</h3><p>Guarda la página entera en tu proyecto. Las páginas largas se dividen cada 8.000&nbsp;píxeles.</p></li>',
 'zh': '<li data-mode="full"><h3>整页截取</h3><p>把整张网页保存到你的项目里。过长的页面按 8,000&nbsp;像素分段。</p></li>',
 'ko': '<li data-mode="full"><h3>전체 페이지</h3><p>페이지 전체를 프로젝트에 저장합니다. 긴 페이지는 8,000&nbsp;픽셀 단위로 나뉩니다.</p></li>',
 'ja': '<li data-mode="full"><h3>ページ全体</h3><p>ページ全体をプロジェクトに保存します。長いページは 8,000&nbsp;ピクセルごとに分割されます。</p></li>'},

'<li data-mode="area"><h3>Select area</h3><p>Draw over exactly what you need. Save only that region.</p></li>': {
 'es': '<li data-mode="area"><h3>Selecciona un área</h3><p>Dibuja justo sobre lo que necesitas. Guarda solo esa zona.</p></li>',
 'zh': '<li data-mode="area"><h3>框选区域</h3><p>在你需要的地方拖出选框。只保存那一块区域。</p></li>',
 'ko': '<li data-mode="area"><h3>영역 선택</h3><p>필요한 부분만 정확히 드래그하세요. 그 영역만 저장됩니다.</p></li>',
 'ja': '<li data-mode="area"><h3>範囲を選ぶ</h3><p>必要なところだけをドラッグ。その範囲だけを保存します。</p></li>'},

'<h2>Built for the screenshot<br>you actually needed.</h2>': {
 'es': '<h2>Hecho para la captura<br>que de verdad necesitabas.</h2>',
 'zh': '<h2>为你真正需要的<br>那张截图而做。</h2>',
 'ko': '<h2>정말 필요했던<br>그 스크린샷을 위해.</h2>',
 'ja': '<h2>本当に必要だった<br>その一枚のために。</h2>'},

# The meta description repeated the same 'captures / captures' wording the hero
# used, so it moves with it.
'Kapture saves full webpages or selected areas straight from Chrome. Kapture Pro turns them into an organised, searchable visual library on your Mac. Everything stays local.': {
 'es': 'Kapture guarda páginas web completas o el área que elijas, directamente desde Chrome. Kapture Pro las convierte en una biblioteca visual ordenada y con búsqueda en tu Mac. Todo se queda en local.',
 'zh': 'Kapture 直接在 Chrome 里保存整张网页或你框选的区域。Kapture Pro 把它们变成 Mac 上一个井井有条、可搜索的可视化图库。一切都留在本地。',
 'ko': 'Kapture는 Chrome에서 바로 전체 웹페이지나 선택한 영역을 저장합니다. Kapture Pro는 그것들을 Mac 안에서 정돈되고 검색 가능한 시각적 라이브러리로 만듭니다. 모든 것이 기기 안에 남습니다.',
 'ja': 'Kapture は Chrome から直接、Web ページ全体や選んだ範囲を保存します。Kapture Pro はそれらを Mac 上の整理された、検索できるビジュアルライブラリにします。すべてローカルのままです。'},

# ---------------------------------------------------------------- closing statement
'<h2>One workflow.<br><span class="accent">Wherever you capture.</span></h2>': {
 'es': '<h2>Un mismo flujo.<br><span class="accent">Captures donde captures.</span></h2>',
 'zh': '<h2>一套流程，<br><span class="accent">无论你在哪里截图。</span></h2>',
 'ko': '<h2>하나의 흐름,<br><span class="accent">어디서 캡처하든.</span></h2>',
 'ja': '<h2>ひとつの流れ。<br><span class="accent">どこで撮っても。</span></h2>'},

# The pricing labels became .kicker eyebrows above the product titles.
'<p class="kicker plan-price">Free</p>': {
 'es': '<p class="kicker plan-price">Gratis</p>', 'zh': '<p class="kicker plan-price">免费</p>',
 'ko': '<p class="kicker plan-price">무료</p>', 'ja': '<p class="kicker plan-price">無料</p>'},

'<p class="kicker plan-price">One-time purchase</p>': {
 'es': '<p class="kicker plan-price">Pago único</p>', 'zh': '<p class="kicker plan-price">一次性买断</p>',
 'ko': '<p class="kicker plan-price">1회 구매</p>', 'ja': '<p class="kicker plan-price">買い切り</p>'},

# ---------------------------------------------------------------- the two products together
# Product names follow the form the rest of the site already uses in each
# language (Kapture para Chrome, Mac 版 Kapture Pro), so this section reads
# consistently with the footer plans rather than switching to English mid-page.
'<p class="kicker">The Kapture workflow</p>': {
 'es': '<p class="kicker">El flujo de Kapture</p>',
 'zh': '<p class="kicker">Kapture 工作流</p>',
 'ko': '<p class="kicker">Kapture 워크플로</p>',
 'ja': '<p class="kicker">Kapture のワークフロー</p>'},

'<h2>Kapture, Kapture Pro,<br>or both?</h2>': {
 'es': '<h2>¿Kapture, Kapture Pro<br>o los dos?</h2>',
 'zh': '<h2>Kapture、Kapture Pro，<br>还是两个一起用？</h2>',
 'ko': '<h2>Kapture, Kapture Pro,<br>아니면 둘 다?</h2>',
 'ja': '<h2>Kapture、Kapture Pro、<br>それとも両方？</h2>'},

'<p class="section-lead">Kapture handles capture in Chrome. Kapture Pro organises everything on your Mac. See what each product does on its own and what they unlock together.</p>': {
 'es': '<p class="section-lead">Kapture se encarga de capturar en Chrome. Kapture Pro lo organiza todo en tu Mac. Mira lo que hace cada uno por separado y lo que consigues con los dos.</p>',
 'zh': '<p class="section-lead">Kapture 负责在 Chrome 里截图，Kapture Pro 负责在 Mac 上整理。看看每个产品单独能做什么，以及两个一起用能带来什么。</p>',
 'ko': '<p class="section-lead">Kapture는 Chrome에서 캡처하고, Kapture Pro는 Mac에서 정리합니다. 각 제품이 따로 할 수 있는 일과, 둘을 함께 썼을 때 열리는 것들을 살펴보세요.</p>',
 'ja': '<p class="section-lead">Kapture は Chrome で撮り、Kapture Pro は Mac で整理します。それぞれが単体でできることと、両方そろって初めてできることをご覧ください。</p>'},

# ---- column headers ----
'<th scope="col">Feature</th>': {
 'es': '<th scope="col">Función</th>', 'zh': '<th scope="col">功能</th>',
 'ko': '<th scope="col">기능</th>', 'ja': '<th scope="col">機能</th>'},

'<th scope="col">Kapture for Chrome</th>': {
 'es': '<th scope="col">Kapture para Chrome</th>', 'zh': '<th scope="col">Chrome 版 Kapture</th>',
 'ko': '<th scope="col">Chrome용 Kapture</th>', 'ja': '<th scope="col">Chrome 版 Kapture</th>'},

'<th scope="col">Kapture Pro for Mac</th>': {
 'es': '<th scope="col">Kapture Pro para Mac</th>', 'zh': '<th scope="col">Mac 版 Kapture Pro</th>',
 'ko': '<th scope="col">Mac용 Kapture Pro</th>', 'ja': '<th scope="col">Mac 版 Kapture Pro</th>'},

'<th scope="col" class="is-both">Together</th>': {
 'es': '<th scope="col" class="is-both">Juntos</th>', 'zh': '<th scope="col" class="is-both">一起用</th>',
 'ko': '<th scope="col" class="is-both">함께</th>', 'ja': '<th scope="col" class="is-both">両方</th>'},

# ---- row labels ----
'<th scope="row">Full-page capture</th>': {
 'es': '<th scope="row">Captura de página completa</th>', 'zh': '<th scope="row">整页截图</th>',
 'ko': '<th scope="row">전체 페이지 캡처</th>', 'ja': '<th scope="row">ページ全体の撮影</th>'},

'<th scope="row">Select-area capture</th>': {
 'es': '<th scope="row">Captura de un área</th>', 'zh': '<th scope="row">框选区域截图</th>',
 'ko': '<th scope="row">영역 선택 캡처</th>', 'ja': '<th scope="row">範囲を選んで撮影</th>'},

'<th scope="row">PNG, JPEG or PDF</th>': {
 'es': '<th scope="row">PNG, JPEG o PDF</th>', 'zh': '<th scope="row">PNG、JPEG 或 PDF</th>',
 'ko': '<th scope="row">PNG, JPEG, PDF</th>', 'ja': '<th scope="row">PNG・JPEG・PDF</th>'},

'<th scope="row">Save locally</th>': {
 'es': '<th scope="row">Guardado en local</th>', 'zh': '<th scope="row">保存到本地</th>',
 'ko': '<th scope="row">로컬 저장</th>', 'ja': '<th scope="row">ローカルに保存</th>'},

'<th scope="row">Visual screenshot library</th>': {
 'es': '<th scope="row">Biblioteca visual de capturas</th>', 'zh': '<th scope="row">可视化截图图库</th>',
 'ko': '<th scope="row">시각적 스크린샷 라이브러리</th>', 'ja': '<th scope="row">ビジュアルなスクリーンショット一覧</th>'},

'<th scope="row">Project &amp; collection management</th>': {
 'es': '<th scope="row">Gestión de proyectos y colecciones</th>', 'zh': '<th scope="row">项目与合集管理</th>',
 'ko': '<th scope="row">프로젝트 및 컬렉션 관리</th>', 'ja': '<th scope="row">プロジェクトとコレクションの管理</th>'},

'<th scope="row">Search and filters</th>': {
 'es': '<th scope="row">Búsqueda y filtros</th>', 'zh': '<th scope="row">搜索与筛选</th>',
 'ko': '<th scope="row">검색과 필터</th>', 'ja': '<th scope="row">検索とフィルター</th>'},

'<th scope="row">Tags and notes</th>': {
 'es': '<th scope="row">Etiquetas y notas</th>', 'zh': '<th scope="row">标签与备注</th>',
 'ko': '<th scope="row">태그와 메모</th>', 'ja': '<th scope="row">タグとメモ</th>'},

'<th scope="row">File inspector</th>': {
 'es': '<th scope="row">Inspector de archivos</th>', 'zh': '<th scope="row">文件信息面板</th>',
 'ko': '<th scope="row">파일 인스펙터</th>', 'ja': '<th scope="row">ファイルインスペクタ</th>'},

'<th scope="row">Capture to organise workflow</th>': {
 'es': '<th scope="row">Flujo de captura a organización</th>', 'zh': '<th scope="row">从截图到整理的完整流程</th>',
 'ko': '<th scope="row">캡처에서 정리까지의 흐름</th>', 'ja': '<th scope="row">撮影から整理までの流れ</th>'},

# ---- the marks' accessible names (replaced everywhere they appear) ----
'aria-label="Yes"': {
 'es': 'aria-label="Sí"', 'zh': 'aria-label="支持"',
 'ko': 'aria-label="지원"', 'ja': 'aria-label="対応"'},

'aria-label="No"': {
 'es': 'aria-label="No"', 'zh': 'aria-label="不支持"',
 'ko': 'aria-label="미지원"', 'ja': 'aria-label="非対応"'},

# ---------------------------------------------------------------- Chrome headline
'<h2>Capture everything.<br>Or exactly one part of it.</h2>': {
 'es': '<h2>Captura todo.<br>O exactamente una parte.</h2>',
 'zh': '<h2>整页全都要，<br>或者只要其中一块。</h2>',
 'ko': '<h2>전부 담거나,<br>딱 필요한 부분만.</h2>',
 'ja': '<h2>すべてを撮る。<br>あるいは必要な一部だけ。</h2>'},


# ---------------------------------------------------------------- figure caption
# Static and visually hidden: it names the figure for assistive technology and
# is never re-announced as the phases cycle.
'<figcaption class="cap-caption">Kapture running in Chrome: first a full page capture, then an area drawn on the same page.</figcaption>': {
 'es': '<figcaption class="cap-caption">Kapture funcionando en Chrome: primero una captura de la página completa y después un área dibujada sobre esa misma página.</figcaption>',
 'zh': '<figcaption class="cap-caption">Kapture 在 Chrome 中运行：先截取整张网页，再在同一页面上框选一块区域。</figcaption>',
 'ko': '<figcaption class="cap-caption">Chrome에서 실행 중인 Kapture: 먼저 전체 페이지를 캡처하고, 이어서 같은 페이지에서 영역을 드래그합니다.</figcaption>',
 'ja': '<figcaption class="cap-caption">Chrome で動く Kapture。まずページ全体を撮り、続いて同じページ上で範囲を選びます。</figcaption>'},

# ---------------------------------------------------------------- Windows platform
# Same product as the Mac build, second platform, same unreleased state.
'aria-label="Kapture Pro for Windows. Coming soon."': {
 'es': 'aria-label="Kapture Pro para Windows. Muy pronto."',
 'zh': 'aria-label="Windows 版 Kapture Pro。即将推出。"',
 'ko': 'aria-label="Windows용 Kapture Pro. 곧 출시됩니다."',
 'ja': 'aria-label="Windows 版 Kapture Pro。近日公開。"'},

'<span class="store-cta-label">Pro for Mac</span>': {
 'es': '<span class="store-cta-label">Pro para Mac</span>',
 'zh': '<span class="store-cta-label">Mac 版 Pro</span>',
 'ko': '<span class="store-cta-label">Mac용 Pro</span>',
 'ja': '<span class="store-cta-label">Mac 版 Pro</span>'},

'<span class="store-cta-label">Pro for Windows</span>': {
 'es': '<span class="store-cta-label">Pro para Windows</span>',
 'zh': '<span class="store-cta-label">Windows 版 Pro</span>',
 'ko': '<span class="store-cta-label">Windows용 Pro</span>',
 'ja': '<span class="store-cta-label">Windows 版 Pro</span>'},

'<h3>Kapture<br>for Chrome</h3>': {
 'es': '<h3>Kapture<br>para Chrome</h3>',
 'zh': '<h3>Kapture<br>Chrome 版</h3>',
 'ko': '<h3>Kapture<br>Chrome용</h3>',
 'ja': '<h3>Kapture<br>Chrome 版</h3>'},

'<h3>Kapture Pro<br>for Mac</h3>': {
 'es': '<h3>Kapture Pro<br>para Mac</h3>',
 'zh': '<h3>Kapture Pro<br>Mac 版</h3>',
 'ko': '<h3>Kapture Pro<br>Mac용</h3>',
 'ja': '<h3>Kapture Pro<br>Mac 版</h3>'},

'<h3>Kapture Pro<br>for Windows</h3>': {
 'es': '<h3>Kapture Pro<br>para Windows</h3>',
 'zh': '<h3>Kapture Pro<br>Windows 版</h3>',
 'ko': '<h3>Kapture Pro<br>Windows용</h3>',
 'ja': '<h3>Kapture Pro<br>Windows 版</h3>'},

# ---------------------------------------------------------------- company credit
'<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; A <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a> product</p>': {
 'es': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; Un producto de <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a></p>',
 'zh': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a> 出品</p>',
 'ko': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a> 제품</p>',
 'ja': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a> のプロダクト</p>'},

# ---------------------------------------------------------------- platform-neutral positioning
# Kapture Pro is one product on two desktop platforms, so the general copy no
# longer names Mac. "Desktop" becomes the everyday word for a personal computer
# in each language, never the Desktop folder.
'<title>Kapture: Capture in Chrome, organise on your desktop</title>': {
 'es': '<title>Kapture: captura en Chrome, organiza en tu ordenador</title>',
 'zh': '<title>Kapture：在 Chrome 截图，在电脑上整理</title>',
 'ko': '<title>Kapture: Chrome에서 캡처하고 컴퓨터에서 정리하세요</title>',
 'ja': '<title>Kapture：Chrome で撮って、パソコンで整理する</title>'},

'Kapture saves full webpages or selected areas straight from Chrome. Kapture Pro turns them into an organised, searchable visual library on your desktop. Everything stays local.': {
 'es': 'Kapture guarda páginas web completas o el área que elijas, directamente desde Chrome. Kapture Pro las convierte en una biblioteca visual ordenada y con búsqueda en tu ordenador. Todo se queda en local.',
 'zh': 'Kapture 直接在 Chrome 里保存整张网页或你框选的区域。Kapture Pro 把它们变成电脑上一个井井有条、可搜索的可视化图库。一切都留在本地。',
 'ko': 'Kapture는 Chrome에서 바로 전체 웹페이지나 선택한 영역을 저장합니다. Kapture Pro는 그것들을 컴퓨터 안에서 정돈되고 검색 가능한 시각적 라이브러리로 만듭니다. 모든 것이 기기 안에 남습니다.',
 'ja': 'Kapture は Chrome から直接、Web ページ全体や選んだ範囲を保存します。Kapture Pro はそれらをパソコン上の整理された、検索できるビジュアルライブラリにします。すべてローカルのままです。'},

'Chrome extension 0.4.7 &middot; Kapture Pro': {
 'es': 'Extensión de Chrome 0.4.7 &middot; Kapture Pro',
 'zh': 'Chrome 扩展程序 0.4.7 &middot; Kapture Pro',
 'ko': 'Chrome 확장 프로그램 0.4.7 &middot; Kapture Pro',
 'ja': 'Chrome 拡張機能 0.4.7 &middot; Kapture Pro'},

'''        Capture in Chrome.<br>
        <span class="accent">Organise on your desktop.</span>''': {
 'es': '''        Captura en Chrome.<br>
        <span class="accent">Organiza en tu ordenador.</span>''',
 'zh': '''        在 Chrome 截图。<br>
        <span class="accent">在电脑上整理。</span>''',
 'ko': '''        Chrome에서 캡처.<br>
        <span class="accent">컴퓨터에서 정리.</span>''',
 'ja': '''        Chrome で撮る。<br>
        <span class="accent">パソコンで整理する。</span>'''},

# og:title and twitter:title carry the title without its tag. They were left in
# English before this pass; keying the bare string localises all three at once.
'Kapture: Capture in Chrome, organise on your desktop': {
 'es': 'Kapture: captura en Chrome, organiza en tu ordenador',
 'zh': 'Kapture：在 Chrome 截图，在电脑上整理',
 'ko': 'Kapture: Chrome에서 캡처하고 컴퓨터에서 정리하세요',
 'ja': 'Kapture：Chrome で撮って、パソコンで整理する'},

'<p class="hero-note">Requires Chrome 120 or later. Kapture for Chrome is free. Kapture Pro is coming soon for Mac and Windows.</p>': {
 'es': '<p class="hero-note">Requiere Chrome 120 o posterior. Kapture para Chrome es gratis. Kapture Pro llega pronto para Mac y Windows.</p>',
 'zh': '<p class="hero-note">需要 Chrome 120 或更高版本。Chrome 版 Kapture 免费，Kapture Pro 即将推出 Mac 版和 Windows 版。</p>',
 'ko': '<p class="hero-note">Chrome 120 이상이 필요합니다. Chrome용 Kapture는 무료이고, Kapture Pro는 Mac과 Windows용으로 곧 출시됩니다.</p>',
 'ja': '<p class="hero-note">Chrome 120 以降が必要です。Chrome 版 Kapture は無料。Kapture Pro は Mac 版と Windows 版を近日公開予定です。</p>'},

'<figcaption>The Chrome extension captures. The desktop app organises what it captures.</figcaption>': {
 'es': '<figcaption>La extensión de Chrome captura. La app de escritorio organiza lo capturado.</figcaption>',
 'zh': '<figcaption>Chrome 扩展负责截图，桌面应用负责整理这些截图。</figcaption>',
 'ko': '<figcaption>Chrome 확장 프로그램이 캡처하고, 데스크톱 앱이 그 캡처를 정리합니다.</figcaption>',
 'ja': '<figcaption>Chrome 拡張機能が撮り、デスクトップアプリがそれを整理します。</figcaption>'},

'''          Kapture Pro indexes the screenshots already on your computer and turns them into a
          searchable visual library. The files never move, never upload, never leave the disk.''': {
 'es': '''          Kapture Pro indexa las capturas que ya tienes en el ordenador y las convierte en una
          biblioteca visual con búsqueda. Los archivos no se mueven, no se suben, no salen del disco.''',
 'zh': '''          Kapture Pro 会索引你电脑上已有的截图，把它们变成一个可搜索的可视化图库。
          文件不会被移动，不会被上传，也不会离开硬盘。''',
 'ko': '''          Kapture Pro는 컴퓨터에 이미 있는 스크린샷을 색인해 검색 가능한 시각적 라이브러리로
          만듭니다. 파일은 옮겨지지도, 업로드되지도, 디스크를 벗어나지도 않습니다.''',
 'ja': '''          Kapture Pro はパソコンにすでにあるスクリーンショットを索引化し、検索できる
          ビジュアルライブラリにします。ファイルは移動せず、アップロードもされず、ディスクから出ません。'''},

'<p class="section-lead">Kapture handles capture in Chrome. Kapture Pro organises everything on your desktop. See what each product does on its own and what they unlock together.</p>': {
 'es': '<p class="section-lead">Kapture se encarga de capturar en Chrome. Kapture Pro lo organiza todo en tu ordenador. Mira lo que hace cada uno por separado y lo que consigues con los dos.</p>',
 'zh': '<p class="section-lead">Kapture 负责在 Chrome 里截图，Kapture Pro 负责在电脑上整理。看看每个产品单独能做什么，以及两个一起用能带来什么。</p>',
 'ko': '<p class="section-lead">Kapture는 Chrome에서 캡처하고, Kapture Pro는 컴퓨터에서 정리합니다. 각 제품이 따로 할 수 있는 일과, 둘을 함께 썼을 때 열리는 것들을 살펴보세요.</p>',
 'ja': '<p class="section-lead">Kapture は Chrome で撮り、Kapture Pro はパソコンで整理します。それぞれが単体でできることと、両方そろって初めてできることをご覧ください。</p>'},

'''            Kapture creates screenshots on your computer and saves them through Chrome's own
            Downloads system. Kapture Pro reads the files already sitting on your computer. Nothing
            is uploaded, neither product needs an account, and there is no analytics,
            advertising or tracking in either one.''': {
 'es': '''            Kapture crea las capturas en tu ordenador y las guarda con el sistema de descargas
            de Chrome. Kapture Pro lee los archivos que ya están en tu ordenador. No se sube nada,
            ninguno de los dos necesita cuenta y ninguno incluye analíticas, publicidad ni
            seguimiento.''',
 'zh': '''            Kapture 在你的电脑上生成截图，并通过 Chrome 自带的下载功能保存。Kapture Pro
            读取的是电脑上已有的文件。没有任何东西被上传，两款产品都不需要账号，也都不含
            分析、广告或追踪。''',
 'ko': '''            Kapture는 사용자의 컴퓨터에서 스크린샷을 만들고 Chrome의 다운로드 기능으로
            저장합니다. Kapture Pro는 이미 컴퓨터에 있는 파일을 읽습니다. 업로드되는 것은 없고,
            두 제품 모두 계정이 필요 없으며, 분석·광고·추적도 들어 있지 않습니다.''',
 'ja': '''            Kapture はあなたのパソコン上でスクリーンショットを作り、Chrome のダウンロード機能で
            保存します。Kapture Pro は、すでにパソコンにあるファイルを読むだけです。アップロードは
            一切なく、どちらの製品もアカウント不要で、解析・広告・トラッキングも含まれていません。'''},

'<figcaption>Captured in Chrome, kept on your computer.</figcaption>': {
 'es': '<figcaption>Capturado en Chrome, guardado en tu ordenador.</figcaption>',
 'zh': '<figcaption>在 Chrome 截图，留在你的电脑上。</figcaption>',
 'ko': '<figcaption>Chrome에서 캡처하고, 컴퓨터에 그대로 보관.</figcaption>',
 'ja': '<figcaption>Chrome で撮って、パソコンに置いたまま。</figcaption>'},

# ---------------------------------------------------------------- Smart
# Smart, its five tools and their names are the app's own approved terms from
# Localizable.xcstrings. Nothing here is translated for the first time.
'<p class="kicker">Smart</p>': {
 'es': '<p class="kicker">Inteligente</p>',
 'zh': '<p class="kicker">智能</p>',
 'ko': '<p class="kicker">스마트</p>',
 'ja': '<p class="kicker">スマート</p>'},

'<h2>Find what your library<br>has been hiding.</h2>': {
 'es': '<h2>Descubre lo que tu<br>biblioteca escondía.</h2>',
 'zh': '<h2>找出图库里<br>一直藏着的东西。</h2>',
 'ko': '<h2>라이브러리가 숨기고 있던<br>것을 찾아보세요.</h2>',
 'ja': '<h2>ライブラリが隠していた<br>ものを見つける。</h2>'},

'<p class="section-lead">Smart is one place in Kapture Pro with five tools. It shows you what still needs organising, which files are exact copies, what is worth a second look, where your captures came from, and the tidying you asked Kapture to do for you.</p>': {
 'es': '<p class="section-lead">Inteligente es un único lugar dentro de Kapture Pro con cinco herramientas. Te enseña lo que aún está sin organizar, qué archivos son copias exactas, qué merece un segundo vistazo, de dónde vienen tus capturas y el orden que le has pedido a Kapture que ponga por ti.</p>',
 'zh': '<p class="section-lead">智能是 Kapture Pro 里的一个地方，包含五个工具。它会告诉你哪些还没整理、哪些文件是完全相同的副本、哪些值得再看一眼、你的截图来自哪里，以及你让 Kapture 替你做的整理。</p>',
 'ko': '<p class="section-lead">스마트는 Kapture Pro 안의 한 곳으로, 다섯 가지 도구가 있습니다. 아직 정리가 필요한 것, 완전히 동일한 파일, 다시 살펴볼 만한 것, 캡처가 어디에서 왔는지, 그리고 Kapture에 맡긴 정리를 보여 줍니다.</p>',
 'ja': '<p class="section-lead">スマートは Kapture Pro のなかの一か所で、5 つのツールがあります。まだ整理が必要なもの、完全に同じファイル、見直す価値のあるもの、キャプチャの取得元、そして Kapture に依頼した整理を教えてくれます。</p>'},

'<li data-tool="unorganised"><button type="button"><h3>Unorganised</h3><p>Everything that is not in a project yet, from every source.</p></button></li>': {
 'es': '<li data-tool="unorganised"><button type="button"><h3>Sin organizar</h3><p>Todo lo que todavía no está en un proyecto, venga de donde venga.</p></button></li>',
 'zh': '<li data-tool="unorganised"><button type="button"><h3>未整理</h3><p>还没有归入项目的所有内容，涵盖所有来源。</p></button></li>',
 'ko': '<li data-tool="unorganised"><button type="button"><h3>미정리</h3><p>출처와 관계없이, 아직 프로젝트에 들어가지 않은 모든 것.</p></button></li>',
 'ja': '<li data-tool="unorganised"><button type="button"><h3>未整理</h3><p>まだプロジェクトに入っていないもの、すべてのソースから。</p></button></li>'},

'<li data-tool="duplicates"><button type="button"><h3>Duplicates</h3><p>Files that are exactly the same, byte for byte. You choose which copy to keep.</p></button></li>': {
 'es': '<li data-tool="duplicates"><button type="button"><h3>Duplicados</h3><p>Archivos exactamente iguales, byte a byte. Tú eliges qué copia se queda.</p></button></li>',
 'zh': '<li data-tool="duplicates"><button type="button"><h3>重复项</h3><p>逐字节完全相同的文件。由你决定保留哪一份。</p></button></li>',
 'ko': '<li data-tool="duplicates"><button type="button"><h3>중복 항목</h3><p>바이트 단위까지 완전히 같은 파일. 어떤 복사본을 남길지는 사용자가 정합니다.</p></button></li>',
 'ja': '<li data-tool="duplicates"><button type="button"><h3>重複</h3><p>バイト単位で完全に同じファイル。どちらを残すかはあなたが選びます。</p></button></li>'},

'<li data-tool="cleanup"><button type="button"><h3>Cleanup</h3><p>Older and larger captures worth a second look. Nothing is removed for you.</p></button></li>': {
 'es': '<li data-tool="cleanup"><button type="button"><h3>Limpieza</h3><p>Capturas antiguas y pesadas que merecen un segundo vistazo. Aquí no se elimina nada por ti.</p></button></li>',
 'zh': '<li data-tool="cleanup"><button type="button"><h3>清理</h3><p>值得再看一眼的旧截图和大文件。这里的内容不会替你移除。</p></button></li>',
 'ko': '<li data-tool="cleanup"><button type="button"><h3>정리</h3><p>다시 살펴볼 만한 오래되고 큰 캡처. 임의로 삭제되지는 않습니다.</p></button></li>',
 'ja': '<li data-tool="cleanup"><button type="button"><h3>クリーンアップ</h3><p>見直す価値のある古くて大きいキャプチャ。自動で削除されることはありません。</p></button></li>'},

'<li data-tool="sources"><button type="button"><h3>Sources</h3><p>Where your captures came from, grouped by site. Worked out locally.</p></button></li>': {
 'es': '<li data-tool="sources"><button type="button"><h3>Fuentes</h3><p>De dónde vienen tus capturas, agrupadas por sitio. Se calcula en local.</p></button></li>',
 'zh': '<li data-tool="sources"><button type="button"><h3>来源</h3><p>你的截图来自哪里，按网站分组。完全在本地算出。</p></button></li>',
 'ko': '<li data-tool="sources"><button type="button"><h3>출처</h3><p>캡처가 어디에서 왔는지, 사이트별로 묶어서. 기기 안에서 계산됩니다.</p></button></li>',
 'ja': '<li data-tool="sources"><button type="button"><h3>ソース</h3><p>キャプチャの取得元を、サイトごとにまとめて。すべてローカルで判定します。</p></button></li>'},

'<li data-tool="rules"><button type="button"><h3>Rules</h3><p>Tidying you asked Kapture to do for you. Rules never delete anything.</p></button></li>': {
 'es': '<li data-tool="rules"><button type="button"><h3>Reglas</h3><p>El orden que le has pedido a Kapture que ponga por ti. Las reglas nunca borran nada.</p></button></li>',
 'zh': '<li data-tool="rules"><button type="button"><h3>规则</h3><p>你让 Kapture 替你做的整理。规则永远不会删除任何东西。</p></button></li>',
 'ko': '<li data-tool="rules"><button type="button"><h3>규칙</h3><p>Kapture에 맡긴 정리. 규칙이 무언가를 삭제하는 일은 없습니다.</p></button></li>',
 'ja': '<li data-tool="rules"><button type="button"><h3>ルール</h3><p>Kapture に依頼した整理。ルールが何かを削除することはありません。</p></button></li>'},

# ---------------------------------------------------------------- Languages
'<p class="kicker">Languages</p>': {
 'es': '<p class="kicker">Idiomas</p>',
 'zh': '<p class="kicker">语言</p>',
 'ko': '<p class="kicker">언어</p>',
 'ja': '<p class="kicker">言語</p>'},

'<h2>Five languages.<br><span class="accent">Or simply follow your system.</span></h2>': {
 'es': '<h2>Cinco idiomas.<br><span class="accent">O simplemente el de tu sistema.</span></h2>',
 'zh': '<h2>五种语言。<br><span class="accent">或者直接跟随系统。</span></h2>',
 'ko': '<h2>다섯 가지 언어.<br><span class="accent">또는 시스템 설정 그대로.</span></h2>',
 'ja': '<h2>5 つの言語。<br><span class="accent">あるいはシステムのままで。</span></h2>'},

'<p class="section-lead">Kapture for Chrome and Kapture Pro both speak English, Spanish, Simplified Chinese, Korean and Japanese. Pick one, or leave it on System and Kapture follows whatever your computer is already set to.</p>': {
 'es': '<p class="section-lead">Kapture para Chrome y Kapture Pro hablan inglés, español, chino simplificado, coreano y japonés. Elige uno, o déjalo en Sistema y Kapture seguirá el idioma que ya tenga tu ordenador.</p>',
 'zh': '<p class="section-lead">Chrome 版 Kapture 和 Kapture Pro 都支持英语、西班牙语、简体中文、韩语和日语。你可以自己选一个，也可以保持“系统”，让 Kapture 跟随电脑已有的设置。</p>',
 'ko': '<p class="section-lead">Chrome용 Kapture와 Kapture Pro 모두 영어, 스페인어, 중국어 간체, 한국어, 일본어를 지원합니다. 직접 고르거나, 시스템으로 두면 Kapture가 컴퓨터에 설정된 언어를 따릅니다.</p>',
 'ja': '<p class="section-lead">Chrome 版 Kapture と Kapture Pro は、英語・スペイン語・簡体中国語・韓国語・日本語に対応しています。ひとつを選んでも、システムのままにしてパソコンの設定に従わせても構いません。</p>'},

# ---------------------------------------------------------------- workflow
'<p class="section-lead">Kapture captures in Chrome. Kapture Pro turns what you captured into a library, then Smart, Collections and Projects keep it in order. See what each product does on its own and what they unlock together.</p>': {
 'es': '<p class="section-lead">Kapture captura en Chrome. Kapture Pro convierte lo capturado en una biblioteca, y luego Inteligente, Colecciones y Proyectos la mantienen en orden. Mira lo que hace cada uno por separado y lo que consigues con los dos.</p>',
 'zh': '<p class="section-lead">Kapture 负责在 Chrome 里截图。Kapture Pro 把截下来的东西变成一个图库，再由智能、收藏集和项目让它保持有序。看看每个产品单独能做什么，以及两个一起用能带来什么。</p>',
 'ko': '<p class="section-lead">Kapture는 Chrome에서 캡처합니다. Kapture Pro는 캡처한 것을 라이브러리로 만들고, 스마트와 컬렉션과 프로젝트가 그것을 정돈된 상태로 유지합니다. 각 제품이 따로 할 수 있는 일과, 둘을 함께 썼을 때 열리는 것들을 살펴보세요.</p>',
 'ja': '<p class="section-lead">Kapture は Chrome で撮ります。Kapture Pro は撮ったものをライブラリに変え、スマート・コレクション・プロジェクトがそれを整った状態に保ちます。それぞれが単体でできることと、両方そろって初めてできることをご覧ください。</p>'},

'<th scope="row">Smart organisation</th>': {
 'es': '<th scope="row">Organización inteligente</th>',
 'zh': '<th scope="row">智能整理</th>',
 'ko': '<th scope="row">스마트 정리</th>',
 'ja': '<th scope="row">スマートによる整理</th>'},

# ---------------------------------------------------------------- version and metadata
'Chrome extension 0.4.9 &middot; Kapture Pro': {
 'es': 'Extensión de Chrome 0.4.9 &middot; Kapture Pro',
 'zh': 'Chrome 扩展程序 0.4.9 &middot; Kapture Pro',
 'ko': 'Chrome 확장 프로그램 0.4.9 &middot; Kapture Pro',
 'ja': 'Chrome 拡張機能 0.4.9 &middot; Kapture Pro'},

'<p class="kicker">Kapture for Chrome &middot; 0.4.9</p>': {
 'es': '<p class="kicker">Kapture para Chrome &middot; 0.4.9</p>',
 'zh': '<p class="kicker">Chrome 版 Kapture &middot; 0.4.9</p>',
 'ko': '<p class="kicker">Chrome용 Kapture &middot; 0.4.9</p>',
 'ja': '<p class="kicker">Chrome 版 Kapture &middot; 0.4.9</p>'},

'Kapture saves full webpages or selected areas straight from Chrome. Kapture Pro turns them into a searchable visual library on your desktop, with Projects, Collections and Smart to keep it organised. Everything stays local.': {
 'es': 'Kapture guarda páginas web completas o el área que elijas, directamente desde Chrome. Kapture Pro las convierte en una biblioteca visual con búsqueda en tu ordenador, con Proyectos, Colecciones e Inteligente para mantenerla en orden. Todo se queda en local.',
 'zh': 'Kapture 直接在 Chrome 里保存整张网页或你框选的区域。Kapture Pro 把它们变成电脑上一个可搜索的可视化图库，并用项目、收藏集和智能保持有序。一切都留在本地。',
 'ko': 'Kapture는 Chrome에서 바로 전체 웹페이지나 선택한 영역을 저장합니다. Kapture Pro는 그것들을 컴퓨터 안에서 검색 가능한 시각적 라이브러리로 만들고, 프로젝트와 컬렉션과 스마트로 정돈된 상태를 유지합니다. 모든 것이 기기 안에 남습니다.',
 'ja': 'Kapture は Chrome から直接、Web ページ全体や選んだ範囲を保存します。Kapture Pro はそれらをパソコン上の検索できるビジュアルライブラリに変え、プロジェクト・コレクション・スマートで整った状態に保ちます。すべてローカルのままです。'},

# The Projects item now draws the Projects / Collections distinction, so the
# whole control block is re-keyed; every other item keeps its approved wording.
'''        <li data-state="projects"><button type="button"><h3>Projects</h3><p>Folders inside Kapture become projects automatically. Projects are the work you are doing; Collections, in the Library, are things you want kept together.</p></button></li>
        <li data-state="search"><button type="button"><h3>Search</h3><p>Find a capture by name, site or project without opening Finder.</p></button></li>
        <li data-state="library"><button type="button"><h3>Visual library</h3><p>Browse everything as previews instead of filenames.</p></button></li>
        <li data-state="inspector"><button type="button"><h3>Inspector</h3><p>Size, format, source and capture time for whatever you select.</p></button></li>
        <li data-state="tags"><button type="button"><h3>Tags and notes</h3><p>Add your own context so a capture still makes sense later.</p></button></li>
        <li data-state="storage"><button type="button"><h3>Local storage</h3><p>No cloud, no sync, no account. It reads the disk you already have.</p></button></li>''': {
 'es': '''        <li data-state="projects"><button type="button"><h3>Proyectos</h3><p>Las carpetas dentro de Kapture se convierten en proyectos automáticamente. Los proyectos son el trabajo que tienes entre manos; las colecciones, dentro de la biblioteca, son las cosas que quieres mantener juntas.</p></button></li>
        <li data-state="search"><button type="button"><h3>Búsqueda</h3><p>Encuentra una captura por nombre, sitio o proyecto sin abrir el Finder.</p></button></li>
        <li data-state="library"><button type="button"><h3>Biblioteca visual</h3><p>Navega con vistas previas en lugar de nombres de archivo.</p></button></li>
        <li data-state="inspector"><button type="button"><h3>Inspector</h3><p>Tamaño, formato, origen y hora de captura de lo que selecciones.</p></button></li>
        <li data-state="tags"><button type="button"><h3>Etiquetas y notas</h3><p>Añade tu propio contexto para que una captura siga teniendo sentido.</p></button></li>
        <li data-state="storage"><button type="button"><h3>Todo en local</h3><p>Sin nube, sin sincronización, sin cuenta. Lee el disco que ya tienes.</p></button></li>''',
 'zh': '''        <li data-state="projects"><button type="button"><h3>项目</h3><p>Kapture 文件夹里的子文件夹会自动变成项目。项目是你正在做的事；收藏集在图库里，是你想放在一起的东西。</p></button></li>
        <li data-state="search"><button type="button"><h3>搜索</h3><p>不用打开访达，按名称、网站或项目就能找到截图。</p></button></li>
        <li data-state="library"><button type="button"><h3>可视化图库</h3><p>用预览图浏览一切，而不是一串文件名。</p></button></li>
        <li data-state="inspector"><button type="button"><h3>检查器</h3><p>选中任意一张，就能看到尺寸、格式、来源和截图时间。</p></button></li>
        <li data-state="tags"><button type="button"><h3>标签与备注</h3><p>加上自己的说明，过段时间再看也知道这张是什么。</p></button></li>
        <li data-state="storage"><button type="button"><h3>本地存储</h3><p>没有云端，不用同步，不用账号。它读的就是你现有的硬盘。</p></button></li>''',
 'ko': '''        <li data-state="projects"><button type="button"><h3>프로젝트</h3><p>Kapture 폴더 안의 폴더는 자동으로 프로젝트가 됩니다. 프로젝트는 지금 하고 있는 일이고, 라이브러리 안의 컬렉션은 함께 두고 싶은 것들입니다.</p></button></li>
        <li data-state="search"><button type="button"><h3>검색</h3><p>Finder를 열지 않고도 이름, 사이트, 프로젝트로 캡처를 찾습니다.</p></button></li>
        <li data-state="library"><button type="button"><h3>시각 라이브러리</h3><p>파일 이름이 아니라 미리보기로 전체를 훑어봅니다.</p></button></li>
        <li data-state="inspector"><button type="button"><h3>인스펙터</h3><p>고른 항목의 크기, 형식, 출처, 캡처 시각을 바로 확인합니다.</p></button></li>
        <li data-state="tags"><button type="button"><h3>태그와 메모</h3><p>직접 맥락을 남겨 두면 나중에 봐도 무슨 캡처인지 압니다.</p></button></li>
        <li data-state="storage"><button type="button"><h3>로컬 저장</h3><p>클라우드도, 동기화도, 계정도 없습니다. 이미 있는 디스크를 읽을 뿐입니다.</p></button></li>''',
 'ja': '''        <li data-state="projects"><button type="button"><h3>プロジェクト</h3><p>Kapture のなかのフォルダーは自動的にプロジェクトになります。プロジェクトは今やっている仕事、ライブラリのなかのコレクションはまとめておきたいものです。</p></button></li>
        <li data-state="search"><button type="button"><h3>検索</h3><p>Finder を開かずに、名前・サイト・プロジェクトから探せます。</p></button></li>
        <li data-state="library"><button type="button"><h3>ビジュアルライブラリ</h3><p>ファイル名ではなくプレビューで全体を見渡せます。</p></button></li>
        <li data-state="inspector"><button type="button"><h3>インスペクタ</h3><p>選んだものの大きさ、形式、取得元、撮影日時をその場で確認できます。</p></button></li>
        <li data-state="tags"><button type="button"><h3>タグとメモ</h3><p>自分で文脈を書き添えておけば、後から見ても用途がわかります。</p></button></li>
        <li data-state="storage"><button type="button"><h3>ローカル保存</h3><p>クラウドも同期もアカウントも不要。手元のディスクを読むだけです。</p></button></li>'''},

}
