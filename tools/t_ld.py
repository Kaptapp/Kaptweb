# -*- coding: utf-8 -*-
"""Localised JSON-LD prose. Factual fields (name, category, version, installUrl) stay identical."""

APP_DESC = {
 'en': 'Kapture is a Chrome extension that captures a complete webpage or a selected area of it and saves the result on your own device as a PNG, JPEG or PDF.',
 'es': 'Kapture es una extensión de Chrome que captura una página web entera o solo una zona y guarda el resultado en tu propio dispositivo en PNG, JPEG o PDF.',
 'zh': 'Kapture 是一款 Chrome 扩展程序，可以截取整个网页或其中指定的区域，并以 PNG、JPEG 或 PDF 保存到你自己的设备上。',
 'ko': 'Kapture는 웹페이지 전체 또는 선택한 영역을 캡처해 PNG, JPEG, PDF로 사용자의 기기에 저장하는 Chrome 확장 프로그램입니다.',
 'ja': 'Kapture は、ウェブページ全体または選択した範囲をキャプチャし、PNG・JPEG・PDF として自分の端末に保存できる Chrome 拡張機能です。',
 'de': 'Kapture ist eine Chrome-Erweiterung, die eine komplette Webseite oder einen ausgewählten Ausschnitt davon aufnimmt und das Ergebnis als PNG, JPEG oder PDF auf dem eigenen Gerät speichert.',
 'fr': 'Kapture est une extension Chrome qui capture une page web entière ou une zone choisie, et enregistre le résultat sur votre appareil au format PNG, JPEG ou PDF.',
 'pt-br': 'O Kapture é uma extensão do Chrome que captura uma página da web inteira ou uma área selecionada dela e salva o resultado no seu próprio dispositivo em PNG, JPEG ou PDF.',
 'it': "Kapture è un'estensione di Chrome che cattura una pagina web intera o una sua porzione selezionata e salva il risultato sul tuo dispositivo in PNG, JPEG o PDF."}

FEATURES = {
 'en': ["Full page capture, including content below the fold",
        "Select and capture an area of the visible page",
        "Save as PNG, JPEG or PDF",
        "Viewport presets for phone, tablet and desktop widths",
        "Choose the Chrome Downloads subfolder for each capture",
        "Local capture history with open and delete",
        "Light and dark side panel themes"],
 'es': ["Captura de página completa, incluido lo que queda por debajo del pliegue",
        "Selección y captura de una zona de la parte visible",
        "Guardado en PNG, JPEG o PDF",
        "Tamaños de pantalla predefinidos para móvil, tablet y escritorio",
        "Elección de la subcarpeta de descargas para cada captura",
        "Historial local de capturas con opción de abrir y eliminar",
        "Temas claro y oscuro en el panel lateral"],
 'zh': ["整页截图，包含首屏以下的内容",
        "在可见区域中选取并截取指定范围",
        "保存为 PNG、JPEG 或 PDF",
        "手机、平板和桌面宽度的预设画面尺寸",
        "为每次截图选择下载子文件夹",
        "本地截图记录，可打开和删除",
        "侧边栏支持浅色和深色主题"],
 'ko': ["첫 화면 아래 내용까지 포함한 전체 페이지 캡처",
        "보이는 화면에서 영역을 선택해 캡처",
        "PNG, JPEG, PDF로 저장",
        "휴대폰·태블릿·데스크톱 너비의 화면 크기 프리셋",
        "캡처마다 Chrome 다운로드 하위 폴더 지정",
        "열기와 삭제가 가능한 기기 내 캡처 기록",
        "사이드 패널의 라이트·다크 테마"],
 'ja': ["ファーストビューより下も含めたページ全体のキャプチャ",
        "表示中の画面から範囲を選んでキャプチャ",
        "PNG・JPEG・PDF での保存",
        "スマホ・タブレット・デスクトップ幅の画面プリセット",
        "キャプチャごとに Chrome のダウンロード先サブフォルダを指定",
        "開く・削除ができる端末内のキャプチャ履歴",
        "サイドパネルのライトテーマとダークテーマ"],
 'de': ["Ganzseiten-Aufnahme, auch der Bereich unterhalb des sichtbaren Fensters",
        "Einen Ausschnitt der sichtbaren Seite auswählen und aufnehmen",
        "Speichern als PNG, JPEG oder PDF",
        "Fenstergrößen für Smartphone, Tablet und Desktop",
        "Für jede Aufnahme den Unterordner in den Chrome-Downloads wählen",
        "Lokaler Aufnahmeverlauf zum Öffnen und Löschen",
        "Helles und dunkles Design für das Seitenpanel"],
 'fr': ["Capture de la page entière, y compris sous la ligne de flottaison",
        "Sélection et capture d'une zone de la partie visible",
        "Enregistrement en PNG, JPEG ou PDF",
        "Largeurs prédéfinies pour téléphone, tablette et ordinateur",
        "Choix du sous-dossier de téléchargement pour chaque capture",
        "Historique local des captures, à ouvrir ou supprimer",
        "Thèmes clair et sombre pour le panneau latéral"],
 'pt-br': ["Captura da página inteira, inclusive o que fica abaixo da dobra",
        "Seleção e captura de uma área da parte visível",
        "Salvamento em PNG, JPEG ou PDF",
        "Larguras predefinidas para celular, tablet e computador",
        "Escolha da subpasta de downloads para cada captura",
        "Histórico local de capturas, com abrir e excluir",
        "Temas claro e escuro no painel lateral"],
 'it': ["Cattura dell'intera pagina, anche sotto la prima schermata",
        "Selezione e cattura di una porzione della parte visibile",
        "Salvataggio in PNG, JPEG o PDF",
        "Larghezze predefinite per telefono, tablet e desktop",
        "Scelta della sottocartella dei download per ogni cattura",
        "Cronologia locale delle catture, da aprire o eliminare",
        "Temi chiaro e scuro per il pannello laterale"]}

