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
 'ja': '''               alt="Chrome で開いた Web ページを Kapture が撮っているところ。"''',
 'de': '               alt="Eine in Chrome geöffnete Webseite, die von Kapture aufgenommen wird."',
 'fr': '               alt="Une page web ouverte dans Chrome, en cours de capture par Kapture."',
 'pt-br': '               alt="Uma página da web aberta no Chrome, sendo capturada pelo Kapture."',
 'it': '               alt="Una pagina web aperta in Chrome, mentre viene catturata da Kapture."'},

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
 'ja': '<p class="plan-note">価格は未確定です。買い切りで、サブスクリプションはありません。</p>',
 'de': '<p class="plan-note">Der Preis steht noch nicht fest. Einmalzahlung, kein Abo.</p>',
 'fr': '<p class="plan-note">Le prix n\'est pas définitif. Un seul paiement, sans abonnement.</p>',
 'pt-br': '<p class="plan-note">O preço ainda não é definitivo. Pagamento único, sem assinatura.</p>',
 'it': '<p class="plan-note">Il prezzo non è definitivo. Pagamento unico, nessun abbonamento.</p>'},

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
 'ja': '<p class="section-lead">Web ページ全体を撮るか、必要な範囲だけを選びます。PNG、JPEG、PDF でローカルに保存できます。</p>',
 'de': '<p class="section-lead">Nimm eine komplette Webseite auf, oder wähle genau den Bereich, den du brauchst. Speichere ihn lokal als PNG, JPEG oder PDF.</p>',
 'fr': '<p class="section-lead">Capturez une page web entière, ou sélectionnez exactement la zone qu\'il vous faut. Enregistrez-la en local en PNG, JPEG ou PDF.</p>',
 'pt-br': '<p class="section-lead">Capture uma página da web inteira ou selecione exatamente a área que você precisa. Salve localmente em PNG, JPEG ou PDF.</p>',
 'it': '<p class="section-lead">Cattura una pagina web intera, oppure seleziona esattamente l\'area che ti serve. Salvala in locale in PNG, JPEG o PDF.</p>'},

'<li data-mode="full"><h3>Full page</h3><p>Save the whole page to your project. Long pages split at 8,000&nbsp;pixels.</p></li>': {
 'es': '<li data-mode="full"><h3>Página completa</h3><p>Guarda la página entera en tu proyecto. Las páginas largas se dividen cada 8.000&nbsp;píxeles.</p></li>',
 'zh': '<li data-mode="full"><h3>整页截取</h3><p>把整张网页保存到你的项目里。过长的页面按 8,000&nbsp;像素分段。</p></li>',
 'ko': '<li data-mode="full"><h3>전체 페이지</h3><p>페이지 전체를 프로젝트에 저장합니다. 긴 페이지는 8,000&nbsp;픽셀 단위로 나뉩니다.</p></li>',
 'ja': '<li data-mode="full"><h3>ページ全体</h3><p>ページ全体をプロジェクトに保存します。長いページは 8,000&nbsp;ピクセルごとに分割されます。</p></li>',
 'de': '<li data-mode="full"><h3>Ganze Seite</h3><p>Sichere die ganze Seite in dein Projekt. Lange Seiten werden bei 8.000&nbsp;Pixeln geteilt.</p></li>',
 'fr': '<li data-mode="full"><h3>Page entière</h3><p>Enregistrez toute la page dans votre projet. Les pages longues sont coupées tous les 8&nbsp;000&nbsp;pixels.</p></li>',
 'pt-br': '<li data-mode="full"><h3>Página inteira</h3><p>Salve a página toda no seu projeto. Páginas longas são divididas a cada 8.000&nbsp;pixels.</p></li>',
 'it': '<li data-mode="full"><h3>Pagina intera</h3><p>Salva tutta la pagina nel tuo progetto. Le pagine lunghe vengono divise ogni 8.000&nbsp;pixel.</p></li>'},

'<li data-mode="area"><h3>Select area</h3><p>Draw over exactly what you need. Save only that region.</p></li>': {
 'es': '<li data-mode="area"><h3>Selecciona un área</h3><p>Dibuja justo sobre lo que necesitas. Guarda solo esa zona.</p></li>',
 'zh': '<li data-mode="area"><h3>框选区域</h3><p>在你需要的地方拖出选框。只保存那一块区域。</p></li>',
 'ko': '<li data-mode="area"><h3>영역 선택</h3><p>필요한 부분만 정확히 드래그하세요. 그 영역만 저장됩니다.</p></li>',
 'ja': '<li data-mode="area"><h3>範囲を選ぶ</h3><p>必要なところだけをドラッグ。その範囲だけを保存します。</p></li>',
 'de': '<li data-mode="area"><h3>Bereich wählen</h3><p>Zieh genau über das, was du brauchst. Nur dieser Ausschnitt wird gespeichert.</p></li>',
 'fr': '<li data-mode="area"><h3>Sélectionner une zone</h3><p>Tracez exactement ce qu\'il vous faut. Seule cette zone est enregistrée.</p></li>',
 'pt-br': '<li data-mode="area"><h3>Selecionar área</h3><p>Arraste sobre exatamente o que você precisa. Só essa região é salva.</p></li>',
 'it': '<li data-mode="area"><h3>Seleziona area</h3><p>Trascina su esattamente ciò che ti serve. Viene salvata solo quella porzione.</p></li>'},

'<h2>Built for the screenshot<br>you actually needed.</h2>': {
 'es': '<h2>Hecho para la captura<br>que de verdad necesitabas.</h2>',
 'zh': '<h2>为你真正需要的<br>那张截图而做。</h2>',
 'ko': '<h2>정말 필요했던<br>그 스크린샷을 위해.</h2>',
 'ja': '<h2>本当に必要だった<br>その一枚のために。</h2>',
 'de': '<h2>Gemacht für den Screenshot,<br>den du wirklich brauchtest.</h2>',
 'fr': '<h2>Pensé pour la capture<br>dont vous aviez vraiment besoin.</h2>',
 'pt-br': '<h2>Feito para a captura<br>que você realmente precisava.</h2>',
 'it': '<h2>Fatto per lo screenshot<br>che ti serviva davvero.</h2>'},

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
 'ja': '<h2>ひとつの流れ。<br><span class="accent">どこで撮っても。</span></h2>',
 'de': '<h2>Ein Ablauf.<br><span class="accent">Wo immer du aufnimmst.</span></h2>',
 'fr': '<h2>Un seul flux.<br><span class="accent">Où que vous captiez.</span></h2>',
 'pt-br': '<h2>Um só fluxo.<br><span class="accent">Onde quer que você capture.</span></h2>',
 'it': '<h2>Un solo flusso.<br><span class="accent">Ovunque tu catturi.</span></h2>'},

# The pricing labels became .kicker eyebrows above the product titles.
'<p class="kicker plan-price">Free</p>': {
 'es': '<p class="kicker plan-price">Gratis</p>', 'zh': '<p class="kicker plan-price">免费</p>',
 'ko': '<p class="kicker plan-price">무료</p>', 'ja': '<p class="kicker plan-price">無料</p>',
 'de': '<p class="kicker plan-price">Gratis</p>',
 'fr': '<p class="kicker plan-price">Gratuit</p>',
 'pt-br': '<p class="kicker plan-price">Grátis</p>',
 'it': '<p class="kicker plan-price">Gratis</p>'},

'<p class="kicker plan-price">One-time purchase</p>': {
 'es': '<p class="kicker plan-price">Pago único</p>', 'zh': '<p class="kicker plan-price">一次性买断</p>',
 'ko': '<p class="kicker plan-price">1회 구매</p>', 'ja': '<p class="kicker plan-price">買い切り</p>',
 'de': '<p class="kicker plan-price">Einmalkauf</p>',
 'fr': '<p class="kicker plan-price">Achat unique</p>',
 'pt-br': '<p class="kicker plan-price">Compra única</p>',
 'it': '<p class="kicker plan-price">Acquisto unico</p>'},

# ---------------------------------------------------------------- the two products together
# Product names follow the form the rest of the site already uses in each
# language (Kapture para Chrome, Mac 版 Kapture Pro), so this section reads
# consistently with the footer plans rather than switching to English mid-page.
'<p class="kicker">The Kapture workflow</p>': {
 'es': '<p class="kicker">El flujo de Kapture</p>',
 'zh': '<p class="kicker">Kapture 工作流</p>',
 'ko': '<p class="kicker">Kapture 워크플로</p>',
 'ja': '<p class="kicker">Kapture のワークフロー</p>',
 'de': '<p class="kicker">Der Kapture-Ablauf</p>',
 'fr': '<p class="kicker">Le flux Kapture</p>',
 'pt-br': '<p class="kicker">O fluxo do Kapture</p>',
 'it': '<p class="kicker">Il flusso di Kapture</p>'},

'<h2>Kapture, Kapture Pro,<br>or both?</h2>': {
 'es': '<h2>¿Kapture, Kapture Pro<br>o los dos?</h2>',
 'zh': '<h2>Kapture、Kapture Pro，<br>还是两个一起用？</h2>',
 'ko': '<h2>Kapture, Kapture Pro,<br>아니면 둘 다?</h2>',
 'ja': '<h2>Kapture、Kapture Pro、<br>それとも両方？</h2>',
 'de': '<h2>Kapture, Kapture Pro<br>oder beides?</h2>',
 'fr': '<h2>Kapture, Kapture Pro,<br>ou les deux&nbsp;?</h2>',
 'pt-br': '<h2>Kapture, Kapture Pro<br>ou os dois?</h2>',
 'it': '<h2>Kapture, Kapture Pro<br>o entrambi?</h2>'},

'<p class="section-lead">Kapture handles capture in Chrome. Kapture Pro organises everything on your Mac. See what each product does on its own and what they unlock together.</p>': {
 'es': '<p class="section-lead">Kapture se encarga de capturar en Chrome. Kapture Pro lo organiza todo en tu Mac. Mira lo que hace cada uno por separado y lo que consigues con los dos.</p>',
 'zh': '<p class="section-lead">Kapture 负责在 Chrome 里截图，Kapture Pro 负责在 Mac 上整理。看看每个产品单独能做什么，以及两个一起用能带来什么。</p>',
 'ko': '<p class="section-lead">Kapture는 Chrome에서 캡처하고, Kapture Pro는 Mac에서 정리합니다. 각 제품이 따로 할 수 있는 일과, 둘을 함께 썼을 때 열리는 것들을 살펴보세요.</p>',
 'ja': '<p class="section-lead">Kapture は Chrome で撮り、Kapture Pro は Mac で整理します。それぞれが単体でできることと、両方そろって初めてできることをご覧ください。</p>'},

# ---- column headers ----
'<th scope="col">Feature</th>': {
 'es': '<th scope="col">Función</th>', 'zh': '<th scope="col">功能</th>',
 'ko': '<th scope="col">기능</th>', 'ja': '<th scope="col">機能</th>',
 'de': '<th scope="col">Funktion</th>',
 'fr': '<th scope="col">Fonction</th>',
 'pt-br': '<th scope="col">Recurso</th>',
 'it': '<th scope="col">Funzione</th>'},

'<th scope="col">Kapture for Chrome</th>': {
 'es': '<th scope="col">Kapture para Chrome</th>', 'zh': '<th scope="col">Chrome 版 Kapture</th>',
 'ko': '<th scope="col">Chrome용 Kapture</th>', 'ja': '<th scope="col">Chrome 版 Kapture</th>',
 'de': '<th scope="col">Kapture für Chrome</th>',
 'fr': '<th scope="col">Kapture pour Chrome</th>',
 'pt-br': '<th scope="col">Kapture para Chrome</th>',
 'it': '<th scope="col">Kapture per Chrome</th>'},

'<th scope="col">Kapture Pro for Mac</th>': {
 'es': '<th scope="col">Kapture Pro para Mac</th>', 'zh': '<th scope="col">Mac 版 Kapture Pro</th>',
 'ko': '<th scope="col">Mac용 Kapture Pro</th>', 'ja': '<th scope="col">Mac 版 Kapture Pro</th>'},

'<th scope="col" class="is-both">Together</th>': {
 'es': '<th scope="col" class="is-both">Juntos</th>', 'zh': '<th scope="col" class="is-both">一起用</th>',
 'ko': '<th scope="col" class="is-both">함께</th>', 'ja': '<th scope="col" class="is-both">両方</th>',
 'de': '<th scope="col" class="is-both">Zusammen</th>',
 'fr': '<th scope="col" class="is-both">Ensemble</th>',
 'pt-br': '<th scope="col" class="is-both">Juntos</th>',
 'it': '<th scope="col" class="is-both">Insieme</th>'},

# ---- row labels ----
'<th scope="row">Full-page capture</th>': {
 'es': '<th scope="row">Captura de página completa</th>', 'zh': '<th scope="row">整页截图</th>',
 'ko': '<th scope="row">전체 페이지 캡처</th>', 'ja': '<th scope="row">ページ全体の撮影</th>',
 'de': '<th scope="row">Ganzseiten-Aufnahme</th>',
 'fr': '<th scope="row">Capture de page entière</th>',
 'pt-br': '<th scope="row">Captura de página inteira</th>',
 'it': '<th scope="row">Cattura pagina intera</th>'},

'<th scope="row">Select-area capture</th>': {
 'es': '<th scope="row">Captura de un área</th>', 'zh': '<th scope="row">框选区域截图</th>',
 'ko': '<th scope="row">영역 선택 캡처</th>', 'ja': '<th scope="row">範囲を選んで撮影</th>',
 'de': '<th scope="row">Bereichsaufnahme</th>',
 'fr': '<th scope="row">Capture de zone</th>',
 'pt-br': '<th scope="row">Captura de área</th>',
 'it': '<th scope="row">Cattura di area</th>'},

