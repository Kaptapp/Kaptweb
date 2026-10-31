# -*- coding: utf-8 -*-
"""Privacy policy. Same clauses, same order, nothing added or removed."""
from t_chrome import CHROME

# Header, footer, skip link and social labels are shared with the help page.
# The page's own entries below win over anything with the same key.
PRIV = {
**CHROME,
'<title>Privacy Policy | Kapture</title>': {
 'es': '<title>Política de privacidad | Kapture</title>',
 'zh': '<title>隐私政策 | Kapture</title>',
 'ko': '<title>개인정보처리방침 | Kapture</title>',
 'ja': '<title>プライバシーポリシー | Kapture</title>',
 'de': '<title>Datenschutzerklärung | Kapture</title>',
 'fr': '<title>Politique de confidentialité | Kapture</title>',
 'pt-br': '<title>Política de Privacidade | Kapture</title>',
 'it': '<title>Informativa sulla privacy | Kapture</title>'},

'How Kapture handles screenshots, local files and privacy. Screenshots are saved on your device through Chrome Downloads and are not sent to the developer or any third party.': {
 'es': 'Cómo trata Kapture las capturas, los archivos locales y la privacidad. Las capturas se guardan en tu dispositivo mediante las descargas de Chrome y no se envían al desarrollador ni a terceros.',
 'zh': 'Kapture 如何处理截图、本地文件和隐私。截图通过 Chrome 下载功能保存在你的设备上，不会发送给开发者或任何第三方。',
 'ko': 'Kapture가 스크린샷과 로컬 파일, 개인정보를 어떻게 다루는지 설명합니다. 스크린샷은 Chrome 다운로드를 통해 기기에 저장되며 개발자나 제3자에게 전송되지 않습니다.',
 'ja': 'Kapture がスクリーンショットやローカルファイル、プライバシーをどう扱うかについて。スクリーンショットは Chrome のダウンロード機能で端末に保存され、開発者や第三者に送信されることはありません。',
 'de': 'Wie Kapture mit Screenshots, lokalen Dateien und Datenschutz umgeht. Screenshots werden über die Chrome-Downloads auf deinem Gerät gespeichert und nicht an den Entwickler oder Dritte gesendet.',
 'fr': 'Comment Kapture traite les captures, les fichiers locaux et la confidentialité. Les captures sont enregistrées sur votre appareil via les téléchargements de Chrome et ne sont transmises ni au développeur ni à des tiers.',
 'pt-br': 'Como o Kapture lida com capturas de tela, arquivos locais e privacidade. As capturas são salvas no seu dispositivo pelos downloads do Chrome e não são enviadas ao desenvolvedor nem a terceiros.',
 'it': 'Come Kapture tratta screenshot, file locali e privacy. Gli screenshot vengono salvati sul tuo dispositivo tramite i download di Chrome e non vengono inviati allo sviluppatore né a terzi.'},

# JSON-LD breadcrumb leaf. "Home" comes from the shared chrome table.
'"name": "Privacy Policy"': {
 'es': '"name": "Política de privacidad"', 'zh': '"name": "隐私政策"',
 'ko': '"name": "개인정보처리방침"', 'ja': '"name": "プライバシーポリシー"',
 'de': '"name": "Datenschutzerklärung"',
 'fr': '"name": "Politique de confidentialité"',
 'pt-br': '"name": "Política de Privacidade"',
 'it': '"name": "Informativa sulla privacy"'},

'content="Privacy Policy | Kapture"': {
 'es': 'content="Política de privacidad | Kapture"',
 'zh': 'content="隐私政策 | Kapture"',
 'ko': 'content="개인정보처리방침 | Kapture"',
 'ja': 'content="プライバシーポリシー | Kapture"',
 'de': 'content="Datenschutzerklärung | Kapture"',
 'fr': 'content="Politique de confidentialité | Kapture"',
 'pt-br': 'content="Política de Privacidade | Kapture"',
 'it': 'content="Informativa sulla privacy | Kapture"'},


'<p class="kicker">Legal</p>': {
 'es': '<p class="kicker">Aviso legal</p>', 'zh': '<p class="kicker">法律条款</p>',
 'ko': '<p class="kicker">법적 고지</p>', 'ja': '<p class="kicker">法的事項</p>',
 'de': '<p class="kicker">Rechtliches</p>',
 'fr': '<p class="kicker">Mentions légales</p>',
 'pt-br': '<p class="kicker">Jurídico</p>',
 'it': '<p class="kicker">Note legali</p>'},
'<h1>Kapture Privacy Policy</h1>': {
 'es': '<h1>Política de privacidad de Kapture</h1>', 'zh': '<h1>Kapture 隐私政策</h1>',
 'ko': '<h1>Kapture 개인정보처리방침</h1>', 'ja': '<h1>Kapture プライバシーポリシー</h1>',
 'de': '<h1>Kapture Datenschutzerklärung</h1>',
 'fr': '<h1>Politique de confidentialité de Kapture</h1>',
 'pt-br': '<h1>Política de Privacidade do Kapture</h1>',
 'it': '<h1>Informativa sulla privacy di Kapture</h1>'},
'<p class="legal-date">Effective 12 September 2026</p>': {
 'es': '<p class="legal-date">En vigor desde el 12 de septiembre de 2026</p>',
 'zh': '<p class="legal-date">自 2026 年 9 月 12 日起生效</p>',
 'ko': '<p class="legal-date">2026년 9월 12일 시행</p>',
 'ja': '<p class="legal-date">2026 年 9 月 12 日発効</p>',
 'de': '<p class="legal-date">Gültig ab 12. September 2026</p>',
 'fr': '<p class="legal-date">En vigueur depuis le 12 septembre 2026</p>',
 'pt-br': '<p class="legal-date">Em vigor desde 12 de setembro de 2026</p>',
 'it': '<p class="legal-date">In vigore dal 12 settembre 2026</p>'},

'<h2>Overview</h2>': {'es': '<h2>Resumen</h2>', 'zh': '<h2>概述</h2>', 'ko': '<h2>개요</h2>', 'ja': '<h2>概要</h2>',
 'de': '<h2>Überblick</h2>',
 'fr': '<h2>Aperçu</h2>',
 'pt-br': '<h2>Visão geral</h2>',
 'it': '<h2>Panoramica</h2>'},
'<p>Kapture is a Chrome extension that creates screenshots of webpages at the user\'s request. This policy explains what information Kapture handles and how it is used.</p>': {
 'es': '<p>Kapture es una extensión de Chrome que crea capturas de pantalla de páginas web a petición del usuario. Esta política explica qué información trata Kapture y cómo se utiliza.</p>',
 'zh': '<p>Kapture 是一款 Chrome 扩展程序，会在用户发起请求时创建网页截图。本政策说明 Kapture 处理哪些信息以及如何使用这些信息。</p>',
 'ko': '<p>Kapture는 사용자의 요청에 따라 웹페이지 스크린샷을 생성하는 Chrome 확장 프로그램입니다. 본 방침은 Kapture가 어떤 정보를 처리하며 이를 어떻게 사용하는지 설명합니다.</p>',
 'ja': '<p>Kapture は、ユーザーの要求に応じてウェブページのスクリーンショットを作成する Chrome 拡張機能です。本ポリシーでは、Kapture が扱う情報とその利用方法について説明します。</p>',
 'de': '<p>Kapture ist eine Chrome-Erweiterung, die auf Wunsch der Nutzerin oder des Nutzers Screenshots von Webseiten erstellt. Diese Erklärung beschreibt, welche Informationen Kapture verarbeitet und wie sie verwendet werden.</p>',
 'fr': "<p>Kapture est une extension Chrome qui crée des captures d'écran de pages web à la demande de l'utilisateur. Cette politique explique quelles informations Kapture traite et comment elles sont utilisées.</p>",
 'pt-br': '<p>O Kapture é uma extensão do Chrome que cria capturas de tela de páginas da web a pedido do usuário. Esta política explica quais informações o Kapture trata e como elas são usadas.</p>',
 'it': "<p>Kapture è un'estensione di Chrome che crea screenshot di pagine web su richiesta dell'utente. Questa informativa spiega quali informazioni Kapture tratta e come vengono utilizzate.</p>"},

'<h2>Information Kapture handles</h2>': {
 'es': '<h2>Información que trata Kapture</h2>', 'zh': '<h2>Kapture 处理的信息</h2>',
 'ko': '<h2>Kapture가 처리하는 정보</h2>', 'ja': '<h2>Kapture が扱う情報</h2>',
 'de': '<h2>Informationen, die Kapture verarbeitet</h2>',
 'fr': '<h2>Informations traitées par Kapture</h2>',
 'pt-br': '<h2>Informações que o Kapture trata</h2>',
 'it': '<h2>Informazioni trattate da Kapture</h2>'},
'<p>When the user starts a capture, Kapture processes the visual content of the active webpage and its address to create the requested PNG, JPEG or PDF file. Kapture stores limited screenshot-history metadata locally in Chrome, including the filename, source website hostname, Chrome download ID, capture time and file-availability status. It also stores the user\'s selected theme and Downloads subfolder setting locally.</p>': {
 'es': '<p>Cuando el usuario inicia una captura, Kapture procesa el contenido visual de la página web activa y su dirección para crear el archivo PNG, JPEG o PDF solicitado. Kapture almacena localmente en Chrome una cantidad limitada de metadatos del historial de capturas, incluidos el nombre del archivo, el nombre de host del sitio de origen, el identificador de descarga de Chrome, la hora de la captura y el estado de disponibilidad del archivo. También almacena localmente el tema elegido por el usuario y la configuración de la subcarpeta de descargas.</p>',
 'zh': '<p>当用户发起截图时，Kapture 会处理当前网页的可见内容及其网址，以生成所请求的 PNG、JPEG 或 PDF 文件。Kapture 会在 Chrome 本地存储有限的截图历史元数据，包括文件名、来源网站主机名、Chrome 下载 ID、截图时间和文件可用状态。它还会在本地存储用户选择的主题和下载子文件夹设置。</p>',
 'ko': '<p>사용자가 캡처를 시작하면 Kapture는 요청된 PNG, JPEG 또는 PDF 파일을 생성하기 위해 활성 웹페이지의 시각적 콘텐츠와 해당 주소를 처리합니다. Kapture는 파일 이름, 출처 웹사이트 호스트명, Chrome 다운로드 ID, 캡처 시각, 파일 사용 가능 여부를 포함한 제한된 스크린샷 기록 메타데이터를 Chrome 내에 로컬로 저장합니다. 또한 사용자가 선택한 테마와 다운로드 하위 폴더 설정도 로컬에 저장합니다.</p>',
 'ja': '<p>ユーザーがキャプチャを開始すると、Kapture は要求された PNG、JPEG または PDF ファイルを作成するために、アクティブなウェブページの表示内容とそのアドレスを処理します。Kapture は、ファイル名、取得元サイトのホスト名、Chrome のダウンロード ID、キャプチャ日時、ファイルの利用可否といった限られたスクリーンショット履歴のメタデータを Chrome 内にローカル保存します。また、ユーザーが選択したテーマとダウンロード先サブフォルダの設定もローカルに保存します。</p>',
 'de': '<p>Wenn eine Aufnahme gestartet wird, verarbeitet Kapture den sichtbaren Inhalt der aktiven Webseite und ihre Adresse, um die gewünschte PNG-, JPEG- oder PDF-Datei zu erstellen. Kapture speichert begrenzte Verlaufs-Metadaten lokal in Chrome, darunter Dateiname, Hostname der Quell-Website, Chrome-Download-ID, Aufnahmezeit und Verfügbarkeitsstatus der Datei. Ebenfalls lokal gespeichert werden das gewählte Design und die Einstellung für den Downloads-Unterordner.</p>',
 'fr': "<p>Lorsqu'une capture est lancée, Kapture traite le contenu visuel de la page web active et son adresse afin de créer le fichier PNG, JPEG ou PDF demandé. Kapture conserve localement, dans Chrome, des métadonnées d'historique limitées&nbsp;: nom du fichier, nom d'hôte du site source, identifiant de téléchargement Chrome, heure de la capture et état de disponibilité du fichier. Le thème choisi et le sous-dossier de téléchargement sont eux aussi stockés localement.</p>",
 'pt-br': '<p>Quando uma captura é iniciada, o Kapture processa o conteúdo visual da página ativa e o endereço dela para criar o arquivo PNG, JPEG ou PDF solicitado. O Kapture guarda localmente, no Chrome, metadados limitados do histórico: nome do arquivo, nome do host do site de origem, ID de download do Chrome, hora da captura e status de disponibilidade do arquivo. O tema escolhido e a subpasta de downloads também ficam guardados localmente.</p>',
 'it': "<p>Quando l'utente avvia una cattura, Kapture elabora il contenuto visivo della pagina web attiva e il suo indirizzo per creare il file PNG, JPEG o PDF richiesto. Kapture conserva localmente in Chrome metadati di cronologia limitati: nome del file, nome host del sito di origine, ID di download di Chrome, ora della cattura e stato di disponibilità del file. Anche il tema scelto e la sottocartella dei download restano in locale.</p>"},

'<h2>How the information is used</h2>': {
 'es': '<h2>Cómo se utiliza la información</h2>', 'zh': '<h2>信息的使用方式</h2>',
 'ko': '<h2>정보의 이용 방식</h2>', 'ja': '<h2>情報の利用方法</h2>',
 'de': '<h2>Wie die Informationen verwendet werden</h2>',
 'fr': '<h2>Utilisation des informations</h2>',
 'pt-br': '<h2>Como as informações são usadas</h2>',
 'it': '<h2>Come vengono utilizzate le informazioni</h2>'},
'<p>The information is used only to create and save screenshots, apply a user-selected viewport size, name downloaded files, display local capture history and let the user open or remove saved captures.</p>': {
 'es': '<p>La información se utiliza únicamente para crear y guardar capturas, aplicar el tamaño de pantalla elegido por el usuario, nombrar los archivos descargados, mostrar el historial local de capturas y permitir al usuario abrir o eliminar las capturas guardadas.</p>',
 'zh': '<p>这些信息仅用于创建和保存截图、应用用户选择的画面宽度、为下载的文件命名、显示本地截图记录，以及让用户打开或删除已保存的截图。</p>',
 'ko': '<p>해당 정보는 스크린샷을 생성하고 저장하며, 사용자가 선택한 화면 크기를 적용하고, 다운로드한 파일의 이름을 지정하며, 로컬 캡처 기록을 표시하고, 저장된 캡처를 열거나 삭제할 수 있도록 하는 목적으로만 사용됩니다.</p>',
 'ja': '<p>これらの情報は、スクリーンショットの作成と保存、ユーザーが選択した画面幅の適用、ダウンロードファイルの命名、ローカルのキャプチャ履歴の表示、および保存済みキャプチャを開いたり削除したりするためだけに使用されます。</p>',
 'de': '<p>Die Informationen werden ausschließlich dafür verwendet, Screenshots zu erstellen und zu speichern, eine gewählte Fenstergröße anzuwenden, heruntergeladene Dateien zu benennen, den lokalen Aufnahmeverlauf anzuzeigen und gespeicherte Aufnahmen zu öffnen oder zu entfernen.</p>',
 'fr': "<p>Ces informations servent uniquement à créer et enregistrer les captures, appliquer la taille d'écran choisie, nommer les fichiers téléchargés, afficher l'historique local des captures et permettre d'ouvrir ou de supprimer les captures enregistrées.</p>",
 'pt-br': '<p>As informações são usadas apenas para criar e salvar capturas, aplicar o tamanho de tela escolhido, nomear os arquivos baixados, exibir o histórico local de capturas e permitir abrir ou remover capturas salvas.</p>',
 'it': '<p>Le informazioni servono soltanto a creare e salvare gli screenshot, applicare la dimensione di finestra scelta, assegnare un nome ai file scaricati, mostrare la cronologia locale delle catture e consentire di aprire o rimuovere le catture salvate.</p>'},

'<h2>Local storage and retention</h2>': {
 'es': '<h2>Almacenamiento local y conservación</h2>', 'zh': '<h2>本地存储与保留</h2>',
 'ko': '<h2>로컬 저장 및 보관</h2>', 'ja': '<h2>ローカル保存と保持</h2>',
 'de': '<h2>Lokale Speicherung und Aufbewahrung</h2>',
 'fr': '<h2>Stockage local et conservation</h2>',
 'pt-br': '<h2>Armazenamento local e retenção</h2>',
 'it': '<h2>Archiviazione locale e conservazione</h2>'},
'<p>Screenshot files are saved directly to the user\'s computer through Chrome\'s Downloads system. History metadata and preferences are stored locally using Chrome storage. Users can clear history from Kapture and delete screenshot files through Kapture or their operating system. Local extension data is removed when the extension is uninstalled, subject to Chrome\'s behaviour. Downloaded screenshot files remain until the user deletes them.</p>': {
 'es': '<p>Los archivos de las capturas se guardan directamente en el ordenador del usuario mediante el sistema de descargas de Chrome. Los metadatos del historial y las preferencias se almacenan localmente con el almacenamiento de Chrome. Los usuarios pueden borrar el historial desde Kapture y eliminar los archivos de las capturas desde Kapture o desde su sistema operativo. Los datos locales de la extensión se eliminan al desinstalarla, según el comportamiento de Chrome. Los archivos de capturas descargados permanecen hasta que el usuario los elimina.</p>',
 'zh': '<p>截图文件通过 Chrome 的下载功能直接保存到用户的电脑上。历史元数据和偏好设置使用 Chrome 存储保存在本地。用户可以在 Kapture 中清除记录，并通过 Kapture 或操作系统删除截图文件。卸载扩展程序时会移除其本地数据，具体取决于 Chrome 的行为。已下载的截图文件会一直保留，直到用户自行删除。</p>',
 'ko': '<p>스크린샷 파일은 Chrome의 다운로드 기능을 통해 사용자의 컴퓨터에 직접 저장됩니다. 기록 메타데이터와 환경설정은 Chrome 저장소를 사용해 로컬에 보관됩니다. 사용자는 Kapture에서 기록을 지울 수 있고, Kapture 또는 운영체제를 통해 스크린샷 파일을 삭제할 수 있습니다. 확장 프로그램을 삭제하면 Chrome의 동작에 따라 로컬 확장 데이터가 제거됩니다. 다운로드된 스크린샷 파일은 사용자가 삭제할 때까지 그대로 남습니다.</p>',
 'ja': '<p>スクリーンショットのファイルは、Chrome のダウンロード機能を通じてユーザーのパソコンに直接保存されます。履歴のメタデータと設定は Chrome のストレージを使ってローカルに保存されます。ユーザーは Kapture から履歴を消去でき、Kapture または OS を通じてスクリーンショットのファイルを削除できます。拡張機能をアンインストールすると、Chrome の動作に従ってローカルの拡張機能データが削除されます。ダウンロード済みのスクリーンショットのファイルは、ユーザーが削除するまで残ります。</p>',
 'de': '<p>Screenshot-Dateien werden über das Download-System von Chrome direkt auf dem Rechner gespeichert. Verlaufs-Metadaten und Einstellungen liegen lokal im Chrome-Speicher. Der Verlauf lässt sich in Kapture leeren, und Screenshot-Dateien können über Kapture oder das Betriebssystem gelöscht werden. Lokale Erweiterungsdaten werden beim Deinstallieren entfernt, abhängig vom Verhalten von Chrome. Heruntergeladene Screenshot-Dateien bleiben erhalten, bis sie gelöscht werden.</p>',
 'fr': "<p>Les fichiers de capture sont enregistrés directement sur l'ordinateur via le système de téléchargement de Chrome. Les métadonnées d'historique et les préférences sont conservées localement dans le stockage de Chrome. L'historique peut être vidé depuis Kapture, et les fichiers de capture supprimés depuis Kapture ou depuis le système d'exploitation. Les données locales de l'extension sont supprimées à la désinstallation, selon le comportement de Chrome. Les fichiers déjà téléchargés restent jusqu'à ce que l'utilisateur les supprime.</p>",
 'pt-br': '<p>Os arquivos de captura são salvos diretamente no computador pelo sistema de downloads do Chrome. Os metadados do histórico e as preferências ficam guardados localmente no armazenamento do Chrome. O histórico pode ser limpo pelo Kapture, e os arquivos de captura podem ser apagados pelo Kapture ou pelo sistema operacional. Os dados locais da extensão são removidos ao desinstalá-la, conforme o comportamento do Chrome. Os arquivos já baixados permanecem até o usuário apagá-los.</p>',
 'it': "<p>I file degli screenshot vengono salvati direttamente sul computer tramite il sistema di download di Chrome. I metadati della cronologia e le preferenze restano in locale nell'archivio di Chrome. La cronologia si può svuotare da Kapture, e i file degli screenshot si possono eliminare da Kapture o dal sistema operativo. I dati locali dell'estensione vengono rimossi alla disinstallazione, secondo il comportamento di Chrome. I file già scaricati restano finché l'utente non li elimina.</p>"},

'<h2>Sharing and transmission</h2>': {
 'es': '<h2>Comunicación y transmisión de datos</h2>', 'zh': '<h2>共享与传输</h2>',
 'ko': '<h2>공유 및 전송</h2>', 'ja': '<h2>共有と送信</h2>',
 'de': '<h2>Weitergabe und Übertragung</h2>',
 'fr': '<h2>Partage et transmission</h2>',
 'pt-br': '<h2>Compartilhamento e transmissão</h2>',
 'it': '<h2>Condivisione e trasmissione</h2>'},
'<p>Kapture does not send webpage content, screenshots, browsing information or history metadata to the developer or to external servers. Kapture does not include analytics, advertising, tracking or third-party data services. User data is not sold or transferred to third parties.</p>': {
 'es': '<p>Kapture no envía el contenido de las páginas web, las capturas, la información de navegación ni los metadatos del historial al desarrollador ni a servidores externos. Kapture no incluye analíticas, publicidad, seguimiento ni servicios de datos de terceros. Los datos del usuario no se venden ni se transfieren a terceros.</p>',
 'zh': '<p>Kapture 不会将网页内容、截图、浏览信息或历史元数据发送给开发者或外部服务器。Kapture 不含分析、广告、追踪或第三方数据服务。用户数据不会被出售或转让给第三方。</p>',
 'ko': '<p>Kapture는 웹페이지 내용, 스크린샷, 브라우징 정보 또는 기록 메타데이터를 개발자나 외부 서버로 전송하지 않습니다. Kapture에는 분석, 광고, 추적 또는 제3자 데이터 서비스가 포함되어 있지 않습니다. 사용자 데이터는 제3자에게 판매되거나 이전되지 않습니다.</p>',
 'ja': '<p>Kapture は、ウェブページの内容、スクリーンショット、閲覧情報、履歴のメタデータを開発者や外部サーバーに送信しません。Kapture には解析、広告、トラッキング、第三者のデータサービスは含まれていません。ユーザーデータが第三者に販売または譲渡されることはありません。</p>',
 'de': '<p>Kapture sendet keine Webseiteninhalte, Screenshots, Browserdaten oder Verlaufs-Metadaten an den Entwickler oder an externe Server. Kapture enthält keine Analyse, Werbung, Tracking oder Datendienste Dritter. Nutzerdaten werden nicht verkauft und nicht an Dritte weitergegeben.</p>',
 'fr': "<p>Kapture n'envoie ni contenu de page, ni captures, ni informations de navigation, ni métadonnées d'historique au développeur ou à des serveurs externes. Kapture ne contient ni analyse, ni publicité, ni suivi, ni service de données tiers. Les données des utilisateurs ne sont ni vendues ni transmises à des tiers.</p>",
 'pt-br': '<p>O Kapture não envia conteúdo de páginas, capturas, informações de navegação nem metadados de histórico ao desenvolvedor ou a servidores externos. O Kapture não inclui analytics, publicidade, rastreamento nem serviços de dados de terceiros. Os dados dos usuários não são vendidos nem transferidos a terceiros.</p>',
 'it': '<p>Kapture non invia contenuti delle pagine, screenshot, informazioni di navigazione o metadati della cronologia allo sviluppatore né a server esterni. Kapture non include analisi, pubblicità, tracciamento o servizi dati di terze parti. I dati degli utenti non vengono venduti né ceduti a terzi.</p>'},

'<h2>Remote code</h2>': {
 'es': '<h2>Código remoto</h2>', 'zh': '<h2>远程代码</h2>',
 'ko': '<h2>원격 코드</h2>', 'ja': '<h2>リモートコード</h2>',
 'de': '<h2>Remote-Code</h2>',
 'fr': '<h2>Code distant</h2>',
 'pt-br': '<h2>Código remoto</h2>',
 'it': '<h2>Codice remoto</h2>'},
'<p>Kapture does not download or execute remote code. All executable code is included in the extension package distributed through the Chrome Web Store.</p>': {
 'es': '<p>Kapture no descarga ni ejecuta código remoto. Todo el código ejecutable está incluido en el paquete de la extensión distribuido a través de Chrome Web Store.</p>',
 'zh': '<p>Kapture 不会下载或执行远程代码。所有可执行代码都包含在通过 Chrome 应用商店分发的扩展程序包中。</p>',
 'ko': '<p>Kapture는 원격 코드를 내려받거나 실행하지 않습니다. 모든 실행 코드는 Chrome 웹 스토어를 통해 배포되는 확장 프로그램 패키지에 포함되어 있습니다.</p>',
 'ja': '<p>Kapture はリモートコードのダウンロードや実行を行いません。実行可能なコードはすべて、Chrome ウェブストアで配布される拡張機能パッケージに含まれています。</p>',
 'de': '<p>Kapture lädt keinen Remote-Code herunter und führt keinen aus. Der gesamte ausführbare Code ist im Erweiterungspaket enthalten, das über den Chrome Web Store verteilt wird.</p>',
 'fr': "<p>Kapture ne télécharge ni n'exécute de code distant. Tout le code exécutable est inclus dans le paquet de l'extension distribué via le Chrome Web Store.</p>",
 'pt-br': '<p>O Kapture não baixa nem executa código remoto. Todo o código executável está incluído no pacote da extensão distribuído pela Chrome Web Store.</p>',
 'it': "<p>Kapture non scarica né esegue codice remoto. Tutto il codice eseguibile è incluso nel pacchetto dell'estensione distribuito tramite il Chrome Web Store.</p>"},

'<h2>Chrome permissions</h2>': {
 'es': '<h2>Permisos de Chrome</h2>', 'zh': '<h2>Chrome 权限</h2>',
 'ko': '<h2>Chrome 권한</h2>', 'ja': '<h2>Chrome の権限</h2>',
 'de': '<h2>Chrome-Berechtigungen</h2>',
 'fr': '<h2>Autorisations Chrome</h2>',
 'pt-br': '<h2>Permissões do Chrome</h2>',
 'it': '<h2>Autorizzazioni di Chrome</h2>'},
'<p>Kapture uses Chrome permissions only to operate its user-requested screenshot features: access the active tab, inject packaged capture controls, save and open downloads, display the side panel, store local preferences and history, and temporarily apply a selected responsive viewport.</p>': {
 'es': '<p>Kapture utiliza los permisos de Chrome únicamente para ofrecer las funciones de captura solicitadas por el usuario: acceder a la pestaña activa, insertar los controles de captura incluidos en el paquete, guardar y abrir descargas, mostrar el panel lateral, almacenar preferencias e historial locales y aplicar temporalmente el tamaño de pantalla seleccionado.</p>',
 'zh': '<p>Kapture 使用 Chrome 权限仅为实现用户主动发起的截图功能：访问当前标签页、注入随扩展程序打包的截图控件、保存和打开下载内容、显示侧边栏、在本地存储偏好设置和记录，以及临时应用所选的响应式画面宽度。</p>',
 'ko': '<p>Kapture는 사용자가 요청한 스크린샷 기능을 제공하기 위해서만 Chrome 권한을 사용합니다. 활성 탭 접근, 패키지에 포함된 캡처 컨트롤 삽입, 다운로드 저장 및 열기, 사이드 패널 표시, 로컬 환경설정 및 기록 저장, 선택한 반응형 화면 크기의 일시 적용이 이에 해당합니다.</p>',
 'ja': '<p>Kapture が Chrome の権限を使用するのは、ユーザーが要求したスクリーンショット機能を動作させるためだけです。具体的には、アクティブなタブへのアクセス、パッケージに含まれるキャプチャ用コントロールの挿入、ダウンロードの保存と表示、サイドパネルの表示、設定と履歴のローカル保存、選択した画面幅の一時的な適用です。</p>',
 'de': '<p>Kapture nutzt Chrome-Berechtigungen ausschließlich für die angeforderten Screenshot-Funktionen: Zugriff auf den aktiven Tab, Einfügen der mitgelieferten Aufnahme-Steuerung, Speichern und Öffnen von Downloads, Anzeigen des Seitenpanels, Ablegen lokaler Einstellungen und des Verlaufs sowie vorübergehendes Anwenden einer gewählten Fenstergröße.</p>',
 'fr': "<p>Kapture n'utilise les autorisations Chrome que pour les fonctions de capture demandées par l'utilisateur&nbsp;: accéder à l'onglet actif, injecter les contrôles de capture fournis, enregistrer et ouvrir les téléchargements, afficher le panneau latéral, stocker les préférences et l'historique en local, et appliquer temporairement une taille d'écran choisie.</p>",
 'pt-br': '<p>O Kapture usa as permissões do Chrome apenas para os recursos de captura solicitados pelo usuário: acessar a aba ativa, injetar os controles de captura incluídos, salvar e abrir downloads, exibir o painel lateral, guardar preferências e histórico localmente e aplicar temporariamente um tamanho de tela escolhido.</p>',
 'it': "<p>Kapture usa le autorizzazioni di Chrome solo per le funzioni di cattura richieste dall'utente: accedere alla scheda attiva, inserire i controlli di cattura inclusi, salvare e aprire i download, mostrare il pannello laterale, conservare preferenze e cronologia in locale e applicare temporaneamente una dimensione di finestra scelta.</p>"},

'<h2>Changes to this policy</h2>': {
 'es': '<h2>Cambios en esta política</h2>', 'zh': '<h2>本政策的变更</h2>',
 'ko': '<h2>본 방침의 변경</h2>', 'ja': '<h2>本ポリシーの変更</h2>',
 'de': '<h2>Änderungen an dieser Erklärung</h2>',
 'fr': '<h2>Modifications de cette politique</h2>',
 'pt-br': '<h2>Alterações nesta política</h2>',
 'it': '<h2>Modifiche a questa informativa</h2>'},
'<p>If Kapture\'s data practices change, this policy and the Chrome Web Store disclosures will be updated before the changed functionality is released.</p>': {
 'es': '<p>Si cambian las prácticas de datos de Kapture, esta política y la información publicada en Chrome Web Store se actualizarán antes de que se publique la funcionalidad modificada.</p>',
 'zh': '<p>如果 Kapture 的数据处理方式发生变化，本政策及 Chrome 应用商店中的相关说明将在变更后的功能发布之前更新。</p>',
 'ko': '<p>Kapture의 데이터 처리 방식이 변경되는 경우, 변경된 기능이 출시되기 전에 본 방침과 Chrome 웹 스토어 고지 내용이 업데이트됩니다.</p>',
 'ja': '<p>Kapture のデータの取り扱いが変更される場合、変更後の機能が公開される前に、本ポリシーおよび Chrome ウェブストアの記載内容を更新します。</p>',
 'de': '<p>Ändern sich die Datenpraktiken von Kapture, werden diese Erklärung und die Angaben im Chrome Web Store aktualisiert, bevor die geänderte Funktion veröffentlicht wird.</p>',
 'fr': '<p>Si les pratiques de Kapture en matière de données changent, cette politique et les déclarations du Chrome Web Store seront mises à jour avant la publication de la fonctionnalité modifiée.</p>',
 'pt-br': '<p>Se as práticas de dados do Kapture mudarem, esta política e as declarações na Chrome Web Store serão atualizadas antes de a funcionalidade alterada ser lançada.</p>',
 'it': '<p>Se le pratiche di Kapture sui dati cambiano, questa informativa e le dichiarazioni sul Chrome Web Store verranno aggiornate prima del rilascio della funzionalità modificata.</p>'},

'<h2>Contact</h2>': {
 'es': '<h2>Contacto</h2>', 'zh': '<h2>联系方式</h2>',
 'ko': '<h2>문의처</h2>', 'ja': '<h2>お問い合わせ</h2>',
 'de': '<h2>Kontakt</h2>',
 'fr': '<h2>Contact</h2>',
 'pt-br': '<h2>Contato</h2>',
 'it': '<h2>Contatti</h2>'},
'<p>For privacy or support questions, email <a href="mailto:hello@kaptapp.com">contact</a>.</p>': {
 'es': '<p>Para consultas sobre privacidad o soporte, escribe a <a href="mailto:hello@kaptapp.com">contacto</a>.</p>',
 'zh': '<p>如有隐私或支持方面的问题，请发送邮件至 <a href="mailto:hello@kaptapp.com">联系</a>。</p>',
 'ko': '<p>개인정보 또는 지원 관련 문의는 <a href="mailto:hello@kaptapp.com">문의</a> 으로 메일을 보내주세요.</p>',
 'ja': '<p>プライバシーやサポートに関するお問い合わせは <a href="mailto:hello@kaptapp.com">お問い合わせ</a> までメールでご連絡ください。</p>',
 'de': '<p>Bei Fragen zu Datenschutz oder Support schreib an <a href="mailto:hello@kaptapp.com">Kontakt</a>.</p>',
 'fr': '<p>Pour toute question de confidentialité ou de support, écrivez à <a href="mailto:hello@kaptapp.com">contact</a>.</p>',
 'pt-br': '<p>Para dúvidas de privacidade ou suporte, escreva para <a href="mailto:hello@kaptapp.com">contato</a>.</p>',
 'it': '<p>Per domande su privacy o assistenza, scrivi a <a href="mailto:hello@kaptapp.com">contatti</a>.</p>'},


# footer nav on the privacy page
'<a href="/#capture">Capture</a>\n      <a href="/#how">How it works</a>\n      <a href="/privacy/">Privacy</a>\n      <a href="mailto:hello@kaptapp.com">Contact</a>': {
 'es': '<a href="/#capture">Captura</a>\n      <a href="/#how">Cómo funciona</a>\n      <a href="/privacy/">Privacidad</a>\n      <a href="mailto:hello@kaptapp.com">Contacto</a>',
 'zh': '<a href="/#capture">截图</a>\n      <a href="/#how">使用方法</a>\n      <a href="/privacy/">隐私</a>\n      <a href="mailto:hello@kaptapp.com">联系我们</a>',
 'ko': '<a href="/#capture">캡처</a>\n      <a href="/#how">사용 방법</a>\n      <a href="/privacy/">개인정보</a>\n      <a href="mailto:hello@kaptapp.com">문의</a>',
 'ja': '<a href="/#capture">キャプチャ</a>\n      <a href="/#how">使い方</a>\n      <a href="/privacy/">プライバシー</a>\n      <a href="mailto:hello@kaptapp.com">お問い合わせ</a>'},
'<a href="/#capture">Capture</a>': {
 'es': '<a href="/#capture">Captura</a>', 'zh': '<a href="/#capture">截图</a>',
 'ko': '<a href="/#capture">캡처</a>', 'ja': '<a href="/#capture">キャプチャ</a>'},
'<a href="/privacy/" aria-current="page">Privacy</a>': {
 'es': '<a href="/privacy/" aria-current="page">Privacidad</a>',
 'zh': '<a href="/privacy/" aria-current="page">隐私</a>',
 'ko': '<a href="/privacy/" aria-current="page">개인정보</a>',
 'ja': '<a href="/privacy/" aria-current="page">プライバシー</a>',
 'de': '<a href="/privacy/" aria-current="page">Datenschutz</a>',
 'fr': '<a href="/privacy/" aria-current="page">Confidentialité</a>',
 'pt-br': '<a href="/privacy/" aria-current="page">Privacidade</a>',
 'it': '<a href="/privacy/" aria-current="page">Privacy</a>'},

# ---------------------------------------------------------------- 2026-10 policy: extension headings now sit under h2 "Kapture for Chrome"
'<h3>Information Kapture handles</h3>': {
 'es': '<h3>Información que trata Kapture</h3>',
 'zh': '<h3>Kapture 处理的信息</h3>',
 'ko': '<h3>Kapture가 처리하는 정보</h3>',
 'ja': '<h3>Kapture が扱う情報</h3>',
 'de': '<h3>Informationen, die Kapture verarbeitet</h3>',
 'fr': '<h3>Informations traitées par Kapture</h3>',
 'pt-br': '<h3>Informações que o Kapture trata</h3>',
 'it': '<h3>Informazioni trattate da Kapture</h3>'},

'<h3>How the information is used</h3>': {
 'es': '<h3>Cómo se utiliza la información</h3>',
 'zh': '<h3>信息的使用方式</h3>',
 'ko': '<h3>정보의 이용 방식</h3>',
 'ja': '<h3>情報の利用方法</h3>',
 'de': '<h3>Wie die Informationen verwendet werden</h3>',
 'fr': '<h3>Utilisation des informations</h3>',
 'pt-br': '<h3>Como as informações são usadas</h3>',
 'it': '<h3>Come vengono utilizzate le informazioni</h3>'},

'<h3>Local storage and retention</h3>': {
 'es': '<h3>Almacenamiento local y conservación</h3>',
 'zh': '<h3>本地存储与保留</h3>',
 'ko': '<h3>로컬 저장 및 보관</h3>',
 'ja': '<h3>ローカル保存と保持</h3>',
 'de': '<h3>Lokale Speicherung und Aufbewahrung</h3>',
 'fr': '<h3>Stockage local et conservation</h3>',
 'pt-br': '<h3>Armazenamento local e retenção</h3>',
 'it': '<h3>Archiviazione locale e conservazione</h3>'},

'<h3>Sharing and transmission</h3>': {
 'es': '<h3>Comunicación y transmisión de datos</h3>',
 'zh': '<h3>共享与传输</h3>',
 'ko': '<h3>공유 및 전송</h3>',
 'ja': '<h3>共有と送信</h3>',
 'de': '<h3>Weitergabe und Übertragung</h3>',
 'fr': '<h3>Partage et transmission</h3>',
 'pt-br': '<h3>Compartilhamento e transmissão</h3>',
 'it': '<h3>Condivisione e trasmissione</h3>'},

'<h3>Remote code</h3>': {
 'es': '<h3>Código remoto</h3>',
 'zh': '<h3>远程代码</h3>',
 'ko': '<h3>원격 코드</h3>',
 'ja': '<h3>リモートコード</h3>',
 'de': '<h3>Remote-Code</h3>',
 'fr': '<h3>Code distant</h3>',
 'pt-br': '<h3>Código remoto</h3>',
 'it': '<h3>Codice remoto</h3>'},

'<h3>Chrome permissions</h3>': {
 'es': '<h3>Permisos de Chrome</h3>',
 'zh': '<h3>Chrome 权限</h3>',
 'ko': '<h3>Chrome 권한</h3>',
 'ja': '<h3>Chrome の権限</h3>',
 'de': '<h3>Chrome-Berechtigungen</h3>',
 'fr': '<h3>Autorisations Chrome</h3>',
 'pt-br': '<h3>Permissões do Chrome</h3>',
 'it': '<h3>Autorizzazioni di Chrome</h3>'},

# ---------------------------------------------------------------- 2026-10 policy: accounts, Kapture Pro, payments
'How Kapture handles your data. Captures stay on your device; this policy explains what we keep for Kapture accounts, licences and payments, and your rights.': {
 'es': 'Cómo trata Kapture tus datos. Las capturas se quedan en tu dispositivo; esta política explica qué conservamos para las cuentas, las licencias y los pagos de Kapture, y cuáles son tus derechos.',
 'zh': 'Kapture 如何处理你的数据。截图保留在你的设备上；本政策说明我们为 Kapture 账户、许可证和付款保存哪些信息，以及你享有的权利。',
 'ko': 'Kapture가 사용자의 데이터를 어떻게 다루는지 설명합니다. 캡처는 기기에만 남습니다. 본 방침은 Kapture 계정, 라이선스, 결제와 관련해 당사가 보관하는 정보와 사용자의 권리를 설명합니다.',
 'ja': 'Kapture がお客様のデータをどう扱うかについて。キャプチャは端末内にとどまります。本ポリシーでは、Kapture アカウント、ライセンス、支払いについて当社が保持する情報と、お客様の権利について説明します。',
 'de': 'Wie Kapture mit deinen Daten umgeht. Aufnahmen bleiben auf deinem Gerät. Diese Erklärung beschreibt, was wir für Kapture-Konten, Lizenzen und Zahlungen speichern, und welche Rechte du hast.',
 'fr': 'Comment Kapture traite vos données. Vos captures restent sur votre appareil. Cette politique explique ce que nous conservons pour les comptes Kapture, les licences et les paiements, ainsi que vos droits.',
 'pt-br': 'Como o Kapture trata seus dados. As capturas ficam no seu dispositivo; esta política explica o que guardamos para contas, licenças e pagamentos do Kapture, e quais são seus direitos.',
 'it': 'Come Kapture tratta i tuoi dati. Le catture restano sul tuo dispositivo; questa informativa spiega cosa conserviamo per account Kapture, licenze e pagamenti, e quali sono i tuoi diritti.'},

'<h2>Who we are</h2>': {
 'es': '<h2>Quiénes somos</h2>',
 'zh': '<h2>我们是谁</h2>',
 'ko': '<h2>당사 소개</h2>',
 'ja': '<h2>当社について</h2>',
 'de': '<h2>Wer wir sind</h2>',
 'fr': '<h2>Qui sommes-nous</h2>',
 'pt-br': '<h2>Quem somos</h2>',
 'it': '<h2>Chi siamo</h2>'},

'<h2>In short</h2>': {
 'es': '<h2>En resumen</h2>',
 'zh': '<h2>简要说明</h2>',
 'ko': '<h2>요약</h2>',
 'ja': '<h2>要点</h2>',
 'de': '<h2>Kurz gesagt</h2>',
 'fr': '<h2>En bref</h2>',
 'pt-br': '<h2>Em resumo</h2>',
 'it': '<h2>In breve</h2>'},

'<h2>Kapture for Chrome</h2>': {
 'es': '<h2>Kapture para Chrome</h2>',
 'zh': '<h2>Chrome 版 Kapture</h2>',
 'ko': '<h2>Chrome용 Kapture</h2>',
 'ja': '<h2>Chrome 版 Kapture</h2>',
 'de': '<h2>Kapture für Chrome</h2>',
 'fr': '<h2>Kapture pour Chrome</h2>',
 'pt-br': '<h2>Kapture para Chrome</h2>',
 'it': '<h2>Kapture per Chrome</h2>'},

'<h2>Your Kapture account and Kapture Pro</h2>': {
 'es': '<h2>Tu cuenta de Kapture y Kapture Pro</h2>',
 'zh': '<h2>你的 Kapture 账户和 Kapture Pro</h2>',
 'ko': '<h2>Kapture 계정과 Kapture Pro</h2>',
 'ja': '<h2>Kapture アカウントと Kapture Pro</h2>',
 'de': '<h2>Dein Kapture-Konto und Kapture Pro</h2>',
 'fr': '<h2>Votre compte Kapture et Kapture Pro</h2>',
 'pt-br': '<h2>Sua conta Kapture e o Kapture Pro</h2>',
 'it': '<h2>Il tuo account Kapture e Kapture Pro</h2>'},

'<h3>What we collect and why</h3>': {
 'es': '<h3>Qué recopilamos y por qué</h3>',
 'zh': '<h3>我们收集哪些信息及原因</h3>',
 'ko': '<h3>수집하는 정보와 수집 목적</h3>',
 'ja': '<h3>収集する情報とその目的</h3>',
 'de': '<h3>Was wir erheben und warum</h3>',
 'fr': '<h3>Ce que nous collectons et pourquoi</h3>',
 'pt-br': '<h3>O que coletamos e por quê</h3>',
 'it': '<h3>Cosa raccogliamo e perché</h3>'},

'<h3>What we do not collect</h3>': {
 'es': '<h3>Qué no recopilamos</h3>',
 'zh': '<h3>我们不收集的信息</h3>',
 'ko': '<h3>수집하지 않는 정보</h3>',
 'ja': '<h3>収集しない情報</h3>',
 'de': '<h3>Was wir nicht erheben</h3>',
 'fr': '<h3>Ce que nous ne collectons pas</h3>',
 'pt-br': '<h3>O que não coletamos</h3>',
 'it': '<h3>Cosa non raccogliamo</h3>'},

'<h3>Payments through Stripe</h3>': {
 'es': '<h3>Pagos a través de Stripe</h3>',
 'zh': '<h3>通过 Stripe 付款</h3>',
 'ko': '<h3>Stripe를 통한 결제</h3>',
 'ja': '<h3>Stripe による支払い</h3>',
 'de': '<h3>Zahlungen über Stripe</h3>',
 'fr': '<h3>Paiements via Stripe</h3>',
 'pt-br': '<h3>Pagamentos pela Stripe</h3>',
 'it': '<h3>Pagamenti tramite Stripe</h3>'},

'<h3>Who processes information for us</h3>': {
 'es': '<h3>Quién trata la información en nuestro nombre</h3>',
 'zh': '<h3>为我们处理信息的服务商</h3>',
 'ko': '<h3>당사를 위해 정보를 처리하는 업체</h3>',
 'ja': '<h3>情報の処理を委託している事業者</h3>',
 'de': '<h3>Wer Daten in unserem Auftrag verarbeitet</h3>',
 'fr': '<h3>Qui traite des informations pour notre compte</h3>',
 'pt-br': '<h3>Quem trata informações em nosso nome</h3>',
 'it': '<h3>Chi tratta le informazioni per nostro conto</h3>'},

'<h3>How long we keep it</h3>': {
 'es': '<h3>Cuánto tiempo la conservamos</h3>',
 'zh': '<h3>保存期限</h3>',
 'ko': '<h3>보관 기간</h3>',
 'ja': '<h3>保存期間</h3>',
 'de': '<h3>Wie lange wir Daten speichern</h3>',
 'fr': '<h3>Durée de conservation</h3>',
 'pt-br': '<h3>Por quanto tempo guardamos</h3>',
 'it': '<h3>Per quanto tempo le conserviamo</h3>'},

'<h3>Browser storage on kaptapp.com</h3>': {
 'es': '<h3>Almacenamiento del navegador en kaptapp.com</h3>',
 'zh': '<h3>kaptapp.com 上的浏览器存储</h3>',
 'ko': '<h3>kaptapp.com의 브라우저 저장소</h3>',
 'ja': '<h3>kaptapp.com でのブラウザーストレージ</h3>',
 'de': '<h3>Browserspeicher auf kaptapp.com</h3>',
 'fr': '<h3>Stockage du navigateur sur kaptapp.com</h3>',
 'pt-br': '<h3>Armazenamento do navegador no kaptapp.com</h3>',
 'it': '<h3>Archiviazione nel browser su kaptapp.com</h3>'},

'<h3>Deleting your account</h3>': {
 'es': '<h3>Eliminar tu cuenta</h3>',
 'zh': '<h3>删除账户</h3>',
 'ko': '<h3>계정 삭제</h3>',
 'ja': '<h3>アカウントの削除</h3>',
 'de': '<h3>Dein Konto löschen</h3>',
 'fr': '<h3>Supprimer votre compte</h3>',
 'pt-br': '<h3>Exclusão da conta</h3>',
 'it': "<h3>Eliminazione dell'account</h3>"},

'<h2>Your rights</h2>': {
 'es': '<h2>Tus derechos</h2>',
 'zh': '<h2>你的权利</h2>',
 'ko': '<h2>사용자의 권리</h2>',
 'ja': '<h2>お客様の権利</h2>',
 'de': '<h2>Deine Rechte</h2>',
 'fr': '<h2>Vos droits</h2>',
 'pt-br': '<h2>Seus direitos</h2>',
 'it': '<h2>I tuoi diritti</h2>'},

'<h2>Children</h2>': {
 'es': '<h2>Menores</h2>',
 'zh': '<h2>儿童</h2>',
 'ko': '<h2>아동</h2>',
 'ja': '<h2>子どもについて</h2>',
 'de': '<h2>Kinder</h2>',
 'fr': '<h2>Enfants</h2>',
 'pt-br': '<h2>Crianças e adolescentes</h2>',
 'it': '<h2>Minori</h2>'},

'<p class="legal-date">Effective 1 November 2026</p>': {
 'es': '<p class="legal-date">En vigor desde el 1 de noviembre de 2026</p>',
 'zh': '<p class="legal-date">自 2026 年 11 月 1 日起生效</p>',
 'ko': '<p class="legal-date">2026년 11월 1일 시행</p>',
 'ja': '<p class="legal-date">2026 年 11 月 1 日発効</p>',
 'de': '<p class="legal-date">Gültig ab 1. November 2026</p>',
 'fr': '<p class="legal-date">En vigueur depuis le 1er novembre 2026</p>',
 'pt-br': '<p class="legal-date">Em vigor desde 1º de novembro de 2026</p>',
 'it': '<p class="legal-date">In vigore dal 1° novembre 2026</p>'},

'<p>Kapture is made by KUMO STUDIO LIMITED, a private limited company registered in England and Wales under company number 08453597, whose registered office is at Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England. We are the controller of the personal data described in this policy.</p>': {
 'es': '<p>Kapture está desarrollado por KUMO STUDIO LIMITED, una sociedad de responsabilidad limitada (private limited company) registrada en Inglaterra y Gales con el número de registro 08453597 y con domicilio social en Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England. Somos el responsable del tratamiento de los datos personales descritos en esta política.</p>',
 'zh': '<p>Kapture 由 KUMO STUDIO LIMITED 开发。KUMO STUDIO LIMITED 是一家在英格兰和威尔士注册的私人有限公司，公司编号为 08453597，注册办公地址为 Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England。我们是本政策所述个人数据的控制者。</p>',
 'ko': '<p>Kapture는 KUMO STUDIO LIMITED가 만듭니다. KUMO STUDIO LIMITED는 잉글랜드 및 웨일스에 회사 번호 08453597로 등록된 비상장 유한회사(private limited company)이며, 등록 사무소는 Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England에 있습니다. 당사는 본 방침에서 설명하는 개인정보의 컨트롤러(controller)입니다.</p>',
 'ja': '<p>Kapture は、イングランドおよびウェールズで登記された非公開有限会社 KUMO STUDIO LIMITED（会社番号 08453597、登記上の事務所：Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England）が提供しています。当社は、本ポリシーに記載する個人データの管理者です。</p>',
 'de': '<p>Kapture wird von der KUMO STUDIO LIMITED entwickelt, einer in England und Wales unter der Registernummer 08453597 eingetragenen Gesellschaft mit beschränkter Haftung nach englischem Recht (Private Limited Company) mit eingetragenem Sitz in Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England. Wir sind Verantwortlicher für die in dieser Erklärung beschriebenen personenbezogenen Daten.</p>',
 'fr': '<p>Kapture est conçu par KUMO STUDIO LIMITED, une société à responsabilité limitée de droit anglais (private limited company) immatriculée en Angleterre et au pays de Galles sous le numéro 08453597, dont le siège social est situé Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England. Nous sommes le responsable du traitement des données personnelles décrites dans cette politique.</p>',
 'pt-br': '<p>O Kapture é feito pela KUMO STUDIO LIMITED, uma sociedade limitada (private limited company) registrada na Inglaterra e no País de Gales sob o número de registro 08453597, com sede social em Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England. Somos o controlador dos dados pessoais descritos nesta política.</p>',
 'it': '<p>Kapture è realizzato da KUMO STUDIO LIMITED, società privata a responsabilità limitata registrata in Inghilterra e Galles con numero di registrazione 08453597 e sede legale in Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England. Siamo il titolare del trattamento dei dati personali descritti in questa informativa.</p>'},

'<p>Your captures stay on your device. We never receive your screenshots, their contents, or your library, projects, tags or notes.</p>': {
 'es': '<p>Tus capturas se quedan en tu dispositivo. Nunca recibimos tus capturas de pantalla, su contenido ni tu biblioteca, proyectos, etiquetas o notas.</p>',
 'zh': '<p>你的截图保留在你的设备上。我们绝不会接收你的截图及其内容，也不会接收你的资料库、项目、标签或备注。</p>',
 'ko': '<p>캡처는 기기에만 남습니다. 당사는 사용자의 스크린샷과 그 내용, 라이브러리, 프로젝트, 태그, 메모를 절대 받지 않습니다.</p>',
 'ja': '<p>キャプチャはお客様の端末内にとどまります。当社がスクリーンショットやその内容、ライブラリ、プロジェクト、タグ、メモを受け取ることはありません。</p>',
 'de': '<p>Deine Aufnahmen bleiben auf deinem Gerät. Wir erhalten niemals deine Screenshots, deren Inhalte oder deine Bibliothek, Projekte, Tags oder Notizen.</p>',
 'fr': "<p>Vos captures restent sur votre appareil. Nous ne recevons jamais vos captures d'écran, leur contenu, ni votre bibliothèque, vos projets, vos tags ou vos notes.</p>",
 'pt-br': '<p>Suas capturas ficam no seu dispositivo. Nunca recebemos suas capturas de tela, o conteúdo delas nem sua biblioteca, projetos, etiquetas ou notas.</p>',
 'it': '<p>Le tue catture restano sul tuo dispositivo. Non riceviamo mai i tuoi screenshot, il loro contenuto, né la tua libreria, i tuoi progetti, tag o note.</p>'},

'<p>Kapture for Chrome needs no account and sends nothing to us.</p>': {
 'es': '<p>Kapture para Chrome no necesita cuenta y no nos envía nada.</p>',
 'zh': '<p>Chrome 版 Kapture 无需账户，也不会向我们发送任何信息。</p>',
 'ko': '<p>Chrome용 Kapture는 계정이 필요 없으며 당사에 아무것도 보내지 않습니다.</p>',
 'ja': '<p>Chrome 版 Kapture はアカウント不要で、当社に何も送信しません。</p>',
 'de': '<p>Kapture für Chrome braucht kein Konto und sendet nichts an uns.</p>',
 'fr': '<p>Kapture pour Chrome ne nécessite aucun compte et ne nous envoie rien.</p>',
 'pt-br': '<p>O Kapture para Chrome não precisa de conta e não nos envia nada.</p>',
 'it': '<p>Kapture per Chrome non richiede alcun account e non ci invia nulla.</p>'},

'<p>A Kapture account holds your email address and, if you use Kapture Pro, your licence and the devices you activate.</p>': {
 'es': '<p>Una cuenta de Kapture contiene tu dirección de correo electrónico y, si usas Kapture Pro, tu licencia y los dispositivos que actives.</p>',
 'zh': '<p>Kapture 账户保存你的电子邮件地址；如果你使用 Kapture Pro，还会保存你的许可证以及你激活的设备。</p>',
 'ko': '<p>Kapture 계정에는 이메일 주소가 저장되며, Kapture Pro를 사용하는 경우 라이선스와 사용자가 활성화한 기기도 저장됩니다.</p>',
 'ja': '<p>Kapture アカウントには、お客様のメールアドレスと、Kapture Pro をご利用の場合はライセンスおよびお客様が有効化した端末の情報が保存されます。</p>',
 'de': '<p>Ein Kapture-Konto enthält deine E-Mail-Adresse und, wenn du Kapture Pro nutzt, deine Lizenz und die Geräte, die du aktivierst.</p>',
 'fr': '<p>Un compte Kapture contient votre adresse e-mail et, si vous utilisez Kapture Pro, votre licence et les appareils que vous activez.</p>',
 'pt-br': '<p>Uma conta Kapture guarda seu endereço de e-mail e, se você usar o Kapture Pro, sua licença e os dispositivos que você ativar.</p>',
 'it': '<p>Un account Kapture contiene il tuo indirizzo email e, se usi Kapture Pro, la tua licenza e i dispositivi che attivi.</p>'},

'<p>We do not use advertising, analytics or tracking, and we never sell your data.</p>': {
 'es': '<p>No usamos publicidad, analíticas ni seguimiento, y nunca vendemos tus datos.</p>',
 'zh': '<p>我们不使用广告、分析或追踪，也绝不出售你的数据。</p>',
 'ko': '<p>당사는 광고, 분석, 추적을 사용하지 않으며 사용자의 데이터를 절대 판매하지 않습니다.</p>',
 'ja': '<p>当社は広告、解析、トラッキングを使用せず、お客様のデータを販売することは一切ありません。</p>',
 'de': '<p>Wir verwenden keine Werbung, keine Analyse und kein Tracking, und wir verkaufen deine Daten niemals.</p>',
 'fr': "<p>Nous n'utilisons ni publicité, ni outils d'analyse, ni suivi, et nous ne vendons jamais vos données.</p>",
 'pt-br': '<p>Não usamos publicidade, analytics nem rastreamento, e nunca vendemos seus dados.</p>',
 'it': '<p>Non usiamo pubblicità, strumenti di analisi o tracciamento, e non vendiamo mai i tuoi dati.</p>'},

'<p>You can already create a Kapture account and sign in at kaptapp.com/account. Kapture Pro, its licences and its payments are not available yet. The parts of this section about them explain how we will handle that information once they are, and we will update this policy if anything changes before then.</p>': {
 'es': '<p>Ya puedes crear una cuenta de Kapture e iniciar sesión en kaptapp.com/account. Kapture Pro, sus licencias y sus pagos aún no están disponibles. Las partes de esta sección que se refieren a ellos explican cómo trataremos esa información cuando lo estén, y actualizaremos esta política si algo cambia antes de ese momento.</p>',
 'zh': '<p>你现在已经可以在 kaptapp.com/account 创建 Kapture 账户并登录。Kapture Pro 及其许可证和付款功能尚未推出。本节中与它们相关的内容，说明的是它们推出后我们将如何处理相关信息；如果在此之前有任何变化，我们会更新本政策。</p>',
 'ko': '<p>지금도 kaptapp.com/account에서 Kapture 계정을 만들고 로그인할 수 있습니다. Kapture Pro와 그 라이선스, 결제는 아직 제공되지 않습니다. 이 섹션에서 이들에 관한 부분은 제공이 시작된 뒤 당사가 해당 정보를 어떻게 처리할지 설명하며, 그 전에 달라지는 점이 있으면 본 방침을 업데이트합니다.</p>',
 'ja': '<p>Kapture アカウントは、すでに kaptapp.com/account で作成してサインインできます。Kapture Pro とそのライセンスおよび支払いは、まだ提供していません。このセクションのうちそれらに関する部分は、提供開始後に当社がその情報をどう扱うかを説明したものです。それまでに変更があれば、本ポリシーを更新します。</p>',
 'de': '<p>Du kannst bereits jetzt unter kaptapp.com/account ein Kapture-Konto erstellen und dich anmelden. Kapture Pro, die zugehörigen Lizenzen und Zahlungen sind noch nicht verfügbar. Die Teile dieses Abschnitts, die sie betreffen, erklären, wie wir mit diesen Informationen umgehen werden, sobald es so weit ist. Ändert sich bis dahin etwas, aktualisieren wir diese Erklärung.</p>',
 'fr': "<p>Vous pouvez déjà créer un compte Kapture et vous connecter sur kaptapp.com/account. Kapture Pro, ses licences et ses paiements ne sont pas encore disponibles. Les parties de cette section qui les concernent expliquent comment nous traiterons ces informations lorsqu'ils le seront, et nous mettrons à jour cette politique si quelque chose change d'ici là.</p>",
 'pt-br': '<p>Você já pode criar uma conta Kapture e entrar em kaptapp.com/account. O Kapture Pro, suas licenças e seus pagamentos ainda não estão disponíveis. As partes desta seção que tratam deles explicam como trataremos essas informações quando estiverem, e atualizaremos esta política se algo mudar antes disso.</p>',
 'it': '<p>Puoi già creare un account Kapture e accedere su kaptapp.com/account. Kapture Pro, le sue licenze e i relativi pagamenti non sono ancora disponibili. Le parti di questa sezione che li riguardano spiegano come tratteremo quelle informazioni quando lo saranno, e aggiorneremo questa informativa se nel frattempo cambierà qualcosa.</p>'},

'<p><strong>Account details.</strong> Your email address, your account ID, and when you signed up and last signed in. We use them to create your account, sign you in with an emailed link and contact you about your account. Legal basis: performing our contract with you.</p>': {
 'es': '<p><strong>Datos de la cuenta.</strong> Tu dirección de correo electrónico, el ID de tu cuenta y cuándo te registraste y cuándo iniciaste sesión por última vez. Los usamos para crear tu cuenta, permitirte iniciar sesión con un enlace que te enviamos por correo electrónico y ponernos en contacto contigo sobre tu cuenta. Base jurídica: la ejecución de nuestro contrato contigo.</p>',
 'zh': '<p><strong>账户信息。</strong>你的电子邮件地址、账户 ID，以及你注册和最近一次登录的时间。我们使用这些信息来创建你的账户、通过电子邮件发送的链接让你登录，并就你的账户与你联系。法律依据：履行我们与你之间的合同。</p>',
 'ko': '<p><strong>계정 정보.</strong> 이메일 주소, 계정 ID, 가입 시각과 마지막 로그인 시각입니다. 당사는 이 정보를 계정 생성, 이메일로 보낸 링크를 통한 로그인, 계정 관련 연락에 사용합니다. 법적 근거: 사용자와의 계약 이행.</p>',
 'ja': '<p><strong>アカウント情報。</strong>メールアドレス、アカウント ID、登録日時、最終サインイン日時。アカウントの作成、メールでお送りするリンクによるサインイン、アカウントに関するご連絡のために使用します。法的根拠：お客様との契約の履行。</p>',
 'de': '<p><strong>Kontodaten.</strong> Deine E-Mail-Adresse, deine Konto-ID sowie der Zeitpunkt deiner Registrierung und deiner letzten Anmeldung. Wir verwenden sie, um dein Konto anzulegen, dich über einen per E-Mail gesendeten Link anzumelden und dich zu deinem Konto zu kontaktieren. Rechtsgrundlage: Erfüllung unseres Vertrags mit dir.</p>',
 'fr': "<p><strong>Données du compte.</strong> Votre adresse e-mail, l'identifiant de votre compte, ainsi que la date de votre inscription et celle de votre dernière connexion. Nous les utilisons pour créer votre compte, vous connecter au moyen d'un lien envoyé par e-mail et vous contacter au sujet de votre compte. Base juridique&nbsp;: l'exécution de notre contrat avec vous.</p>",
 'pt-br': '<p><strong>Dados da conta.</strong> Seu endereço de e-mail, o ID da sua conta e quando você se cadastrou e entrou pela última vez. Usamos esses dados para criar sua conta, permitir que você entre com um link enviado por e-mail e entrar em contato com você sobre sua conta. Base legal: execução do nosso contrato com você.</p>',
 'it': "<p><strong>Dati dell'account.</strong> Il tuo indirizzo email, l'ID del tuo account, la data di registrazione e quella dell'ultimo accesso. Li usiamo per creare il tuo account, farti accedere con un link inviato via email e contattarti in merito al tuo account. Base giuridica: esecuzione del contratto con te.</p>"},

'<p><strong>Sign-in sessions.</strong> For each signed-in session, the IP address and browser information recorded by our sign-in provider. We use them to keep accounts secure and to stop misuse. Legal basis: our legitimate interest in security.</p>': {
 'es': '<p><strong>Sesiones de acceso.</strong> Para cada sesión iniciada, la dirección IP y la información del navegador que registra nuestro proveedor de inicio de sesión. Las usamos para mantener la seguridad de las cuentas e impedir usos indebidos. Base jurídica: nuestro interés legítimo en la seguridad.</p>',
 'zh': '<p><strong>登录会话。</strong>每个已登录会话中，由我们的登录服务提供商记录的 IP 地址和浏览器信息。我们使用这些信息来保障账户安全并防止滥用。法律依据：我们在安全方面的正当利益。</p>',
 'ko': '<p><strong>로그인 세션.</strong> 로그인한 각 세션에 대해 당사의 로그인 서비스 제공업체가 기록하는 IP 주소와 브라우저 정보입니다. 당사는 이 정보를 계정을 안전하게 보호하고 오용을 막는 데 사용합니다. 법적 근거: 보안에 관한 당사의 정당한 이익.</p>',
 'ja': '<p><strong>サインインセッション。</strong>サインイン中の各セッションについて、当社のサインインサービス提供事業者が記録する IP アドレスとブラウザー情報。アカウントの安全を保ち、不正利用を防ぐために使用します。法的根拠：セキュリティに関する当社の正当な利益。</p>',
 'de': '<p><strong>Anmeldesitzungen.</strong> Für jede angemeldete Sitzung die IP-Adresse und die Browserinformationen, die unser Anmeldedienst erfasst. Wir verwenden sie, um Konten zu schützen und Missbrauch zu verhindern. Rechtsgrundlage: unser berechtigtes Interesse an Sicherheit.</p>',
 'fr': "<p><strong>Sessions de connexion.</strong> Pour chaque session connectée, l'adresse IP et les informations sur le navigateur enregistrées par notre prestataire de connexion. Nous les utilisons pour sécuriser les comptes et empêcher les abus. Base juridique&nbsp;: notre intérêt légitime en matière de sécurité.</p>",
 'pt-br': '<p><strong>Sessões de login.</strong> Para cada sessão iniciada, o endereço IP e as informações do navegador registrados pelo nosso provedor de login. Usamos esses dados para manter as contas seguras e impedir o uso indevido. Base legal: nosso legítimo interesse em segurança.</p>',
 'it': "<p><strong>Sessioni di accesso.</strong> Per ogni sessione di accesso, l'indirizzo IP e le informazioni sul browser registrati dal nostro fornitore del servizio di accesso. Li usiamo per mantenere sicuri gli account e impedire abusi. Base giuridica: il nostro legittimo interesse alla sicurezza.</p>"},

'<p><strong>Devices.</strong> When you use Kapture Pro: an identifier created by the app, the device name, the platform (macOS or Windows), the app version, and when the device was activated, last checked its licence and was deactivated. We use them to apply the two-device limit, issue licences and show your devices on your account page. Legal basis: performing our contract with you.</p>': {
 'es': '<p><strong>Dispositivos.</strong> Cuando usas Kapture Pro: un identificador creado por la app, el nombre del dispositivo, la plataforma (macOS o Windows), la versión de la app y cuándo se activó el dispositivo, cuándo comprobó su licencia por última vez y cuándo se desactivó. Los usamos para aplicar el límite de dos dispositivos, emitir licencias y mostrar tus dispositivos en la página de tu cuenta. Base jurídica: la ejecución de nuestro contrato contigo.</p>',
 'zh': '<p><strong>设备。</strong>当你使用 Kapture Pro 时：应用生成的标识符、设备名称、平台（macOS 或 Windows）、应用版本，以及设备的激活时间、最近一次检查许可证的时间和停用时间。我们使用这些信息来执行两台设备的限制、签发许可证，并在你的账户页面上显示你的设备。法律依据：履行我们与你之间的合同。</p>',
 'ko': '<p><strong>기기.</strong> Kapture Pro를 사용하는 경우: 앱이 생성한 식별자, 기기 이름, 플랫폼(macOS 또는 Windows), 앱 버전, 그리고 기기가 활성화된 시각, 마지막으로 라이선스를 확인한 시각, 비활성화된 시각입니다. 당사는 이 정보를 기기 2대 제한 적용, 라이선스 발급, 계정 페이지의 기기 표시에 사용합니다. 법적 근거: 사용자와의 계약 이행.</p>',
 'ja': '<p><strong>端末。</strong>Kapture Pro をご利用の場合：アプリが作成する識別子、端末名、プラットフォーム（macOS または Windows）、アプリのバージョン、および端末を有効化した日時、最後にライセンスを確認した日時、無効化した日時。2 台までの端末制限の適用、ライセンスの発行、アカウントページでの端末の表示のために使用します。法的根拠：お客様との契約の履行。</p>',
 'de': '<p><strong>Geräte.</strong> Wenn du Kapture Pro nutzt: eine von der App erzeugte Kennung, der Gerätename, die Plattform (macOS oder Windows), die App-Version sowie die Zeitpunkte, zu denen das Gerät aktiviert wurde, zuletzt seine Lizenz geprüft hat und deaktiviert wurde. Wir verwenden sie, um die Begrenzung auf zwei Geräte umzusetzen, Lizenzen auszustellen und deine Geräte auf deiner Kontoseite anzuzeigen. Rechtsgrundlage: Erfüllung unseres Vertrags mit dir.</p>',
 'fr': "<p><strong>Appareils.</strong> Lorsque vous utilisez Kapture Pro&nbsp;: un identifiant créé par l'application, le nom de l'appareil, la plateforme (macOS ou Windows), la version de l'application, ainsi que les dates auxquelles l'appareil a été activé, a vérifié sa licence pour la dernière fois et a été désactivé. Nous les utilisons pour appliquer la limite de deux appareils, délivrer les licences et afficher vos appareils sur la page de votre compte. Base juridique&nbsp;: l'exécution de notre contrat avec vous.</p>",
 'pt-br': '<p><strong>Dispositivos.</strong> Quando você usa o Kapture Pro: um identificador criado pelo aplicativo, o nome do dispositivo, a plataforma (macOS ou Windows), a versão do aplicativo e quando o dispositivo foi ativado, verificou a licença pela última vez e foi desativado. Usamos esses dados para aplicar o limite de dois dispositivos, emitir licenças e mostrar seus dispositivos na página da sua conta. Base legal: execução do nosso contrato com você.</p>',
 'it': "<p><strong>Dispositivi.</strong> Quando usi Kapture Pro: un identificativo creato dall'app, il nome del dispositivo, la piattaforma (macOS o Windows), la versione dell'app e le date in cui il dispositivo è stato attivato, ha verificato per l'ultima volta la licenza ed è stato disattivato. Li usiamo per applicare il limite di due dispositivi, emettere le licenze e mostrare i tuoi dispositivi nella pagina del tuo account. Base giuridica: esecuzione del contratto con te.</p>"},

'<p><strong>Licence and trial.</strong> Whether you have Kapture Pro, on which plan and until when, when a free trial started and ends, and a one-way cryptographic hash of your email address. We use them to issue licences and to offer one free trial per person. Legal basis: performing our contract with you, and our legitimate interest in preventing repeated free trials.</p>': {
 'es': '<p><strong>Licencia y prueba.</strong> Si tienes Kapture Pro, con qué plan y hasta cuándo, cuándo empezó y cuándo termina una prueba gratuita, y un hash criptográfico unidireccional de tu dirección de correo electrónico. Los usamos para emitir licencias y ofrecer una sola prueba gratuita por persona. Base jurídica: la ejecución de nuestro contrato contigo y nuestro interés legítimo en evitar que se repitan las pruebas gratuitas.</p>',
 'zh': '<p><strong>许可证和试用。</strong>你是否拥有 Kapture Pro、使用哪种方案及有效期至何时、免费试用的开始和结束时间，以及你的电子邮件地址的单向加密哈希值。我们使用这些信息来签发许可证，并为每人提供一次免费试用。法律依据：履行我们与你之间的合同，以及我们在防止重复免费试用方面的正当利益。</p>',
 'ko': '<p><strong>라이선스 및 체험.</strong> Kapture Pro 보유 여부, 요금제와 이용 기한, 무료 체험의 시작 시점과 종료 시점, 그리고 이메일 주소의 단방향 암호화 해시입니다. 당사는 이 정보를 라이선스 발급과 1인당 1회 무료 체험 제공에 사용합니다. 법적 근거: 사용자와의 계약 이행, 그리고 무료 체험의 반복 이용을 막는 데 대한 당사의 정당한 이익.</p>',
 'ja': '<p><strong>ライセンスとトライアル。</strong>Kapture Pro の利用の有無、プランと有効期限、無料トライアルの開始日時と終了日時、およびメールアドレスの一方向暗号学的ハッシュ。ライセンスの発行と、無料トライアルをお一人様 1 回に限って提供するために使用します。法的根拠：お客様との契約の履行、および無料トライアルの繰り返し利用を防ぐという当社の正当な利益。</p>',
 'de': '<p><strong>Lizenz und Testphase.</strong> Ob du Kapture Pro hast, mit welchem Tarif und bis wann, wann eine kostenlose Testphase begonnen hat und endet, sowie ein kryptografischer Einweg-Hash deiner E-Mail-Adresse. Wir verwenden sie, um Lizenzen auszustellen und eine kostenlose Testphase pro Person anzubieten. Rechtsgrundlage: Erfüllung unseres Vertrags mit dir sowie unser berechtigtes Interesse daran, wiederholte kostenlose Testphasen zu verhindern.</p>',
 'fr': "<p><strong>Licence et essai.</strong> Si vous disposez de Kapture Pro, avec quelle formule et jusqu'à quand, quand un essai gratuit a commencé et quand il se termine, ainsi qu'une empreinte cryptographique à sens unique de votre adresse e-mail. Nous les utilisons pour délivrer les licences et proposer un essai gratuit par personne. Base juridique&nbsp;: l'exécution de notre contrat avec vous, et notre intérêt légitime à empêcher les essais gratuits répétés.</p>",
 'pt-br': '<p><strong>Licença e teste.</strong> Se você tem o Kapture Pro, em qual plano e até quando, quando um teste gratuito começou e quando termina, e um hash criptográfico unidirecional do seu endereço de e-mail. Usamos esses dados para emitir licenças e oferecer um único teste gratuito por pessoa. Base legal: execução do nosso contrato com você e nosso legítimo interesse em evitar testes gratuitos repetidos.</p>',
 'it': '<p><strong>Licenza e prova.</strong> Se hai Kapture Pro, con quale piano e fino a quando, quando è iniziata e quando termina una prova gratuita, e un hash crittografico unidirezionale del tuo indirizzo email. Li usiamo per emettere le licenze e offrire una sola prova gratuita a persona. Base giuridica: esecuzione del contratto con te e il nostro legittimo interesse a impedire prove gratuite ripetute.</p>'},

'<p><strong>Payments.</strong> When you pay for Kapture Pro: your Stripe customer and subscription IDs, plan, price, status, renewal and cancellation dates, and the amount, currency, date and refund status of each payment. We use them to give you the access you pay for and to keep financial records. Legal basis: performing our contract with you, and our legal obligation to keep accounting records.</p>': {
 'es': '<p><strong>Pagos.</strong> Cuando pagas por Kapture Pro: tus ID de cliente y de suscripción de Stripe, el plan, el precio, el estado, las fechas de renovación y cancelación, y el importe, la moneda, la fecha y el estado de reembolso de cada pago. Los usamos para darte el acceso por el que pagas y para llevar nuestros registros financieros. Base jurídica: la ejecución de nuestro contrato contigo y nuestra obligación legal de conservar registros contables.</p>',
 'zh': '<p><strong>付款。</strong>当你为 Kapture Pro 付款时：你的 Stripe 客户 ID 和订阅 ID、方案、价格、状态、续订和取消日期，以及每笔付款的金额、币种、日期和退款状态。我们使用这些信息来为你提供你所付费的使用权限，并保存财务记录。法律依据：履行我们与你之间的合同，以及我们保存会计记录的法定义务。</p>',
 'ko': '<p><strong>결제.</strong> Kapture Pro 요금을 결제하는 경우: Stripe 고객 ID와 구독 ID, 요금제, 가격, 상태, 갱신일과 해지일, 그리고 각 결제의 금액, 통화, 날짜, 환불 상태입니다. 당사는 이 정보를 결제한 만큼의 이용 권한을 제공하고 재무 기록을 보관하는 데 사용합니다. 법적 근거: 사용자와의 계약 이행, 그리고 회계 기록을 보관해야 하는 당사의 법적 의무.</p>',
 'ja': '<p><strong>支払い。</strong>Kapture Pro の料金をお支払いいただく場合：Stripe の顧客 ID とサブスクリプション ID、プラン、価格、ステータス、更新日と解約日、および各支払いの金額、通貨、日付、返金状況。お支払いいただいた利用権の提供と、財務記録の保管のために使用します。法的根拠：お客様との契約の履行、および会計記録を保管する当社の法的義務。</p>',
 'de': '<p><strong>Zahlungen.</strong> Wenn du für Kapture Pro bezahlst: deine Stripe-Kunden- und Abonnement-IDs, Tarif, Preis, Status, Verlängerungs- und Kündigungsdaten sowie Betrag, Währung, Datum und Erstattungsstatus jeder Zahlung. Wir verwenden sie, um dir den Zugang zu gewähren, für den du bezahlst, und um unsere Finanzunterlagen zu führen. Rechtsgrundlage: Erfüllung unseres Vertrags mit dir sowie unsere gesetzliche Pflicht, Buchführungsunterlagen aufzubewahren.</p>',
 'fr': "<p><strong>Paiements.</strong> Lorsque vous payez Kapture Pro&nbsp;: vos identifiants client et d'abonnement Stripe, la formule, le prix, le statut, les dates de renouvellement et de résiliation, ainsi que le montant, la devise, la date et le statut de remboursement de chaque paiement. Nous les utilisons pour vous donner l'accès pour lequel vous payez et pour tenir nos registres financiers. Base juridique&nbsp;: l'exécution de notre contrat avec vous, et notre obligation légale de conserver des documents comptables.</p>",
 'pt-br': '<p><strong>Pagamentos.</strong> Quando você paga pelo Kapture Pro: seus IDs de cliente e de assinatura na Stripe, plano, preço, status, datas de renovação e cancelamento, e o valor, a moeda, a data e o status de reembolso de cada pagamento. Usamos esses dados para dar a você o acesso pelo qual pagou e para manter registros financeiros. Base legal: execução do nosso contrato com você e nossa obrigação legal de manter registros contábeis.</p>',
 'it': "<p><strong>Pagamenti.</strong> Quando paghi Kapture Pro: i tuoi ID cliente e abbonamento Stripe, il piano, il prezzo, lo stato, le date di rinnovo e di annullamento, e l'importo, la valuta, la data e lo stato di rimborso di ogni pagamento. Li usiamo per darti l'accesso per cui paghi e per tenere la documentazione finanziaria. Base giuridica: esecuzione del contratto con te e il nostro obbligo legale di tenere le scritture contabili.</p>"},

'<p><strong>Messages you send us.</strong> We use them to answer you. Legal basis: our legitimate interest in responding to you, or our contract with you where your message is about your account.</p>': {
 'es': '<p><strong>Mensajes que nos envías.</strong> Los usamos para responderte. Base jurídica: nuestro interés legítimo en responderte o, cuando tu mensaje trata sobre tu cuenta, nuestro contrato contigo.</p>',
 'zh': '<p><strong>你发给我们的消息。</strong>我们使用这些消息来回复你。法律依据：我们在回复你方面的正当利益；如果消息与你的账户有关，则为我们与你之间的合同。</p>',
 'ko': '<p><strong>사용자가 보낸 메시지.</strong> 당사는 메시지에 답변하는 데 이를 사용합니다. 법적 근거: 사용자에게 답변하는 데 대한 당사의 정당한 이익, 또는 메시지가 계정에 관한 것인 경우 사용자와의 계약.</p>',
 'ja': '<p><strong>お客様からのメッセージ。</strong>お客様への返信のために使用します。法的根拠：お客様に返信するという当社の正当な利益、またはメッセージがアカウントに関するものである場合はお客様との契約。</p>',
 'de': '<p><strong>Nachrichten, die du uns sendest.</strong> Wir verwenden sie, um dir zu antworten. Rechtsgrundlage: unser berechtigtes Interesse daran, dir zu antworten, oder unser Vertrag mit dir, wenn deine Nachricht dein Konto betrifft.</p>',
 'fr': '<p><strong>Messages que vous nous envoyez.</strong> Nous les utilisons pour vous répondre. Base juridique&nbsp;: notre intérêt légitime à vous répondre, ou notre contrat avec vous lorsque votre message concerne votre compte.</p>',
 'pt-br': '<p><strong>Mensagens que você nos envia.</strong> Usamos essas mensagens para responder a você. Base legal: nosso legítimo interesse em responder a você ou, quando sua mensagem for sobre sua conta, nosso contrato com você.</p>',
 'it': '<p><strong>Messaggi che ci invii.</strong> Li usiamo per risponderti. Base giuridica: il nostro legittimo interesse a risponderti, oppure il contratto con te quando il messaggio riguarda il tuo account.</p>'},

'<p>A Kapture Pro licence saved on your computer contains your account ID, a one-way hash of the device identifier, your plan and the dates it is valid for. We sign it so the app can check it offline.</p>': {
 'es': '<p>Una licencia de Kapture Pro guardada en tu ordenador contiene el ID de tu cuenta, un hash unidireccional del identificador del dispositivo, tu plan y las fechas en que es válida. La firmamos para que la app pueda comprobarla sin conexión.</p>',
 'zh': '<p>保存在你电脑上的 Kapture Pro 许可证包含你的账户 ID、设备标识符的单向哈希值、你的方案及其有效日期。我们会对许可证进行签名，以便应用在离线状态下验证它。</p>',
 'ko': '<p>컴퓨터에 저장되는 Kapture Pro 라이선스에는 계정 ID, 기기 식별자의 단방향 해시, 요금제와 유효 기간이 담겨 있습니다. 당사는 앱이 오프라인에서도 라이선스를 확인할 수 있도록 여기에 서명합니다.</p>',
 'ja': '<p>お客様のパソコンに保存される Kapture Pro のライセンスには、アカウント ID、端末識別子の一方向ハッシュ、プラン、有効期間が含まれます。アプリがオフラインで確認できるよう、当社がライセンスに署名しています。</p>',
 'de': '<p>Eine auf deinem Computer gespeicherte Lizenz für Kapture Pro enthält deine Konto-ID, einen Einweg-Hash der Gerätekennung, deinen Tarif und den Zeitraum, für den sie gilt. Wir signieren sie, damit die App sie offline prüfen kann.</p>',
 'fr': "<p>Une licence Kapture Pro enregistrée sur votre ordinateur contient l'identifiant de votre compte, une empreinte à sens unique de l'identifiant de l'appareil, votre formule et ses dates de validité. Nous la signons pour que l'application puisse la vérifier hors ligne.</p>",
 'pt-br': '<p>Uma licença do Kapture Pro salva no seu computador contém o ID da sua conta, um hash unidirecional do identificador do dispositivo, seu plano e as datas em que ela é válida. Nós a assinamos para que o aplicativo possa verificá-la offline.</p>',
 'it': "<p>Una licenza Kapture Pro salvata sul tuo computer contiene l'ID del tuo account, un hash unidirezionale dell'identificativo del dispositivo, il tuo piano e le date di validità. La firmiamo perché l'app possa verificarla offline.</p>"},

'<p>We do not receive your screenshots or PDFs, their file names or contents, the pages you capture, or your library, projects, collections, tags, notes or searches. kaptapp.com, Kapture for Chrome and Kapture Pro contain no advertising, analytics or tracking.</p>': {
 'es': '<p>No recibimos tus capturas de pantalla ni tus PDF, sus nombres de archivo ni su contenido, las páginas que capturas, ni tu biblioteca, proyectos, colecciones, etiquetas, notas o búsquedas. kaptapp.com, Kapture para Chrome y Kapture Pro no incluyen publicidad, analíticas ni seguimiento.</p>',
 'zh': '<p>我们不会接收你的截图或 PDF、它们的文件名或内容、你截取的页面，也不会接收你的资料库、项目、合集、标签、备注或搜索内容。kaptapp.com、Chrome 版 Kapture 和 Kapture Pro 均不含广告、分析或追踪。</p>',
 'ko': '<p>당사는 사용자의 스크린샷이나 PDF, 그 파일 이름이나 내용, 캡처한 페이지, 라이브러리, 프로젝트, 컬렉션, 태그, 메모, 검색 내용을 받지 않습니다. kaptapp.com, Chrome용 Kapture, Kapture Pro에는 광고, 분석, 추적이 포함되어 있지 않습니다.</p>',
 'ja': '<p>当社は、スクリーンショットや PDF、そのファイル名や内容、キャプチャしたページ、ライブラリ、プロジェクト、コレクション、タグ、メモ、検索内容を受け取りません。kaptapp.com、Chrome 版 Kapture、Kapture Pro には、広告、解析、トラッキングは含まれていません。</p>',
 'de': '<p>Wir erhalten weder deine Screenshots oder PDFs noch deren Dateinamen oder Inhalte, die Seiten, die du aufnimmst, oder deine Bibliothek, Projekte, Sammlungen, Tags, Notizen oder Suchen. kaptapp.com, Kapture für Chrome und Kapture Pro enthalten keine Werbung, keine Analyse und kein Tracking.</p>',
 'fr': "<p>Nous ne recevons pas vos captures d'écran ni vos PDF, leurs noms de fichier ni leur contenu, les pages que vous capturez, ni votre bibliothèque, vos projets, collections, tags, notes ou recherches. kaptapp.com, Kapture pour Chrome et Kapture Pro ne contiennent ni publicité, ni outils d'analyse, ni suivi.</p>",
 'pt-br': '<p>Não recebemos suas capturas de tela nem seus PDFs, os nomes ou o conteúdo desses arquivos, as páginas que você captura, nem sua biblioteca, projetos, coleções, etiquetas, notas ou buscas. O kaptapp.com, o Kapture para Chrome e o Kapture Pro não têm publicidade, analytics nem rastreamento.</p>',
 'it': '<p>Non riceviamo i tuoi screenshot o PDF, i nomi dei file o il loro contenuto, le pagine che catturi, né la tua libreria, i progetti, le raccolte, i tag, le note o le ricerche. kaptapp.com, Kapture per Chrome e Kapture Pro non contengono pubblicità, strumenti di analisi o tracciamento.</p>'},

'<p>Payments will be handled by Stripe (Stripe Payments Europe, Limited, with Stripe Payments UK Ltd for regulated payment services). Stripe collects your payment details and billing address and, if you give one, your tax ID. We never receive or store your full card number or security code. Stripe also uses payment information for its own purposes, such as preventing fraud and meeting its legal obligations, as described in its privacy policy at stripe.com/privacy.</p>': {
 'es': '<p>Los pagos los gestionará Stripe (Stripe Payments Europe, Limited, junto con Stripe Payments UK Ltd para los servicios de pago regulados). Stripe recopila tus datos de pago y tu dirección de facturación y, si lo facilitas, tu número de identificación fiscal. Nunca recibimos ni almacenamos el número completo de tu tarjeta ni su código de seguridad. Stripe también usa la información de pago para sus propios fines, como prevenir el fraude y cumplir sus obligaciones legales, según se describe en su política de privacidad en stripe.com/privacy.</p>',
 'zh': '<p>付款将由 Stripe 处理（Stripe Payments Europe, Limited，受监管的支付服务则由 Stripe Payments UK Ltd 提供）。Stripe 会收集你的付款信息和账单地址，如果你提供了税号，也会收集你的税号。我们绝不会接收或存储你的完整卡号或安全码。Stripe 还会将付款信息用于其自身目的，例如防范欺诈和履行其法定义务，详见其隐私政策 stripe.com/privacy。</p>',
 'ko': '<p>결제는 Stripe(Stripe Payments Europe, Limited, 규제 대상 결제 서비스는 Stripe Payments UK Ltd)가 처리할 예정입니다. Stripe는 결제 정보와 청구지 주소를 수집하며, 사용자가 제공하는 경우 세금 식별 번호도 수집합니다. 당사는 전체 카드 번호나 보안 코드를 절대 받거나 저장하지 않습니다. Stripe는 사기 방지와 법적 의무 이행 등 자체 목적으로도 결제 정보를 사용하며, 이는 stripe.com/privacy의 Stripe 개인정보처리방침에 설명되어 있습니다.</p>',
 'ja': '<p>支払いは Stripe（Stripe Payments Europe, Limited。規制対象の決済サービスについては Stripe Payments UK Ltd）が取り扱う予定です。Stripe は、お客様の支払い情報と請求先住所、および提供された場合は税番号を収集します。当社がカード番号の全桁やセキュリティコードを受け取ったり保存したりすることはありません。また Stripe は、不正防止や法的義務の履行など、Stripe 自身の目的のためにも支払い情報を利用します。詳しくは stripe.com/privacy にある Stripe のプライバシーポリシーをご覧ください。</p>',
 'de': '<p>Zahlungen wird Stripe abwickeln (Stripe Payments Europe, Limited, mit Stripe Payments UK Ltd für regulierte Zahlungsdienste). Stripe erhebt deine Zahlungsdaten und deine Rechnungsadresse sowie, falls du sie angibst, deine Steuernummer. Wir erhalten oder speichern niemals deine vollständige Kartennummer oder deinen Sicherheitscode. Stripe verwendet Zahlungsinformationen auch für eigene Zwecke, etwa um Betrug zu verhindern und gesetzliche Pflichten zu erfüllen, wie in der Datenschutzerklärung von Stripe unter stripe.com/privacy beschrieben.</p>',
 'fr': "<p>Les paiements seront gérés par Stripe (Stripe Payments Europe, Limited, avec Stripe Payments UK Ltd pour les services de paiement réglementés). Stripe collecte vos informations de paiement et votre adresse de facturation et, si vous en indiquez un, votre numéro d'identification fiscale. Nous ne recevons ni ne conservons jamais votre numéro de carte complet ni votre code de sécurité. Stripe utilise également les informations de paiement à ses propres fins, par exemple pour prévenir la fraude et respecter ses obligations légales, comme l'explique sa politique de confidentialité sur stripe.com/privacy.</p>",
 'pt-br': '<p>Os pagamentos serão processados pela Stripe (Stripe Payments Europe, Limited, com a Stripe Payments UK Ltd para serviços de pagamento regulados). A Stripe coleta seus dados de pagamento e seu endereço de cobrança e, se você informar, seu número de identificação fiscal. Nunca recebemos nem armazenamos o número completo do seu cartão nem o código de segurança. A Stripe também usa as informações de pagamento para fins próprios, como prevenir fraudes e cumprir suas obrigações legais, conforme descrito na política de privacidade dela em stripe.com/privacy.</p>',
 'it': "<p>I pagamenti saranno gestiti da Stripe (Stripe Payments Europe, Limited, con Stripe Payments UK Ltd per i servizi di pagamento regolamentati). Stripe raccoglie i tuoi dati di pagamento e l'indirizzo di fatturazione e, se lo fornisci, il tuo identificativo fiscale. Non riceviamo né conserviamo mai il numero completo della tua carta o il codice di sicurezza. Stripe usa le informazioni di pagamento anche per scopi propri, come prevenire le frodi e adempiere ai propri obblighi di legge, come descritto nella sua informativa sulla privacy su stripe.com/privacy.</p>"},

'<p><strong>Supabase</strong> runs account sign-in, including sign-in emails, our account and licence database, and the service that issues licences. The data is stored in the European Union (Ireland). Supabase, Inc. is based in the United States and may access data to provide support.</p>': {
 'es': '<p><strong>Supabase</strong> gestiona el inicio de sesión en las cuentas, incluidos los correos de inicio de sesión, nuestra base de datos de cuentas y licencias, y el servicio que emite las licencias. Los datos se almacenan en la Unión Europea (Irlanda). Supabase, Inc. tiene su sede en Estados Unidos y puede acceder a los datos para prestar asistencia.</p>',
 'zh': '<p><strong>Supabase</strong> 负责运行账户登录（包括登录邮件）、我们的账户和许可证数据库，以及签发许可证的服务。这些数据存储在欧盟（爱尔兰）。Supabase, Inc. 位于美国，可能会为提供支持而访问数据。</p>',
 'ko': '<p><strong>Supabase</strong>는 로그인 이메일을 포함한 계정 로그인, 당사의 계정 및 라이선스 데이터베이스, 라이선스를 발급하는 서비스를 운영합니다. 데이터는 유럽연합(아일랜드)에 저장됩니다. Supabase, Inc.는 미국에 소재하며 지원 제공을 위해 데이터에 접근할 수 있습니다.</p>',
 'ja': '<p><strong>Supabase</strong> は、サインイン用メールを含むアカウントのサインイン、当社のアカウントおよびライセンスのデータベース、ライセンスを発行するサービスを運用しています。データは欧州連合（アイルランド）に保存されます。Supabase, Inc. は米国を拠点としており、サポート提供のためにデータにアクセスすることがあります。</p>',
 'de': '<p><strong>Supabase</strong> betreibt die Kontoanmeldung, einschließlich der Anmelde-E-Mails, unsere Konto- und Lizenzdatenbank sowie den Dienst, der Lizenzen ausstellt. Die Daten werden in der Europäischen Union (Irland) gespeichert. Supabase, Inc. hat ihren Sitz in den Vereinigten Staaten und kann zu Supportzwecken auf Daten zugreifen.</p>',
 'fr': "<p><strong>Supabase</strong> assure la connexion aux comptes, y compris les e-mails de connexion, notre base de données des comptes et des licences, et le service qui délivre les licences. Les données sont stockées dans l'Union européenne (Irlande). Supabase, Inc. est établie aux États-Unis et peut accéder aux données pour fournir une assistance.</p>",
 'pt-br': '<p>A <strong>Supabase</strong> opera o login das contas, incluindo os e-mails de login, nosso banco de dados de contas e licenças e o serviço que emite as licenças. Os dados são armazenados na União Europeia (Irlanda). A Supabase, Inc. tem sede nos Estados Unidos e pode acessar os dados para prestar suporte.</p>',
 'it': "<p><strong>Supabase</strong> gestisce l'accesso agli account, comprese le email di accesso, il nostro database di account e licenze e il servizio che emette le licenze. I dati sono conservati nell'Unione europea (Irlanda). Supabase, Inc. ha sede negli Stati Uniti e può accedere ai dati per fornire assistenza.</p>"},

'<p><strong>Stripe</strong> will process payments and subscriptions, as described above.</p>': {
 'es': '<p><strong>Stripe</strong> tratará los pagos y las suscripciones, como se describe más arriba.</p>',
 'zh': '<p><strong>Stripe</strong> 将按上文所述处理付款和订阅。</p>',
 'ko': '<p><strong>Stripe</strong>는 위에서 설명한 대로 결제와 구독을 처리할 예정입니다.</p>',
 'ja': '<p><strong>Stripe</strong> は、上記のとおり支払いとサブスクリプションを処理する予定です。</p>',
 'de': '<p><strong>Stripe</strong> wird Zahlungen und Abonnements verarbeiten, wie oben beschrieben.</p>',
 'fr': '<p><strong>Stripe</strong> traitera les paiements et les abonnements, comme décrit ci-dessus.</p>',
 'pt-br': '<p>A <strong>Stripe</strong> processará pagamentos e assinaturas, conforme descrito acima.</p>',
 'it': '<p><strong>Stripe</strong> tratterà pagamenti e abbonamenti, come descritto sopra.</p>'},

'<p><strong>GitHub Pages</strong> hosts kaptapp.com and receives standard web request information, such as IP addresses. It is based in the United States.</p>': {
 'es': '<p><strong>GitHub Pages</strong> aloja kaptapp.com y recibe la información estándar de las solicitudes web, como las direcciones IP. Tiene su sede en Estados Unidos.</p>',
 'zh': '<p><strong>GitHub Pages</strong> 托管 kaptapp.com，并会接收标准的网络请求信息，例如 IP 地址。它位于美国。</p>',
 'ko': '<p><strong>GitHub Pages</strong>는 kaptapp.com을 호스팅하며, IP 주소 등 일반적인 웹 요청 정보를 수신합니다. GitHub Pages는 미국에 소재합니다.</p>',
 'ja': '<p><strong>GitHub Pages</strong> は kaptapp.com をホストしており、IP アドレスなど、ウェブリクエストに伴う標準的な情報を受け取ります。米国を拠点としています。</p>',
 'de': '<p><strong>GitHub Pages</strong> hostet kaptapp.com und erhält die üblichen Informationen von Webanfragen, etwa IP-Adressen. Der Dienst hat seinen Sitz in den Vereinigten Staaten.</p>',
 'fr': '<p><strong>GitHub Pages</strong> héberge kaptapp.com et reçoit les informations habituelles des requêtes web, comme les adresses IP. Ce service est établi aux États-Unis.</p>',
 'pt-br': '<p>O <strong>GitHub Pages</strong> hospeda o kaptapp.com e recebe informações padrão de requisições web, como endereços IP. Ele tem sede nos Estados Unidos.</p>',
 'it': '<p><strong>GitHub Pages</strong> ospita kaptapp.com e riceve le normali informazioni delle richieste web, come gli indirizzi IP. Ha sede negli Stati Uniti.</p>'},

'<p>When information is transferred outside the UK or the European Economic Area, we rely on the safeguards these providers offer, such as UK adequacy regulations, the UK&ndash;US data bridge, the EU&ndash;US Data Privacy Framework or standard contractual clauses.</p>': {
 'es': '<p>Cuando la información se transfiere fuera del Reino Unido o del Espacio Económico Europeo, nos basamos en las garantías que ofrecen estos proveedores, como los reglamentos de adecuación del Reino Unido, el puente de datos Reino Unido&ndash;EE. UU., el Marco de Privacidad de Datos UE&ndash;EE. UU. o las cláusulas contractuales tipo.</p>',
 'zh': '<p>当信息被传输到英国或欧洲经济区以外时，我们依靠这些服务商提供的保障措施，例如英国充分性认定条例、英国&ndash;美国数据桥、欧盟&ndash;美国数据隐私框架或标准合同条款。</p>',
 'ko': '<p>정보가 영국 또는 유럽경제지역 밖으로 이전되는 경우, 당사는 영국 적정성 규정, 영국&ndash;미국 데이터 브리지, EU&ndash;미국 데이터 프라이버시 프레임워크, 표준계약조항 등 이들 업체가 제공하는 보호 조치에 의존합니다.</p>',
 'ja': '<p>情報が英国または欧州経済領域の外に移転される場合、当社はこれらの事業者が提供する保護措置に依拠します。たとえば、英国の十分性認定規則、英国・米国間のデータブリッジ、EU・米国データプライバシーフレームワーク、標準契約条項などです。</p>',
 'de': '<p>Werden Informationen in Länder außerhalb des Vereinigten Königreichs oder des Europäischen Wirtschaftsraums übermittelt, stützen wir uns auf die Garantien dieser Anbieter, etwa Angemessenheitsregelungen des Vereinigten Königreichs, die UK&ndash;US-Datenbrücke (UK&ndash;US Data Bridge), das EU&ndash;US Data Privacy Framework oder Standardvertragsklauseln.</p>',
 'fr': "<p>Lorsque des informations sont transférées hors du Royaume-Uni ou de l'Espace économique européen, nous nous appuyons sur les garanties proposées par ces prestataires, telles que les règlements d'adéquation du Royaume-Uni, le pont de données Royaume-Uni&ndash;États-Unis (UK&ndash;US data bridge), le cadre de protection des données UE&ndash;États-Unis (EU&ndash;US Data Privacy Framework) ou les clauses contractuelles types.</p>",
 'pt-br': '<p>Quando informações são transferidas para fora do Reino Unido ou do Espaço Econômico Europeu, contamos com as salvaguardas oferecidas por esses provedores, como os regulamentos de adequação do Reino Unido, a ponte de dados Reino Unido&ndash;EUA, o Data Privacy Framework UE&ndash;EUA ou cláusulas contratuais padrão.</p>',
 'it': '<p>Quando le informazioni vengono trasferite fuori dal Regno Unito o dallo Spazio economico europeo, ci basiamo sulle garanzie offerte da questi fornitori, come i regolamenti di adeguatezza del Regno Unito, il data bridge Regno Unito&ndash;USA, il Data Privacy Framework UE&ndash;USA o le clausole contrattuali standard.</p>'},

'<p>Account details, sign-in sessions and device records, including devices you have deactivated, are kept while your account exists and are deleted when it is deleted.</p>': {
 'es': '<p>Los datos de la cuenta, las sesiones de acceso y los registros de dispositivos, incluidos los dispositivos que hayas desactivado, se conservan mientras exista tu cuenta y se eliminan cuando esta se elimina.</p>',
 'zh': '<p>账户信息、登录会话和设备记录（包括你已停用的设备）会在你的账户存续期间保留，并在账户删除时一并删除。</p>',
 'ko': '<p>계정 정보, 로그인 세션, 기기 기록(비활성화한 기기 포함)은 계정이 존재하는 동안 보관되며 계정을 삭제하면 함께 삭제됩니다.</p>',
 'ja': '<p>アカウント情報、サインインセッション、端末の記録（無効化した端末を含む）は、アカウントが存在する間保存され、アカウントの削除時に削除されます。</p>',
 'de': '<p>Kontodaten, Anmeldesitzungen und Geräteeinträge, einschließlich der Geräte, die du deaktiviert hast, werden gespeichert, solange dein Konto besteht, und gelöscht, wenn es gelöscht wird.</p>',
 'fr': "<p>Les données du compte, les sessions de connexion et les enregistrements d'appareils, y compris les appareils que vous avez désactivés, sont conservés tant que votre compte existe et supprimés lorsqu'il est supprimé.</p>",
 'pt-br': '<p>Os dados da conta, as sessões de login e os registros de dispositivos, incluindo os dispositivos que você desativou, são mantidos enquanto sua conta existir e são excluídos quando ela for excluída.</p>',
 'it': "<p>I dati dell'account, le sessioni di accesso e i registri dei dispositivi, compresi i dispositivi che hai disattivato, sono conservati finché il tuo account esiste e vengono eliminati quando l'account viene eliminato.</p>"},

'<p>The trial record, including the hash of your email address, is kept after your account is deleted for as long as we offer free trials, so that a trial cannot be claimed again with the same email address. The hash cannot be turned back into your address.</p>': {
 'es': '<p>El registro de la prueba, incluido el hash de tu dirección de correo electrónico, se conserva después de eliminar tu cuenta mientras ofrezcamos pruebas gratuitas, para que no se pueda volver a solicitar una prueba con la misma dirección de correo electrónico. El hash no se puede convertir de nuevo en tu dirección.</p>',
 'zh': '<p>试用记录（包括你的电子邮件地址的哈希值）在你的账户删除后仍会保留，只要我们仍提供免费试用就会一直保留，以防同一电子邮件地址再次申领试用。该哈希值无法还原为你的电子邮件地址。</p>',
 'ko': '<p>이메일 주소의 해시를 포함한 체험 기록은 같은 이메일 주소로 체험을 다시 신청할 수 없도록, 계정을 삭제한 뒤에도 당사가 무료 체험을 제공하는 동안 보관됩니다. 이 해시는 원래 이메일 주소로 되돌릴 수 없습니다.</p>',
 'ja': '<p>メールアドレスのハッシュを含むトライアルの記録は、同じメールアドレスで再びトライアルを利用できないよう、アカウント削除後も、当社が無料トライアルを提供している間は保存されます。このハッシュからお客様のメールアドレスを復元することはできません。</p>',
 'de': '<p>Der Eintrag zur Testphase, einschließlich des Hashs deiner E-Mail-Adresse, wird nach der Löschung deines Kontos so lange aufbewahrt, wie wir kostenlose Testphasen anbieten, damit eine Testphase nicht erneut mit derselben E-Mail-Adresse in Anspruch genommen werden kann. Aus dem Hash lässt sich deine Adresse nicht wiederherstellen.</p>',
 'fr': "<p>L'enregistrement de l'essai, y compris l'empreinte de votre adresse e-mail, est conservé après la suppression de votre compte aussi longtemps que nous proposons des essais gratuits, afin qu'un essai ne puisse pas être obtenu à nouveau avec la même adresse e-mail. L'empreinte ne permet pas de retrouver votre adresse.</p>",
 'pt-br': '<p>O registro do teste, incluindo o hash do seu endereço de e-mail, é mantido após a exclusão da sua conta enquanto oferecermos testes gratuitos, para que um teste não possa ser solicitado novamente com o mesmo endereço de e-mail. O hash não pode ser convertido de volta no seu endereço.</p>',
 'it': "<p>Il registro della prova, compreso l'hash del tuo indirizzo email, viene conservato anche dopo l'eliminazione del tuo account finché offriamo prove gratuite, così che non si possa richiedere di nuovo una prova con lo stesso indirizzo email. Dall'hash non è possibile risalire al tuo indirizzo.</p>"},

'<p>Payment records are kept by Stripe, and we keep the payment records that UK law requires for accounting, generally for six years.</p>': {
 'es': '<p>Stripe conserva los registros de pago, y nosotros conservamos los registros de pago que exige la legislación del Reino Unido a efectos contables, por lo general durante seis años.</p>',
 'zh': '<p>付款记录由 Stripe 保存；我们也会按照英国法律对会计的要求保存付款记录，保存期限一般为六年。</p>',
 'ko': '<p>결제 기록은 Stripe가 보관하며, 당사는 영국 법률이 회계 목적으로 요구하는 결제 기록을 일반적으로 6년간 보관합니다.</p>',
 'ja': '<p>支払いの記録は Stripe が保管します。また当社は、英国法が会計上求める支払いの記録を、通常 6 年間保管します。</p>',
 'de': '<p>Zahlungsunterlagen werden von Stripe aufbewahrt. Wir selbst bewahren die Zahlungsunterlagen auf, die das britische Recht für die Buchführung vorschreibt, in der Regel sechs Jahre lang.</p>',
 'fr': '<p>Les registres de paiement sont conservés par Stripe, et nous conservons ceux que le droit britannique exige à des fins comptables, en général pendant six ans.</p>',
 'pt-br': '<p>Os registros de pagamento são mantidos pela Stripe, e nós mantemos os registros de pagamento que a legislação do Reino Unido exige para fins contábeis, geralmente por seis anos.</p>',
 'it': '<p>I registri dei pagamenti sono conservati da Stripe, e noi conserviamo i registri dei pagamenti che la legge del Regno Unito richiede a fini contabili, in genere per sei anni.</p>'},

'<p>Records of payment notifications from Stripe hold Stripe IDs and processing status, not payment details, and are kept while we need them to process and check those notifications.</p>': {
 'es': '<p>Los registros de las notificaciones de pago de Stripe contienen los ID de Stripe y el estado de procesamiento, no los datos de pago, y se conservan mientras los necesitemos para procesar y verificar esas notificaciones.</p>',
 'zh': '<p>来自 Stripe 的付款通知记录包含 Stripe ID 和处理状态，不含付款信息，并会在我们处理和核对这些通知所需的期间内保留。</p>',
 'ko': '<p>Stripe에서 받은 결제 알림 기록에는 결제 정보가 아니라 Stripe ID와 처리 상태가 담기며, 해당 알림을 처리하고 확인하는 데 필요한 동안 보관됩니다.</p>',
 'ja': '<p>Stripe からの支払い通知の記録には、支払い情報ではなく Stripe の ID と処理状況が含まれ、それらの通知の処理と確認に必要な間保存されます。</p>',
 'de': '<p>Einträge zu Zahlungsbenachrichtigungen von Stripe enthalten Stripe-IDs und den Verarbeitungsstatus, keine Zahlungsdaten, und werden aufbewahrt, solange wir sie benötigen, um diese Benachrichtigungen zu verarbeiten und zu prüfen.</p>',
 'fr': "<p>Les enregistrements des notifications de paiement envoyées par Stripe contiennent des identifiants Stripe et l'état du traitement, mais pas de données de paiement, et sont conservés tant que nous en avons besoin pour traiter et vérifier ces notifications.</p>",
 'pt-br': '<p>Os registros das notificações de pagamento da Stripe contêm IDs da Stripe e o status de processamento, não dados de pagamento, e são mantidos enquanto precisarmos deles para processar e verificar essas notificações.</p>',
 'it': '<p>I registri delle notifiche di pagamento inviate da Stripe contengono gli ID Stripe e lo stato di elaborazione, non i dati di pagamento, e sono conservati finché ci servono per elaborare e verificare tali notifiche.</p>'},

'<p>The account page keeps your signed-in session in your browser&rsquo;s local storage so that you stay signed in. It is needed for the page to work and is removed when you sign out. kaptapp.com sets no advertising or analytics cookies.</p>': {
 'es': '<p>La página de la cuenta guarda tu sesión iniciada en el almacenamiento local de tu navegador para que mantengas la sesión abierta. Es necesaria para que la página funcione y se elimina cuando cierras sesión. kaptapp.com no instala cookies de publicidad ni de analíticas.</p>',
 'zh': '<p>账户页面会将你的登录会话保存在浏览器的本地存储中，以便你保持登录状态。这是页面正常运行所必需的，并会在你退出登录时删除。kaptapp.com 不设置任何广告或分析 Cookie。</p>',
 'ko': '<p>계정 페이지는 로그인 상태가 유지되도록 로그인 세션을 브라우저의 로컬 저장소에 보관합니다. 이는 페이지가 작동하는 데 필요하며 로그아웃하면 삭제됩니다. kaptapp.com은 광고 또는 분석 쿠키를 설정하지 않습니다.</p>',
 'ja': '<p>アカウントページは、サインインした状態を保つため、サインインセッションをブラウザーのローカルストレージに保存します。これはページの動作に必要なもので、サインアウトすると削除されます。kaptapp.com は広告用や解析用の Cookie を設定しません。</p>',
 'de': '<p>Die Kontoseite speichert deine Anmeldesitzung im lokalen Speicher deines Browsers, damit du angemeldet bleibst. Das ist für die Funktion der Seite erforderlich und wird entfernt, wenn du dich abmeldest. kaptapp.com setzt keine Werbe- oder Analyse-Cookies.</p>',
 'fr': "<p>La page du compte conserve votre session de connexion dans le stockage local de votre navigateur pour que vous restiez connecté. Ce stockage est nécessaire au fonctionnement de la page et est supprimé lorsque vous vous déconnectez. kaptapp.com ne dépose aucun cookie publicitaire ou d'analyse.</p>",
 'pt-br': '<p>A página da conta guarda sua sessão no armazenamento local do navegador para que você continue conectado. Isso é necessário para que a página funcione e é removido quando você sai da conta. O kaptapp.com não define cookies de publicidade nem de analytics.</p>',
 'it': "<p>La pagina dell'account conserva la tua sessione nella memoria locale del browser, così l'accesso resta attivo. È necessaria per il funzionamento della pagina e viene rimossa quando esci. kaptapp.com non imposta cookie pubblicitari o di analisi.</p>"},

'<p>Email us from the address on your account and we will delete your account, sign-in sessions and device records. We keep the trial record and payment records described above. Deleting your account does not delete anything on your computer.</p>': {
 'es': '<p>Escríbenos desde la dirección de correo electrónico de tu cuenta y eliminaremos tu cuenta, tus sesiones de acceso y tus registros de dispositivos. Conservamos el registro de la prueba y los registros de pago descritos más arriba. Eliminar tu cuenta no borra nada de tu ordenador.</p>',
 'zh': '<p>请使用你账户中的电子邮件地址给我们发送邮件，我们将删除你的账户、登录会话和设备记录。我们会保留上文所述的试用记录和付款记录。删除账户不会删除你电脑上的任何内容。</p>',
 'ko': '<p>계정에 등록된 이메일 주소로 당사에 메일을 보내 주시면 계정, 로그인 세션, 기기 기록을 삭제해 드립니다. 위에서 설명한 체험 기록과 결제 기록은 보관됩니다. 계정을 삭제해도 컴퓨터에 있는 것은 아무것도 삭제되지 않습니다.</p>',
 'ja': '<p>アカウントに登録しているメールアドレスからご連絡いただければ、アカウント、サインインセッション、端末の記録を削除します。上記のトライアルの記録と支払いの記録は保持します。アカウントを削除しても、お客様のパソコン上のものは何も削除されません。</p>',
 'de': '<p>Schreib uns eine E-Mail von der Adresse deines Kontos, dann löschen wir dein Konto, deine Anmeldesitzungen und deine Geräteeinträge. Den Eintrag zur Testphase und die oben beschriebenen Zahlungsunterlagen bewahren wir auf. Das Löschen deines Kontos löscht nichts auf deinem Computer.</p>',
 'fr': "<p>Écrivez-nous depuis l'adresse associée à votre compte et nous supprimerons votre compte, vos sessions de connexion et vos enregistrements d'appareils. Nous conservons l'enregistrement de l'essai et les registres de paiement décrits ci-dessus. La suppression de votre compte ne supprime rien sur votre ordinateur.</p>",
 'pt-br': '<p>Envie um e-mail a partir do endereço da sua conta e excluiremos sua conta, suas sessões de login e seus registros de dispositivos. Mantemos o registro do teste e os registros de pagamento descritos acima. Excluir sua conta não apaga nada do seu computador.</p>',
 'it': "<p>Scrivici dall'indirizzo email associato al tuo account ed elimineremo il tuo account, le sessioni di accesso e i registri dei dispositivi. Conserviamo il registro della prova e i registri dei pagamenti descritti sopra. Eliminare l'account non elimina nulla sul tuo computer.</p>"},

'<p>You can ask us for a copy of your personal data, and ask us to correct or delete it, to restrict how we use it, or to give you the data you provided in a portable format. You can object to uses based on our legitimate interests. We reply within one month.</p>': {
 'es': '<p>Puedes pedirnos una copia de tus datos personales y solicitar que los rectifiquemos o eliminemos, que limitemos cómo los usamos o que te entreguemos en un formato portátil los datos que nos facilitaste. Puedes oponerte a los usos basados en nuestros intereses legítimos. Respondemos en el plazo de un mes.</p>',
 'zh': '<p>你可以要求我们提供你的个人数据副本，也可以要求我们更正或删除这些数据、限制我们对其的使用，或以可移植的格式向你提供你所提供的数据。你可以反对我们基于正当利益对数据的使用。我们会在一个月内答复。</p>',
 'ko': '<p>사용자는 당사에 개인정보 사본을 요청할 수 있으며, 개인정보의 정정 또는 삭제, 이용 제한, 또는 사용자가 제공한 데이터를 이동 가능한 형식으로 제공해 줄 것을 요청할 수 있습니다. 당사의 정당한 이익에 근거한 이용에 대해서는 이의를 제기할 수 있습니다. 당사는 1개월 이내에 답변합니다.</p>',
 'ja': '<p>お客様は、ご自身の個人データの写しを請求できるほか、その訂正や削除、利用の制限、またはお客様が提供したデータを持ち運び可能な形式で受け取ることを求めることができます。当社の正当な利益に基づく利用に異議を申し立てることもできます。当社は 1 か月以内に回答します。</p>',
 'de': '<p>Du kannst eine Kopie deiner personenbezogenen Daten anfordern und uns bitten, sie zu berichtigen oder zu löschen, ihre Verwendung einzuschränken oder dir die von dir bereitgestellten Daten in einem übertragbaren Format zu geben. Du kannst Verwendungen widersprechen, die auf unseren berechtigten Interessen beruhen. Wir antworten innerhalb eines Monats.</p>',
 'fr': "<p>Vous pouvez nous demander une copie de vos données personnelles, et nous demander de les corriger ou de les supprimer, d'en limiter l'utilisation ou de vous remettre les données que vous avez fournies dans un format portable. Vous pouvez vous opposer aux utilisations fondées sur nos intérêts légitimes. Nous répondons dans un délai d'un mois.</p>",
 'pt-br': '<p>Você pode nos pedir uma cópia dos seus dados pessoais e pedir que os corrijamos ou excluamos, que restrinjamos a forma como os usamos ou que entreguemos a você, em formato portável, os dados que você forneceu. Você pode se opor a usos baseados em nossos legítimos interesses. Respondemos em até um mês.</p>',
 'it': "<p>Puoi chiederci una copia dei tuoi dati personali e chiederci di rettificarli o cancellarli, di limitarne l'uso o di fornirti in un formato portabile i dati che ci hai fornito. Puoi opporti agli usi basati sui nostri legittimi interessi. Rispondiamo entro un mese.</p>"},

'<p>If you are unhappy with how we handle your data, please tell us first. You can also complain to the UK Information Commissioner&rsquo;s Office (ico.org.uk) or, if you live in the European Union, to your national data protection authority.</p>': {
 'es': '<p>Si no estás conforme con cómo tratamos tus datos, te pedimos que nos lo digas primero. También puedes presentar una reclamación ante la autoridad de protección de datos del Reino Unido, la Information Commissioner&rsquo;s Office (ico.org.uk), o, si vives en la Unión Europea, ante tu autoridad nacional de protección de datos.</p>',
 'zh': '<p>如果你对我们处理你数据的方式不满意，请先告诉我们。你也可以向英国信息专员办公室（Information Commissioner&rsquo;s Office，ico.org.uk）投诉；如果你居住在欧盟，也可以向你所在国家的数据保护机构投诉。</p>',
 'ko': '<p>당사의 데이터 처리 방식에 만족하지 않으시면 먼저 당사에 알려 주세요. 영국 정보위원회(Information Commissioner&rsquo;s Office, ico.org.uk)에 민원을 제기할 수도 있으며, 유럽연합에 거주하는 경우에는 거주 국가의 데이터 보호 기관에 민원을 제기할 수 있습니다.</p>',
 'ja': '<p>当社のデータの取り扱いにご不満がある場合は、まず当社にお知らせください。英国の情報コミッショナー事務局（Information Commissioner&rsquo;s Office、ico.org.uk）、または欧州連合にお住まいの場合はお住まいの国のデータ保護機関に苦情を申し立てることもできます。</p>',
 'de': '<p>Wenn du mit unserem Umgang mit deinen Daten unzufrieden bist, wende dich bitte zuerst an uns. Du kannst dich auch bei der britischen Datenschutzbehörde, dem Information Commissioner&rsquo;s Office (ico.org.uk), beschweren oder, wenn du in der Europäischen Union lebst, bei deiner nationalen Datenschutzbehörde.</p>',
 'fr': "<p>Si vous n'êtes pas satisfait de la manière dont nous traitons vos données, merci de nous le signaler d'abord. Vous pouvez aussi déposer une plainte auprès de l'autorité britannique de protection des données, l'Information Commissioner&rsquo;s Office (ico.org.uk), ou, si vous résidez dans l'Union européenne, auprès de votre autorité nationale de protection des données.</p>",
 'pt-br': '<p>Se você não estiver satisfeito com a forma como tratamos seus dados, fale conosco primeiro. Você também pode apresentar uma reclamação à autoridade de proteção de dados do Reino Unido, o Information Commissioner&rsquo;s Office (ico.org.uk), ou, se morar na União Europeia, à autoridade nacional de proteção de dados do seu país.</p>',
 'it': "<p>Se qualcosa non ti convince nel modo in cui trattiamo i tuoi dati, dillo prima a noi. Puoi anche presentare un reclamo all'Information Commissioner&rsquo;s Office del Regno Unito (ico.org.uk) o, se vivi nell'Unione europea, all'autorità nazionale per la protezione dei dati del tuo paese.</p>"},

'<p>Kapture accounts are not intended for anyone under 16, or older where local law requires it, and we do not knowingly create accounts for them.</p>': {
 'es': '<p>Las cuentas de Kapture no están destinadas a menores de 16 años, o de una edad superior cuando la legislación local lo exija, y no creamos a sabiendas cuentas para ellos.</p>',
 'zh': '<p>Kapture 账户不面向 16 岁以下的人士（如当地法律规定了更高年龄，则以该年龄为准），我们也不会在知情的情况下为他们创建账户。</p>',
 'ko': '<p>Kapture 계정은 16세 미만(현지 법률이 더 높은 연령을 요구하는 경우 해당 연령 미만)인 사람을 대상으로 하지 않으며, 당사는 이들의 계정을 알면서 생성하지 않습니다.</p>',
 'ja': '<p>Kapture アカウントは 16 歳未満の方（現地の法律でそれより高い年齢が定められている場合は、その年齢未満の方）を対象としておらず、当社がそうした方のアカウントを故意に作成することはありません。</p>',
 'de': '<p>Kapture-Konten sind nicht für Personen unter 16 Jahren gedacht, oder unter einem höheren Alter, wenn das örtliche Recht dies vorschreibt. Wir legen wissentlich keine Konten für sie an.</p>',
 'fr': "<p>Les comptes Kapture ne sont pas destinés aux personnes de moins de 16 ans, ou d'un âge supérieur lorsque la loi locale l'exige, et nous ne créons pas sciemment de comptes pour elles.</p>",
 'pt-br': '<p>As contas Kapture não se destinam a menores de 16 anos, ou de idade superior quando a lei local exigir, e não criamos conscientemente contas para eles.</p>',
 'it': "<p>Gli account Kapture non sono destinati a chi ha meno di 16 anni, o un'età superiore se la legge locale lo richiede, e non creiamo consapevolmente account per queste persone.</p>"},

'<p>If a change materially affects how we use account holders&rsquo; data, we tell them by email before it takes effect.</p>': {
 'es': '<p>Si un cambio afecta de forma sustancial al uso que hacemos de los datos de los titulares de cuentas, se lo comunicamos por correo electrónico antes de que entre en vigor.</p>',
 'zh': '<p>如果某项变更会对我们使用账户持有人数据的方式产生重大影响，我们会在变更生效前通过电子邮件通知他们。</p>',
 'ko': '<p>변경 사항이 계정 보유자의 데이터 이용 방식에 중대한 영향을 미치는 경우, 당사는 변경 사항이 시행되기 전에 이메일로 알립니다.</p>',
 'ja': '<p>変更がアカウント保有者のデータの利用方法に重大な影響を与える場合は、その変更の発効前にメールでお知らせします。</p>',
 'de': '<p>Wirkt sich eine Änderung wesentlich darauf aus, wie wir die Daten von Kontoinhabern verwenden, informieren wir sie per E-Mail, bevor die Änderung in Kraft tritt.</p>',
 'fr': '<p>Si une modification affecte de manière importante la façon dont nous utilisons les données des titulaires de compte, nous les en informons par e-mail avant son entrée en vigueur.</p>',
 'pt-br': '<p>Se uma alteração afetar de forma relevante o uso que fazemos dos dados dos titulares de contas, avisamos essas pessoas por e-mail antes de ela entrar em vigor.</p>',
 'it': '<p>Se una modifica incide in modo sostanziale sul modo in cui usiamo i dati dei titolari di account, li avvisiamo via email prima che entri in vigore.</p>'},
}