# Language selector
SELECTOR_LABEL = {'en': 'Language', 'es': 'Idioma', 'zh': '语言', 'ko': '언어', 'ja': '言語',
                  'de': 'Sprache', 'fr': 'Langue', 'pt-br': 'Idioma', 'it': 'Lingua'}
NATIVE_NAME    = {'en': 'English',  'es': 'Español', 'zh': '中文', 'ko': '한국어', 'ja': '日本語',
                  'de': 'Deutsch', 'fr': 'Français', 'pt-br': 'Português (Brasil)', 'it': 'Italiano'}
SHORT_NAME     = {'en': 'EN',       'es': 'ES',      'zh': '中文', 'ko': '한국어', 'ja': '日本語',
                  'de': 'DE', 'fr': 'FR', 'pt-br': 'PT-BR', 'it': 'IT'}

# The directory name is the locale key. Brazilian Portuguese is the only one
# that needs a region, and it is the only Portuguese the products ship, so
# there is no /pt/ to disambiguate it from.
LANGS   = ['en', 'es', 'zh', 'ko', 'ja', 'de', 'fr', 'pt-br', 'it']
HTMLLANG = {'en': 'en', 'es': 'es', 'zh': 'zh-CN', 'ko': 'ko', 'ja': 'ja',
            'de': 'de', 'fr': 'fr', 'pt-br': 'pt-BR', 'it': 'it'}
BASE    = 'https://kaptapp.com'

def home_url(lang):
    return f'{BASE}/' if lang == 'en' else f'{BASE}/{lang}/'

def privacy_url(lang):
    return f'{BASE}/privacy/' if lang == 'en' else f'{BASE}/{lang}/privacy/'

def help_url(lang):
    return f'{BASE}/help/' if lang == 'en' else f'{BASE}/{lang}/help/'

# One place that maps a page to its URL builder, so adding a page does not mean
# editing a chain of conditionals in the build script.
PAGE_URL = {'index': home_url, 'privacy': privacy_url, 'help': help_url}

