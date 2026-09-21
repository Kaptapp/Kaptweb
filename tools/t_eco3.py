# -*- coding: utf-8 -*-
"""Curation pass: hero labels, per-mode flows, the six-point spotlight."""

ECO3 = {
'<p class="stage-label"><span class="stage-dot" aria-hidden="true"></span>Kapture&nbsp;Pro <em>for Mac</em></p>': {
 'es': '<p class="stage-label"><span class="stage-dot" aria-hidden="true"></span>Kapture&nbsp;Pro <em>para Mac</em></p>',
 'zh': '<p class="stage-label"><span class="stage-dot" aria-hidden="true"></span>Kapture&nbsp;Pro <em>Mac 版</em></p>',
 'ko': '<p class="stage-label"><span class="stage-dot" aria-hidden="true"></span>Kapture&nbsp;Pro <em>Mac용</em></p>',
 'ja': '<p class="stage-label"><span class="stage-dot" aria-hidden="true"></span>Kapture&nbsp;Pro <em>Mac 版</em></p>'},

'<p class="stage-label stage-label-front"><span class="stage-dot" aria-hidden="true"></span>Kapture <em>for Chrome</em></p>': {
 'es': '<p class="stage-label stage-label-front"><span class="stage-dot" aria-hidden="true"></span>Kapture <em>para Chrome</em></p>',
 'zh': '<p class="stage-label stage-label-front"><span class="stage-dot" aria-hidden="true"></span>Kapture <em>Chrome 版</em></p>',
 'ko': '<p class="stage-label stage-label-front"><span class="stage-dot" aria-hidden="true"></span>Kapture <em>Chrome용</em></p>',
 'ja': '<p class="stage-label stage-label-front"><span class="stage-dot" aria-hidden="true"></span>Kapture <em>Chrome 版</em></p>'},

'<figcaption>The Chrome extension captures. The Mac app organises what it captures.</figcaption>': {
 'es': '<figcaption>La extensión de Chrome captura. La app de Mac organiza lo capturado.</figcaption>',
 'zh': '<figcaption>Chrome 扩展负责截图，Mac 应用负责整理这些截图。</figcaption>',
 'ko': '<figcaption>Chrome 확장 프로그램이 캡처하고, Mac 앱이 그 캡처를 정리합니다.</figcaption>',
 'ja': '<figcaption>Chrome 拡張機能が撮り、Mac アプリがそれを整理します。</figcaption>'},

# ---- Full page flow ----
'''            <li><span>1</span>Pick a project folder and hit <b>Capture page</b>.</li>
            <li><span>2</span>Kapture scrolls the whole document, not just the visible part.</li>
            <li><span>3</span>Saved to your project, split at 8,000&nbsp;pixels so files stay usable.</li>''': {
 'es': '''            <li><span>1</span>Elige una carpeta de proyecto y pulsa <b>Capture page</b>.</li>
            <li><span>2</span>Kapture recorre todo el documento, no solo la parte visible.</li>
            <li><span>3</span>Se guarda en tu proyecto, dividido en secciones de 8.000&nbsp;píxeles.</li>''',
 'zh': '''            <li><span>1</span>选好项目文件夹，点 <b>Capture page</b>。</li>
            <li><span>2</span>Kapture 会滚动整个文档，而不只是可见的部分。</li>
            <li><span>3</span>保存到你的项目里，按 8,000&nbsp;像素分段，文件好用。</li>''',
 'ko': '''            <li><span>1</span>프로젝트 폴더를 고르고 <b>Capture page</b>를 누릅니다.</li>
            <li><span>2</span>Kapture가 보이는 부분만이 아니라 문서 전체를 스크롤합니다.</li>
            <li><span>3</span>프로젝트에 저장되고, 8,000&nbsp;픽셀 단위로 나뉩니다.</li>''',
 'ja': '''            <li><span>1</span>プロジェクトフォルダを選んで <b>Capture page</b> を押します。</li>
            <li><span>2</span>Kapture が表示範囲だけでなくドキュメント全体をスクロールします。</li>
            <li><span>3</span>プロジェクトに保存。8,000&nbsp;ピクセルごとに分割されます。</li>'''},

# ---- Select area flow ----
'''            <li><span>1</span>Switch the panel to <b>Select area</b>.</li>
            <li><span>2</span>Drag over the page. Freeform, 1:1, 16:9 or 9:16, resize before you commit.</li>
            <li><span>3</span>Only that region is captured, into the same project.</li>''': {
 'es': '''            <li><span>1</span>Cambia el panel a <b>Select area</b>.</li>
            <li><span>2</span>Arrastra sobre la página. Formato libre, 1:1, 16:9 o 9:16, y ajusta antes de confirmar.</li>
            <li><span>3</span>Solo se captura esa zona, en el mismo proyecto.</li>''',
 'zh': '''            <li><span>1</span>把面板切到 <b>Select area</b>。</li>
            <li><span>2</span>在页面上拖动。自由比例、1:1、16:9 或 9:16，确认前还能调整。</li>
            <li><span>3</span>只截取那块区域，存进同一个项目。</li>''',
 'ko': '''            <li><span>1</span>패널을 <b>Select area</b>로 바꿉니다.</li>
            <li><span>2</span>페이지 위를 드래그하세요. 자유 비율, 1:1, 16:9, 9:16으로 확정 전에 조정할 수 있습니다.</li>
            <li><span>3</span>그 영역만 같은 프로젝트에 캡처됩니다.</li>''',
 'ja': '''            <li><span>1</span>パネルを <b>Select area</b> に切り替えます。</li>
            <li><span>2</span>ページ上をドラッグ。フリー、1:1、16:9、9:16 から選び、決める前に調整できます。</li>
            <li><span>3</span>その範囲だけを、同じプロジェクトに保存します。</li>'''},

# ---- Kapture Pro onboarding visual ----
'alt="Kapture Pro on macOS welcoming a new library: captures fanned out above the line Your captures deserve better."': {
 'es': 'alt="Kapture Pro en macOS dando la bienvenida a una biblioteca nueva: capturas desplegadas sobre la frase Your captures deserve better."',
 'zh': 'alt="macOS 上的 Kapture Pro 欢迎新图库：一排截图展开在 Your captures deserve better 这句话上方。"',
 'ko': 'alt="새 라이브러리를 맞이하는 macOS의 Kapture Pro: Your captures deserve better 문구 위로 캡처들이 펼쳐져 있습니다."',
 'ja': 'alt="新しいライブラリを迎える macOS 上の Kapture Pro：Your captures deserve better の一文の上にキャプチャが扇状に並んでいます。"'},

'<figcaption>Kapture Pro on first run.</figcaption>': {
 'es': '<figcaption>Kapture Pro al abrirlo por primera vez.</figcaption>',
 'zh': '<figcaption>第一次打开 Kapture Pro 时。</figcaption>',
 'ko': '<figcaption>Kapture Pro를 처음 실행했을 때.</figcaption>',
 'ja': '<figcaption>Kapture Pro の初回起動時。</figcaption>'},

'alt="The Kapture Pro library on macOS: projects in the sidebar, a search field in the header, a grid of captures, and the inspector on the right."': {
 'es': 'alt="La biblioteca de Kapture Pro en macOS: los proyectos en la barra lateral, un campo de búsqueda en la cabecera, una cuadrícula de capturas y el inspector a la derecha."',
 'zh': 'alt="macOS 上的 Kapture Pro 图库：侧边栏是项目，顶部是搜索框，中间是截图网格，右侧是检查器。"',
 'ko': 'alt="macOS의 Kapture Pro 라이브러리: 사이드바의 프로젝트, 헤더의 검색창, 캡처 격자, 오른쪽의 인스펙터."',
 'ja': 'alt="macOS 上の Kapture Pro のライブラリ：サイドバーにプロジェクト、ヘッダーに検索欄、中央にキャプチャの一覧、右にインスペクタ。"'},

# ---- the six spotlight points ----
'''          <li data-spot="1,29,13,20"><button type="button"><h3>Projects</h3><p>Every capture folder becomes a project you can move between.</p></button></li>
          <li data-spot="39,0.5,22,4.5"><button type="button"><h3>Search</h3><p>Find a capture by name, site or project without opening Finder.</p></button></li>
          <li data-spot="14.5,12,69,86"><button type="button"><h3>Visual library</h3><p>Browse everything as previews instead of filenames.</p></button></li>
          <li data-spot="83,11,17,88"><button type="button"><h3>Inspector</h3><p>Size, format, source and capture time for whatever you select.</p></button></li>
          <li data-spot="21,40,10,5"><button type="button"><h3>Tags and notes</h3><p>Add your own context so a capture still makes sense later.</p></button></li>
          <li data-spot="1,91,13,7"><button type="button"><h3>Local storage</h3><p>No cloud, no sync, no account. It reads the disk you already have.</p></button></li>''': {
 'es': '''          <li data-spot="1,29,13,20"><button type="button"><h3>Proyectos</h3><p>Cada carpeta de capturas es un proyecto por el que puedes moverte.</p></button></li>
          <li data-spot="39,0.5,22,4.5"><button type="button"><h3>Búsqueda</h3><p>Encuentra una captura por nombre, sitio o proyecto sin abrir el Finder.</p></button></li>
          <li data-spot="14.5,12,69,86"><button type="button"><h3>Biblioteca visual</h3><p>Navega con vistas previas en lugar de nombres de archivo.</p></button></li>
          <li data-spot="83,11,17,88"><button type="button"><h3>Inspector</h3><p>Tamaño, formato, origen y hora de captura de lo que selecciones.</p></button></li>
          <li data-spot="21,40,10,5"><button type="button"><h3>Etiquetas y notas</h3><p>Añade tu propio contexto para que una captura siga teniendo sentido.</p></button></li>
          <li data-spot="1,91,13,7"><button type="button"><h3>Todo en local</h3><p>Sin nube, sin sincronización, sin cuenta. Lee el disco que ya tienes.</p></button></li>''',
 'zh': '''          <li data-spot="1,29,13,20"><button type="button"><h3>项目</h3><p>每个截图文件夹都会变成一个可以随时切换的项目。</p></button></li>
          <li data-spot="39,0.5,22,4.5"><button type="button"><h3>搜索</h3><p>不用打开访达，按名称、网站或项目就能找到截图。</p></button></li>
          <li data-spot="14.5,12,69,86"><button type="button"><h3>可视化图库</h3><p>用预览图浏览一切，而不是一串文件名。</p></button></li>
          <li data-spot="83,11,17,88"><button type="button"><h3>检查器</h3><p>选中任意一张，就能看到尺寸、格式、来源和截图时间。</p></button></li>
          <li data-spot="21,40,10,5"><button type="button"><h3>标签与备注</h3><p>加上自己的说明，过段时间再看也知道这张是什么。</p></button></li>
          <li data-spot="1,91,13,7"><button type="button"><h3>本地存储</h3><p>没有云端，不用同步，不用账号。它读的就是你现有的硬盘。</p></button></li>''',
 'ko': '''          <li data-spot="1,29,13,20"><button type="button"><h3>프로젝트</h3><p>캡처 폴더 하나하나가 오가며 작업할 수 있는 프로젝트가 됩니다.</p></button></li>
          <li data-spot="39,0.5,22,4.5"><button type="button"><h3>검색</h3><p>Finder를 열지 않고도 이름, 사이트, 프로젝트로 캡처를 찾습니다.</p></button></li>
          <li data-spot="14.5,12,69,86"><button type="button"><h3>시각 라이브러리</h3><p>파일 이름이 아니라 미리보기로 전체를 훑어봅니다.</p></button></li>
          <li data-spot="83,11,17,88"><button type="button"><h3>인스펙터</h3><p>고른 항목의 크기, 형식, 출처, 캡처 시각을 바로 확인합니다.</p></button></li>
          <li data-spot="21,40,10,5"><button type="button"><h3>태그와 메모</h3><p>직접 맥락을 남겨 두면 나중에 봐도 무슨 캡처인지 압니다.</p></button></li>
          <li data-spot="1,91,13,7"><button type="button"><h3>로컬 저장</h3><p>클라우드도, 동기화도, 계정도 없습니다. 이미 있는 디스크를 읽을 뿐입니다.</p></button></li>''',
 'ja': '''          <li data-spot="1,29,13,20"><button type="button"><h3>プロジェクト</h3><p>キャプチャのフォルダが、そのまま行き来できるプロジェクトになります。</p></button></li>
          <li data-spot="39,0.5,22,4.5"><button type="button"><h3>検索</h3><p>Finder を開かずに、名前・サイト・プロジェクトから探せます。</p></button></li>
          <li data-spot="14.5,12,69,86"><button type="button"><h3>ビジュアルライブラリ</h3><p>ファイル名ではなくプレビューで全体を見渡せます。</p></button></li>
          <li data-spot="83,11,17,88"><button type="button"><h3>インスペクタ</h3><p>選んだものの大きさ、形式、取得元、撮影日時をその場で確認できます。</p></button></li>
          <li data-spot="21,40,10,5"><button type="button"><h3>タグとメモ</h3><p>自分で文脈を書き添えておけば、後から見ても用途がわかります。</p></button></li>
          <li data-spot="1,91,13,7"><button type="button"><h3>ローカル保存</h3><p>クラウドも同期もアカウントも不要。手元のディスクを読むだけです。</p></button></li>'''},
}