'<th scope="row">PNG, JPEG or PDF</th>': {
 'es': '<th scope="row">PNG, JPEG o PDF</th>', 'zh': '<th scope="row">PNG、JPEG 或 PDF</th>',
 'ko': '<th scope="row">PNG, JPEG, PDF</th>', 'ja': '<th scope="row">PNG・JPEG・PDF</th>',
 'de': '<th scope="row">PNG, JPEG oder PDF</th>',
 'fr': '<th scope="row">PNG, JPEG ou PDF</th>',
 'pt-br': '<th scope="row">PNG, JPEG ou PDF</th>',
 'it': '<th scope="row">PNG, JPEG o PDF</th>'},

'<th scope="row">Save locally</th>': {
 'es': '<th scope="row">Guardado en local</th>', 'zh': '<th scope="row">保存到本地</th>',
 'ko': '<th scope="row">로컬 저장</th>', 'ja': '<th scope="row">ローカルに保存</th>',
 'de': '<th scope="row">Lokal speichern</th>',
 'fr': '<th scope="row">Enregistrement local</th>',
 'pt-br': '<th scope="row">Salvar localmente</th>',
 'it': '<th scope="row">Salvataggio in locale</th>'},

'<th scope="row">Visual screenshot library</th>': {
 'es': '<th scope="row">Biblioteca visual de capturas</th>', 'zh': '<th scope="row">可视化截图图库</th>',
 'ko': '<th scope="row">시각적 스크린샷 라이브러리</th>', 'ja': '<th scope="row">ビジュアルなスクリーンショット一覧</th>',
 'de': '<th scope="row">Visuelle Screenshot-Bibliothek</th>',
 'fr': '<th scope="row">Bibliothèque visuelle de captures</th>',
 'pt-br': '<th scope="row">Biblioteca visual de capturas</th>',
 'it': '<th scope="row">Libreria visiva degli screenshot</th>'},

'<th scope="row">Project &amp; collection management</th>': {
 'es': '<th scope="row">Gestión de proyectos y colecciones</th>', 'zh': '<th scope="row">项目与合集管理</th>',
 'ko': '<th scope="row">프로젝트 및 컬렉션 관리</th>', 'ja': '<th scope="row">プロジェクトとコレクションの管理</th>',
 'de': '<th scope="row">Projekt- und Sammlungsverwaltung</th>',
 'fr': '<th scope="row">Gestion des projets et collections</th>',
 'pt-br': '<th scope="row">Gestão de projetos e coleções</th>',
 'it': '<th scope="row">Gestione di progetti e raccolte</th>'},

'<th scope="row">Search and filters</th>': {
 'es': '<th scope="row">Búsqueda y filtros</th>', 'zh': '<th scope="row">搜索与筛选</th>',
 'ko': '<th scope="row">검색과 필터</th>', 'ja': '<th scope="row">検索とフィルター</th>',
 'de': '<th scope="row">Suche und Filter</th>',
 'fr': '<th scope="row">Recherche et filtres</th>',
 'pt-br': '<th scope="row">Busca e filtros</th>',
 'it': '<th scope="row">Ricerca e filtri</th>'},

'<th scope="row">Tags and notes</th>': {
 'es': '<th scope="row">Etiquetas y notas</th>', 'zh': '<th scope="row">标签与备注</th>',
 'ko': '<th scope="row">태그와 메모</th>', 'ja': '<th scope="row">タグとメモ</th>',
 'de': '<th scope="row">Tags und Notizen</th>',
 'fr': '<th scope="row">Étiquettes et notes</th>',
 'pt-br': '<th scope="row">Etiquetas e notas</th>',
 'it': '<th scope="row">Tag e note</th>'},

'<th scope="row">File inspector</th>': {
 'es': '<th scope="row">Inspector de archivos</th>', 'zh': '<th scope="row">文件信息面板</th>',
 'ko': '<th scope="row">파일 인스펙터</th>', 'ja': '<th scope="row">ファイルインスペクタ</th>',
 'de': '<th scope="row">Datei-Inspektor</th>',
 'fr': '<th scope="row">Inspecteur de fichiers</th>',
 'pt-br': '<th scope="row">Inspetor de arquivos</th>',
 'it': '<th scope="row">Ispettore file</th>'},

'<th scope="row">Capture to organise workflow</th>': {
 'es': '<th scope="row">Flujo de captura a organización</th>', 'zh': '<th scope="row">从截图到整理的完整流程</th>',
 'ko': '<th scope="row">캡처에서 정리까지의 흐름</th>', 'ja': '<th scope="row">撮影から整理までの流れ</th>',
 'de': '<th scope="row">Vom Aufnehmen zum Ordnen</th>',
 'fr': '<th scope="row">De la capture au rangement</th>',
 'pt-br': '<th scope="row">Da captura à organização</th>',
 'it': '<th scope="row">Dalla cattura all\'organizzazione</th>'},

# ---- the marks' accessible names (replaced everywhere they appear) ----
'aria-label="Yes"': {
 'es': 'aria-label="Sí"', 'zh': 'aria-label="支持"',
 'ko': 'aria-label="지원"', 'ja': 'aria-label="対応"',
 'de': 'aria-label="Ja"',
 'fr': 'aria-label="Oui"',
 'pt-br': 'aria-label="Sim"',
 'it': 'aria-label="Sì"'},

'aria-label="No"': {
 'es': 'aria-label="No"', 'zh': 'aria-label="不支持"',
 'ko': 'aria-label="미지원"', 'ja': 'aria-label="非対応"',
 'de': 'aria-label="Nein"',
 'fr': 'aria-label="Non"',
 'pt-br': 'aria-label="Não"',
 'it': 'aria-label="No"'},

# ---------------------------------------------------------------- Chrome headline
'<h2>Capture everything.<br>Or exactly one part of it.</h2>': {
 'es': '<h2>Captura todo.<br>O exactamente una parte.</h2>',
 'zh': '<h2>整页全都要，<br>或者只要其中一块。</h2>',
 'ko': '<h2>전부 담거나,<br>딱 필요한 부분만.</h2>',
 'ja': '<h2>すべてを撮る。<br>あるいは必要な一部だけ。</h2>',
 'de': '<h2>Nimm alles auf.<br>Oder genau einen Teil davon.</h2>',
 'fr': '<h2>Capturez tout.<br>Ou exactement une partie.</h2>',
 'pt-br': '<h2>Capture tudo.<br>Ou exatamente uma parte.</h2>',
 'it': '<h2>Cattura tutto.<br>O esattamente una parte.</h2>'},


# ---------------------------------------------------------------- figure caption
# Static and visually hidden: it names the figure for assistive technology and
# is never re-announced as the phases cycle.
'<figcaption class="cap-caption">Kapture running in Chrome: first a full page capture, then an area drawn on the same page.</figcaption>': {
 'es': '<figcaption class="cap-caption">Kapture funcionando en Chrome: primero una captura de la página completa y después un área dibujada sobre esa misma página.</figcaption>',
 'zh': '<figcaption class="cap-caption">Kapture 在 Chrome 中运行：先截取整张网页，再在同一页面上框选一块区域。</figcaption>',
 'ko': '<figcaption class="cap-caption">Chrome에서 실행 중인 Kapture: 먼저 전체 페이지를 캡처하고, 이어서 같은 페이지에서 영역을 드래그합니다.</figcaption>',
 'ja': '<figcaption class="cap-caption">Chrome で動く Kapture。まずページ全体を撮り、続いて同じページ上で範囲を選びます。</figcaption>',
 'de': '<figcaption class="cap-caption">Kapture in Chrome: erst eine Ganzseiten-Aufnahme, dann ein Bereich auf derselben Seite.</figcaption>',
 'fr': '<figcaption class="cap-caption">Kapture dans Chrome&nbsp;: d\'abord une capture de page entière, puis une zone tracée sur la même page.</figcaption>',
 'pt-br': '<figcaption class="cap-caption">Kapture no Chrome: primeiro uma captura de página inteira, depois uma área desenhada na mesma página.</figcaption>',
 'it': '<figcaption class="cap-caption">Kapture in Chrome: prima una cattura di pagina intera, poi un\'area tracciata sulla stessa pagina.</figcaption>'},

# ---------------------------------------------------------------- Windows platform
# Same product as the Mac build, second platform, same unreleased state.
'aria-label="Kapture Pro for Windows. Coming soon."': {
 'es': 'aria-label="Kapture Pro para Windows. Muy pronto."',
 'zh': 'aria-label="Windows 版 Kapture Pro。即将推出。"',
 'ko': 'aria-label="Windows용 Kapture Pro. 곧 출시됩니다."',
 'ja': 'aria-label="Windows 版 Kapture Pro。近日公開。"',
 'de': 'aria-label="Kapture Pro für Windows. Demnächst."',
 'fr': 'aria-label="Kapture Pro pour Windows. Bientôt disponible."',
 'pt-br': 'aria-label="Kapture Pro para Windows. Em breve."',
 'it': 'aria-label="Kapture Pro per Windows. Presto disponibile."'},

'<span class="store-cta-label">Pro for Mac</span>': {
 'es': '<span class="store-cta-label">Pro para Mac</span>',
 'zh': '<span class="store-cta-label">Mac 版 Pro</span>',
 'ko': '<span class="store-cta-label">Mac용 Pro</span>',
 'ja': '<span class="store-cta-label">Mac 版 Pro</span>',
 'de': '<span class="store-cta-label">Pro für Mac</span>',
 'fr': '<span class="store-cta-label">Pro pour Mac</span>',
 'pt-br': '<span class="store-cta-label">Pro para Mac</span>',
 'it': '<span class="store-cta-label">Pro per Mac</span>'},

'<span class="store-cta-label">Pro for Windows</span>': {
 'es': '<span class="store-cta-label">Pro para Windows</span>',
 'zh': '<span class="store-cta-label">Windows 版 Pro</span>',
 'ko': '<span class="store-cta-label">Windows용 Pro</span>',
 'ja': '<span class="store-cta-label">Windows 版 Pro</span>',
 'de': '<span class="store-cta-label">Pro für Windows</span>',
 'fr': '<span class="store-cta-label">Pro pour Windows</span>',
 'pt-br': '<span class="store-cta-label">Pro para Windows</span>',
 'it': '<span class="store-cta-label">Pro per Windows</span>'},

'<h3>Kapture<br>for Chrome</h3>': {
 'es': '<h3>Kapture<br>para Chrome</h3>',
 'zh': '<h3>Kapture<br>Chrome 版</h3>',
 'ko': '<h3>Kapture<br>Chrome용</h3>',
 'ja': '<h3>Kapture<br>Chrome 版</h3>',
 'de': '<h3>Kapture<br>für Chrome</h3>',
 'fr': '<h3>Kapture<br>pour Chrome</h3>',
 'pt-br': '<h3>Kapture<br>para Chrome</h3>',
 'it': '<h3>Kapture<br>per Chrome</h3>'},

'<h3>Kapture Pro<br>for Mac</h3>': {
 'es': '<h3>Kapture Pro<br>para Mac</h3>',
 'zh': '<h3>Kapture Pro<br>Mac 版</h3>',
 'ko': '<h3>Kapture Pro<br>Mac용</h3>',
 'ja': '<h3>Kapture Pro<br>Mac 版</h3>',
 'de': '<h3>Kapture Pro<br>für Mac</h3>',
 'fr': '<h3>Kapture Pro<br>pour Mac</h3>',
 'pt-br': '<h3>Kapture Pro<br>para Mac</h3>',
 'it': '<h3>Kapture Pro<br>per Mac</h3>'},

'<h3>Kapture Pro<br>for Windows</h3>': {
 'es': '<h3>Kapture Pro<br>para Windows</h3>',
 'zh': '<h3>Kapture Pro<br>Windows 版</h3>',
 'ko': '<h3>Kapture Pro<br>Windows용</h3>',
 'ja': '<h3>Kapture Pro<br>Windows 版</h3>',
 'de': '<h3>Kapture Pro<br>für Windows</h3>',
 'fr': '<h3>Kapture Pro<br>pour Windows</h3>',
 'pt-br': '<h3>Kapture Pro<br>para Windows</h3>',
 'it': '<h3>Kapture Pro<br>per Windows</h3>'},

# ---------------------------------------------------------------- company credit
'<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; A <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a> product</p>': {
 'es': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; Un producto de <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a></p>',
 'zh': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a> 出品</p>',
 'ko': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a> 제품</p>',
 'ja': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a> のプロダクト</p>',
 'de': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; Ein Produkt von <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a></p>',
 'fr': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; Un produit <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a></p>',
 'pt-br': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; Um produto <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a></p>',
 'it': '<p class="copyright">&copy; <span id="year">2026</span> Kapture &middot; Un prodotto <a href="https://kumo.studio" target="_blank" rel="noopener noreferrer">Kumo Studio</a></p>'},

