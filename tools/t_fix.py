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

}
