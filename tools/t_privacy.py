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
'<p>For privacy or support questions, email <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a>.</p>': {
 'es': '<p>Para consultas sobre privacidad o soporte, escribe a <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a>.</p>',
 'zh': '<p>如有隐私或支持方面的问题，请发送邮件至 <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a>。</p>',
 'ko': '<p>개인정보 또는 지원 관련 문의는 <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a> 으로 메일을 보내주세요.</p>',
 'ja': '<p>プライバシーやサポートに関するお問い合わせは <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a> までメールでご連絡ください。</p>',
 'de': '<p>Bei Fragen zu Datenschutz oder Support schreib an <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a>.</p>',
 'fr': '<p>Pour toute question de confidentialité ou de support, écrivez à <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a>.</p>',
 'pt-br': '<p>Para dúvidas de privacidade ou suporte, escreva para <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a>.</p>',
 'it': '<p>Per domande su privacy o assistenza, scrivi a <a href="mailto:pequelord@gmail.com">pequelord@gmail.com</a>.</p>'},


# footer nav on the privacy page
'<a href="/#capture">Capture</a>\n      <a href="/#how">How it works</a>\n      <a href="/privacy/">Privacy</a>\n      <a href="mailto:pequelord@gmail.com">Contact</a>': {
 'es': '<a href="/#capture">Captura</a>\n      <a href="/#how">Cómo funciona</a>\n      <a href="/privacy/">Privacidad</a>\n      <a href="mailto:pequelord@gmail.com">Contacto</a>',
 'zh': '<a href="/#capture">截图</a>\n      <a href="/#how">使用方法</a>\n      <a href="/privacy/">隐私</a>\n      <a href="mailto:pequelord@gmail.com">联系我们</a>',
 'ko': '<a href="/#capture">캡처</a>\n      <a href="/#how">사용 방법</a>\n      <a href="/privacy/">개인정보</a>\n      <a href="mailto:pequelord@gmail.com">문의</a>',
 'ja': '<a href="/#capture">キャプチャ</a>\n      <a href="/#how">使い方</a>\n      <a href="/privacy/">プライバシー</a>\n      <a href="mailto:pequelord@gmail.com">お問い合わせ</a>'},
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
}