# ---------------------------------------------------------------- platform-neutral positioning
# Kapture Pro is one product on two desktop platforms, so the general copy no
# longer names Mac. "Desktop" becomes the everyday word for a personal computer
# in each language, never the Desktop folder.
'<title>Kapture: Capture in Chrome, organise on your desktop</title>': {
 'es': '<title>Kapture: captura en Chrome, organiza en tu ordenador</title>',
 'zh': '<title>Kapture：在 Chrome 截图，在电脑上整理</title>',
 'ko': '<title>Kapture: Chrome에서 캡처하고 컴퓨터에서 정리하세요</title>',
 'ja': '<title>Kapture：Chrome で撮って、パソコンで整理する</title>',
 'de': '<title>Kapture: in Chrome aufnehmen, auf dem Desktop ordnen</title>',
 'fr': '<title>Kapture&nbsp;: capturez dans Chrome, rangez sur votre ordinateur</title>',
 'pt-br': '<title>Kapture: capture no Chrome, organize no computador</title>',
 'it': '<title>Kapture: cattura in Chrome, organizza sul desktop</title>'},

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
        <span class="accent">パソコンで整理する。</span>''',
 'de': '        In Chrome aufnehmen.<br>\n        <span class="accent">Auf dem Desktop ordnen.</span>',
 'fr': '        Capturez dans Chrome.<br>\n        <span class="accent">Rangez sur votre ordinateur.</span>',
 'pt-br': '        Capture no Chrome.<br>\n        <span class="accent">Organize no computador.</span>',
 'it': '        Cattura in Chrome.<br>\n        <span class="accent">Organizza sul desktop.</span>'},

# og:title and twitter:title carry the title without its tag. They were left in
# English before this pass; keying the bare string localises all three at once.
'Kapture: Capture in Chrome, organise on your desktop': {
 'es': 'Kapture: captura en Chrome, organiza en tu ordenador',
 'zh': 'Kapture：在 Chrome 截图，在电脑上整理',
 'ko': 'Kapture: Chrome에서 캡처하고 컴퓨터에서 정리하세요',
 'ja': 'Kapture：Chrome で撮って、パソコンで整理する',
 'de': 'Kapture: in Chrome aufnehmen, auf dem Desktop ordnen',
 'fr': 'Kapture : capturez dans Chrome, rangez sur votre ordinateur',
 'pt-br': 'Kapture: capture no Chrome, organize no computador',
 'it': 'Kapture: cattura in Chrome, organizza sul desktop'},

'<p class="hero-note">Requires Chrome 120 or later. Kapture for Chrome is free. Kapture Pro is coming soon for Mac and Windows.</p>': {
 'es': '<p class="hero-note">Requiere Chrome 120 o posterior. Kapture para Chrome es gratis. Kapture Pro llega pronto para Mac y Windows.</p>',
 'zh': '<p class="hero-note">需要 Chrome 120 或更高版本。Chrome 版 Kapture 免费，Kapture Pro 即将推出 Mac 版和 Windows 版。</p>',
 'ko': '<p class="hero-note">Chrome 120 이상이 필요합니다. Chrome용 Kapture는 무료이고, Kapture Pro는 Mac과 Windows용으로 곧 출시됩니다.</p>',
 'ja': '<p class="hero-note">Chrome 120 以降が必要です。Chrome 版 Kapture は無料。Kapture Pro は Mac 版と Windows 版を近日公開予定です。</p>',
 'de': '<p class="hero-note">Erfordert Chrome 120 oder neuer. Kapture für Chrome ist gratis. Kapture Pro kommt demnächst für Mac und Windows.</p>',
 'fr': '<p class="hero-note">Nécessite Chrome 120 ou plus récent. Kapture pour Chrome est gratuit. Kapture Pro arrive bientôt pour Mac et Windows.</p>',
 'pt-br': '<p class="hero-note">Requer o Chrome 120 ou mais recente. O Kapture para Chrome é grátis. O Kapture Pro chega em breve para Mac e Windows.</p>',
 'it': '<p class="hero-note">Richiede Chrome 120 o successivo. Kapture per Chrome è gratis. Kapture Pro arriva presto per Mac e Windows.</p>'},

'<figcaption>The Chrome extension captures. The desktop app organises what it captures.</figcaption>': {
 'es': '<figcaption>La extensión de Chrome captura. La app de escritorio organiza lo capturado.</figcaption>',
 'zh': '<figcaption>Chrome 扩展负责截图，桌面应用负责整理这些截图。</figcaption>',
 'ko': '<figcaption>Chrome 확장 프로그램이 캡처하고, 데스크톱 앱이 그 캡처를 정리합니다.</figcaption>',
 'ja': '<figcaption>Chrome 拡張機能が撮り、デスクトップアプリがそれを整理します。</figcaption>',
 'de': '<figcaption>Die Chrome-Erweiterung nimmt auf. Die Desktop-App ordnet, was sie aufnimmt.</figcaption>',
 'fr': "<figcaption>L'extension Chrome capture. L'application de bureau range ce qu'elle capture.</figcaption>",
 'pt-br': '<figcaption>A extensão do Chrome captura. O aplicativo de desktop organiza o que foi capturado.</figcaption>',
 'it': "<figcaption>L'estensione di Chrome cattura. L'app desktop organizza ciò che cattura.</figcaption>"},

'''          Kapture Pro indexes the screenshots already on your computer and turns them into a
          searchable visual library. The files never move, never upload, never leave the disk.''': {
 'es': '''          Kapture Pro indexa las capturas que ya tienes en el ordenador y las convierte en una
          biblioteca visual con búsqueda. Los archivos no se mueven, no se suben, no salen del disco.''',
 'zh': '''          Kapture Pro 会索引你电脑上已有的截图，把它们变成一个可搜索的可视化图库。
          文件不会被移动，不会被上传，也不会离开硬盘。''',
 'ko': '''          Kapture Pro는 컴퓨터에 이미 있는 스크린샷을 색인해 검색 가능한 시각적 라이브러리로
          만듭니다. 파일은 옮겨지지도, 업로드되지도, 디스크를 벗어나지도 않습니다.''',
 'ja': '''          Kapture Pro はパソコンにすでにあるスクリーンショットを索引化し、検索できる
          ビジュアルライブラリにします。ファイルは移動せず、アップロードもされず、ディスクから出ません。''',
 'de': '          Kapture Pro indexiert die Screenshots, die schon auf deinem Rechner liegen, und macht\n          daraus eine durchsuchbare visuelle Bibliothek. Die Dateien wandern nicht, werden nie hochgeladen und verlassen die Platte nie.',
 'fr': '          Kapture Pro indexe les captures déjà présentes sur votre ordinateur et en fait une\n          bibliothèque visuelle interrogeable. Les fichiers ne bougent pas, ne partent jamais en ligne, ne quittent jamais le disque.',
 'pt-br': '          O Kapture Pro indexa as capturas que já estão no seu computador e as transforma em uma\n          biblioteca visual pesquisável. Os arquivos não saem do lugar, não sobem para lugar nenhum, não deixam o disco.',
 'it': '          Kapture Pro indicizza gli screenshot già presenti sul tuo computer e li trasforma in una\n          libreria visiva consultabile. I file non si spostano, non vengono mai caricati, non lasciano mai il disco.'},

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
            一切なく、どちらの製品もアカウント不要で、解析・広告・トラッキングも含まれていません。''',
 'de': '            Kapture erzeugt die Screenshots auf deinem Rechner und speichert sie über das eigene\n            Download-System von Chrome. Kapture Pro liest die Dateien, die schon auf deinem Rechner\n            liegen. Nichts wird hochgeladen, keines der beiden Produkte braucht ein Konto, und in\n            keinem steckt Analyse, Werbung oder Tracking.',
 'fr': "            Kapture crée les captures sur votre ordinateur et les enregistre via le système de\n            téléchargement de Chrome. Kapture Pro lit les fichiers déjà présents sur votre machine.\n            Rien n'est envoyé en ligne, aucun des deux produits ne demande de compte, et aucun ne\n            contient d'analyse, de publicité ni de suivi.",
 'pt-br': '            O Kapture cria as capturas no seu computador e as salva pelo próprio sistema de\n            downloads do Chrome. O Kapture Pro lê os arquivos que já estão no seu computador. Nada é\n            enviado para lugar nenhum, nenhum dos dois produtos precisa de conta, e nenhum tem\n            analytics, publicidade ou rastreamento.',
 'it': '            Kapture crea gli screenshot sul tuo computer e li salva tramite il sistema di download\n            di Chrome. Kapture Pro legge i file già presenti sul tuo computer. Nulla viene caricato,\n            nessuno dei due prodotti richiede un account e nessuno contiene analisi, pubblicità o\n            tracciamento.'},

'<figcaption>Captured in Chrome, kept on your computer.</figcaption>': {
 'es': '<figcaption>Capturado en Chrome, guardado en tu ordenador.</figcaption>',
 'zh': '<figcaption>在 Chrome 截图，留在你的电脑上。</figcaption>',
 'ko': '<figcaption>Chrome에서 캡처하고, 컴퓨터에 그대로 보관.</figcaption>',
 'ja': '<figcaption>Chrome で撮って、パソコンに置いたまま。</figcaption>',
 'de': '<figcaption>In Chrome aufgenommen, auf deinem Rechner geblieben.</figcaption>',
 'fr': '<figcaption>Capturé dans Chrome, gardé sur votre ordinateur.</figcaption>',
 'pt-br': '<figcaption>Capturado no Chrome, guardado no seu computador.</figcaption>',
 'it': '<figcaption>Catturato in Chrome, conservato sul tuo computer.</figcaption>'},

# ---------------------------------------------------------------- Smart
# Smart, its five tools and their names are the app's own approved terms from
# Localizable.xcstrings. Nothing here is translated for the first time.
'<p class="kicker">Smart</p>': {
 'es': '<p class="kicker">Inteligente</p>',
 'zh': '<p class="kicker">智能</p>',
 'ko': '<p class="kicker">스마트</p>',
 'ja': '<p class="kicker">スマート</p>',
 'de': '<p class="kicker">Smart</p>',
 'fr': '<p class="kicker">Smart</p>',
 'pt-br': '<p class="kicker">Smart</p>',
 'it': '<p class="kicker">Smart</p>'},

'<h2>Find what your library<br>has been hiding.</h2>': {
 'es': '<h2>Descubre lo que tu<br>biblioteca escondía.</h2>',
 'zh': '<h2>找出图库里<br>一直藏着的东西。</h2>',
 'ko': '<h2>라이브러리가 숨기고 있던<br>것을 찾아보세요.</h2>',
 'ja': '<h2>ライブラリが隠していた<br>ものを見つける。</h2>',
 'de': '<h2>Finde, was deine Bibliothek<br>bisher verborgen hat.</h2>',
 'fr': '<h2>Trouvez ce que votre bibliothèque<br>vous cachait.</h2>',
 'pt-br': '<h2>Descubra o que sua biblioteca<br>estava escondendo.</h2>',
 'it': '<h2>Scopri cosa nascondeva<br>la tua libreria.</h2>'},

'<p class="section-lead">Smart is one place in Kapture Pro with five tools. It shows you what still needs organising, which files are exact copies, what is worth a second look, where your captures came from, and the tidying you asked Kapture to do for you.</p>': {
 'es': '<p class="section-lead">Inteligente es un único lugar dentro de Kapture Pro con cinco herramientas. Te enseña lo que aún está sin organizar, qué archivos son copias exactas, qué merece un segundo vistazo, de dónde vienen tus capturas y el orden que le has pedido a Kapture que ponga por ti.</p>',
 'zh': '<p class="section-lead">智能是 Kapture Pro 里的一个地方，包含五个工具。它会告诉你哪些还没整理、哪些文件是完全相同的副本、哪些值得再看一眼、你的截图来自哪里，以及你让 Kapture 替你做的整理。</p>',
 'ko': '<p class="section-lead">스마트는 Kapture Pro 안의 한 곳으로, 다섯 가지 도구가 있습니다. 아직 정리가 필요한 것, 완전히 동일한 파일, 다시 살펴볼 만한 것, 캡처가 어디에서 왔는지, 그리고 Kapture에 맡긴 정리를 보여 줍니다.</p>',
 'ja': '<p class="section-lead">スマートは Kapture Pro のなかの一か所で、5 つのツールがあります。まだ整理が必要なもの、完全に同じファイル、見直す価値のあるもの、キャプチャの取得元、そして Kapture に依頼した整理を教えてくれます。</p>',
 'de': '<p class="section-lead">Smart ist ein Ort in Kapture Pro mit fünf Werkzeugen. Es zeigt dir, was noch zu ordnen ist, welche Dateien exakte Kopien sind, was einen zweiten Blick verdient, woher deine Aufnahmen stammen, und das Aufräumen, um das du Kapture gebeten hast.</p>',
 'fr': '<p class="section-lead">Smart est un seul endroit dans Kapture Pro, avec cinq outils. Il vous montre ce qui reste à ranger, quels fichiers sont des copies exactes, ce qui mérite un second regard, d\'où viennent vos captures, et le rangement que vous avez demandé à Kapture.</p>',
 'pt-br': '<p class="section-lead">O Smart é um lugar só dentro do Kapture Pro, com cinco ferramentas. Ele mostra o que ainda falta organizar, quais arquivos são cópias exatas, o que merece um segundo olhar, de onde vieram suas capturas e a arrumação que você pediu ao Kapture.</p>',
 'it': '<p class="section-lead">Smart è un unico posto dentro Kapture Pro, con cinque strumenti. Ti mostra cosa resta da organizzare, quali file sono copie esatte, cosa merita una seconda occhiata, da dove arrivano le tue catture e il riordino che hai chiesto a Kapture.</p>'},

'<li data-tool="unorganised"><button type="button"><h3>Unorganised</h3><p>Everything that is not in a project yet, from every source.</p></button></li>': {
 'es': '<li data-tool="unorganised"><button type="button"><h3>Sin organizar</h3><p>Todo lo que todavía no está en un proyecto, venga de donde venga.</p></button></li>',
 'zh': '<li data-tool="unorganised"><button type="button"><h3>未整理</h3><p>还没有归入项目的所有内容，涵盖所有来源。</p></button></li>',
 'ko': '<li data-tool="unorganised"><button type="button"><h3>미정리</h3><p>출처와 관계없이, 아직 프로젝트에 들어가지 않은 모든 것.</p></button></li>',
 'ja': '<li data-tool="unorganised"><button type="button"><h3>未整理</h3><p>まだプロジェクトに入っていないもの、すべてのソースから。</p></button></li>',
 'de': '<li data-tool="unorganised"><button type="button"><h3>Unsortiert</h3><p>Alles, was noch in keinem Projekt liegt, aus allen Quellen.</p></button></li>',
 'fr': '<li data-tool="unorganised"><button type="button"><h3>Non classées</h3><p>Tout ce qui n\'est pas encore dans un projet, quelle qu\'en soit la source.</p></button></li>',
 'pt-br': '<li data-tool="unorganised"><button type="button"><h3>Sem organizar</h3><p>Tudo o que ainda não está em um projeto, venha de onde vier.</p></button></li>',
 'it': '<li data-tool="unorganised"><button type="button"><h3>Non organizzate</h3><p>Tutto ciò che non è ancora in un progetto, da qualsiasi origine.</p></button></li>'},

