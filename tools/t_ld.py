# -*- coding: utf-8 -*-
"""Localised JSON-LD prose. Factual fields (name, category, version, installUrl) stay identical."""

APP_DESC = {
 'en': 'Kapture is a Chrome extension that captures a complete webpage or a selected area of it and saves the result on your own device as a PNG, JPEG or PDF.',
 'es': 'Kapture es una extensión de Chrome que captura una página web entera o solo una zona y guarda el resultado en tu propio dispositivo en PNG, JPEG o PDF.',
 'zh': 'Kapture 是一款 Chrome 扩展程序，可以截取整个网页或其中指定的区域，并以 PNG、JPEG 或 PDF 保存到你自己的设备上。',
 'ko': 'Kapture는 웹페이지 전체 또는 선택한 영역을 캡처해 PNG, JPEG, PDF로 사용자의 기기에 저장하는 Chrome 확장 프로그램입니다.',
 'ja': 'Kapture は、ウェブページ全体または選択した範囲をキャプチャし、PNG・JPEG・PDF として自分の端末に保存できる Chrome 拡張機能です。'}

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
        "サイドパネルのライトテーマとダークテーマ"]}

# Language selector
SELECTOR_LABEL = {'en': 'Language', 'es': 'Idioma', 'zh': '语言', 'ko': '언어', 'ja': '言語'}
NATIVE_NAME    = {'en': 'English',  'es': 'Español', 'zh': '中文', 'ko': '한국어', 'ja': '日本語'}
SHORT_NAME     = {'en': 'EN',       'es': 'ES',      'zh': '中文', 'ko': '한국어', 'ja': '日本語'}

LANGS   = ['en', 'es', 'zh', 'ko', 'ja']
HTMLLANG = {'en': 'en', 'es': 'es', 'zh': 'zh-CN', 'ko': 'ko', 'ja': 'ja'}
BASE    = 'https://kaptapp.com'

def home_url(lang):
    return f'{BASE}/' if lang == 'en' else f'{BASE}/{lang}/'

def privacy_url(lang):
    return f'{BASE}/privacy/' if lang == 'en' else f'{BASE}/{lang}/privacy/'
