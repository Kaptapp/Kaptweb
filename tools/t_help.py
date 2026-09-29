# -*- coding: utf-8 -*-
"""Help and updates page.

Version numbers, brand names (Kapture, Kapture Pro, Chrome, Mac, Windows),
filenames, folder paths and permission identifiers stay in English. Product
wording matches the extension's own locales, so a reader sees the same terms in
the side panel and on this page.
"""

HELP = {

# ---------------------------------------------------------------- metadata
'<title>Help and Updates | Kapture</title>': {
 'es': '<title>Ayuda y novedades | Kapture</title>',
 'zh': '<title>帮助与更新 | Kapture</title>',
 'ko': '<title>도움말 및 업데이트 | Kapture</title>',
 'ja': '<title>ヘルプと更新情報 | Kapture</title>'},

'Kapture help, current extension version and release history. What changed in version 0.4.8, what came before it, and how to use Kapture for Chrome.': {
 'es': 'Ayuda de Kapture, versión actual de la extensión e historial de versiones. Qué cambió en la versión 0.4.8, qué hubo antes y cómo usar Kapture para Chrome.',
 'zh': 'Kapture 帮助、扩展程序当前版本和版本历史。0.4.8 版做了哪些改动、之前有哪些版本，以及如何使用 Chrome 版 Kapture。',
 'ko': 'Kapture 도움말과 현재 확장 프로그램 버전, 릴리스 기록. 0.4.8 버전에서 달라진 점과 이전 버전, 그리고 Chrome용 Kapture 사용 방법을 안내합니다.',
 'ja': 'Kapture のヘルプ、現在の拡張機能のバージョン、リリース履歴。バージョン 0.4.8 での変更点とそれ以前のバージョン、そして Chrome 版 Kapture の使い方を説明します。'},

# og:title and twitter:title carry the bare form; the <title> key above wins first
'Help and Updates | Kapture': {
 'es': 'Ayuda y novedades | Kapture',
 'zh': '帮助与更新 | Kapture',
 'ko': '도움말 및 업데이트 | Kapture',
 'ja': 'ヘルプと更新情報 | Kapture'},

'content="Kapture, full page screenshots for Chrome."': {
 'es': 'content="Kapture, capturas de página completa para Chrome."',
 'zh': 'content="Kapture，Chrome 的整页截图工具。"',
 'ko': 'content="Kapture, Chrome용 전체 페이지 스크린샷."',
 'ja': 'content="Kapture、Chrome 用のページ全体スクリーンショット。"'},

# JSON-LD breadcrumb. localise_ld rewrites ids and urls, not these names.
'"name": "Home"': {
 'es': '"name": "Inicio"', 'zh': '"name": "首页"',
 'ko': '"name": "홈"', 'ja': '"name": "ホーム"'},
'"name": "Help and Updates"': {
 'es': '"name": "Ayuda y novedades"', 'zh': '"name": "帮助与更新"',
 'ko': '"name": "도움말 및 업데이트"', 'ja': '"name": "ヘルプと更新情報"'},

# ---------------------------------------------------------------- chrome
'<a class="skip-link" href="#main">Skip to content</a>': {
 'es': '<a class="skip-link" href="#main">Saltar al contenido</a>',
 'zh': '<a class="skip-link" href="#main">跳到主要内容</a>',
 'ko': '<a class="skip-link" href="#main">본문으로 건너뛰기</a>',
 'ja': '<a class="skip-link" href="#main">本文へスキップ</a>'},

'<nav class="header-nav" aria-label="Primary">': {
 'es': '<nav class="header-nav" aria-label="Principal">',
 'zh': '<nav class="header-nav" aria-label="主导航">',
 'ko': '<nav class="header-nav" aria-label="기본">',
 'ja': '<nav class="header-nav" aria-label="メイン">'},
'<nav class="footer-nav" aria-label="Footer">': {
 'es': '<nav class="footer-nav" aria-label="Pie de página">',
 'zh': '<nav class="footer-nav" aria-label="页脚">',
 'ko': '<nav class="footer-nav" aria-label="푸터">',
 'ja': '<nav class="footer-nav" aria-label="フッター">'},

'<a href="/#how">How it works</a>': {
 'es': '<a href="/#how">Cómo funciona</a>', 'zh': '<a href="/#how">工作方式</a>',
 'ko': '<a href="/#how">작동 방식</a>', 'ja': '<a href="/#how">仕組み</a>'},
'<a href="/privacy/">Privacy</a>': {
 'es': '<a href="/privacy/">Privacidad</a>', 'zh': '<a href="/privacy/">隐私</a>',
 'ko': '<a href="/privacy/">개인정보</a>', 'ja': '<a href="/privacy/">プライバシー</a>'},
'<a href="mailto:pequelord@gmail.com">Contact</a>': {
 'es': '<a href="mailto:pequelord@gmail.com">Contacto</a>',
 'zh': '<a href="mailto:pequelord@gmail.com">联系我们</a>',
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

'<p class="legal-foot">Kapture by Pequelord &middot; Screenshots stay on your device.</p>': {
 'es': '<p class="legal-foot">Kapture, de Pequelord &middot; Tus capturas se quedan en tu dispositivo.</p>',
 'zh': '<p class="legal-foot">Kapture，由 Pequelord 开发 &middot; 截图只保存在你的设备上。</p>',
 'ko': '<p class="legal-foot">Pequelord가 만든 Kapture &middot; 스크린샷은 기기에만 남습니다.</p>',
 'ja': '<p class="legal-foot">Pequelord による Kapture &middot; スクリーンショットは端末内にとどまります。</p>'},

# ---------------------------------------------------------------- page head
'<p class="kicker">Help</p>': {
 'es': '<p class="kicker">Ayuda</p>', 'zh': '<p class="kicker">帮助</p>',
 'ko': '<p class="kicker">도움말</p>', 'ja': '<p class="kicker">ヘルプ</p>'},
'<h1>Kapture Help</h1>': {
 'es': '<h1>Ayuda de Kapture</h1>', 'zh': '<h1>Kapture 帮助</h1>',
 'ko': '<h1>Kapture 도움말</h1>', 'ja': '<h1>Kapture ヘルプ</h1>'},
'<p class="legal-date">Current extension information, the latest changes and previous updates.</p>': {
 'es': '<p class="legal-date">Información de la extensión actual, los últimos cambios y las novedades anteriores.</p>',
 'zh': '<p class="legal-date">当前扩展程序的信息、最新改动以及以往的更新。</p>',
 'ko': '<p class="legal-date">현재 확장 프로그램 정보와 최신 변경 사항, 이전 업데이트를 안내합니다.</p>',
 'ja': '<p class="legal-date">現在の拡張機能の情報、最新の変更点、これまでの更新内容をまとめています。</p>'},

# ---------------------------------------------------------------- headings
'<h2 class="rel-h">Latest update</h2>': {
 'es': '<h2 class="rel-h">Última novedad</h2>', 'zh': '<h2 class="rel-h">最新更新</h2>',
 'ko': '<h2 class="rel-h">최신 업데이트</h2>', 'ja': '<h2 class="rel-h">最新の更新</h2>'},
'<h2 class="rel-h">Previous updates</h2>': {
 'es': '<h2 class="rel-h">Novedades anteriores</h2>', 'zh': '<h2 class="rel-h">以往的更新</h2>',
 'ko': '<h2 class="rel-h">이전 업데이트</h2>', 'ja': '<h2 class="rel-h">これまでの更新</h2>'},
'<h2 class="rel-h">Using Kapture</h2>': {
 'es': '<h2 class="rel-h">Cómo usar Kapture</h2>', 'zh': '<h2 class="rel-h">使用 Kapture</h2>',
 'ko': '<h2 class="rel-h">Kapture 사용하기</h2>', 'ja': '<h2 class="rel-h">Kapture の使い方</h2>'},

# ---------------------------------------------------------------- 0.4.8
'>Version 0.4.8<': {'es': '>Versión 0.4.8<', 'zh': '>版本 0.4.8<',
                    'ko': '>버전 0.4.8<', 'ja': '>バージョン 0.4.8<'},
'>Version 0.4.7<': {'es': '>Versión 0.4.7<', 'zh': '>版本 0.4.7<',
                    'ko': '>버전 0.4.7<', 'ja': '>バージョン 0.4.7<'},
'>Version 0.4.6<': {'es': '>Versión 0.4.6<', 'zh': '>版本 0.4.6<',
                    'ko': '>버전 0.4.6<', 'ja': '>バージョン 0.4.6<'},

'</span>Current version</p>': {
 'es': '</span>Versión actual</p>', 'zh': '</span>当前版本</p>',
 'ko': '</span>현재 버전</p>', 'ja': '</span>現在のバージョン</p>'},

'<p class="rel-when">Released 25 September 2026</p>': {
 'es': '<p class="rel-when">Publicada el 25 de septiembre de 2026</p>',
 'zh': '<p class="rel-when">发布于 2026 年 9 月 25 日</p>',
 'ko': '<p class="rel-when">2026년 9월 25일 출시</p>',
 'ja': '<p class="rel-when">2026 年 9 月 25 日リリース</p>'},
'<span class="rel-when">16 September 2026</span>': {
 'es': '<span class="rel-when">16 de septiembre de 2026</span>',
 'zh': '<span class="rel-when">2026 年 9 月 16 日</span>',
 'ko': '<span class="rel-when">2026년 9월 16일</span>',
 'ja': '<span class="rel-when">2026 年 9 月 16 日</span>'},

'<p class="rel-sum">Kapture speaks five languages, History separates the captures you still have from the ones that are gone, and every new screenshot carries a small record of how it was taken.</p>': {
 'es': '<p class="rel-sum">Kapture habla cinco idiomas, el Historial separa las capturas que aún conservas de las que ya no están, y cada captura nueva lleva un pequeño registro de cómo se hizo.</p>',
 'zh': '<p class="rel-sum">Kapture 现在支持五种语言，历史记录会把仍保留的截图和已消失的记录分开，而且每张新截图都会带上一小段关于拍摄方式的记录。</p>',
 'ko': '<p class="rel-sum">Kapture가 다섯 개 언어를 지원하고, 기록에서 아직 남아 있는 캡처와 사라진 캡처를 나눠 보여 주며, 새로 만든 스크린샷마다 어떻게 찍었는지에 대한 작은 기록이 함께 담깁니다.</p>',
 'ja': '<p class="rel-sum">Kapture が 5 か国語に対応し、履歴では手元に残っているキャプチャと消えたキャプチャを分けて表示するようになりました。新しいスクリーンショットには、どう撮影されたかの小さな記録が含まれます。</p>'},

'<li><strong>Five languages.</strong> The side panel is available in English, Espa&ntilde;ol, &#31616;&#20307;&#20013;&#25991;, &#54620;&#44397;&#50612; and &#26085;&#26412;&#35486;.</li>': {
 'es': '<li><strong>Cinco idiomas.</strong> El panel lateral está disponible en English, Espa&ntilde;ol, &#31616;&#20307;&#20013;&#25991;, &#54620;&#44397;&#50612; y &#26085;&#26412;&#35486;.</li>',
 'zh': '<li><strong>五种语言。</strong>侧边栏支持 English、Espa&ntilde;ol、&#31616;&#20307;&#20013;&#25991;、&#54620;&#44397;&#50612; 和 &#26085;&#26412;&#35486;。</li>',
 'ko': '<li><strong>다섯 개 언어.</strong> 사이드 패널을 English, Espa&ntilde;ol, &#31616;&#20307;&#20013;&#25991;, &#54620;&#44397;&#50612;, &#26085;&#26412;&#35486;로 사용할 수 있습니다.</li>',
 'ja': '<li><strong>5 か国語に対応。</strong>サイドパネルは English、Espa&ntilde;ol、&#31616;&#20307;&#20013;&#25991;、&#54620;&#44397;&#50612;、&#26085;&#26412;&#35486; で利用できます。</li>'},

'<li><strong>Language setting.</strong> Settings has a Language control. It follows the browser language by default, and any choice you make is remembered.</li>': {
 'es': '<li><strong>Ajuste de idioma.</strong> Ajustes incluye un control de Idioma. De forma predeterminada sigue el idioma del navegador, y la opción que elijas se recuerda.</li>',
 'zh': '<li><strong>语言设置。</strong>设置中新增了语言选项。默认跟随浏览器语言，你选择的语言会被记住。</li>',
 'ko': '<li><strong>언어 설정.</strong> 설정에 언어 항목이 생겼습니다. 기본적으로 브라우저 언어를 따르며, 선택한 언어는 그대로 유지됩니다.</li>',
 'ja': '<li><strong>言語設定。</strong>設定に言語の項目を追加しました。既定ではブラウザーの言語に従い、選んだ言語は記憶されます。</li>'},

'<li><strong>Kept and Deleted History tabs.</strong> Captures whose file is still on the device are separated from records whose file has gone.</li>': {
 'es': '<li><strong>Pestañas Guardadas y Eliminadas en el Historial.</strong> Las capturas cuyo archivo sigue en el dispositivo se separan de los registros cuyo archivo ya no está.</li>',
 'zh': '<li><strong>历史记录分为“保留”和“已删除”两个标签页。</strong>文件仍在设备上的截图与文件已消失的记录分开显示。</li>',
 'ko': '<li><strong>기록의 보관됨·삭제됨 탭.</strong> 파일이 기기에 남아 있는 캡처와 파일이 사라진 기록을 나눠서 보여 줍니다.</li>',
 'ja': '<li><strong>履歴の「保存済み」と「削除済み」タブ。</strong>ファイルが端末に残っているキャプチャと、ファイルが失われた記録を分けて表示します。</li>'},

'<li><strong>Ten items per History page</strong>, up from six.</li>': {
 'es': '<li><strong>Diez elementos por página del Historial</strong>, antes eran seis.</li>',
 'zh': '<li><strong>历史记录每页显示十条</strong>，之前是六条。</li>',
 'ko': '<li><strong>기록 페이지당 10개 항목</strong>으로 늘었습니다. 이전에는 6개였습니다.</li>',
 'ja': '<li><strong>履歴は 1 ページ 10 件に。</strong>これまでは 6 件でした。</li>'},

'<li><strong>Success messages clear themselves</strong> after a few seconds. Errors and warnings stay until something replaces them.</li>': {
 'es': '<li><strong>Los mensajes de confirmación desaparecen solos</strong> al cabo de unos segundos. Los errores y los avisos permanecen hasta que algo los sustituye.</li>',
 'zh': '<li><strong>成功提示会自动消失</strong>，几秒后自动清除。错误和警告会一直显示，直到被其他消息替换。</li>',
 'ko': '<li><strong>완료 메시지는 몇 초 뒤 사라집니다.</strong> 오류와 경고는 다른 메시지가 나타날 때까지 남아 있습니다.</li>',
 'ja': '<li><strong>完了メッセージは数秒で自動的に消えます。</strong>エラーと警告は、別のメッセージに置き換わるまで表示され続けます。</li>'},

'<li><strong>Capture record inside the image.</strong> New PNG and JPEG captures carry the page address, website name, viewport, capture type and capture time inside the file itself. It stays on your device.</li>': {
 'es': '<li><strong>Registro de la captura dentro de la imagen.</strong> Las capturas nuevas en PNG y JPEG llevan dentro del propio archivo la dirección de la página, el nombre del sitio, el tamaño de ventana, el tipo de captura y la hora. Todo se queda en tu dispositivo.</li>',
 'zh': '<li><strong>图片内含截图记录。</strong>新的 PNG 和 JPEG 截图会在文件内部记录页面地址、网站名称、视口、截图类型和截图时间。这些信息只保存在你的设备上。</li>',
 'ko': '<li><strong>이미지 안에 담기는 캡처 기록.</strong> 새로 만든 PNG와 JPEG 캡처에는 페이지 주소, 사이트 이름, 뷰포트, 캡처 방식, 캡처 시각이 파일 안에 함께 저장됩니다. 이 정보는 기기에만 남습니다.</li>',
 'ja': '<li><strong>画像の中に残るキャプチャ記録。</strong>新しい PNG と JPEG のキャプチャには、ページのアドレス、サイト名、ビューポート、キャプチャの種類、撮影日時がファイル自体に記録されます。この情報は端末内にとどまります。</li>'},

'<li><strong>Current browser viewport fix.</strong> The recorded viewport is now the layout width the page was actually rendered at, so a page with a visible scrollbar is no longer recorded a few pixels too wide.</li>': {
 'es': '<li><strong>Corrección del tamaño de ventana en Navegador actual.</strong> Ahora se registra el ancho de maquetación con el que se representó la página, de modo que una página con barra de desplazamiento visible ya no queda registrada unos píxeles más ancha de lo real.</li>',
 'zh': '<li><strong>修复“当前浏览器”的视口记录。</strong>现在记录的是页面实际渲染时的布局宽度，带有可见滚动条的页面不会再被记成宽出几个像素。</li>',
 'ko': '<li><strong>현재 브라우저 뷰포트 수정.</strong> 이제 페이지가 실제로 그려진 레이아웃 너비를 기록하므로, 스크롤바가 보이는 페이지가 몇 픽셀 더 넓게 기록되지 않습니다.</li>',
 'ja': '<li><strong>「現在のブラウザー」のビューポート修正。</strong>ページが実際に描画されたレイアウト幅を記録するようになり、スクロールバーが表示されるページが数ピクセル広く記録されることがなくなりました。</li>'},

'<li><strong>Kapture Pro banner.</strong> A dismissible note about Kapture Pro for Mac, with a link to kaptapp.com.</li>': {
 'es': '<li><strong>Aviso de Kapture Pro.</strong> Una nota que puedes descartar sobre Kapture Pro para Mac, con un enlace a kaptapp.com.</li>',
 'zh': '<li><strong>Kapture Pro 提示卡片。</strong>介绍 Mac 版 Kapture Pro 的提示，可以随时关闭，并附有 kaptapp.com 的链接。</li>',
 'ko': '<li><strong>Kapture Pro 안내.</strong> Mac용 Kapture Pro를 소개하는 알림으로, 닫을 수 있으며 kaptapp.com 링크가 있습니다.</li>',
 'ja': '<li><strong>Kapture Pro のお知らせ。</strong>Mac 版 Kapture Pro を紹介する、閉じられるお知らせです。kaptapp.com へのリンクが付いています。</li>'},

'<li><strong>Refined footer.</strong> Settings and Privacy sit on the left, kaptapp.com on the right.</li>': {
 'es': '<li><strong>Pie de página depurado.</strong> Ajustes y Privacidad a la izquierda, kaptapp.com a la derecha.</li>',
 'zh': '<li><strong>页脚更清爽。</strong>设置和隐私在左侧，kaptapp.com 在右侧。</li>',
 'ko': '<li><strong>정돈된 하단 영역.</strong> 왼쪽에 설정과 개인정보, 오른쪽에 kaptapp.com이 있습니다.</li>',
 'ja': '<li><strong>フッターを整理。</strong>左に設定とプライバシー、右に kaptapp.com を配置しました。</li>'},

'<li><strong>Viewport labels name the device</strong> rather than repeating its pixel width.</li>': {
 'es': '<li><strong>Las etiquetas de tamaño de ventana nombran el dispositivo</strong> en lugar de repetir su ancho en píxeles.</li>',
 'zh': '<li><strong>视口标签直接显示设备名称</strong>，不再重复标注像素宽度。</li>',
 'ko': '<li><strong>뷰포트 라벨이 기기 이름을 표시합니다.</strong> 픽셀 너비를 반복해서 보여 주지 않습니다.</li>',
 'ja': '<li><strong>ビューポートのラベルに端末名を表示。</strong>ピクセル幅を繰り返し表示しなくなりました。</li>'},

'<li><strong>Closer to Kapture Pro.</strong> Panel spacing, controls and history cards were aligned with the Mac app, with a subtle Kapture teal in the header and footer.</li>': {
 'es': '<li><strong>Más cerca de Kapture Pro.</strong> El espaciado del panel, los controles y las tarjetas del historial se alinearon con la app de Mac, con un toque sutil del verde azulado de Kapture en la cabecera y el pie.</li>',
 'zh': '<li><strong>更接近 Kapture Pro。</strong>面板间距、控件和历史卡片与 Mac 应用保持一致，页眉和页脚带有淡淡的 Kapture 青色。</li>',
 'ko': '<li><strong>Kapture Pro에 더 가깝게.</strong> 패널 여백과 컨트롤, 기록 카드를 Mac 앱에 맞추고 상단과 하단에 은은한 Kapture 청록색을 더했습니다.</li>',
 'ja': '<li><strong>Kapture Pro に近づけました。</strong>パネルの余白、コントロール、履歴カードを Mac アプリに合わせ、ヘッダーとフッターに控えめな Kapture のティールを添えています。</li>'},

'<li><strong>Better contrast.</strong> Light mode secondary text was darkened to meet the 4.5:1 contrast ratio.</li>': {
 'es': '<li><strong>Mejor contraste.</strong> El texto secundario en modo claro se oscureció para alcanzar una relación de contraste de 4,5:1.</li>',
 'zh': '<li><strong>对比度更好。</strong>浅色模式下的次要文字已加深，达到 4.5:1 的对比度。</li>',
 'ko': '<li><strong>개선된 명암비.</strong> 라이트 모드의 보조 텍스트를 더 어둡게 조정해 4.5:1 명암비를 만족합니다.</li>',
 'ja': '<li><strong>コントラストを改善。</strong>ライトモードの補助テキストを濃くし、4.5:1 のコントラスト比を満たすようにしました。</li>'},

# ---------------------------------------------------------------- 0.4.7
'<p class="rel-sum">A save path that repairs itself, honest confirmation messages and multipart captures that number correctly.</p>': {
 'es': '<p class="rel-sum">Una ruta de guardado que se repara sola, mensajes de confirmación fieles a la realidad y capturas de varias partes numeradas correctamente.</p>',
 'zh': '<p class="rel-sum">保存路径会自我修复，确认消息如实反映结果，多张连续截图的编号也不再出错。</p>',
 'ko': '<p class="rel-sum">저장 경로가 스스로 복구되고, 확인 메시지가 실제 결과를 정확히 알려 주며, 여러 장으로 나뉜 캡처의 번호가 올바르게 매겨집니다.</p>',
 'ja': '<p class="rel-sum">保存先が自動的に修復され、確認メッセージが実際の結果どおりになり、分割キャプチャの番号も正しく振られます。</p>'},

'<li><strong>Legacy save folder migration.</strong> Older builds that stored <span class="rel-code">Kapture</span> as a Project name are corrected once, so captures no longer land in <span class="rel-code">Downloads/Kapture/Kapture</span>.</li>': {
 'es': '<li><strong>Migración de la carpeta de guardado antigua.</strong> Las versiones anteriores que guardaban <span class="rel-code">Kapture</span> como nombre de Proyecto se corrigen una sola vez, de modo que las capturas ya no acaban en <span class="rel-code">Downloads/Kapture/Kapture</span>.</li>',
 'zh': '<li><strong>迁移旧的保存文件夹。</strong>早期版本会把 <span class="rel-code">Kapture</span> 当作项目名称，现在会一次性修正，截图不会再保存到 <span class="rel-code">Downloads/Kapture/Kapture</span>。</li>',
 'ko': '<li><strong>이전 저장 폴더 정리.</strong> <span class="rel-code">Kapture</span>를 프로젝트 이름으로 저장하던 예전 버전의 설정을 한 번만 바로잡아, 캡처가 더 이상 <span class="rel-code">Downloads/Kapture/Kapture</span>에 저장되지 않습니다.</li>',
 'ja': '<li><strong>以前の保存フォルダーの移行。</strong><span class="rel-code">Kapture</span> をプロジェクト名として保存していた古いバージョンの設定を一度だけ修正し、キャプチャが <span class="rel-code">Downloads/Kapture/Kapture</span> に保存されないようにしました。</li>'},

'<li><strong>Accurate confirmations.</strong> Success messages name the folder the files actually went to.</li>': {
 'es': '<li><strong>Confirmaciones exactas.</strong> Los mensajes de confirmación indican la carpeta en la que realmente se guardaron los archivos.</li>',
 'zh': '<li><strong>准确的确认信息。</strong>成功提示会显示文件实际保存到的文件夹。</li>',
 'ko': '<li><strong>정확한 확인 메시지.</strong> 완료 메시지가 파일이 실제로 저장된 폴더를 알려 줍니다.</li>',
 'ja': '<li><strong>正確な確認メッセージ。</strong>完了メッセージに、ファイルが実際に保存されたフォルダー名が表示されます。</li>'},

'<li><strong>Sequential multipart numbering.</strong> A capture split into several images no longer skips numbers in the filenames.</li>': {
 'es': '<li><strong>Numeración correlativa en varias partes.</strong> Una captura dividida en varias imágenes ya no se salta números en los nombres de archivo.</li>',
 'zh': '<li><strong>分段截图连续编号。</strong>拆分成多张图片的截图不会再跳过文件名中的编号。</li>',
 'ko': '<li><strong>분할 캡처의 연속 번호.</strong> 여러 이미지로 나뉜 캡처의 파일 이름에서 번호가 건너뛰지 않습니다.</li>',
 'ja': '<li><strong>分割キャプチャの連番。</strong>複数の画像に分かれたキャプチャで、ファイル名の番号が飛ばなくなりました。</li>'},

'<li><strong>Production help and copy</strong> replaced the remaining prototype text.</li>': {
 'es': '<li><strong>Ayuda y textos definitivos</strong> en lugar del texto de prototipo que quedaba.</li>',
 'zh': '<li><strong>正式的帮助与文案</strong>取代了残留的原型文字。</li>',
 'ko': '<li><strong>정식 도움말과 문구</strong>가 남아 있던 시제품 문구를 대체했습니다.</li>',
 'ja': '<li><strong>正式なヘルプと文言</strong>が、残っていた試作版のテキストを置き換えました。</li>'},

# ---------------------------------------------------------------- 0.4.6
'<p class="rel-sum">The baseline. This is the published Chrome Web Store build, brought into version control unchanged so every later release can be compared against it.</p>': {
 'es': '<p class="rel-sum">El punto de partida. Es la versión publicada en Chrome Web Store, incorporada al control de versiones sin cambios para poder comparar con ella todas las versiones posteriores.</p>',
 'zh': '<p class="rel-sum">基准版本。这是已发布到 Chrome 应用商店的版本，原封不动地纳入版本管理，之后的每个版本都可以与它对比。</p>',
 'ko': '<p class="rel-sum">기준이 되는 버전입니다. Chrome 웹 스토어에 공개된 빌드를 그대로 버전 관리에 담아, 이후 모든 릴리스를 이 버전과 비교할 수 있습니다.</p>',
 'ja': '<p class="rel-sum">基準となるバージョンです。Chrome ウェブストアで公開されたビルドをそのままバージョン管理に取り込み、以降のリリースを比較できるようにしました。</p>'},

'<li>Full page and Select area capture, as PNG, JPEG or PDF.</li>': {
 'es': '<li>Captura de Página completa y de Seleccionar área, en PNG, JPEG o PDF.</li>',
 'zh': '<li>整页截图和选择区域截图，可保存为 PNG、JPEG 或 PDF。</li>',
 'ko': '<li>전체 페이지와 영역 선택 캡처를 PNG, JPEG, PDF로 저장.</li>',
 'ja': '<li>ページ全体と範囲を選択したキャプチャを、PNG・JPEG・PDF で保存。</li>'},

'<li>Current browser plus Phone, Tablet and two Desktop viewport presets.</li>': {
 'es': '<li>Navegador actual más los tamaños de ventana predefinidos de Teléfono, Tableta y dos de Escritorio.</li>',
 'zh': '<li>当前浏览器，以及手机、平板和两种桌面视口预设。</li>',
 'ko': '<li>현재 브라우저와 휴대폰, 태블릿, 두 가지 데스크톱 뷰포트 프리셋.</li>',
 'ja': '<li>現在のブラウザーに加え、スマートフォン・タブレット・デスクトップ 2 種類のビューポートプリセット。</li>'},

'<li>Local capture history with open and delete.</li>': {
 'es': '<li>Historial local de capturas con opciones de abrir y eliminar.</li>',
 'zh': '<li>本地截图历史记录，可打开和删除。</li>',
 'ko': '<li>열기와 삭제가 가능한 기기 내 캡처 기록.</li>',
 'ja': '<li>開く・削除ができる端末内のキャプチャ履歴。</li>'},

'<li>Saving into a <span class="rel-code">Kapture</span> folder, with an optional Project subfolder.</li>': {
 'es': '<li>Guardado en una carpeta <span class="rel-code">Kapture</span>, con una subcarpeta de Proyecto opcional.</li>',
 'zh': '<li>保存到 <span class="rel-code">Kapture</span> 文件夹，可选择再建一个项目子文件夹。</li>',
 'ko': '<li><span class="rel-code">Kapture</span> 폴더에 저장하며, 프로젝트 하위 폴더를 선택적으로 사용.</li>',
 'ja': '<li><span class="rel-code">Kapture</span> フォルダーに保存し、任意でプロジェクトのサブフォルダーも指定可能。</li>'},

# ---------------------------------------------------------------- using Kapture
'<h3>Capture from the side panel</h3>': {
 'es': '<h3>Capturar desde el panel lateral</h3>', 'zh': '<h3>从侧边栏截图</h3>',
 'ko': '<h3>사이드 패널에서 캡처하기</h3>', 'ja': '<h3>サイドパネルからキャプチャする</h3>'},
'<p>Click the Kapture icon on the website you want to capture. Choose Full page or Select area, and PNG, JPEG or PDF. Current browser uses the webpage width available beside the side panel. Keep the tab active while capture runs. Cancel stops the capture, and image parts already saved remain.</p>': {
 'es': '<p>Haz clic en el icono de Kapture en la web que quieras capturar. Elige Página completa o Seleccionar área, y PNG, JPEG o PDF. Navegador actual usa el ancho de página disponible junto al panel lateral. Mantén la pestaña activa mientras se ejecuta la captura. Cancelar detiene la captura, y las partes de imagen ya guardadas se conservan.</p>',
 'zh': '<p>在想要截图的网站上点击 Kapture 图标。选择整页或选择区域，以及 PNG、JPEG 或 PDF。当前浏览器使用侧边栏旁边可用的页面宽度。截图过程中请保持该标签页处于活动状态。取消会停止截图，已经保存的图片部分会保留。</p>',
 'ko': '<p>캡처하려는 사이트에서 Kapture 아이콘을 클릭하세요. 전체 페이지 또는 영역 선택을 고르고 PNG, JPEG, PDF 중에서 선택합니다. 현재 브라우저는 사이드 패널 옆에 남은 페이지 너비를 사용합니다. 캡처가 진행되는 동안에는 해당 탭을 활성 상태로 두세요. 취소하면 캡처가 멈추고, 이미 저장된 이미지 조각은 그대로 남습니다.</p>',
 'ja': '<p>キャプチャしたいサイトで Kapture のアイコンをクリックします。ページ全体か範囲を選択を選び、PNG・JPEG・PDF のいずれかを指定します。現在のブラウザーは、サイドパネルの横に残っているページ幅を使います。キャプチャ中はそのタブをアクティブなままにしてください。キャンセルするとキャプチャは停止し、すでに保存された画像はそのまま残ります。</p>'},

'<h3>Select an area</h3>': {
 'es': '<h3>Seleccionar una zona</h3>', 'zh': '<h3>选择一个区域</h3>',
 'ko': '<h3>영역 선택하기</h3>', 'ja': '<h3>範囲を選択する</h3>'},
'<p>Select area opens controls over the current webpage while the side panel stays visible. Choose Freeform, 1:1, 16:9 or 9:16, then drag over the visible part of the page. Move the selection or resize it from a corner before choosing Capture. Kapture hides its own controls before taking the image. Escape cancels. Selected-area capture uses the current browser view and native screen density, and does not continue beyond the visible screen.</p>': {
 'es': '<p>Seleccionar área abre controles sobre la página actual mientras el panel lateral sigue visible. Elige Libre, 1:1, 16:9 o 9:16 y arrastra sobre la parte visible de la página. Mueve la selección o cambia su tamaño desde una esquina antes de pulsar Capturar. Kapture oculta sus propios controles antes de tomar la imagen. Escape cancela. La captura de zona usa la vista actual del navegador y la densidad nativa de la pantalla, y no continúa más allá de la parte visible.</p>',
 'zh': '<p>选择区域会在当前网页上显示控件，同时侧边栏保持可见。选择自由、1:1、16:9 或 9:16，然后在页面可见部分拖动。按下捕获前，可以移动选区或从角落调整大小。Kapture 会在拍摄前隐藏自己的控件。按 Escape 取消。区域截图使用当前浏览器视图和屏幕原生像素密度，不会超出可见范围。</p>',
 'ko': '<p>영역 선택을 누르면 사이드 패널이 열린 채로 현재 페이지 위에 조작 버튼이 나타납니다. 자유형, 1:1, 16:9, 9:16 중에서 고른 뒤 페이지의 보이는 부분에서 드래그하세요. 캡처를 누르기 전에 선택 영역을 옮기거나 모서리를 끌어 크기를 조절할 수 있습니다. Kapture는 이미지를 찍기 전에 자체 조작 버튼을 숨깁니다. Escape 키로 취소합니다. 영역 캡처는 현재 브라우저 화면과 기기의 원래 화면 밀도를 사용하며, 보이는 화면을 넘어가지 않습니다.</p>',
 'ja': '<p>範囲を選択すると、サイドパネルを表示したまま現在のページの上に操作ボタンが現れます。フリーフォーム、1:1、16:9、9:16 から選び、ページの見えている部分をドラッグします。キャプチャを押す前に、選択範囲を動かしたり角をつまんでサイズを変えたりできます。Kapture は撮影の直前に自身の操作ボタンを隠します。Escape キーでキャンセルできます。範囲キャプチャは現在のブラウザー表示と端末本来の画面密度を使い、見えている画面より先には進みません。</p>'},

'<h3>Viewports</h3>': {
 'es': '<h3>Tamaños de ventana</h3>', 'zh': '<h3>视口</h3>',
 'ko': '<h3>뷰포트</h3>', 'ja': '<h3>ビューポート</h3>'},
'<p>Current browser preserves native screenshot density. Phone (390), Tablet (820), Desktop (1440) and Desktop (1920) render the page at the chosen width during capture, then restore it. These presets export at one image pixel per CSS pixel. They are responsive viewport presets, not exact replicas of physical devices. Chrome may show a debugging banner, so close DevTools before using a preset.</p>': {
 'es': '<p>Navegador actual conserva la densidad nativa de la captura. Teléfono (390), Tableta (820), Escritorio (1440) y Escritorio (1920) representan la página al ancho elegido durante la captura y después la restauran. Estos ajustes exportan a un píxel de imagen por píxel CSS. Son tamaños de ventana adaptables, no réplicas exactas de dispositivos físicos. Chrome puede mostrar un aviso de depuración, así que cierra las herramientas de desarrollo antes de usar uno.</p>',
 'zh': '<p>当前浏览器会保留截图的原生像素密度。手机 (390)、平板 (820)、桌面 (1440) 和桌面 (1920) 会在截图时按所选宽度渲染页面，之后再恢复。这些预设按每个 CSS 像素对应一个图片像素导出。它们是响应式视口预设，并不是实体设备的精确复制。Chrome 可能会显示调试提示条，因此使用预设前请先关闭开发者工具。</p>',
 'ko': '<p>현재 브라우저는 기기 본래의 스크린샷 밀도를 유지합니다. 휴대폰(390), 태블릿(820), 데스크톱(1440), 데스크톱(1920)은 캡처하는 동안 페이지를 해당 너비로 그린 뒤 원래대로 되돌립니다. 이 프리셋은 CSS 픽셀 하나당 이미지 픽셀 하나로 내보냅니다. 반응형 뷰포트 프리셋일 뿐, 실제 기기를 그대로 재현한 것은 아닙니다. Chrome이 디버깅 배너를 표시할 수 있으니 프리셋을 쓰기 전에 개발자 도구를 닫으세요.</p>',
 'ja': '<p>現在のブラウザーは、端末本来のスクリーンショット密度を保ちます。スマートフォン (390)、タブレット (820)、デスクトップ (1440)、デスクトップ (1920) は、キャプチャ中にページを指定の幅で描画し、その後もとに戻します。これらのプリセットは CSS ピクセル 1 つにつき画像ピクセル 1 つで書き出します。レスポンシブ表示のプリセットであり、実機を正確に再現するものではありません。Chrome がデバッグ用のバナーを表示することがあるため、プリセットを使う前にデベロッパーツールを閉じてください。</p>'},

'<p>Kapture captures the full main document, splitting at 8,000 image rows. Moving content is captured as it appears when each section is reached, so different sections are not captured at the same instant.</p>': {
 'es': '<p>Kapture captura el documento principal completo y lo divide cada 8.000 filas de imagen. El contenido en movimiento se captura tal como aparece al llegar a cada sección, de modo que las distintas secciones no se capturan en el mismo instante.</p>',
 'zh': '<p>Kapture 会截取整个主文档，每 8,000 行图像分割一次。动态内容按到达每个区块时的样子截取，因此不同区块并不是在同一瞬间拍下的。</p>',
 'ko': '<p>Kapture는 본문 전체를 캡처하며 이미지 8,000행마다 나눕니다. 움직이는 콘텐츠는 각 구간에 도달한 시점의 모습으로 담기므로, 서로 다른 구간이 같은 순간에 캡처되는 것은 아닙니다.</p>',
 'ja': '<p>Kapture はメインの文書全体をキャプチャし、画像 8,000 行ごとに分割します。動きのあるコンテンツは各区間に到達した時点の状態で記録されるため、異なる区間が同じ瞬間に撮影されるわけではありません。</p>'},

'<h3>Where captures are saved</h3>': {
 'es': '<h3>Dónde se guardan las capturas</h3>', 'zh': '<h3>截图保存在哪里</h3>',
 'ko': '<h3>캡처가 저장되는 위치</h3>', 'ja': '<h3>キャプチャの保存先</h3>'},
'<p>Kapture always saves new captures inside a <span class="rel-code">Kapture</span> folder in Chrome\'s download location, shown in Kapture as <span class="rel-code">Downloads/Kapture</span>. Leave the Project field empty to save directly there, or enter a Project name to save inside a subfolder such as <span class="rel-code">Downloads/Kapture/Research</span>. A Project is a single folder, so slashes and other characters that folder names cannot contain are replaced with a hyphen. Files are named after the website with a running number, such as <span class="rel-code">bbc_001.png</span>.</p>': {
 'es': '<p>Kapture guarda siempre las capturas nuevas dentro de una carpeta <span class="rel-code">Kapture</span> en la ubicación de descargas de Chrome, que en Kapture aparece como <span class="rel-code">Downloads/Kapture</span>. Deja el campo Proyecto vacío para guardar ahí directamente, o escribe un nombre de Proyecto para guardar en una subcarpeta como <span class="rel-code">Downloads/Kapture/Research</span>. Un Proyecto es una sola carpeta, así que las barras y otros caracteres que los nombres de carpeta no admiten se sustituyen por un guion. Los archivos se nombran según el sitio web con un número correlativo, por ejemplo <span class="rel-code">bbc_001.png</span>.</p>',
 'zh': '<p>Kapture 始终把新截图保存在 Chrome 下载位置中的 <span class="rel-code">Kapture</span> 文件夹里，在 Kapture 中显示为 <span class="rel-code">Downloads/Kapture</span>。项目字段留空即可直接保存在该文件夹，或者填写项目名称保存到子文件夹，例如 <span class="rel-code">Downloads/Kapture/Research</span>。项目只对应一层文件夹，因此斜杠和其他文件夹名称不允许的字符会替换成连字符。文件按网站名称加连续编号命名，例如 <span class="rel-code">bbc_001.png</span>。</p>',
 'ko': '<p>Kapture는 새 캡처를 항상 Chrome 다운로드 위치 안의 <span class="rel-code">Kapture</span> 폴더에 저장하며, Kapture에서는 <span class="rel-code">Downloads/Kapture</span>로 표시됩니다. 프로젝트 칸을 비워 두면 그 폴더에 바로 저장되고, 프로젝트 이름을 적으면 <span class="rel-code">Downloads/Kapture/Research</span>처럼 하위 폴더에 저장됩니다. 프로젝트는 폴더 한 단계이므로, 폴더 이름에 쓸 수 없는 슬래시 등의 문자는 하이픈으로 바뀝니다. 파일 이름은 사이트 이름과 일련번호로 지어지며 <span class="rel-code">bbc_001.png</span>과 같은 형태입니다.</p>',
 'ja': '<p>Kapture は新しいキャプチャを、必ず Chrome のダウンロード先にある <span class="rel-code">Kapture</span> フォルダーに保存します。Kapture 上では <span class="rel-code">Downloads/Kapture</span> と表示されます。プロジェクト欄を空のままにするとそのフォルダーに直接保存され、プロジェクト名を入力すると <span class="rel-code">Downloads/Kapture/Research</span> のようなサブフォルダーに保存されます。プロジェクトはフォルダー 1 階層なので、フォルダー名に使えないスラッシュなどの文字はハイフンに置き換えられます。ファイル名はサイト名と連番で、<span class="rel-code">bbc_001.png</span> のようになります。</p>'},

'<p>The download location is the one set in Chrome settings, which is usually your Downloads folder. To save somewhere else, change the download location in Chrome.</p>': {
 'es': '<p>La ubicación de descargas es la que está configurada en los ajustes de Chrome, que suele ser tu carpeta de descargas. Para guardar en otro sitio, cambia la ubicación de descargas en Chrome.</p>',
 'zh': '<p>下载位置由 Chrome 设置决定，通常是你的下载文件夹。想保存到别处，请在 Chrome 中修改下载位置。</p>',
 'ko': '<p>다운로드 위치는 Chrome 설정에 지정된 폴더이며, 보통 다운로드 폴더입니다. 다른 곳에 저장하려면 Chrome에서 다운로드 위치를 바꾸세요.</p>',
 'ja': '<p>ダウンロード先は Chrome の設定で指定した場所で、通常はダウンロードフォルダーです。別の場所に保存したい場合は、Chrome でダウンロード先を変更してください。</p>'},

'<h3>PDF export</h3>': {
 'es': '<h3>Exportar a PDF</h3>', 'zh': '<h3>导出 PDF</h3>',
 'ko': '<h3>PDF로 내보내기</h3>', 'ja': '<h3>PDF への書き出し</h3>'},
'<p>PDF creates one local, multi-page PDF. Each section of up to 8,000 captured image rows becomes one PDF page. The pages use JPEG compression internally to keep the file practical. PNG and JPEG remain available when an image file is preferred.</p>': {
 'es': '<p>PDF crea un único PDF local de varias páginas. Cada sección de hasta 8.000 filas de imagen capturadas se convierte en una página del PDF. Internamente las páginas usan compresión JPEG para que el archivo siga siendo manejable. PNG y JPEG siguen disponibles si prefieres un archivo de imagen.</p>',
 'zh': '<p>PDF 会在本地生成一个多页 PDF。每段最多 8,000 行的截图内容会成为一页 PDF。页面内部使用 JPEG 压缩，以保持文件大小实用。如果更需要图片文件，仍然可以选择 PNG 和 JPEG。</p>',
 'ko': '<p>PDF를 고르면 여러 쪽짜리 PDF 하나가 기기에 만들어집니다. 최대 8,000행씩 캡처된 각 구간이 PDF 한 쪽이 됩니다. 파일 크기를 적당히 유지하기 위해 내부적으로 JPEG 압축을 사용합니다. 이미지 파일이 더 편하다면 PNG와 JPEG도 그대로 쓸 수 있습니다.</p>',
 'ja': '<p>PDF を選ぶと、複数ページの PDF が端末内に 1 つ作成されます。最大 8,000 行ずつキャプチャされた各区間が PDF の 1 ページになります。ファイルサイズを実用的に保つため、ページ内部では JPEG 圧縮を使っています。画像ファイルのほうが都合がよい場合は、PNG と JPEG も引き続き利用できます。</p>'},

'<h3>History</h3>': {
 'es': '<h3>Historial</h3>', 'zh': '<h3>历史记录</h3>',
 'ko': '<h3>기록</h3>', 'ja': '<h3>履歴</h3>'},
'<p>Each saved PNG or JPEG part adds one compact history entry, and a complete PDF adds one entry. History is newest first, with ten entries per page, split into Kept and Deleted tabs. Open launches an available file using the computer\'s normal application. Select individual cards, or Select all across the current tab, then use the bin and confirm in the dialog to permanently delete the screenshot files and remove their records. Refresh asks Chrome to check availability again.</p>': {
 'es': '<p>Cada parte guardada en PNG o JPEG añade una entrada compacta al historial, y un PDF completo añade una entrada. El historial se ordena de más reciente a más antiguo, con diez entradas por página, repartidas en las pestañas Guardadas y Eliminadas. Abrir inicia un archivo disponible con la aplicación habitual del ordenador. Selecciona tarjetas sueltas, o Seleccionar todo dentro de la pestaña actual, y luego usa la papelera y confirma en el diálogo para eliminar de forma permanente los archivos de captura y borrar sus registros. Actualizar pide a Chrome que vuelva a comprobar la disponibilidad.</p>',
 'zh': '<p>每保存一段 PNG 或 JPEG 都会新增一条简洁的历史记录，一个完整的 PDF 也算一条。历史记录按时间从新到旧排列，每页十条，分为“保留”和“已删除”两个标签页。打开会用电脑的默认应用启动可用的文件。你可以逐个选择卡片，或在当前标签页中全选，然后点击垃圾桶并在对话框中确认，即可永久删除截图文件并移除对应记录。刷新会让 Chrome 重新检查文件是否仍然可用。</p>',
 'ko': '<p>저장된 PNG 또는 JPEG 조각마다 간결한 기록이 하나씩 추가되고, 완성된 PDF도 하나의 기록이 됩니다. 기록은 최신순으로 한 쪽에 10개씩, 보관됨과 삭제됨 탭으로 나뉘어 표시됩니다. 열기를 누르면 컴퓨터의 기본 앱으로 파일이 열립니다. 카드를 하나씩 선택하거나 현재 탭에서 전체 선택한 뒤 휴지통을 누르고 대화상자에서 확인하면, 스크린샷 파일이 완전히 삭제되고 기록도 사라집니다. 새로 고침을 누르면 Chrome이 파일이 남아 있는지 다시 확인합니다.</p>',
 'ja': '<p>保存された PNG または JPEG のパーツごとに履歴が 1 件ずつ追加され、完成した PDF も 1 件として記録されます。履歴は新しい順に 1 ページ 10 件で、「保存済み」と「削除済み」のタブに分かれています。開くを押すと、パソコンの通常のアプリでファイルが開きます。カードを個別に選ぶか、現在のタブで全選択したあと、ごみ箱を押してダイアログで確認すると、スクリーンショットのファイルが完全に削除され、履歴からも消えます。更新を押すと、Chrome がファイルの有無を確認し直します。</p>'},

'<p>Chrome\'s existence check can lag, and a file moved or renamed outside Chrome may no longer be locatable. Existing filenames are never overwritten: Chrome adds a collision suffix instead.</p>': {
 'es': '<p>La comprobación de existencia de Chrome puede ir con retraso, y un archivo movido o renombrado fuera de Chrome quizá ya no se pueda localizar. Los nombres de archivo existentes nunca se sobrescriben: Chrome añade un sufijo para evitar la colisión.</p>',
 'zh': '<p>Chrome 检查文件是否存在可能会有延迟，在 Chrome 之外移动或重命名的文件可能就找不到了。已有的文件名永远不会被覆盖：Chrome 会另外加上一个后缀。</p>',
 'ko': '<p>Chrome의 파일 확인은 조금 늦을 수 있고, Chrome 밖에서 옮기거나 이름을 바꾼 파일은 더 이상 찾지 못할 수 있습니다. 기존 파일 이름을 덮어쓰는 일은 없으며, Chrome이 대신 뒤에 구분용 접미사를 붙입니다.</p>',
 'ja': '<p>Chrome によるファイルの存在確認は遅れることがあり、Chrome の外で移動したり名前を変えたりしたファイルは見つけられなくなる場合があります。既存のファイル名が上書きされることはなく、Chrome が代わりに重複回避の接尾辞を付けます。</p>'},

'<h3>What the image file records</h3>': {
 'es': '<h3>Qué registra el archivo de imagen</h3>', 'zh': '<h3>图片文件记录了什么</h3>',
 'ko': '<h3>이미지 파일에 기록되는 정보</h3>', 'ja': '<h3>画像ファイルに記録される情報</h3>'},
'<p>New PNG and JPEG captures carry a small record inside the image file: the page address, the website name, the viewport used, the capture type and the time of capture. It travels with the file so Kapture Pro for Mac can read it, and it stays on your device. Anyone you send a screenshot to can read that record, so share captures of private pages with the same care you already use for the picture itself.</p>': {
 'es': '<p>Las capturas nuevas en PNG y JPEG llevan un pequeño registro dentro del archivo de imagen: la dirección de la página, el nombre del sitio, el tamaño de ventana utilizado, el tipo de captura y la hora. Viaja con el archivo para que Kapture Pro para Mac pueda leerlo, y se queda en tu dispositivo. Cualquier persona a la que envíes una captura puede leer ese registro, así que comparte capturas de páginas privadas con el mismo cuidado que ya aplicas a la propia imagen.</p>',
 'zh': '<p>新的 PNG 和 JPEG 截图会在图片文件内部带上一小段记录：页面地址、网站名称、所用视口、截图类型和截图时间。它随文件一起保存，供 Mac 版 Kapture Pro 读取，并且只留在你的设备上。收到截图的人也能读到这段记录，因此分享私密页面的截图时，请像对待图片本身一样谨慎。</p>',
 'ko': '<p>새로 만든 PNG와 JPEG 캡처에는 이미지 파일 안에 작은 기록이 담깁니다. 페이지 주소, 사이트 이름, 사용한 뷰포트, 캡처 방식, 캡처 시각입니다. 이 기록은 Mac용 Kapture Pro가 읽을 수 있도록 파일과 함께 이동하며, 기기에만 남습니다. 스크린샷을 받은 사람도 이 기록을 볼 수 있으니, 비공개 페이지의 캡처는 사진 자체를 다룰 때와 똑같이 신중하게 공유하세요.</p>',
 'ja': '<p>新しい PNG と JPEG のキャプチャには、画像ファイルの中に小さな記録が含まれます。ページのアドレス、サイト名、使用したビューポート、キャプチャの種類、撮影日時です。この記録は Mac 版 Kapture Pro が読み取れるようファイルとともに保存され、端末内にとどまります。スクリーンショットを受け取った人もこの記録を読めるため、非公開ページのキャプチャは画像そのものと同じ注意を払って共有してください。</p>'},

'<h3>Permissions</h3>': {
 'es': '<h3>Permisos</h3>', 'zh': '<h3>权限</h3>',
 'ko': '<h3>권한</h3>', 'ja': '<h3>権限</h3>'},
'<p>activeTab grants temporary access after you click the icon. scripting runs the page capture. downloads saves, checks and deletes Kapture\'s files. downloads.open opens a screenshot only after its history button is clicked. sidePanel provides the interface. storage keeps local history, folder, theme, language and capture status. Debugger access applies viewport presets and captures device-sized images, and Kapture detaches afterwards, including on handled failures. Kapture does not request permanent host access, browsing history or cookies.</p>': {
 'es': '<p>activeTab concede acceso temporal después de que hagas clic en el icono. scripting ejecuta la captura de la página. downloads guarda, comprueba y elimina los archivos de Kapture. downloads.open abre una captura solo después de pulsar su botón en el historial. sidePanel proporciona la interfaz. storage conserva el historial local, la carpeta, el tema, el idioma y el estado de la captura. El acceso de depuración aplica los tamaños de ventana predefinidos y captura imágenes al tamaño del dispositivo; Kapture se desconecta al terminar, también cuando se produce un error controlado. Kapture no solicita acceso permanente a sitios, ni al historial de navegación ni a las cookies.</p>',
 'zh': '<p>activeTab 在你点击图标后授予临时访问权限。scripting 用于执行页面截图。downloads 用于保存、检查和删除 Kapture 的文件。downloads.open 只在你点击历史记录中的按钮后才打开截图。sidePanel 提供界面。storage 保存本地历史记录、文件夹、主题、语言和截图状态。调试权限用于应用视口预设并截取设备尺寸的图片，Kapture 会在结束后断开连接，遇到已处理的错误时同样如此。Kapture 不会请求永久的网站访问权限、浏览历史或 Cookie。</p>',
 'ko': '<p>activeTab은 아이콘을 클릭한 뒤 일시적인 접근 권한을 줍니다. scripting은 페이지 캡처를 실행합니다. downloads는 Kapture의 파일을 저장하고 확인하고 삭제합니다. downloads.open은 기록에서 버튼을 눌렀을 때만 스크린샷을 엽니다. sidePanel은 인터페이스를 제공합니다. storage는 기기 내 기록과 폴더, 테마, 언어, 캡처 상태를 보관합니다. 디버거 권한은 뷰포트 프리셋을 적용하고 기기 크기의 이미지를 캡처하는 데 쓰이며, 처리된 오류가 발생한 경우를 포함해 작업이 끝나면 Kapture가 연결을 해제합니다. Kapture는 사이트에 대한 영구 접근 권한이나 방문 기록, 쿠키를 요청하지 않습니다.</p>',
 'ja': '<p>activeTab は、アイコンをクリックしたあとの一時的なアクセスを許可します。scripting はページのキャプチャを実行します。downloads は Kapture のファイルの保存・確認・削除を行います。downloads.open は、履歴のボタンを押したときにだけスクリーンショットを開きます。sidePanel はインターフェースを提供します。storage は端末内の履歴、フォルダー、テーマ、言語、キャプチャの状態を保持します。デバッガー権限はビューポートのプリセットを適用し、端末サイズの画像をキャプチャするために使われ、処理済みのエラーが起きた場合も含め、終了後に Kapture は接続を解除します。Kapture はサイトへの恒久的なアクセス権、閲覧履歴、Cookie を要求しません。</p>'},

'<h3>Limits</h3>': {
 'es': '<h3>Límites</h3>', 'zh': '<h3>限制</h3>',
 'ko': '<h3>제한 사항</h3>', 'ja': '<h3>制限事項</h3>'},
'<p>Chrome-protected pages, including the Chrome Web Store, browser settings and some embedded viewers, cannot be captured. Area selection is limited to the visible webpage. Independent scroll panels, virtualised content and complex sticky layouts may need additional handling. Full-page capture stops at 300 screens to avoid endless feeds, and large images depend on browser memory.</p>': {
 'es': '<p>Las páginas protegidas por Chrome, incluidas Chrome Web Store, los ajustes del navegador y algunos visores incrustados, no se pueden capturar. La selección de zona se limita a la parte visible de la página. Los paneles con desplazamiento propio, el contenido virtualizado y los diseños fijos complejos pueden requerir un tratamiento adicional. La captura de página completa se detiene a las 300 pantallas para evitar los feeds infinitos, y las imágenes grandes dependen de la memoria del navegador.</p>',
 'zh': '<p>受 Chrome 保护的页面无法截图，包括 Chrome 应用商店、浏览器设置和部分内嵌查看器。区域选择只限于页面可见部分。独立滚动面板、虚拟化内容和复杂的吸顶布局可能需要额外处理。整页截图最多到 300 屏，以避免无限信息流，而大图能否生成取决于浏览器内存。</p>',
 'ko': '<p>Chrome 웹 스토어, 브라우저 설정, 일부 내장 뷰어를 비롯해 Chrome이 보호하는 페이지는 캡처할 수 없습니다. 영역 선택은 화면에 보이는 부분으로 제한됩니다. 따로 스크롤되는 패널, 가상화된 콘텐츠, 복잡한 고정 레이아웃은 추가 처리가 필요할 수 있습니다. 전체 페이지 캡처는 끝없이 이어지는 피드를 막기 위해 300화면에서 멈추며, 큰 이미지는 브라우저 메모리에 좌우됩니다.</p>',
 'ja': '<p>Chrome ウェブストア、ブラウザーの設定、一部の埋め込みビューアーなど、Chrome が保護しているページはキャプチャできません。範囲選択は表示中のページ内に限られます。独立してスクロールするパネル、仮想化されたコンテンツ、複雑な固定レイアウトは追加の対応が必要になることがあります。ページ全体のキャプチャは、終わりのないフィードを避けるため 300 画面で停止します。大きな画像はブラウザーのメモリに依存します。</p>'},

'<h3>Privacy</h3>': {
 'es': '<h3>Privacidad</h3>', 'zh': '<h3>隐私</h3>',
 'ko': '<h3>개인정보</h3>', 'ja': '<h3>プライバシー</h3>'},
'<p>Kapture processes the selected page\'s visible pixels and layout on your device. No screenshots, URLs, website content or usage data are sent to the developer or to third parties. The full policy is on the <a href="/privacy/">privacy page</a>.</p>': {
 'es': '<p>Kapture procesa en tu dispositivo los píxeles visibles y la maquetación de la página seleccionada. No se envían capturas, URL, contenido de sitios web ni datos de uso al desarrollador ni a terceros. La política completa está en la <a href="/privacy/">página de privacidad</a>.</p>',
 'zh': '<p>Kapture 在你的设备上处理所选页面的可见像素和布局。截图、网址、网站内容和使用数据都不会发送给开发者或第三方。完整政策见<a href="/privacy/">隐私页面</a>。</p>',
 'ko': '<p>Kapture는 선택한 페이지의 보이는 픽셀과 레이아웃을 기기 안에서 처리합니다. 스크린샷, URL, 사이트 내용, 사용 데이터를 개발자나 제3자에게 보내지 않습니다. 전체 방침은 <a href="/privacy/">개인정보 페이지</a>에서 확인할 수 있습니다.</p>',
 'ja': '<p>Kapture は、選択したページの表示部分のピクセルとレイアウトを端末内で処理します。スクリーンショット、URL、サイトの内容、利用データが開発者や第三者に送信されることはありません。詳細は<a href="/privacy/">プライバシーページ</a>をご覧ください。</p>'},

}