'<li data-tool="duplicates"><button type="button"><h3>Duplicates</h3><p>Files that are exactly the same, byte for byte. You choose which copy to keep.</p></button></li>': {
 'es': '<li data-tool="duplicates"><button type="button"><h3>Duplicados</h3><p>Archivos exactamente iguales, byte a byte. Tú eliges qué copia se queda.</p></button></li>',
 'zh': '<li data-tool="duplicates"><button type="button"><h3>重复项</h3><p>逐字节完全相同的文件。由你决定保留哪一份。</p></button></li>',
 'ko': '<li data-tool="duplicates"><button type="button"><h3>중복 항목</h3><p>바이트 단위까지 완전히 같은 파일. 어떤 복사본을 남길지는 사용자가 정합니다.</p></button></li>',
 'ja': '<li data-tool="duplicates"><button type="button"><h3>重複</h3><p>バイト単位で完全に同じファイル。どちらを残すかはあなたが選びます。</p></button></li>',
 'de': '<li data-tool="duplicates"><button type="button"><h3>Duplikate</h3><p>Dateien, die Byte für Byte gleich sind. Du entscheidest, welche Kopie bleibt.</p></button></li>',
 'fr': '<li data-tool="duplicates"><button type="button"><h3>Doublons</h3><p>Des fichiers identiques octet pour octet. Vous choisissez la copie à garder.</p></button></li>',
 'pt-br': '<li data-tool="duplicates"><button type="button"><h3>Duplicadas</h3><p>Arquivos idênticos byte a byte. Você escolhe qual cópia fica.</p></button></li>',
 'it': '<li data-tool="duplicates"><button type="button"><h3>Duplicati</h3><p>File identici byte per byte. Scegli tu quale copia tenere.</p></button></li>'},

'<li data-tool="cleanup"><button type="button"><h3>Cleanup</h3><p>Older and larger captures worth a second look. Nothing is removed for you.</p></button></li>': {
 'es': '<li data-tool="cleanup"><button type="button"><h3>Limpieza</h3><p>Capturas antiguas y pesadas que merecen un segundo vistazo. Aquí no se elimina nada por ti.</p></button></li>',
 'zh': '<li data-tool="cleanup"><button type="button"><h3>清理</h3><p>值得再看一眼的旧截图和大文件。这里的内容不会替你移除。</p></button></li>',
 'ko': '<li data-tool="cleanup"><button type="button"><h3>정리</h3><p>다시 살펴볼 만한 오래되고 큰 캡처. 임의로 삭제되지는 않습니다.</p></button></li>',
 'ja': '<li data-tool="cleanup"><button type="button"><h3>クリーンアップ</h3><p>見直す価値のある古くて大きいキャプチャ。自動で削除されることはありません。</p></button></li>',
 'de': '<li data-tool="cleanup"><button type="button"><h3>Aufräumen</h3><p>Ältere und größere Aufnahmen, die einen zweiten Blick verdienen. Nichts wird für dich entfernt.</p></button></li>',
 'fr': '<li data-tool="cleanup"><button type="button"><h3>Nettoyage</h3><p>Des captures plus anciennes et plus lourdes, à revoir. Rien ne vous est supprimé.</p></button></li>',
 'pt-br': '<li data-tool="cleanup"><button type="button"><h3>Limpeza</h3><p>Capturas antigas e pesadas que merecem um segundo olhar. Nada é removido por você.</p></button></li>',
 'it': '<li data-tool="cleanup"><button type="button"><h3>Pulizia</h3><p>Catture più vecchie e più grandi da rivedere. Niente viene rimosso al posto tuo.</p></button></li>'},

'<li data-tool="sources"><button type="button"><h3>Sources</h3><p>Where your captures came from, grouped by site. Worked out locally.</p></button></li>': {
 'es': '<li data-tool="sources"><button type="button"><h3>Fuentes</h3><p>De dónde vienen tus capturas, agrupadas por sitio. Se calcula en local.</p></button></li>',
 'zh': '<li data-tool="sources"><button type="button"><h3>来源</h3><p>你的截图来自哪里，按网站分组。完全在本地算出。</p></button></li>',
 'ko': '<li data-tool="sources"><button type="button"><h3>출처</h3><p>캡처가 어디에서 왔는지, 사이트별로 묶어서. 기기 안에서 계산됩니다.</p></button></li>',
 'ja': '<li data-tool="sources"><button type="button"><h3>ソース</h3><p>キャプチャの取得元を、サイトごとにまとめて。すべてローカルで判定します。</p></button></li>',
 'de': '<li data-tool="sources"><button type="button"><h3>Quellen</h3><p>Woher deine Aufnahmen kommen, nach Website gruppiert. Lokal ermittelt.</p></button></li>',
 'fr': '<li data-tool="sources"><button type="button"><h3>Sources</h3><p>D\'où viennent vos captures, regroupées par site. Calculé en local.</p></button></li>',
 'pt-br': '<li data-tool="sources"><button type="button"><h3>Origens</h3><p>De onde vieram suas capturas, agrupadas por site. Calculado localmente.</p></button></li>',
 'it': '<li data-tool="sources"><button type="button"><h3>Origini</h3><p>Da dove arrivano le tue catture, raggruppate per sito. Calcolato in locale.</p></button></li>'},

'<li data-tool="rules"><button type="button"><h3>Rules</h3><p>Tidying you asked Kapture to do for you. Rules never delete anything.</p></button></li>': {
 'es': '<li data-tool="rules"><button type="button"><h3>Reglas</h3><p>El orden que le has pedido a Kapture que ponga por ti. Las reglas nunca borran nada.</p></button></li>',
 'zh': '<li data-tool="rules"><button type="button"><h3>规则</h3><p>你让 Kapture 替你做的整理。规则永远不会删除任何东西。</p></button></li>',
 'ko': '<li data-tool="rules"><button type="button"><h3>규칙</h3><p>Kapture에 맡긴 정리. 규칙이 무언가를 삭제하는 일은 없습니다.</p></button></li>',
 'ja': '<li data-tool="rules"><button type="button"><h3>ルール</h3><p>Kapture に依頼した整理。ルールが何かを削除することはありません。</p></button></li>',
 'de': '<li data-tool="rules"><button type="button"><h3>Regeln</h3><p>Das Aufräumen, um das du Kapture gebeten hast. Regeln löschen nie etwas.</p></button></li>',
 'fr': '<li data-tool="rules"><button type="button"><h3>Règles</h3><p>Le rangement que vous avez demandé à Kapture. Les règles ne suppriment jamais rien.</p></button></li>',
 'pt-br': '<li data-tool="rules"><button type="button"><h3>Regras</h3><p>A arrumação que você pediu ao Kapture. As regras nunca apagam nada.</p></button></li>',
 'it': '<li data-tool="rules"><button type="button"><h3>Regole</h3><p>Il riordino che hai chiesto a Kapture. Le regole non eliminano mai nulla.</p></button></li>'},

# ---------------------------------------------------------------- Languages
'<p class="kicker">Languages</p>': {
 'es': '<p class="kicker">Idiomas</p>',
 'zh': '<p class="kicker">语言</p>',
 'ko': '<p class="kicker">언어</p>',
 'ja': '<p class="kicker">言語</p>',
 'de': '<p class="kicker">Sprachen</p>',
 'fr': '<p class="kicker">Langues</p>',
 'pt-br': '<p class="kicker">Idiomas</p>',
 'it': '<p class="kicker">Lingue</p>'},

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
 'ja': '<p class="section-lead">Kapture は Chrome で撮ります。Kapture Pro は撮ったものをライブラリに変え、スマート・コレクション・プロジェクトがそれを整った状態に保ちます。それぞれが単体でできることと、両方そろって初めてできることをご覧ください。</p>',
 'de': '<p class="section-lead">Kapture nimmt in Chrome auf. Kapture Pro macht daraus eine Bibliothek, und Smart, Sammlungen und Projekte halten sie in Ordnung. Sieh, was jedes Produkt für sich kann und was beide zusammen ermöglichen.</p>',
 'fr': '<p class="section-lead">Kapture capture dans Chrome. Kapture Pro transforme vos captures en bibliothèque, puis Smart, Collections et Projets la gardent en ordre. Voyez ce que chaque produit fait seul et ce qu\'ils permettent ensemble.</p>',
 'pt-br': '<p class="section-lead">O Kapture captura no Chrome. O Kapture Pro transforma o que você capturou em uma biblioteca, e Smart, Coleções e Projetos mantêm tudo em ordem. Veja o que cada produto faz sozinho e o que os dois liberam juntos.</p>',
 'it': '<p class="section-lead">Kapture cattura in Chrome. Kapture Pro trasforma ciò che hai catturato in una libreria, poi Smart, Raccolte e Progetti la tengono in ordine. Guarda cosa fa ogni prodotto da solo e cosa permettono insieme.</p>'},

'<th scope="row">Smart organisation</th>': {
 'es': '<th scope="row">Organización inteligente</th>',
 'zh': '<th scope="row">智能整理</th>',
 'ko': '<th scope="row">스마트 정리</th>',
 'ja': '<th scope="row">スマートによる整理</th>',
 'de': '<th scope="row">Smart-Organisation</th>',
 'fr': '<th scope="row">Organisation Smart</th>',
 'pt-br': '<th scope="row">Organização com o Smart</th>',
 'it': '<th scope="row">Organizzazione con Smart</th>'},

# ---------------------------------------------------------------- version and metadata
'Chrome extension 0.4.9 &middot; Kapture Pro': {
 'es': 'Extensión de Chrome 0.4.9 &middot; Kapture Pro',
 'zh': 'Chrome 扩展程序 0.4.9 &middot; Kapture Pro',
 'ko': 'Chrome 확장 프로그램 0.4.9 &middot; Kapture Pro',
 'ja': 'Chrome 拡張機能 0.4.9 &middot; Kapture Pro',
 'de': 'Chrome-Erweiterung 0.4.9 &middot; Kapture Pro',
 'fr': 'Extension Chrome 0.4.9 &middot; Kapture Pro',
 'pt-br': 'Extensão do Chrome 0.4.9 &middot; Kapture Pro',
 'it': 'Estensione Chrome 0.4.9 &middot; Kapture Pro'},

'<p class="kicker">Kapture for Chrome &middot; 0.4.9</p>': {
 'es': '<p class="kicker">Kapture para Chrome &middot; 0.4.9</p>',
 'zh': '<p class="kicker">Chrome 版 Kapture &middot; 0.4.9</p>',
 'ko': '<p class="kicker">Chrome용 Kapture &middot; 0.4.9</p>',
 'ja': '<p class="kicker">Chrome 版 Kapture &middot; 0.4.9</p>',
 'de': '<p class="kicker">Kapture für Chrome &middot; 0.4.9</p>',
 'fr': '<p class="kicker">Kapture pour Chrome &middot; 0.4.9</p>',
 'pt-br': '<p class="kicker">Kapture para Chrome &middot; 0.4.9</p>',
 'it': '<p class="kicker">Kapture per Chrome &middot; 0.4.9</p>'},

'Kapture saves full webpages or selected areas straight from Chrome. Kapture Pro turns them into a searchable visual library on your desktop, with Projects, Collections and Smart to keep it organised. Everything stays local.': {
 'es': 'Kapture guarda páginas web completas o el área que elijas, directamente desde Chrome. Kapture Pro las convierte en una biblioteca visual con búsqueda en tu ordenador, con Proyectos, Colecciones e Inteligente para mantenerla en orden. Todo se queda en local.',
 'zh': 'Kapture 直接在 Chrome 里保存整张网页或你框选的区域。Kapture Pro 把它们变成电脑上一个可搜索的可视化图库，并用项目、收藏集和智能保持有序。一切都留在本地。',
 'ko': 'Kapture는 Chrome에서 바로 전체 웹페이지나 선택한 영역을 저장합니다. Kapture Pro는 그것들을 컴퓨터 안에서 검색 가능한 시각적 라이브러리로 만들고, 프로젝트와 컬렉션과 스마트로 정돈된 상태를 유지합니다. 모든 것이 기기 안에 남습니다.',
 'ja': 'Kapture は Chrome から直接、Web ページ全体や選んだ範囲を保存します。Kapture Pro はそれらをパソコン上の検索できるビジュアルライブラリに変え、プロジェクト・コレクション・スマートで整った状態に保ちます。すべてローカルのままです。',
 'de': 'Kapture sichert komplette Webseiten oder ausgewählte Bereiche direkt aus Chrome. Kapture Pro macht daraus eine durchsuchbare visuelle Bibliothek auf deinem Rechner, mit Projekten, Sammlungen und Smart für die Ordnung. Alles bleibt lokal.',
 'fr': 'Kapture enregistre des pages web entières ou des zones choisies directement depuis Chrome. Kapture Pro en fait une bibliothèque visuelle interrogeable sur votre ordinateur, avec Projets, Collections et Smart pour la tenir en ordre. Tout reste en local.',
 'pt-br': 'O Kapture salva páginas da web inteiras ou áreas selecionadas direto do Chrome. O Kapture Pro transforma isso em uma biblioteca visual pesquisável no seu computador, com Projetos, Coleções e Smart para manter tudo organizado. Tudo fica local.',
 'it': 'Kapture salva pagine web intere o aree selezionate direttamente da Chrome. Kapture Pro le trasforma in una libreria visiva consultabile sul tuo computer, con Progetti, Raccolte e Smart per tenerla in ordine. Tutto resta in locale.'},