def page_url(lang, page):
    return PAGE_URL[page](lang)


# ---- Kapture Pro: localised JSON-LD prose. Factual fields stay identical. ----
PRO_DESC = {
 'en': 'Kapture Pro indexes the screenshots already on your computer and turns them into a searchable visual library, with Projects, Collections, Smart, tags and an inspector.',
 'es': 'Kapture Pro indexa las capturas que ya tienes en el ordenador y las convierte en una biblioteca visual en la que puedes buscar, con Proyectos, Colecciones, Inteligente, etiquetas e inspector.',
 'zh': 'Kapture Pro 会索引电脑上已经保存的截图，把它们变成一个可搜索的可视化图库，带有项目、收藏集、智能、标签和检查器。',
 'ko': 'Kapture Pro는 이미 컴퓨터에 저장된 스크린샷을 색인해 프로젝트, 컬렉션, 스마트, 태그, 인스펙터를 갖춘 검색 가능한 시각 라이브러리로 만들어 줍니다.',
 'ja': 'Kapture Pro は、すでにパソコンに保存されているスクリーンショットを取り込み、プロジェクト・コレクション・スマート・タグ・インスペクタを備えた検索できるビジュアルライブラリに変えます。',
 'de': 'Kapture Pro indexiert die Screenshots, die schon auf dem Rechner liegen, und macht daraus eine durchsuchbare visuelle Bibliothek mit Projekten, Sammlungen, Smart, Tags und einem Inspektor.',
 'fr': 'Kapture Pro indexe les captures déjà présentes sur votre ordinateur et les transforme en une bibliothèque visuelle interrogeable, avec Projets, Collections, Smart, étiquettes et un inspecteur.',
 'pt-br': 'O Kapture Pro indexa as capturas que já estão no seu computador e as transforma em uma biblioteca visual pesquisável, com Projetos, Coleções, Smart, etiquetas e um inspetor.',
 'it': "Kapture Pro indicizza gli screenshot già presenti sul tuo computer e li trasforma in una libreria visiva consultabile, con Progetti, Raccolte, Smart, tag e un ispettore."}

PRO_FEATURES = {
 'en': ['Projects', 'Collections', 'Smart', 'Search', 'Visual library', 'Inspector',
        'Tags and notes', 'Local storage with no cloud sync'],
 'es': ['Proyectos', 'Colecciones', 'Inteligente', 'Búsqueda', 'Biblioteca visual',
        'Inspector', 'Etiquetas y notas', 'Almacenamiento local sin sincronización en la nube'],
 'zh': ['项目', '收藏集', '智能', '搜索', '可视化图库', '检查器', '标签与备注',
        '本地存储，无需云同步'],
 'ko': ['프로젝트', '컬렉션', '스마트', '검색', '시각 라이브러리', '인스펙터', '태그와 메모',
        '클라우드 동기화 없는 로컬 저장'],
 'ja': ['プロジェクト', 'コレクション', 'スマート', '検索', 'ビジュアルライブラリ',
        'インスペクタ', 'タグとメモ', 'クラウド同期なしのローカル保存'],
 'de': ['Projekte', 'Sammlungen', 'Smart', 'Suche', 'Visuelle Bibliothek', 'Inspektor',
        'Tags und Notizen', 'Lokale Ablage ohne Cloud-Sync'],
 'fr': ['Projets', 'Collections', 'Smart', 'Recherche', 'Bibliothèque visuelle', 'Inspecteur',
        'Étiquettes et notes', 'Stockage local sans synchronisation cloud'],
 'pt-br': ['Projetos', 'Coleções', 'Smart', 'Busca', 'Biblioteca visual', 'Inspetor',
        'Etiquetas e notas', 'Armazenamento local sem sincronização na nuvem'],
 'it': ['Progetti', 'Raccolte', 'Smart', 'Ricerca', 'Libreria visiva', 'Ispettore',
        'Tag e note', 'Archiviazione locale senza sincronizzazione cloud']}
