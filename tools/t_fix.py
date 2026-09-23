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

'''          <span data-for="full">Full page is selected.</span>
          <span data-for="scan">Capture page scrolls the whole document.</span>
          <span data-for="kept">Saved to your project, split at 8,000&nbsp;pixels.</span>
          <span data-for="area">Switch the panel to Select area.</span>
          <span data-for="draw">Drag over the part you actually need.</span>
          <span data-for="crop">Only that region is captured.</span>''': {
 'es': '''          <span data-for="full">Full page está seleccionado.</span>
          <span data-for="scan">Capture page recorre el documento entero.</span>
          <span data-for="kept">Se guarda en tu proyecto, en secciones de 8.000&nbsp;píxeles.</span>
          <span data-for="area">Cambia el panel a Select area.</span>
          <span data-for="draw">Arrastra sobre la parte que de verdad necesitas.</span>
          <span data-for="crop">Solo se captura esa zona.</span>''',
 'zh': '''          <span data-for="full">已选中 Full page。</span>
          <span data-for="scan">Capture page 会滚动整个文档。</span>
          <span data-for="kept">保存到你的项目，按 8,000&nbsp;像素分段。</span>
          <span data-for="area">把面板切换到 Select area。</span>
          <span data-for="draw">在页面上拖出你真正需要的部分。</span>
          <span data-for="crop">只有这块区域会被截取。</span>''',
 'ko': '''          <span data-for="full">Full page가 선택되어 있습니다.</span>
          <span data-for="scan">Capture page가 문서 전체를 스크롤합니다.</span>
          <span data-for="kept">프로젝트에 저장되며 8,000&nbsp;픽셀 단위로 나뉩니다.</span>
          <span data-for="area">패널을 Select area로 바꿉니다.</span>
          <span data-for="draw">실제로 필요한 부분만 드래그합니다.</span>
          <span data-for="crop">그 영역만 캡처됩니다.</span>''',
 'ja': '''          <span data-for="full">Full page が選ばれています。</span>
          <span data-for="scan">Capture page がドキュメント全体をスクロールします。</span>
          <span data-for="kept">プロジェクトに保存され、8,000&nbsp;ピクセルごとに分割されます。</span>
          <span data-for="area">パネルを Select area に切り替えます。</span>
          <span data-for="draw">本当に必要な部分をドラッグします。</span>
          <span data-for="crop">その範囲だけが撮られます。</span>'''},

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

'<li data-mode="full"><h3>Full page</h3><p>Kapture scrolls the page from top to bottom and saves the complete webpage.</p></li>': {
 'es': '<li data-mode="full"><h3>Página completa</h3><p>Kapture recorre la página de arriba abajo y guarda la web entera.</p></li>',
 'zh': '<li data-mode="full"><h3>整页截取</h3><p>Kapture 从上到下滚动页面，保存完整的网页。</p></li>',
 'ko': '<li data-mode="full"><h3>전체 페이지</h3><p>Kapture가 페이지를 위에서 아래까지 스크롤해 웹페이지 전체를 저장합니다.</p></li>',
 'ja': '<li data-mode="full"><h3>ページ全体</h3><p>Kapture がページを上から下までスクロールし、Web ページ全体を保存します。</p></li>'},

'<li data-mode="area"><h3>Select area</h3><p>Draw over exactly what you need and save only that part.</p></li>': {
 'es': '<li data-mode="area"><h3>Selecciona un área</h3><p>Dibuja justo sobre lo que necesitas y guarda solo esa parte.</p></li>',
 'zh': '<li data-mode="area"><h3>框选区域</h3><p>在你真正需要的地方拖出选框，只保存那一部分。</p></li>',
 'ko': '<li data-mode="area"><h3>영역 선택</h3><p>필요한 부분만 정확히 드래그해서 그 부분만 저장합니다.</p></li>',
 'ja': '<li data-mode="area"><h3>範囲を選ぶ</h3><p>必要なところだけをドラッグして、その部分だけを保存します。</p></li>'},

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
'<h2>Two products.<br><span class="accent">One workflow.</span></h2>': {
 'es': '<h2>Dos productos.<br><span class="accent">Un mismo flujo.</span></h2>',
 'zh': '<h2>两款产品，<br><span class="accent">一套流程。</span></h2>',
 'ko': '<h2>두 개의 제품,<br><span class="accent">하나의 흐름.</span></h2>',
 'ja': '<h2>2 つのプロダクト、<br><span class="accent">ひとつの流れ。</span></h2>'},

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

}