# The Projects item now draws the Projects / Collections distinction, so the
# whole control block is re-keyed; every other item keeps its approved wording.
'''        <li data-state="projects"><button type="button"><h3>Projects</h3><p>Folders inside Kapture become projects, and projects hold the work in hand.</p></button></li>
        <li data-state="search"><button type="button"><h3>Search</h3><p>Find a capture by name, site or project without opening Finder.</p></button></li>
        <li data-state="library"><button type="button"><h3>Visual library</h3><p>Browse everything as previews instead of filenames.</p></button></li>
        <li data-state="inspector"><button type="button"><h3>Inspector</h3><p>Size, format, source and capture time for whatever you select.</p></button></li>
        <li data-state="tags"><button type="button"><h3>Tags and notes</h3><p>Add your own context so a capture still makes sense later.</p></button></li>
        <li data-state="storage"><button type="button"><h3>Local storage</h3><p>No cloud, no sync, no account. It reads the disk you already have.</p></button></li>''': {
 'es': '''        <li data-state="projects"><button type="button"><h3>Proyectos</h3><p>Las carpetas dentro de Kapture se convierten en proyectos, y ahí vive el trabajo que tienes en marcha.</p></button></li>
        <li data-state="search"><button type="button"><h3>Búsqueda</h3><p>Encuentra una captura por nombre, sitio o proyecto sin abrir el Finder.</p></button></li>
        <li data-state="library"><button type="button"><h3>Biblioteca visual</h3><p>Navega con vistas previas en lugar de nombres de archivo.</p></button></li>
        <li data-state="inspector"><button type="button"><h3>Inspector</h3><p>Tamaño, formato, origen y hora de captura de lo que selecciones.</p></button></li>
        <li data-state="tags"><button type="button"><h3>Etiquetas y notas</h3><p>Añade tu propio contexto para que una captura siga teniendo sentido.</p></button></li>
        <li data-state="storage"><button type="button"><h3>Todo en local</h3><p>Sin nube, sin sincronización, sin cuenta. Lee el disco que ya tienes.</p></button></li>''',
 'zh': '''        <li data-state="projects"><button type="button"><h3>项目</h3><p>Kapture 文件夹里的子文件夹会变成项目，手头的工作就放在项目里。</p></button></li>
        <li data-state="search"><button type="button"><h3>搜索</h3><p>不用打开访达，按名称、网站或项目就能找到截图。</p></button></li>
        <li data-state="library"><button type="button"><h3>可视化图库</h3><p>用预览图浏览一切，而不是一串文件名。</p></button></li>
        <li data-state="inspector"><button type="button"><h3>检查器</h3><p>选中任意一张，就能看到尺寸、格式、来源和截图时间。</p></button></li>
        <li data-state="tags"><button type="button"><h3>标签与备注</h3><p>加上自己的说明，过段时间再看也知道这张是什么。</p></button></li>
        <li data-state="storage"><button type="button"><h3>本地存储</h3><p>没有云端，不用同步，不用账号。它读的就是你现有的硬盘。</p></button></li>''',
 'ko': '''        <li data-state="projects"><button type="button"><h3>프로젝트</h3><p>Kapture 폴더 안의 폴더는 프로젝트가 되고, 지금 하는 일은 프로젝트에 담깁니다.</p></button></li>
        <li data-state="search"><button type="button"><h3>검색</h3><p>Finder를 열지 않고도 이름, 사이트, 프로젝트로 캡처를 찾습니다.</p></button></li>
        <li data-state="library"><button type="button"><h3>시각 라이브러리</h3><p>파일 이름이 아니라 미리보기로 전체를 훑어봅니다.</p></button></li>
        <li data-state="inspector"><button type="button"><h3>인스펙터</h3><p>고른 항목의 크기, 형식, 출처, 캡처 시각을 바로 확인합니다.</p></button></li>
        <li data-state="tags"><button type="button"><h3>태그와 메모</h3><p>직접 맥락을 남겨 두면 나중에 봐도 무슨 캡처인지 압니다.</p></button></li>
        <li data-state="storage"><button type="button"><h3>로컬 저장</h3><p>클라우드도, 동기화도, 계정도 없습니다. 이미 있는 디스크를 읽을 뿐입니다.</p></button></li>''',
 'ja': '''        <li data-state="projects"><button type="button"><h3>プロジェクト</h3><p>Kapture のなかのフォルダーはプロジェクトになり、進行中の仕事はそこに入ります。</p></button></li>
        <li data-state="search"><button type="button"><h3>検索</h3><p>Finder を開かずに、名前・サイト・プロジェクトから探せます。</p></button></li>
        <li data-state="library"><button type="button"><h3>ビジュアルライブラリ</h3><p>ファイル名ではなくプレビューで全体を見渡せます。</p></button></li>
        <li data-state="inspector"><button type="button"><h3>インスペクタ</h3><p>選んだものの大きさ、形式、取得元、撮影日時をその場で確認できます。</p></button></li>
        <li data-state="tags"><button type="button"><h3>タグとメモ</h3><p>自分で文脈を書き添えておけば、後から見ても用途がわかります。</p></button></li>
        <li data-state="storage"><button type="button"><h3>ローカル保存</h3><p>クラウドも同期もアカウントも不要。手元のディスクを読むだけです。</p></button></li>''',
 'de': '        <li data-state="projects"><button type="button"><h3>Projekte</h3><p>Ordner in Kapture werden zu Projekten, und Projekte halten die Arbeit, die gerade ansteht.</p></button></li>\n        <li data-state="search"><button type="button"><h3>Suche</h3><p>Finde eine Aufnahme nach Name, Website oder Projekt, ohne den Finder zu öffnen.</p></button></li>\n        <li data-state="library"><button type="button"><h3>Visuelle Bibliothek</h3><p>Sieh alles als Vorschau statt als Dateinamen.</p></button></li>\n        <li data-state="inspector"><button type="button"><h3>Inspektor</h3><p>Größe, Format, Quelle und Aufnahmezeit für alles, was du auswählst.</p></button></li>\n        <li data-state="tags"><button type="button"><h3>Tags und Notizen</h3><p>Gib einer Aufnahme deinen eigenen Kontext, damit sie später noch Sinn ergibt.</p></button></li>\n        <li data-state="storage"><button type="button"><h3>Lokale Ablage</h3><p>Keine Cloud, kein Sync, kein Konto. Es liest die Platte, die du schon hast.</p></button></li>',
 'fr': '        <li data-state="projects"><button type="button"><h3>Projets</h3><p>Les dossiers dans Kapture deviennent des projets, et les projets contiennent le travail en cours.</p></button></li>\n        <li data-state="search"><button type="button"><h3>Recherche</h3><p>Retrouvez une capture par nom, par site ou par projet sans ouvrir le Finder.</p></button></li>\n        <li data-state="library"><button type="button"><h3>Bibliothèque visuelle</h3><p>Parcourez tout en aperçus plutôt qu\'en noms de fichiers.</p></button></li>\n        <li data-state="inspector"><button type="button"><h3>Inspecteur</h3><p>Taille, format, source et heure de capture pour ce que vous sélectionnez.</p></button></li>\n        <li data-state="tags"><button type="button"><h3>Étiquettes et notes</h3><p>Ajoutez votre propre contexte pour qu\'une capture ait encore du sens plus tard.</p></button></li>\n        <li data-state="storage"><button type="button"><h3>Stockage local</h3><p>Pas de cloud, pas de synchro, pas de compte. Il lit le disque que vous avez déjà.</p></button></li>',
 'pt-br': '        <li data-state="projects"><button type="button"><h3>Projetos</h3><p>Pastas dentro do Kapture viram projetos, e os projetos guardam o trabalho em andamento.</p></button></li>\n        <li data-state="search"><button type="button"><h3>Busca</h3><p>Encontre uma captura por nome, site ou projeto sem abrir o Finder.</p></button></li>\n        <li data-state="library"><button type="button"><h3>Biblioteca visual</h3><p>Navegue por tudo em prévias, e não por nomes de arquivo.</p></button></li>\n        <li data-state="inspector"><button type="button"><h3>Inspetor</h3><p>Tamanho, formato, origem e hora da captura para o que você selecionar.</p></button></li>\n        <li data-state="tags"><button type="button"><h3>Etiquetas e notas</h3><p>Adicione seu próprio contexto para que a captura ainda faça sentido depois.</p></button></li>\n        <li data-state="storage"><button type="button"><h3>Armazenamento local</h3><p>Sem nuvem, sem sincronização, sem conta. Ele lê o disco que você já tem.</p></button></li>',
 'it': '        <li data-state="projects"><button type="button"><h3>Progetti</h3><p>Le cartelle dentro Kapture diventano progetti, e i progetti contengono il lavoro in corso.</p></button></li>\n        <li data-state="search"><button type="button"><h3>Ricerca</h3><p>Trova una cattura per nome, sito o progetto senza aprire il Finder.</p></button></li>\n        <li data-state="library"><button type="button"><h3>Libreria visiva</h3><p>Sfoglia tutto per anteprime invece che per nomi di file.</p></button></li>\n        <li data-state="inspector"><button type="button"><h3>Ispettore</h3><p>Dimensione, formato, origine e ora di cattura per ciò che selezioni.</p></button></li>\n        <li data-state="tags"><button type="button"><h3>Tag e note</h3><p>Aggiungi il tuo contesto, così una cattura ha ancora senso più avanti.</p></button></li>\n        <li data-state="storage"><button type="button"><h3>Archiviazione locale</h3><p>Nessun cloud, nessuna sincronizzazione, nessun account. Legge il disco che hai già.</p></button></li>'},

# ---------------------------------------------------------------- workflow: languages
# System / Default is not a sixth language, so the row counts five and names the
# system option separately.
'<th scope="row">Five languages + System default</th>': {
 'es': '<th scope="row">Cinco idiomas + el del sistema</th>',
 'zh': '<th scope="row">五种语言 + 跟随系统</th>',
 'ko': '<th scope="row">다섯 가지 언어 + 시스템 기본값</th>',
 'ja': '<th scope="row">5 つの言語 + システムに従う</th>'},

# ---------------------------------------------------------------- common questions
# Short factual answers. Every one repeats something already stated elsewhere on
# the page, so nothing here is a new product claim.
'<p class="kicker">Common questions</p>': {
 'es': '<p class="kicker">Preguntas frecuentes</p>',
 'zh': '<p class="kicker">常见问题</p>',
 'ko': '<p class="kicker">자주 묻는 질문</p>',
 'ja': '<p class="kicker">よくある質問</p>',
 'de': '<p class="kicker">Häufige Fragen</p>',
 'fr': '<p class="kicker">Questions fréquentes</p>',
 'pt-br': '<p class="kicker">Perguntas frequentes</p>',
 'it': '<p class="kicker">Domande frequenti</p>'},

'<h2>Short answers.</h2>': {
 'es': '<h2>Respuestas breves.</h2>',
 'zh': '<h2>简短的回答。</h2>',
 'ko': '<h2>짧은 답변.</h2>',
 'ja': '<h2>短い答え。</h2>',
 'de': '<h2>Kurze Antworten.</h2>',
 'fr': '<h2>Réponses courtes.</h2>',
 'pt-br': '<h2>Respostas curtas.</h2>',
 'it': '<h2>Risposte brevi.</h2>'},

'<h3>What is Kapture?</h3>': {
 'es': '<h3>¿Qué es Kapture?</h3>', 'zh': '<h3>Kapture 是什么？</h3>',
 'ko': '<h3>Kapture란 무엇인가요?</h3>', 'ja': '<h3>Kapture とは？</h3>',
 'de': '<h3>Was ist Kapture?</h3>',
 'fr': "<h3>Qu'est-ce que Kapture&nbsp;?</h3>",
 'pt-br': '<h3>O que é o Kapture?</h3>',
 'it': "<h3>Che cos'è Kapture?</h3>"},
'<p>Kapture is a screenshot capture and visual library product in two parts. Kapture for Chrome captures web pages. Kapture Pro is a desktop screenshot manager that turns the captures already on your computer into a searchable visual library.</p>': {
 'es': '<p>Kapture es un producto de captura de pantalla y biblioteca visual en dos partes. Kapture para Chrome captura páginas web. Kapture Pro es un gestor de capturas de escritorio que convierte las capturas que ya tienes en el ordenador en una biblioteca visual con búsqueda.</p>',
 'zh': '<p>Kapture 是一款分为两部分的截图与可视化图库产品。Chrome 版 Kapture 负责截取网页。Kapture Pro 是桌面端的截图管理器，把电脑上已有的截图变成一个可搜索的可视化图库。</p>',
 'ko': '<p>Kapture는 두 부분으로 이루어진 스크린샷 캡처 및 시각 라이브러리 제품입니다. Chrome용 Kapture는 웹페이지를 캡처합니다. Kapture Pro는 이미 컴퓨터에 있는 캡처를 검색 가능한 시각 라이브러리로 만들어 주는 데스크톱 스크린샷 관리자입니다.</p>',
 'ja': '<p>Kapture は 2 つの部分からなるスクリーンショットのキャプチャとビジュアルライブラリの製品です。Chrome 版 Kapture は Web ページを撮ります。Kapture Pro はデスクトップのスクリーンショット管理アプリで、すでにパソコンにあるキャプチャを検索できるビジュアルライブラリに変えます。</p>',
 'de': '<p>Kapture ist ein Produkt für Screenshots und visuelle Bibliotheken, in zwei Teilen. Kapture für Chrome nimmt Webseiten auf. Kapture Pro ist eine Screenshot-Verwaltung für den Desktop, die aus den Aufnahmen auf deinem Rechner eine durchsuchbare visuelle Bibliothek macht.</p>',
 'fr': "<p>Kapture est un produit de capture d'écran et de bibliothèque visuelle en deux parties. Kapture pour Chrome capture les pages web. Kapture Pro est un gestionnaire de captures d'écran pour ordinateur, qui transforme les captures déjà présentes sur votre machine en une bibliothèque visuelle interrogeable.</p>",
 'pt-br': '<p>O Kapture é um produto de captura de tela e biblioteca visual em duas partes. O Kapture para Chrome captura páginas da web. O Kapture Pro é um gerenciador de capturas de tela para desktop que transforma as capturas já presentes no seu computador em uma biblioteca visual pesquisável.</p>',
 'it': '<p>Kapture è un prodotto per catturare schermate e costruire una libreria visiva, in due parti. Kapture per Chrome cattura le pagine web. Kapture Pro è un gestore di screenshot per desktop che trasforma le catture già presenti sul tuo computer in una libreria visiva consultabile.</p>'},

