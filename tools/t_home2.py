# -*- coding: utf-8 -*-
"""Homepage strings, part 2: sections, features, steps, privacy block, footer."""

HOME2 = {
# ---------------------------------------------------------------- two ways
'<p class="kicker">Two ways to capture</p>': {
 'es': '<p class="kicker">Dos formas de capturar</p>',
 'zh': '<p class="kicker">两种截图方式</p>',
 'ko': '<p class="kicker">캡처하는 두 가지 방법</p>',
 'ja': '<p class="kicker">2 つのキャプチャ方法</p>'},
'<h2>Everything, or exactly<br>one part of it.</h2>': {
 'es': '<h2>Todo, o justo<br>la parte que quieras.</h2>',
 'zh': '<h2>整页，或者<br>只要其中一块。</h2>',
 'ko': '<h2>전체를, 아니면<br>원하는 부분만.</h2>',
 'ja': '<h2>ページ全体か、<br>必要な一部だけか。</h2>'},

'<h3>Full page</h3>': {
 'es': '<h3>Páginas completas</h3>', 'zh': '<h3>整页截图</h3>',
 'ko': '<h3>전체 페이지</h3>', 'ja': '<h3>ページ全体</h3>'},
'            Kapture scrolls the main document and captures it end to end, splitting very long\n            pages into 8,000&nbsp;pixel sections so the files stay usable.': {
 'es': '            Kapture recorre el documento y lo captura de principio a fin. Las páginas muy\n            largas se dividen en secciones de 8.000 píxeles para que los archivos sigan siendo manejables.',
 'zh': '            Kapture 会滚动整个文档，从头截到尾。超长页面会按 8,000 像素分段，\n            文件不至于大到不好用。',
 'ko': '            Kapture가 문서를 처음부터 끝까지 스크롤하며 캡처합니다. 아주 긴 페이지는\n            8,000픽셀 단위로 나눠 파일을 다루기 쉽게 유지합니다.',
 'ja': '            Kapture がドキュメントをスクロールして最初から最後まで撮影します。とても長い\n            ページは 8,000 ピクセルごとに分割するので、ファイルが扱いやすいままです。'},

'<h3>Select area</h3>': {
 'es': '<h3>Seleccionar zona</h3>', 'zh': '<h3>区域截图</h3>',
 'ko': '<h3>영역 선택</h3>', 'ja': '<h3>範囲を選ぶ</h3>'},
'            Drag over the visible page to grab one region. Choose Freeform, 1:1, 16:9 or 9:16,\n            then move or resize the selection before you capture.': {
 'es': '            Arrastra sobre la parte visible para marcar una zona. Elige formato libre, 1:1,\n            16:9 o 9:16, y mueve o ajusta la selección antes de capturar.',
 'zh': '            在可见区域拖动，框出想要的部分。可选自由比例、1:1、16:9 或 9:16，\n            截图前还能移动或调整选区。',
 'ko': '            보이는 화면에서 드래그해 원하는 영역을 지정하세요. 자유 비율, 1:1, 16:9, 9:16 중에서\n            고르고 캡처 전에 위치와 크기를 조정할 수 있습니다.',
 'ja': '            表示中の画面をドラッグして範囲を指定します。フリー、1:1、16:9、9:16 から選び、\n            撮影前に位置やサイズを調整できます。'},

# ---------------------------------------------------------------- what you get
'<p class="kicker">What you get</p>': {
 'es': '<p class="kicker">Lo que incluye</p>', 'zh': '<p class="kicker">你会得到什么</p>',
 'ko': '<p class="kicker">이런 걸 할 수 있어요</p>', 'ja': '<p class="kicker">できること</p>'},
'<h2>Built for the screenshot you actually needed.</h2>': {
 'es': '<h2>Pensado para capturar lo que de verdad necesitas.</h2>',
 'zh': '<h2>为你真正需要的那张截图而做。</h2>',
 'ko': '<h2>정말 필요했던 그 스크린샷을 위해.</h2>',
 'ja': '<h2>本当に必要だったスクリーンショットのために。</h2>'},

'<h3>PNG, JPEG or PDF</h3>': {
 'es': '<h3>PNG, JPEG o PDF</h3>', 'zh': '<h3>PNG、JPEG 或 PDF</h3>',
 'ko': '<h3>PNG, JPEG, PDF</h3>', 'ja': '<h3>PNG・JPEG・PDF</h3>'},
'<p>Pick the format before you capture. PDF produces one local, multi&#8209;page file.</p>': {
 'es': '<p>Elige el formato antes de capturar. El PDF se genera como un único archivo local de varias páginas.</p>',
 'zh': '<p>截图前先选好格式。PDF 会生成一个本地的多页文件。</p>',
 'ko': '<p>캡처하기 전에 형식을 고르세요. PDF는 여러 페이지가 담긴 파일 하나로 저장됩니다.</p>',
 'ja': '<p>撮影前に形式を選べます。PDF は複数ページをまとめた 1 つのファイルになります。</p>'},

'<h3>Viewport presets</h3>': {
 'es': '<h3>Tamaños de pantalla</h3>', 'zh': '<h3>预设画面宽度</h3>',
 'ko': '<h3>화면 크기 프리셋</h3>', 'ja': '<h3>画面幅プリセット</h3>'},
'<p>Capture at your current window, or render the page at Phone&nbsp;390, Tablet&nbsp;820, Desktop&nbsp;1440 or Desktop&nbsp;1920 first.</p>': {
 'es': '<p>Captura con el tamaño actual de tu ventana o muestra antes la página a 390&nbsp;(móvil), 820&nbsp;(tablet), 1440 o 1920&nbsp;(escritorio).</p>',
 'zh': '<p>按当前窗口截图，也可以先用手机&nbsp;390、平板&nbsp;820、桌面&nbsp;1440 或桌面&nbsp;1920 的宽度重新渲染页面。</p>',
 'ko': '<p>지금 창 크기 그대로 찍거나, 휴대폰&nbsp;390, 태블릿&nbsp;820, 데스크톱&nbsp;1440·1920 너비로 페이지를 다시 그린 뒤 찍을 수 있습니다.</p>',
 'ja': '<p>今のウィンドウのまま撮るか、スマホ&nbsp;390・タブレット&nbsp;820・デスクトップ&nbsp;1440 / 1920 の幅で表示し直してから撮れます。</p>'},

'<h3>Save where it makes sense</h3>': {
 'es': '<h3>Guarda donde tenga sentido</h3>', 'zh': '<h3>存到该存的地方</h3>',
 'ko': '<h3>필요한 곳에 저장</h3>', 'ja': '<h3>置きたい場所に保存</h3>'},
'<p>Send captures straight to Downloads, or name a folder per page or project to keep them organised.</p>': {
 'es': '<p>Envía las capturas directamente a Descargas o crea una carpeta por página o proyecto para tenerlo todo ordenado.</p>',
 'zh': '<p>截图可以直接进下载文件夹，也可以按页面或项目分别指定文件夹，方便归类。</p>',
 'ko': '<p>다운로드 폴더에 바로 저장하거나, 페이지나 프로젝트별로 폴더 이름을 정해 정리할 수 있습니다.</p>',
 'ja': '<p>そのままダウンロードフォルダへ。ページやプロジェクトごとにフォルダ名を決めて整理することもできます。</p>'},

'<h3>Local history</h3>': {
 'es': '<h3>Historial local</h3>', 'zh': '<h3>本地记录</h3>',
 'ko': '<h3>기기 안의 기록</h3>', 'ja': '<h3>端末内の履歴</h3>'},
'<p>Newest first, with the site and time. Open a screenshot, or select entries and delete the files for good.</p>': {
 'es': '<p>Lo más reciente primero, con el sitio y la hora. Abre una captura o selecciona varias y bórralas definitivamente.</p>',
 'zh': '<p>最新的排在最前，带上网站和时间。可以直接打开某张截图，也可以勾选后彻底删除。</p>',
 'ko': '<p>최신 항목이 위에, 사이트와 시간까지 함께. 스크린샷을 바로 열거나 골라서 완전히 삭제할 수 있습니다.</p>',
 'ja': '<p>新しい順に、サイト名と時刻つきで。その場で開くことも、選んでまとめて削除することもできます。</p>'},

'<h3>Light and dark</h3>': {
 'es': '<h3>Claro y oscuro</h3>', 'zh': '<h3>浅色和深色</h3>',
 'ko': '<h3>라이트와 다크</h3>', 'ja': '<h3>ライトとダーク</h3>'},
'<p>The side panel has both themes, and remembers the one you chose.</p>': {
 'es': '<p>El panel lateral tiene los dos temas y recuerda el que elijas.</p>',
 'zh': '<p>侧边栏两种主题都有，并会记住你的选择。</p>',
 'ko': '<p>사이드 패널은 두 테마를 모두 지원하고, 고른 테마를 기억합니다.</p>',
 'ja': '<p>サイドパネルは両方のテーマに対応し、選んだほうを覚えています。</p>'},

'<h3>Nothing to sign up for</h3>': {
 'es': '<h3>Sin registros</h3>', 'zh': '<h3>不用注册</h3>',
 'ko': '<h3>가입 없이 바로</h3>', 'ja': '<h3>登録は不要</h3>'},
'<p>No account, no ads, no analytics. Install it and capture.</p>': {
 'es': '<p>Sin cuenta, sin anuncios, sin analíticas. Instálalo y captura.</p>',
 'zh': '<p>没有账号，没有广告，没有数据统计。装上就能用。</p>',
 'ko': '<p>계정도, 광고도, 분석도 없습니다. 설치하고 바로 캡처하세요.</p>',
 'ja': '<p>アカウントも広告も解析もありません。入れたらすぐ撮れます。</p>'},

# ---------------------------------------------------------------- how it works
'<p class="kicker">How it works</p>': {
 'es': '<p class="kicker">Cómo funciona</p>', 'zh': '<p class="kicker">使用方法</p>',
 'ko': '<p class="kicker">사용 방법</p>', 'ja': '<p class="kicker">使い方</p>'},
'<h2>Three steps. No setup.</h2>': {
 'es': '<h2>Tres pasos.<br>Sin configurar nada.</h2>', 'zh': '<h2>三步搞定，无需设置。</h2>',
 'ko': '<h2>세 단계. 설정은 없습니다.</h2>', 'ja': '<h2>3 ステップ。設定は不要。</h2>'},

'<h3>Open the page</h3>\n          <p>Go to whatever you want to keep.</p>': {
 'es': '<h3>Abre la página</h3>\n          <p>Ve a la página que quieras guardar.</p>',
 'zh': '<h3>打开页面</h3>\n          <p>找到你想保存的内容。</p>',
 'ko': '<h3>페이지 열기</h3>\n          <p>남겨두고 싶은 화면으로 이동하세요.</p>',
 'ja': '<h3>ページを開く</h3>\n          <p>残しておきたいものを表示します。</p>'},
'<h3>Click Kapture</h3>\n          <p>The side panel opens beside the page.</p>': {
 'es': '<h3>Haz clic en Kapture</h3>\n          <p>El panel lateral se abre junto a la página.</p>',
 'zh': '<h3>点击 Kapture</h3>\n          <p>侧边栏会在页面旁边打开。</p>',
 'ko': '<h3>Kapture 클릭</h3>\n          <p>페이지 옆에 사이드 패널이 열립니다.</p>',
 'ja': '<h3>Kapture をクリック</h3>\n          <p>ページの横にサイドパネルが開きます。</p>'},
'<h3>Capture</h3>\n          <p>Choose full page or an area, then save.</p>': {
 'es': '<h3>Captura</h3>\n          <p>Elige toda la página o solo una zona, y guarda.</p>',
 'zh': '<h3>截图</h3>\n          <p>选整页或某个区域，然后保存。</p>',
 'ko': '<h3>캡처</h3>\n          <p>전체 페이지나 영역을 고르고 저장하세요.</p>',
 'ja': '<h3>キャプチャ</h3>\n          <p>ページ全体か範囲を選んで保存。</p>'},
}