'<h3>Which platforms is Kapture available on?</h3>': {
 'es': '<h3>¿En qué plataformas está disponible Kapture?</h3>', 'zh': '<h3>Kapture 支持哪些平台？</h3>',
 'ko': '<h3>Kapture는 어떤 플랫폼에서 쓸 수 있나요?</h3>', 'ja': '<h3>Kapture はどのプラットフォームで使えますか？</h3>',
 'de': '<h3>Auf welchen Plattformen gibt es Kapture?</h3>',
 'fr': '<h3>Sur quelles plateformes Kapture est-il disponible&nbsp;?</h3>',
 'pt-br': '<h3>Em quais plataformas o Kapture está disponível?</h3>',
 'it': '<h3>Su quali piattaforme è disponibile Kapture?</h3>'},
'<p>Kapture for Chrome is available now and free, for Google Chrome 120 or later. Kapture Pro is the desktop app, planned for Mac and for Windows. Neither desktop build has been released yet, so there is nothing to download for Mac or Windows today.</p>': {
 'es': '<p>Kapture para Chrome ya está disponible y es gratis, para Google Chrome 120 o posterior. Kapture Pro es la app de escritorio, prevista para Mac y para Windows. Todavía no se ha publicado ninguna de las dos versiones de escritorio, así que hoy no hay nada que descargar para Mac ni para Windows.</p>',
 'zh': '<p>Chrome 版 Kapture 现已推出，免费，需要 Google Chrome 120 或更高版本。Kapture Pro 是桌面应用，计划支持 Mac 和 Windows。两个桌面版都尚未发布，所以目前 Mac 和 Windows 都还没有可下载的版本。</p>',
 'ko': '<p>Chrome용 Kapture는 지금 사용할 수 있고 무료이며, Google Chrome 120 이상이 필요합니다. Kapture Pro는 데스크톱 앱으로 Mac과 Windows를 목표로 하고 있습니다. 두 데스크톱 빌드 모두 아직 출시되지 않아, 현재 Mac이나 Windows용으로 내려받을 수 있는 것은 없습니다.</p>',
 'ja': '<p>Chrome 版 Kapture は現在提供中で無料です。Google Chrome 120 以降が必要です。Kapture Pro はデスクトップアプリで、Mac 版と Windows 版を予定しています。どちらもまだ公開されていないため、現時点で Mac や Windows 向けにダウンロードできるものはありません。</p>',
 'de': '<p>Kapture für Chrome gibt es jetzt und kostenlos, für Google Chrome 120 oder neuer. Kapture Pro ist die Desktop-App, geplant für Mac und für Windows. Beide Desktop-Versionen sind noch nicht erschienen, es gibt also heute nichts für Mac oder Windows herunterzuladen.</p>',
 'fr': "<p>Kapture pour Chrome est disponible dès maintenant et gratuit, pour Google Chrome 120 ou plus récent. Kapture Pro est l'application de bureau, prévue pour Mac et pour Windows. Aucune des deux versions de bureau n'est encore sortie&nbsp;: il n'y a donc rien à télécharger pour Mac ni pour Windows aujourd'hui.</p>",
 'pt-br': '<p>O Kapture para Chrome já está disponível e é grátis, para o Google Chrome 120 ou mais recente. O Kapture Pro é o aplicativo de desktop, previsto para Mac e para Windows. Nenhuma das duas versões de desktop foi lançada ainda, então hoje não há nada para baixar para Mac nem para Windows.</p>',
 'it': "<p>Kapture per Chrome è disponibile ora ed è gratis, per Google Chrome 120 o successivo. Kapture Pro è l'app desktop, prevista per Mac e per Windows. Nessuna delle due versioni desktop è ancora uscita, quindi oggi non c'è nulla da scaricare per Mac o Windows.</p>"},

'<h3>Can Kapture capture a full web page and save it as a PDF?</h3>': {
 'es': '<h3>¿Kapture puede capturar una página web completa y guardarla como PDF?</h3>',
 'zh': '<h3>Kapture 能截取整张网页并保存为 PDF 吗？</h3>',
 'ko': '<h3>Kapture로 전체 웹페이지를 캡처해 PDF로 저장할 수 있나요?</h3>',
 'ja': '<h3>Kapture で Web ページ全体を撮って PDF で保存できますか？</h3>',
 'de': '<h3>Kann Kapture eine ganze Webseite aufnehmen und als PDF speichern?</h3>',
 'fr': "<h3>Kapture peut-il capturer une page web entière et l'enregistrer en PDF&nbsp;?</h3>",
 'pt-br': '<h3>O Kapture captura uma página da web inteira e salva em PDF?</h3>',
 'it': '<h3>Kapture può catturare una pagina web intera e salvarla in PDF?</h3>'},
'<p>Yes. Kapture for Chrome scrolls the whole document rather than capturing only the visible part, and it can also capture just an area you drag over. Either one saves as PNG, JPEG or PDF.</p>': {
 'es': '<p>Sí. Kapture para Chrome recorre el documento entero en lugar de capturar solo la parte visible, y también puede capturar únicamente el área que selecciones arrastrando. En ambos casos se guarda como PNG, JPEG o PDF.</p>',
 'zh': '<p>可以。Chrome 版 Kapture 会滚动整个文档，而不是只截取可见部分，也可以只截取你拖选的区域。两种方式都能保存为 PNG、JPEG 或 PDF。</p>',
 'ko': '<p>네. Chrome용 Kapture는 보이는 부분만이 아니라 문서 전체를 스크롤하며 캡처하고, 드래그한 영역만 캡처할 수도 있습니다. 어느 쪽이든 PNG, JPEG, PDF로 저장됩니다.</p>',
 'ja': '<p>できます。Chrome 版 Kapture は見えている部分だけでなく文書全体をスクロールして撮り、ドラッグした範囲だけを撮ることもできます。どちらも PNG、JPEG、PDF で保存できます。</p>',
 'de': '<p>Ja. Kapture für Chrome scrollt das ganze Dokument, statt nur den sichtbaren Teil aufzunehmen, und kann auch nur einen Bereich aufnehmen, über den du ziehst. Beides wird als PNG, JPEG oder PDF gespeichert.</p>',
 'fr': "<p>Oui. Kapture pour Chrome fait défiler tout le document au lieu de ne capturer que la partie visible, et il peut aussi ne capturer qu'une zone que vous tracez. Dans les deux cas, l'enregistrement se fait en PNG, JPEG ou PDF.</p>",
 'pt-br': '<p>Sim. O Kapture para Chrome percorre o documento inteiro em vez de capturar só a parte visível, e também pode capturar apenas uma área que você arrastar. Qualquer um dos dois salva em PNG, JPEG ou PDF.</p>',
 'it': "<p>Sì. Kapture per Chrome scorre tutto il documento invece di catturare solo la parte visibile, e può anche catturare solo un'area che trascini. In entrambi i casi il salvataggio è in PNG, JPEG o PDF.</p>"},

'<h3>How does Kapture Pro organise screenshots?</h3>': {
 'es': '<h3>¿Cómo organiza Kapture Pro las capturas?</h3>', 'zh': '<h3>Kapture Pro 怎么整理截图？</h3>',
 'ko': '<h3>Kapture Pro는 스크린샷을 어떻게 정리하나요?</h3>', 'ja': '<h3>Kapture Pro はスクリーンショットをどう整理しますか？</h3>',
 'de': '<h3>Wie ordnet Kapture Pro Screenshots?</h3>',
 'fr': '<h3>Comment Kapture Pro range-t-il les captures&nbsp;?</h3>',
 'pt-br': '<h3>Como o Kapture Pro organiza as capturas?</h3>',
 'it': '<h3>Come organizza gli screenshot Kapture Pro?</h3>'},
'<p>With Projects and Collections. Projects are the primary working structure, one per piece of work in hand, and any folder inside your Kapture folder becomes one automatically. Collections sit inside the Library and group things you simply want kept together. A capture can be in a project and in collections at the same time. There is more on this on the <a href="/screenshot-organizer/">screenshot organizer</a> page.</p>': {
 'es': '<p>Con Proyectos y Colecciones. Los proyectos son la estructura de trabajo principal, uno por cada cosa que tengas en marcha, y cualquier carpeta dentro de tu carpeta de Kapture se convierte en uno automáticamente. Las colecciones están dentro de la biblioteca y agrupan cosas que simplemente quieres mantener juntas. Una captura puede estar en un proyecto y en colecciones a la vez.</p>',
 'zh': '<p>用项目和收藏集。项目是主要的工作结构，手头每件工作一个，Kapture 文件夹里的任何子文件夹都会自动成为一个项目。收藏集在图库里，用来把你想放在一起的东西归到一处。一张截图可以同时属于一个项目和多个收藏集。</p>',
 'ko': '<p>프로젝트와 컬렉션으로 정리합니다. 프로젝트는 주된 작업 구조로 지금 하는 일마다 하나씩 두며, Kapture 폴더 안의 폴더는 자동으로 프로젝트가 됩니다. 컬렉션은 라이브러리 안에 있으며 그냥 함께 두고 싶은 것들을 묶습니다. 하나의 캡처가 프로젝트와 컬렉션에 동시에 속할 수 있습니다.</p>',
 'ja': '<p>プロジェクトとコレクションで整理します。プロジェクトは主な作業単位で、進行中の仕事ごとに 1 つ持ち、Kapture フォルダーのなかのフォルダーは自動的にプロジェクトになります。コレクションはライブラリのなかにあり、まとめておきたいものをまとめます。1 つのキャプチャがプロジェクトとコレクションの両方に同時に入ることもできます。</p>',
 'de': '<p>Mit Projekten und Sammlungen. Projekte sind die eigentliche Arbeitsstruktur, eines pro anstehender Arbeit, und jeder Ordner in deinem Kapture-Ordner wird automatisch zu einem. Sammlungen liegen in der Bibliothek und fassen zusammen, was du einfach beisammenhalten willst. Eine Aufnahme kann gleichzeitig in einem Projekt und in Sammlungen liegen.</p>',
 'fr': '<p>Avec les Projets et les Collections. Les projets sont la structure de travail principale, un par chantier en cours, et tout dossier placé dans votre dossier Kapture en devient un automatiquement. Les collections vivent dans la bibliothèque et regroupent ce que vous voulez simplement garder ensemble. Une capture peut être dans un projet et dans des collections en même temps.</p>',
 'pt-br': '<p>Com Projetos e Coleções. Os projetos são a estrutura principal de trabalho, um para cada frente em andamento, e qualquer pasta dentro da sua pasta do Kapture vira um automaticamente. As coleções ficam dentro da biblioteca e agrupam o que você simplesmente quer manter junto. Uma captura pode estar em um projeto e em coleções ao mesmo tempo.</p>',
 'it': '<p>Con Progetti e Raccolte. I progetti sono la struttura di lavoro principale, uno per ogni cosa che hai per le mani, e qualsiasi cartella dentro la tua cartella Kapture ne diventa uno automaticamente. Le raccolte stanno nella libreria e mettono insieme ciò che vuoi semplicemente tenere unito. Una cattura può stare in un progetto e in più raccolte allo stesso tempo.</p>'},

'<h3>What is Smart?</h3>': {
 'es': '<h3>¿Qué es Inteligente?</h3>', 'zh': '<h3>什么是智能？</h3>',
 'ko': '<h3>스마트란 무엇인가요?</h3>', 'ja': '<h3>スマートとは？</h3>',
 'de': '<h3>Was ist Smart?</h3>',
 'fr': "<h3>Qu'est-ce que Smart&nbsp;?</h3>",
 'pt-br': '<h3>O que é o Smart?</h3>',
 'it': "<h3>Che cos'è Smart?</h3>"},
'<p>Smart is one workspace in Kapture Pro holding five tools: Unorganised finds captures that are not in a project yet, Duplicates finds files that are identical byte for byte, Cleanup surfaces older and larger captures worth a second look, Sources groups captures by where they came from, and Rules files new captures the way you asked. Smart never deletes anything for you.</p>': {
 'es': '<p>Inteligente es un único espacio dentro de Kapture Pro con cinco herramientas: Sin organizar encuentra las capturas que aún no están en un proyecto, Duplicados encuentra archivos idénticos byte a byte, Limpieza saca a la luz capturas antiguas y pesadas que merecen un segundo vistazo, Fuentes agrupa las capturas por su procedencia y Reglas archiva las capturas nuevas como le hayas pedido. Inteligente nunca borra nada por ti.</p>',
 'zh': '<p>智能是 Kapture Pro 里的一个工作区，包含五个工具：未整理会找出还没归入项目的截图，重复项会找出逐字节完全相同的文件，清理会列出值得再看一眼的旧文件和大文件，来源按出处把截图分组，规则则按你的要求归档新截图。智能永远不会替你删除任何东西。</p>',
 'ko': '<p>스마트는 Kapture Pro 안의 한 작업 공간으로 다섯 가지 도구가 있습니다. 미정리는 아직 프로젝트에 들어가지 않은 캡처를 찾고, 중복 항목은 바이트 단위까지 같은 파일을 찾고, 정리는 다시 살펴볼 만한 오래되고 큰 캡처를 보여 주고, 출처는 캡처를 출처별로 묶고, 규칙은 새 캡처를 요청한 대로 정리합니다. 스마트가 무언가를 대신 삭제하는 일은 없습니다.</p>',
 'ja': '<p>スマートは Kapture Pro のなかのひとつのワークスペースで、5 つのツールがあります。未整理はまだプロジェクトに入っていないキャプチャを探し、重複はバイト単位で同一のファイルを探し、クリーンアップは見直す価値のある古くて大きいキャプチャを示し、ソースは取得元ごとにまとめ、ルールは新しいキャプチャを依頼どおりに振り分けます。スマートが何かを勝手に削除することはありません。</p>',
 'de': '<p>Smart ist ein Arbeitsbereich in Kapture Pro mit fünf Werkzeugen: Unsortiert findet Aufnahmen, die noch in keinem Projekt liegen, Duplikate findet Byte für Byte identische Dateien, Aufräumen zeigt ältere und größere Aufnahmen, die einen zweiten Blick verdienen, Quellen gruppiert Aufnahmen nach ihrer Herkunft, und Regeln legen neue Aufnahmen so ab, wie du es gewünscht hast. Smart löscht nie etwas für dich.</p>',
 'fr': "<p>Smart est un espace de travail dans Kapture Pro qui réunit cinq outils&nbsp;: Non classées trouve les captures qui ne sont pas encore dans un projet, Doublons trouve les fichiers identiques octet pour octet, Nettoyage fait remonter les captures plus anciennes et plus lourdes à revoir, Sources regroupe les captures selon leur provenance, et Règles classe les nouvelles captures comme vous l'avez demandé. Smart ne supprime jamais rien à votre place.</p>",
 'pt-br': '<p>O Smart é um espaço de trabalho dentro do Kapture Pro com cinco ferramentas: Sem organizar acha as capturas que ainda não estão em um projeto, Duplicadas acha arquivos idênticos byte a byte, Limpeza mostra capturas antigas e pesadas que merecem um segundo olhar, Origens agrupa as capturas por onde vieram, e Regras arquiva as novas capturas do jeito que você pediu. O Smart nunca apaga nada por você.</p>',
 'it': '<p>Smart è uno spazio di lavoro dentro Kapture Pro con cinque strumenti: Non organizzate trova le catture che non sono ancora in un progetto, Duplicati trova i file identici byte per byte, Pulizia mostra le catture più vecchie e più grandi da rivedere, Origini raggruppa le catture per provenienza, e Regole archivia le nuove catture come hai chiesto. Smart non elimina mai nulla al posto tuo.</p>'},

'<h3>Where are my screenshots stored?</h3>': {
 'es': '<h3>¿Dónde se guardan mis capturas?</h3>', 'zh': '<h3>我的截图保存在哪里？</h3>',
 'ko': '<h3>스크린샷은 어디에 저장되나요?</h3>', 'ja': '<h3>スクリーンショットはどこに保存されますか？</h3>',
 'de': '<h3>Wo werden meine Screenshots gespeichert?</h3>',
 'fr': '<h3>Où mes captures sont-elles stockées&nbsp;?</h3>',
 'pt-br': '<h3>Onde minhas capturas ficam guardadas?</h3>',
 'it': '<h3>Dove vengono salvati i miei screenshot?</h3>'},
'<p>On your own computer. Kapture for Chrome saves through Chrome\'s own Downloads system, and Kapture Pro reads the files already on your disk without moving them. There is no account, no cloud sync and no upload, and neither product contains analytics, advertising or tracking.</p>': {
 'es': '<p>En tu propio ordenador. Kapture para Chrome guarda con el sistema de descargas de Chrome, y Kapture Pro lee los archivos que ya están en tu disco sin moverlos. No hay cuenta, ni sincronización en la nube, ni subidas, y ninguno de los dos productos incluye analíticas, publicidad ni seguimiento.</p>',
 'zh': '<p>就在你自己的电脑上。Chrome 版 Kapture 通过 Chrome 自带的下载功能保存，Kapture Pro 读取硬盘上已有的文件而不会移动它们。没有账号，没有云同步，也没有上传，两款产品都不含分析、广告或追踪。</p>',
 'ko': '<p>사용자의 컴퓨터에 저장됩니다. Chrome용 Kapture는 Chrome의 다운로드 기능으로 저장하고, Kapture Pro는 이미 디스크에 있는 파일을 옮기지 않고 읽습니다. 계정도, 클라우드 동기화도, 업로드도 없으며 두 제품 모두 분석·광고·추적을 담고 있지 않습니다.</p>',
 'ja': '<p>あなたのパソコンのなかです。Chrome 版 Kapture は Chrome のダウンロード機能で保存し、Kapture Pro はすでにディスクにあるファイルを移動せずに読みます。アカウントもクラウド同期もアップロードもなく、どちらの製品にも解析・広告・トラッキングは含まれていません。</p>'},

'<h3>What languages does Kapture support?</h3>': {
 'es': '<h3>¿Qué idiomas admite Kapture?</h3>', 'zh': '<h3>Kapture 支持哪些语言？</h3>',
 'ko': '<h3>Kapture는 어떤 언어를 지원하나요?</h3>', 'ja': '<h3>Kapture は何語に対応していますか？</h3>',
 'de': '<h3>Welche Sprachen unterstützt Kapture?</h3>',
 'fr': '<h3>Quelles langues Kapture prend-il en charge&nbsp;?</h3>',
 'pt-br': '<h3>Quais idiomas o Kapture oferece?</h3>',
 'it': '<h3>Quali lingue supporta Kapture?</h3>'},
'<p>Both products are available in five languages: English, Spanish, Simplified Chinese, Korean and Japanese. Each also has a System / Default option that follows whatever language your computer is set to.</p>': {
 'es': '<p>Ambos productos están disponibles en cinco idiomas: inglés, español, chino simplificado, coreano y japonés. Los dos tienen además una opción Sistema / Por omisión que sigue el idioma que tengas configurado en el ordenador.</p>',
 'zh': '<p>两款产品都提供五种语言：英语、西班牙语、简体中文、韩语和日语。两者还都有“系统 / 默认”选项，跟随你电脑已设置的语言。</p>',
 'ko': '<p>두 제품 모두 영어, 스페인어, 중국어 간체, 한국어, 일본어의 다섯 가지 언어로 제공됩니다. 둘 다 컴퓨터에 설정된 언어를 따르는 시스템 / 기본값 옵션도 있습니다.</p>',
 'ja': '<p>どちらの製品も英語・スペイン語・簡体中国語・韓国語・日本語の 5 言語で利用できます。どちらにも、パソコンの設定言語に従う「システム / デフォルト」も用意されています。</p>'},

'<h3>Does Kapture use AI?</h3>': {
 'es': '<h3>¿Kapture usa IA?</h3>', 'zh': '<h3>Kapture 会用 AI 吗？</h3>',
 'ko': '<h3>Kapture는 AI를 사용하나요?</h3>', 'ja': '<h3>Kapture は AI を使いますか？</h3>'},
'<p>No. Kapture does not use AI to name, tag, read or sort your screenshots. Everything it does is ordinary local indexing of files that are already on your disk.</p>': {
 'es': '<p>No. Kapture no usa IA para nombrar, etiquetar, leer ni ordenar tus capturas. Todo lo que hace es indexado local corriente de archivos que ya están en tu disco.</p>',
 'zh': '<p>不会。Kapture 不使用 AI 来命名、打标签、读取或整理你的截图。它所做的只是对硬盘上已有文件进行普通的本地索引。</p>',
 'ko': '<p>아닙니다. Kapture는 스크린샷의 이름을 짓거나 태그를 달거나 읽거나 정렬하는 데 AI를 쓰지 않습니다. 하는 일은 이미 디스크에 있는 파일을 평범하게 로컬에서 색인하는 것뿐입니다.</p>',
 'ja': '<p>使いません。Kapture はスクリーンショットの命名・タグ付け・読み取り・並べ替えに AI を使いません。行うのは、すでにディスクにあるファイルを普通にローカルで索引化することだけです。</p>'},

# The homepage footer nav is one block key; Help joins it here.
'''<a href="#capture">Chrome</a>
      <a href="#pro">Kapture Pro</a>
      <a href="/help/">Help</a>
      <a href="/privacy/">Privacy</a>
      <a href="mailto:pequelord@gmail.com">Contact</a>''': {
 'es': '''<a href="#capture">Chrome</a>
      <a href="#pro">Kapture Pro</a>
      <a href="/help/">Ayuda</a>
      <a href="/privacy/">Privacidad</a>
      <a href="mailto:pequelord@gmail.com">Contacto</a>''',
 'zh': '''<a href="#capture">Chrome</a>
      <a href="#pro">Kapture Pro</a>
      <a href="/help/">帮助</a>
      <a href="/privacy/">隐私</a>
      <a href="mailto:pequelord@gmail.com">联系</a>''',
 'ko': '''<a href="#capture">Chrome</a>
      <a href="#pro">Kapture Pro</a>
      <a href="/help/">도움말</a>
      <a href="/privacy/">개인정보</a>
      <a href="mailto:pequelord@gmail.com">문의</a>''',
 'ja': '''<a href="#capture">Chrome</a>
      <a href="#pro">Kapture Pro</a>
      <a href="/help/">ヘルプ</a>
      <a href="/privacy/">プライバシー</a>
      <a href="mailto:pequelord@gmail.com">お問い合わせ</a>''',
 'de': '<a href="#capture">Chrome</a>\n      <a href="#pro">Kapture Pro</a>\n      <a href="/help/">Hilfe</a>\n      <a href="/privacy/">Datenschutz</a>\n      <a href="mailto:pequelord@gmail.com">Kontakt</a>',
 'fr': '<a href="#capture">Chrome</a>\n      <a href="#pro">Kapture Pro</a>\n      <a href="/help/">Aide</a>\n      <a href="/privacy/">Confidentialité</a>\n      <a href="mailto:pequelord@gmail.com">Contact</a>',
 'pt-br': '<a href="#capture">Chrome</a>\n      <a href="#pro">Kapture Pro</a>\n      <a href="/help/">Ajuda</a>\n      <a href="/privacy/">Privacidade</a>\n      <a href="mailto:pequelord@gmail.com">Contato</a>',
 'it': '<a href="#capture">Chrome</a>\n      <a href="#pro">Kapture Pro</a>\n      <a href="/help/">Guida</a>\n      <a href="/privacy/">Privacy</a>\n      <a href="mailto:pequelord@gmail.com">Contatti</a>'},

# ---------------------------------------------------------------- FAQ, refined
'<p class="section-lead">The things people ask most often about Kapture, answered plainly.</p>': {
 'es': '<p class="section-lead">Lo que más se pregunta sobre Kapture, respondido sin rodeos.</p>',
 'zh': '<p class="section-lead">关于 Kapture 最常见的问题，直接给出答案。</p>',
 'ko': '<p class="section-lead">Kapture에 대해 가장 많이 묻는 것들에 대한 솔직한 답변입니다.</p>',
 'ja': '<p class="section-lead">Kapture について最もよく聞かれることに、率直にお答えします。</p>',
 'de': '<p class="section-lead">Was am häufigsten zu Kapture gefragt wird, schlicht beantwortet.</p>',
 'fr': '<p class="section-lead">Ce qu\'on demande le plus souvent à propos de Kapture, répondu simplement.</p>',
 'pt-br': '<p class="section-lead">O que mais perguntam sobre o Kapture, respondido sem rodeios.</p>',
 'it': '<p class="section-lead">Le cose che si chiedono più spesso su Kapture, spiegate in breve.</p>'},

# Replaces "Does Kapture use AI?", whose answer would date as soon as the
# product changed. This one stays true whatever gets built next.
'<h3>Do I need Kapture Pro to use Kapture for Chrome?</h3>': {
 'es': '<h3>¿Necesito Kapture Pro para usar Kapture para Chrome?</h3>',
 'zh': '<h3>要用 Chrome 版 Kapture，必须有 Kapture Pro 吗？</h3>',
 'ko': '<h3>Chrome용 Kapture를 쓰려면 Kapture Pro가 필요한가요?</h3>',
 'ja': '<h3>Chrome 版 Kapture を使うのに Kapture Pro は必要ですか？</h3>',
 'de': '<h3>Brauche ich Kapture Pro, um Kapture für Chrome zu nutzen?</h3>',
 'fr': '<h3>Ai-je besoin de Kapture Pro pour utiliser Kapture pour Chrome&nbsp;?</h3>',
 'pt-br': '<h3>Preciso do Kapture Pro para usar o Kapture para Chrome?</h3>',
 'it': '<h3>Serve Kapture Pro per usare Kapture per Chrome?</h3>'},
'<p>No. Kapture for Chrome works on its own: it captures a page and saves the file wherever you tell it to. Kapture Pro is the desktop half, and it adds the library, the search and the organising on top of captures you already have. They are built to work together, and each is useful without the other.</p>': {
 'es': '<p>No. Kapture para Chrome funciona por su cuenta: captura una página y guarda el archivo donde tú le digas. Kapture Pro es la mitad de escritorio, y añade la biblioteca, la búsqueda y la organización sobre las capturas que ya tienes. Están pensados para funcionar juntos, y cada uno sirve sin el otro.</p>',
 'zh': '<p>不需要。Chrome 版 Kapture 可以单独使用：它截取页面，并把文件保存到你指定的位置。Kapture Pro 是桌面的那一半，在你已有的截图之上加上图库、搜索和整理。两者是为配合使用而设计的，各自单独也都好用。</p>',
 'ko': '<p>아닙니다. Chrome용 Kapture는 그 자체로 동작합니다. 페이지를 캡처해 원하는 위치에 파일을 저장합니다. Kapture Pro는 데스크톱 쪽으로, 이미 가지고 있는 캡처 위에 라이브러리와 검색과 정리를 더해 줍니다. 둘은 함께 쓰도록 만들어졌지만, 각각만으로도 쓸모가 있습니다.</p>',
 'ja': '<p>必要ありません。Chrome 版 Kapture は単体で動きます。ページを撮り、指定した場所にファイルを保存します。Kapture Pro はデスクトップ側で、すでにあるキャプチャの上にライブラリ・検索・整理を加えます。2 つは一緒に使うために作られていますが、それぞれ単体でも役に立ちます。</p>',
 'de': '<p>Nein. Kapture für Chrome funktioniert allein: Es nimmt eine Seite auf und speichert die Datei dorthin, wo du es sagst. Kapture Pro ist die Desktop-Hälfte und legt Bibliothek, Suche und Ordnung über die Aufnahmen, die du schon hast. Sie sind füreinander gebaut, und jedes ist auch ohne das andere nützlich.</p>',
 'fr': "<p>Non. Kapture pour Chrome fonctionne seul&nbsp;: il capture une page et enregistre le fichier là où vous le demandez. Kapture Pro est la moitié de bureau, et il ajoute la bibliothèque, la recherche et le rangement par-dessus les captures que vous avez déjà. Les deux sont faits pour aller ensemble, et chacun sert sans l'autre.</p>",
 'pt-br': '<p>Não. O Kapture para Chrome funciona sozinho: ele captura uma página e salva o arquivo onde você mandar. O Kapture Pro é a metade de desktop, e acrescenta a biblioteca, a busca e a organização sobre as capturas que você já tem. Os dois foram feitos para trabalhar juntos, e cada um é útil sem o outro.</p>',
 'it': "<p>No. Kapture per Chrome funziona da solo: cattura una pagina e salva il file dove gli dici. Kapture Pro è la metà desktop, e aggiunge la libreria, la ricerca e l'organizzazione sopra le catture che hai già. Sono fatti per stare insieme, e ognuno è utile anche senza l'altro.</p>"},

# Local-first stated as what is true today, not as a promise about what will
# never be built.
'<p>On your own computer. Kapture for Chrome saves through Chrome\'s own Downloads system, and Kapture Pro reads the files already on your disk without moving them. Kapture is local-first: capturing, storing and organising your library all happen on your machine and do not depend on a cloud service. Neither product contains analytics, advertising or tracking.</p>': {
 'es': '<p>En tu propio ordenador. Kapture para Chrome guarda con el sistema de descargas de Chrome, y Kapture Pro lee los archivos que ya están en tu disco sin moverlos. Kapture es local-first: capturar, guardar y organizar tu biblioteca ocurre todo en tu máquina y no depende de ningún servicio en la nube. Ninguno de los dos productos incluye analíticas, publicidad ni seguimiento.</p>',
 'zh': '<p>就在你自己的电脑上。Chrome 版 Kapture 通过 Chrome 自带的下载功能保存，Kapture Pro 读取硬盘上已有的文件而不会移动它们。Kapture 以本地优先：截图、保存和整理图库都在你的机器上完成，不依赖任何云服务。两款产品都不含分析、广告或追踪。</p>',
 'ko': '<p>사용자의 컴퓨터에 저장됩니다. Chrome용 Kapture는 Chrome의 다운로드 기능으로 저장하고, Kapture Pro는 이미 디스크에 있는 파일을 옮기지 않고 읽습니다. Kapture는 로컬 우선입니다. 캡처하고 저장하고 라이브러리를 정리하는 일이 모두 사용자의 기기에서 이루어지며 클라우드 서비스에 의존하지 않습니다. 두 제품 모두 분석·광고·추적을 담고 있지 않습니다.</p>',
 'ja': '<p>あなたのパソコンのなかです。Chrome 版 Kapture は Chrome のダウンロード機能で保存し、Kapture Pro はすでにディスクにあるファイルを移動せずに読みます。Kapture はローカルファーストです。撮ることも、保存することも、ライブラリを整理することも、すべてあなたの端末のなかで行われ、クラウドサービスに依存しません。どちらの製品にも解析・広告・トラッキングは含まれていません。</p>',
 'de': '<p>Auf deinem eigenen Rechner. Kapture für Chrome speichert über das eigene Download-System von Chrome, und Kapture Pro liest die Dateien, die schon auf deiner Platte liegen, ohne sie zu verschieben. Kapture ist local-first: Aufnehmen, Speichern und Ordnen deiner Bibliothek geschehen auf deinem Gerät und hängen an keinem Cloud-Dienst. Keines der beiden Produkte enthält Analyse, Werbung oder Tracking.</p>',
 'fr': "<p>Sur votre propre ordinateur. Kapture pour Chrome enregistre via le système de téléchargement de Chrome, et Kapture Pro lit les fichiers déjà présents sur votre disque sans les déplacer. Kapture est local-first&nbsp;: capturer, stocker et ranger votre bibliothèque se passent sur votre machine et ne dépendent d'aucun service cloud. Aucun des deux produits ne contient d'analyse, de publicité ni de suivi.</p>",
 'pt-br': '<p>No seu próprio computador. O Kapture para Chrome salva pelo sistema de downloads do Chrome, e o Kapture Pro lê os arquivos que já estão no seu disco sem movê-los. O Kapture é local-first: capturar, guardar e organizar sua biblioteca acontece na sua máquina e não depende de nenhum serviço na nuvem. Nenhum dos dois produtos tem analytics, publicidade ou rastreamento.</p>',
 'it': '<p>Sul tuo computer. Kapture per Chrome salva tramite il sistema di download di Chrome, e Kapture Pro legge i file già presenti sul tuo disco senza spostarli. Kapture è local-first: catturare, conservare e organizzare la libreria avviene sul tuo dispositivo e non dipende da un servizio cloud. Nessuno dei due prodotti contiene analisi, pubblicità o tracciamento.</p>'},

# ---------------------------------------------------------------- nine languages
# The product ships in nine languages now. System / Default is a preference that
# follows the machine, so it is never counted as one of them.
'<h2>Nine languages.<br><span class="accent">Or simply follow your system.</span></h2>': {
 'es': '<h2>Nueve idiomas.<br><span class="accent">O simplemente el de tu sistema.</span></h2>',
 'zh': '<h2>九种语言。<br><span class="accent">或者直接跟随系统。</span></h2>',
 'ko': '<h2>아홉 가지 언어.<br><span class="accent">또는 시스템 설정 그대로.</span></h2>',
 'ja': '<h2>9 つの言語。<br><span class="accent">あるいはシステムのままで。</span></h2>',
 'de': '<h2>Neun Sprachen.<br><span class="accent">Oder einfach dem System folgen.</span></h2>',
 'fr': '<h2>Neuf langues.<br><span class="accent">Ou tout simplement celle de votre système.</span></h2>',
 'pt-br': '<h2>Nove idiomas.<br><span class="accent">Ou simplesmente o do seu sistema.</span></h2>',
 'it': '<h2>Nove lingue.<br><span class="accent">O semplicemente quella del tuo sistema.</span></h2>'},

'<th scope="row">Nine languages + System default</th>': {
 'es': '<th scope="row">Nueve idiomas + el del sistema</th>',
 'zh': '<th scope="row">九种语言 + 跟随系统</th>',
 'ko': '<th scope="row">아홉 가지 언어 + 시스템 기본값</th>',
 'ja': '<th scope="row">9 つの言語 + システムに従う</th>',
 'de': '<th scope="row">Neun Sprachen + Systemsprache</th>',
 'fr': '<th scope="row">Neuf langues + celle du système</th>',
 'pt-br': '<th scope="row">Nove idiomas + o do sistema</th>',
 'it': '<th scope="row">Nove lingue + quella di sistema</th>'},

'<p class="section-lead">Kapture for Chrome and Kapture Pro both speak English, Spanish, Simplified Chinese, Korean, Japanese, German, French, Brazilian Portuguese and Italian. Pick one, or leave it on System and Kapture follows whatever your computer is already set to.</p>': {
 'es': '<p class="section-lead">Kapture para Chrome y Kapture Pro hablan inglés, español, chino simplificado, coreano, japonés, alemán, francés, portugués de Brasil e italiano. Elige uno, o déjalo en Sistema y Kapture seguirá el idioma que ya tenga tu ordenador.</p>',
 'zh': '<p class="section-lead">Chrome 版 Kapture 和 Kapture Pro 都支持英语、西班牙语、简体中文、韩语、日语、德语、法语、巴西葡萄牙语和意大利语。你可以自己选一个，也可以保持“系统”，让 Kapture 跟随电脑已有的设置。</p>',
 'ko': '<p class="section-lead">Chrome용 Kapture와 Kapture Pro 모두 영어, 스페인어, 중국어 간체, 한국어, 일본어, 독일어, 프랑스어, 브라질 포르투갈어, 이탈리아어를 지원합니다. 직접 고르거나, 시스템으로 두면 Kapture가 컴퓨터에 설정된 언어를 따릅니다.</p>',
 'ja': '<p class="section-lead">Chrome 版 Kapture と Kapture Pro は、英語・スペイン語・簡体中国語・韓国語・日本語・ドイツ語・フランス語・ブラジルポルトガル語・イタリア語に対応しています。ひとつを選んでも、システムのままにしてパソコンの設定に従わせても構いません。</p>',
 'de': '<p class="section-lead">Kapture für Chrome und Kapture Pro sprechen Englisch, Spanisch, Chinesisch (vereinfacht), Koreanisch, Japanisch, Deutsch, Französisch, brasilianisches Portugiesisch und Italienisch. Wähle eine, oder lass es auf System, dann folgt Kapture dem, was dein Rechner ohnehin eingestellt hat.</p>',
 'fr': '<p class="section-lead">Kapture pour Chrome et Kapture Pro parlent anglais, espagnol, chinois simplifié, coréen, japonais, allemand, français, portugais brésilien et italien. Choisissez-en une, ou laissez sur Système et Kapture suivra la langue déjà réglée sur votre ordinateur.</p>',
 'pt-br': '<p class="section-lead">O Kapture para Chrome e o Kapture Pro falam inglês, espanhol, chinês simplificado, coreano, japonês, alemão, francês, português do Brasil e italiano. Escolha um, ou deixe em Sistema que o Kapture segue o idioma já configurado no seu computador.</p>',
 'it': '<p class="section-lead">Kapture per Chrome e Kapture Pro parlano inglese, spagnolo, cinese semplificato, coreano, giapponese, tedesco, francese, portoghese brasiliano e italiano. Scegline una, oppure lascia su Sistema e Kapture seguirà quella già impostata sul tuo computer.</p>'},

'<p>Both products are available in nine languages: English, Spanish, Simplified Chinese, Korean, Japanese, German, French, Brazilian Portuguese and Italian. Each also has a System / Default option that follows whatever language your computer is set to.</p>': {
 'es': '<p>Ambos productos están disponibles en nueve idiomas: inglés, español, chino simplificado, coreano, japonés, alemán, francés, portugués de Brasil e italiano. Los dos tienen además una opción Sistema / Por omisión que sigue el idioma que tengas configurado en el ordenador.</p>',
 'zh': '<p>两款产品都提供九种语言：英语、西班牙语、简体中文、韩语、日语、德语、法语、巴西葡萄牙语和意大利语。两者还都有“系统 / 默认”选项，跟随你电脑已设置的语言。</p>',
 'ko': '<p>두 제품 모두 아홉 가지 언어로 제공됩니다. 영어, 스페인어, 중국어 간체, 한국어, 일본어, 독일어, 프랑스어, 브라질 포르투갈어, 이탈리아어입니다. 둘 다 컴퓨터에 설정된 언어를 따르는 시스템 / 기본값 옵션도 있습니다.</p>',
 'ja': '<p>どちらの製品も 9 つの言語で利用できます。英語・スペイン語・簡体中国語・韓国語・日本語・ドイツ語・フランス語・ブラジルポルトガル語・イタリア語です。どちらにも、パソコンの設定言語に従う「システム / デフォルト」も用意されています。</p>',
 'de': '<p>Beide Produkte gibt es in neun Sprachen: Englisch, Spanisch, Chinesisch (vereinfacht), Koreanisch, Japanisch, Deutsch, Französisch, brasilianisches Portugiesisch und Italienisch. Beide haben außerdem die Option System / Standard, die der Spracheinstellung deines Rechners folgt.</p>',
 'fr': '<p>Les deux produits sont disponibles en neuf langues&nbsp;: anglais, espagnol, chinois simplifié, coréen, japonais, allemand, français, portugais brésilien et italien. Chacun propose aussi une option Système / Par défaut qui suit la langue réglée sur votre ordinateur.</p>',
 'pt-br': '<p>Os dois produtos estão disponíveis em nove idiomas: inglês, espanhol, chinês simplificado, coreano, japonês, alemão, francês, português do Brasil e italiano. Cada um também tem a opção Sistema / Padrão, que segue o idioma configurado no seu computador.</p>',
 'it': '<p>Entrambi i prodotti sono disponibili in nove lingue: inglese, spagnolo, cinese semplificato, coreano, giapponese, tedesco, francese, portoghese brasiliano e italiano. Ognuno ha anche l\'opzione Sistema / Predefinito, che segue la lingua impostata sul tuo computer.</p>'},

# ---------------------------------------------------------------- hero sub
# This shipped in English on every locale from the pass that changed "on your
# Mac" to "on your desktop": the key stopped matching and the English fell
# through. The sentinel list did not cover it, which is why tools/check_leaks.py
# now compares every built page against the English one sentence by sentence.
'''        Kapture saves full webpages or selected areas straight from Chrome.
        Kapture Pro turns them into an organised, searchable visual library on your desktop.''': {
 'es': '''        Kapture guarda páginas web completas o el área que elijas, directamente desde Chrome.
        Kapture Pro las convierte en una biblioteca visual ordenada y con búsqueda en tu ordenador.''',
 'zh': '''        Kapture 直接在 Chrome 里保存整张网页或你框选的区域。
        Kapture Pro 把它们变成电脑上一个井井有条、可搜索的可视化图库。''',
 'ko': '''        Kapture는 Chrome에서 바로 전체 웹페이지나 선택한 영역을 저장합니다.
        Kapture Pro는 그것들을 컴퓨터 안에서 정돈되고 검색 가능한 시각적 라이브러리로 만듭니다.''',
 'ja': '''        Kapture は Chrome から直接、Web ページ全体や選んだ範囲を保存します。
        Kapture Pro はそれらをパソコン上の整理された、検索できるビジュアルライブラリにします。''',
 'de': '''        Kapture sichert komplette Webseiten oder ausgewählte Bereiche direkt aus Chrome.
        Kapture Pro macht daraus eine geordnete, durchsuchbare visuelle Bibliothek auf deinem Rechner.''',
 'fr': '''        Kapture enregistre des pages web entières ou des zones choisies directement depuis Chrome.
        Kapture Pro en fait une bibliothèque visuelle rangée et interrogeable sur votre ordinateur.''',
 'pt-br': '''        O Kapture salva páginas da web inteiras ou áreas selecionadas direto do Chrome.
        O Kapture Pro transforma isso em uma biblioteca visual organizada e pesquisável no seu computador.''',
 'it': '''        Kapture salva pagine web intere o aree selezionate direttamente da Chrome.
        Kapture Pro le trasforma in una libreria visiva ordinata e consultabile sul tuo computer.''',
}

}
