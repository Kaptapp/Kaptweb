# -*- coding: utf-8 -*-
"""Terms of Service. Header, footer and shared labels come from the chrome table;
the page's own entries below win over anything with the same key."""
from t_chrome import CHROME

TERMS = {
**CHROME,

'<title>Terms of Service | Kapture</title>': {
 'es': '<title>Términos del servicio | Kapture</title>',
 'zh': '<title>服务条款 | Kapture</title>',
 'ko': '<title>이용약관 | Kapture</title>',
 'ja': '<title>利用規約 | Kapture</title>',
 'de': '<title>Allgemeine Geschäftsbedingungen | Kapture</title>',
 'fr': "<title>Conditions d'utilisation | Kapture</title>",
 'pt-br': '<title>Termos de Serviço | Kapture</title>',
 'it': '<title>Termini di servizio | Kapture</title>'},

'The terms for using kaptapp.com, Kapture for Chrome and a Kapture account, from KUMO STUDIO LIMITED.': {
 'es': 'Los términos para usar kaptapp.com, Kapture para Chrome y una cuenta de Kapture, de KUMO STUDIO LIMITED.',
 'zh': 'KUMO STUDIO LIMITED 关于使用 kaptapp.com、Chrome 版 Kapture 和 Kapture 账户的条款。',
 'ko': 'KUMO STUDIO LIMITED가 정한 kaptapp.com, Chrome용 Kapture, Kapture 계정의 이용약관입니다.',
 'ja': 'KUMO STUDIO LIMITED が定める、kaptapp.com、Chrome 版 Kapture、Kapture アカウントの利用規約です。',
 'de': 'Die Bedingungen der KUMO STUDIO LIMITED für die Nutzung von kaptapp.com, Kapture für Chrome und eines Kapture-Kontos.',
 'fr': "Les conditions d'utilisation de kaptapp.com, de Kapture pour Chrome et d'un compte Kapture, établies par KUMO STUDIO LIMITED.",
 'pt-br': 'Os termos para usar o kaptapp.com, o Kapture para Chrome e uma conta Kapture, da KUMO STUDIO LIMITED.',
 'it': "I termini per l'uso di kaptapp.com, di Kapture per Chrome e di un account Kapture, stabiliti da KUMO STUDIO LIMITED."},

'"name": "Terms of Service"': {
 'es': '"name": "Términos del servicio"',
 'zh': '"name": "服务条款"',
 'ko': '"name": "이용약관"',
 'ja': '"name": "利用規約"',
 'de': '"name": "Allgemeine Geschäftsbedingungen"',
 'fr': '"name": "Conditions d\'utilisation"',
 'pt-br': '"name": "Termos de Serviço"',
 'it': '"name": "Termini di servizio"'},

'content="Terms of Service | Kapture"': {
 'es': 'content="Términos del servicio | Kapture"',
 'zh': 'content="服务条款 | Kapture"',
 'ko': 'content="이용약관 | Kapture"',
 'ja': 'content="利用規約 | Kapture"',
 'de': 'content="Allgemeine Geschäftsbedingungen | Kapture"',
 'fr': 'content="Conditions d\'utilisation | Kapture"',
 'pt-br': 'content="Termos de Serviço | Kapture"',
 'it': 'content="Termini di servizio | Kapture"'},

'<h1>Kapture Terms of Service</h1>': {
 'es': '<h1>Términos del servicio de Kapture</h1>',
 'zh': '<h1>Kapture 服务条款</h1>',
 'ko': '<h1>Kapture 이용약관</h1>',
 'ja': '<h1>Kapture 利用規約</h1>',
 'de': '<h1>Allgemeine Geschäftsbedingungen von Kapture</h1>',
 'fr': "<h1>Conditions d'utilisation de Kapture</h1>",
 'pt-br': '<h1>Termos de Serviço do Kapture</h1>',
 'it': '<h1>Termini di servizio di Kapture</h1>'},

'<h2>About these terms</h2>': {
 'es': '<h2>Sobre estos términos</h2>',
 'zh': '<h2>关于本条款</h2>',
 'ko': '<h2>본 약관에 대하여</h2>',
 'ja': '<h2>本規約について</h2>',
 'de': '<h2>Über diese Bedingungen</h2>',
 'fr': '<h2>À propos de ces conditions</h2>',
 'pt-br': '<h2>Sobre estes termos</h2>',
 'it': '<h2>Informazioni su questi termini</h2>'},

'<h2>Kapture for Chrome</h2>': {
 'es': '<h2>Kapture para Chrome</h2>',
 'zh': '<h2>Chrome 版 Kapture</h2>',
 'ko': '<h2>Chrome용 Kapture</h2>',
 'ja': '<h2>Chrome 版 Kapture</h2>',
 'de': '<h2>Kapture für Chrome</h2>',
 'fr': '<h2>Kapture pour Chrome</h2>',
 'pt-br': '<h2>Kapture para Chrome</h2>',
 'it': '<h2>Kapture per Chrome</h2>'},

'<h2>Your Kapture account</h2>': {
 'es': '<h2>Tu cuenta de Kapture</h2>',
 'zh': '<h2>你的 Kapture 账户</h2>',
 'ko': '<h2>Kapture 계정</h2>',
 'ja': '<h2>Kapture アカウント</h2>',
 'de': '<h2>Dein Kapture-Konto</h2>',
 'fr': '<h2>Votre compte Kapture</h2>',
 'pt-br': '<h2>Sua conta Kapture</h2>',
 'it': '<h2>Il tuo account Kapture</h2>'},

'<h2>Kapture Pro</h2>': {
 'es': '<h2>Kapture Pro</h2>',
 'zh': '<h2>Kapture Pro</h2>',
 'ko': '<h2>Kapture Pro</h2>',
 'ja': '<h2>Kapture Pro</h2>',
 'de': '<h2>Kapture Pro</h2>',
 'fr': '<h2>Kapture Pro</h2>',
 'pt-br': '<h2>Kapture Pro</h2>',
 'it': '<h2>Kapture Pro</h2>'},

'<h2>Using Kapture fairly</h2>': {
 'es': '<h2>Uso adecuado de Kapture</h2>',
 'zh': '<h2>合理使用 Kapture</h2>',
 'ko': '<h2>Kapture의 올바른 이용</h2>',
 'ja': '<h2>Kapture の適正な利用</h2>',
 'de': '<h2>Faire Nutzung von Kapture</h2>',
 'fr': '<h2>Utiliser Kapture de manière loyale</h2>',
 'pt-br': '<h2>Uso adequado do Kapture</h2>',
 'it': '<h2>Usare Kapture in modo corretto</h2>'},

'<h2>Our responsibility to you</h2>': {
 'es': '<h2>Nuestra responsabilidad contigo</h2>',
 'zh': '<h2>我们对你的责任</h2>',
 'ko': '<h2>당사의 책임</h2>',
 'ja': '<h2>当社の責任</h2>',
 'de': '<h2>Unsere Verantwortung dir gegenüber</h2>',
 'fr': '<h2>Notre responsabilité envers vous</h2>',
 'pt-br': '<h2>Nossa responsabilidade com você</h2>',
 'it': '<h2>La nostra responsabilità nei tuoi confronti</h2>'},

'<h2>Complaints</h2>': {
 'es': '<h2>Reclamaciones</h2>',
 'zh': '<h2>投诉</h2>',
 'ko': '<h2>불만 처리</h2>',
 'ja': '<h2>苦情の受付</h2>',
 'de': '<h2>Beschwerden</h2>',
 'fr': '<h2>Réclamations</h2>',
 'pt-br': '<h2>Reclamações</h2>',
 'it': '<h2>Reclami</h2>'},

'<h2>Changes to these terms</h2>': {
 'es': '<h2>Cambios en estos términos</h2>',
 'zh': '<h2>本条款的变更</h2>',
 'ko': '<h2>약관의 변경</h2>',
 'ja': '<h2>本規約の変更</h2>',
 'de': '<h2>Änderungen dieser Bedingungen</h2>',
 'fr': '<h2>Modifications de ces conditions</h2>',
 'pt-br': '<h2>Alterações nestes termos</h2>',
 'it': '<h2>Modifiche a questi termini</h2>'},

'<h2>Law and courts</h2>': {
 'es': '<h2>Legislación aplicable y tribunales</h2>',
 'zh': '<h2>适用法律与管辖法院</h2>',
 'ko': '<h2>준거법 및 관할 법원</h2>',
 'ja': '<h2>準拠法と裁判管轄</h2>',
 'de': '<h2>Anwendbares Recht und Gerichtsstand</h2>',
 'fr': '<h2>Droit applicable et juridictions</h2>',
 'pt-br': '<h2>Lei aplicável e foro</h2>',
 'it': '<h2>Legge applicabile e foro competente</h2>'},

'<p class="kicker">Legal</p>': {
 'es': '<p class="kicker">Aviso legal</p>',
 'zh': '<p class="kicker">法律条款</p>',
 'ko': '<p class="kicker">법적 고지</p>',
 'ja': '<p class="kicker">法的事項</p>',
 'de': '<p class="kicker">Rechtliches</p>',
 'fr': '<p class="kicker">Mentions légales</p>',
 'pt-br': '<p class="kicker">Jurídico</p>',
 'it': '<p class="kicker">Note legali</p>'},

'<p class="legal-date">Effective 1 November 2026</p>': {
 'es': '<p class="legal-date">En vigor desde el 1 de noviembre de 2026</p>',
 'zh': '<p class="legal-date">自 2026 年 11 月 1 日起生效</p>',
 'ko': '<p class="legal-date">2026년 11월 1일 시행</p>',
 'ja': '<p class="legal-date">2026 年 11 月 1 日発効</p>',
 'de': '<p class="legal-date">Gültig ab 1. November 2026</p>',
 'fr': '<p class="legal-date">En vigueur depuis le 1er novembre 2026</p>',
 'pt-br': '<p class="legal-date">Em vigor desde 1º de novembro de 2026</p>',
 'it': '<p class="legal-date">In vigore dal 1° novembre 2026</p>'},

'<p>These terms apply when you use kaptapp.com, Kapture for Chrome or a Kapture account. They are an agreement between you and KUMO STUDIO LIMITED, a private limited company registered in England and Wales under company number 08453597, whose registered office is at Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England (&ldquo;Kapture&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;).</p>': {
 'es': '<p>Estos términos se aplican cuando usas kaptapp.com, Kapture para Chrome o una cuenta de Kapture. Constituyen un acuerdo entre tú y KUMO STUDIO LIMITED, una sociedad de responsabilidad limitada (private limited company) registrada en Inglaterra y Gales con el número de registro 08453597 y con domicilio social en Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England («Kapture», «nosotros», «nos»).</p>',
 'zh': '<p>当你使用 kaptapp.com、Chrome 版 Kapture 或 Kapture 账户时，适用本条款。本条款是你与 KUMO STUDIO LIMITED 之间的协议。KUMO STUDIO LIMITED 是一家在英格兰和威尔士注册的私人有限公司，公司编号为 08453597，注册办公地址为 Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England（以下简称“Kapture”或“我们”）。</p>',
 'ko': '<p>본 약관은 사용자가 kaptapp.com, Chrome용 Kapture 또는 Kapture 계정을 이용할 때 적용됩니다. 본 약관은 사용자와 KUMO STUDIO LIMITED(이하 “Kapture” 또는 “당사”) 간의 계약입니다. KUMO STUDIO LIMITED는 잉글랜드 및 웨일스에 회사 번호 08453597로 등록된 비상장 유한회사(private limited company)이며, 등록 사무소는 Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England에 있습니다.</p>',
 'ja': '<p>本規約は、お客様が kaptapp.com、Chrome 版 Kapture、または Kapture アカウントを利用する際に適用されます。本規約は、お客様と KUMO STUDIO LIMITED（以下「Kapture」または「当社」）との間の合意です。KUMO STUDIO LIMITED は、イングランドおよびウェールズで登記された非公開有限会社（会社番号 08453597）で、登記上の事務所は Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England にあります。</p>',
 'de': '<p>Diese Bedingungen gelten, wenn du kaptapp.com, Kapture für Chrome oder ein Kapture-Konto nutzt. Sie sind eine Vereinbarung zwischen dir und der KUMO STUDIO LIMITED, einer in England und Wales unter der Registernummer 08453597 eingetragenen Gesellschaft mit beschränkter Haftung nach englischem Recht (Private Limited Company) mit eingetragenem Sitz in Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England („Kapture“, „wir“, „uns“).</p>',
 'fr': "<p>Ces conditions s'appliquent lorsque vous utilisez kaptapp.com, Kapture pour Chrome ou un compte Kapture. Elles constituent un accord entre vous et KUMO STUDIO LIMITED, une société à responsabilité limitée de droit anglais (private limited company) immatriculée en Angleterre et au pays de Galles sous le numéro 08453597, dont le siège social est situé Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England («&nbsp;Kapture&nbsp;», «&nbsp;nous&nbsp;»).</p>",
 'pt-br': '<p>Estes termos se aplicam quando você usa o kaptapp.com, o Kapture para Chrome ou uma conta Kapture. Eles constituem um acordo entre você e a KUMO STUDIO LIMITED, uma sociedade limitada (private limited company) registrada na Inglaterra e no País de Gales sob o número de registro 08453597, com sede social em Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England (&ldquo;Kapture&rdquo;, &ldquo;nós&rdquo;, &ldquo;nos&rdquo;).</p>',
 'it': '<p>Questi termini si applicano quando usi kaptapp.com, Kapture per Chrome o un account Kapture. Costituiscono un accordo tra te e KUMO STUDIO LIMITED, società privata a responsabilità limitata registrata in Inghilterra e Galles con numero di registrazione 08453597 e sede legale in Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England (&ldquo;Kapture&rdquo; o &ldquo;noi&rdquo;).</p>'},

'<p>You can <a href="mailto:hello@kaptapp.com">email us</a> or write to us at our registered office.</p>': {
 'es': '<p>Puedes <a href="mailto:hello@kaptapp.com">enviarnos un correo electrónico</a> o escribirnos por correo postal a nuestro domicilio social.</p>',
 'zh': '<p>你可以<a href="mailto:hello@kaptapp.com">给我们发送邮件</a>，或写信至我们的注册办公地址。</p>',
 'ko': '<p><a href="mailto:hello@kaptapp.com">이메일</a>을 보내거나 등록 사무소로 우편을 보내 당사에 연락할 수 있습니다.</p>',
 'ja': '<p>お問い合わせは<a href="mailto:hello@kaptapp.com">メール</a>、または当社の登記上の事務所宛ての郵便で受け付けています。</p>',
 'de': '<p>Du kannst uns <a href="mailto:hello@kaptapp.com">per E-Mail erreichen</a> oder uns per Post an unseren eingetragenen Sitz schreiben.</p>',
 'fr': '<p>Vous pouvez <a href="mailto:hello@kaptapp.com">nous écrire par e-mail</a> ou nous écrire par courrier à notre siège social.</p>',
 'pt-br': '<p>Você pode <a href="mailto:hello@kaptapp.com">nos enviar um e-mail</a> ou nos escrever no endereço da nossa sede social.</p>',
 'it': '<p>Puoi <a href="mailto:hello@kaptapp.com">scriverci via email</a> o per posta presso la nostra sede legale.</p>'},

'<p>If you are a consumer, nothing in these terms affects your legal rights. Where these terms and the law differ, the law applies.</p>': {
 'es': '<p>Si eres consumidor, nada de lo dispuesto en estos términos afecta a tus derechos legales. Cuando estos términos y la ley no coincidan, prevalece la ley.</p>',
 'zh': '<p>如果你是消费者，本条款的任何内容均不影响你的法定权利。如本条款与法律规定不一致，以法律为准。</p>',
 'ko': '<p>사용자가 소비자인 경우, 본 약관의 어떠한 내용도 사용자의 법적 권리에 영향을 미치지 않습니다. 본 약관과 법률이 서로 다른 경우에는 법률이 적용됩니다.</p>',
 'ja': '<p>お客様が消費者である場合、本規約のいかなる規定もお客様の法的権利に影響を与えるものではありません。本規約と法律が異なる場合は、法律が優先されます。</p>',
 'de': '<p>Wenn du Verbraucherin oder Verbraucher bist, berührt nichts in diesen Bedingungen deine gesetzlichen Rechte. Wo diese Bedingungen und das Gesetz voneinander abweichen, gilt das Gesetz.</p>',
 'fr': "<p>Si vous êtes un consommateur, rien dans ces conditions n'affecte vos droits légaux. En cas de divergence entre ces conditions et la loi, la loi s'applique.</p>",
 'pt-br': '<p>Se você for consumidor, nada nestes termos afeta seus direitos legais. Quando estes termos e a lei divergirem, prevalece a lei.</p>',
 'it': '<p>Se sei un consumatore, nulla in questi termini pregiudica i tuoi diritti previsti dalla legge. Dove questi termini e la legge non coincidono, prevale la legge.</p>'},

'<p>Kapture for Chrome is free. It is distributed through the Chrome Web Store, whose terms also apply when you install it. How it handles information is explained in our <a href="/privacy/">Privacy Policy</a>.</p>': {
 'es': '<p>Kapture para Chrome es gratis. Se distribuye a través de Chrome Web Store, cuyos términos también se aplican cuando lo instalas. Cómo trata la información se explica en nuestra <a href="/privacy/">Política de privacidad</a>.</p>',
 'zh': '<p>Chrome 版 Kapture 免费提供。它通过 Chrome 应用商店 分发，安装时也须遵守 Chrome 应用商店 的条款。它如何处理信息，请参阅我们的<a href="/privacy/">隐私政策</a>。</p>',
 'ko': '<p>Chrome용 Kapture는 무료입니다. Chrome 웹 스토어를 통해 배포되며, 설치할 때는 Chrome 웹 스토어의 약관도 함께 적용됩니다. 정보 처리 방식은 당사의 <a href="/privacy/">개인정보처리방침</a>에서 설명합니다.</p>',
 'ja': '<p>Chrome 版 Kapture は無料です。Chrome ウェブストア を通じて配布されており、インストールの際には Chrome ウェブストア の規約も適用されます。情報の取り扱いについては、当社の<a href="/privacy/">プライバシーポリシー</a>で説明しています。</p>',
 'de': '<p>Kapture für Chrome ist kostenlos. Die Erweiterung wird über den Chrome Web Store vertrieben, dessen Bedingungen bei der Installation ebenfalls gelten. Wie sie mit Informationen umgeht, erklären wir in unserer <a href="/privacy/">Datenschutzerklärung</a>.</p>',
 'fr': '<p>Kapture pour Chrome est gratuit. Il est distribué via le Chrome Web Store, dont les conditions s\'appliquent également lorsque vous l\'installez. La façon dont il traite les informations est expliquée dans notre <a href="/privacy/">Politique de confidentialité</a>.</p>',
 'pt-br': '<p>O Kapture para Chrome é grátis. Ele é distribuído pela Chrome Web Store, cujos termos também se aplicam quando você o instala. A forma como ele trata as informações está explicada na nossa <a href="/privacy/">Política de Privacidade</a>.</p>',
 'it': '<p>Kapture per Chrome è gratuito. È distribuito tramite il Chrome Web Store, i cui termini si applicano anche quando lo installi. Il modo in cui tratta le informazioni è spiegato nella nostra <a href="/privacy/">Informativa sulla privacy</a>.</p>'},

'<p>A Kapture account lets you sign in at kaptapp.com/account to see your Kapture Pro licence and the devices it is active on. You sign in with a link we email to you. There is no password, so keep access to your email account secure.</p>': {
 'es': '<p>Una cuenta de Kapture te permite iniciar sesión en kaptapp.com/account para ver tu licencia de Kapture Pro y los dispositivos en los que está activa. Inicias sesión con un enlace que te enviamos por correo electrónico. No hay contraseña, así que mantén protegido el acceso a tu cuenta de correo electrónico.</p>',
 'zh': '<p>通过 Kapture 账户，你可以在 kaptapp.com/account 登录，查看你的 Kapture Pro 许可证以及该许可证已在哪些设备上激活。你需通过我们发送到你邮箱的链接登录。账户没有密码，因此请妥善保护你的电子邮箱账户。</p>',
 'ko': '<p>Kapture 계정이 있으면 kaptapp.com/account에 로그인해 Kapture Pro 라이선스와 해당 라이선스가 활성화된 기기를 확인할 수 있습니다. 로그인은 당사가 이메일로 보내는 링크로 합니다. 비밀번호가 없으므로 이메일 계정에 대한 접근을 안전하게 관리하세요.</p>',
 'ja': '<p>Kapture アカウントでは、kaptapp.com/account にサインインして、Kapture Pro のライセンスと、そのライセンスが有効になっている端末を確認できます。サインインには、当社がメールでお送りするリンクを使います。パスワードはないため、ご自身のメールアカウントへのアクセスは安全に管理してください。</p>',
 'de': '<p>Mit einem Kapture-Konto kannst du dich unter kaptapp.com/account anmelden, um deine Lizenz für Kapture Pro und die Geräte zu sehen, auf denen sie aktiv ist. Du meldest dich über einen Link an, den wir dir per E-Mail senden. Es gibt kein Passwort, also schütze den Zugang zu deinem E-Mail-Konto.</p>',
 'fr': "<p>Un compte Kapture vous permet de vous connecter sur kaptapp.com/account pour voir votre licence Kapture Pro et les appareils sur lesquels elle est active. Vous vous connectez au moyen d'un lien que nous vous envoyons par e-mail. Il n'y a pas de mot de passe&nbsp;: veillez donc à protéger l'accès à votre compte e-mail.</p>",
 'pt-br': '<p>Uma conta Kapture permite que você entre em kaptapp.com/account para ver sua licença do Kapture Pro e os dispositivos em que ela está ativa. Você entra com um link que enviamos por e-mail. Não há senha, então mantenha seguro o acesso à sua conta de e-mail.</p>',
 'it': "<p>Un account Kapture ti permette di accedere su kaptapp.com/account per vedere la tua licenza Kapture Pro e i dispositivi su cui è attiva. Accedi con un link che ti inviamo via email. Non c'è una password, quindi proteggi l'accesso al tuo account email.</p>"},

'<p>You must be at least 16 years old to create an account, or older if the law where you live requires it.</p>': {
 'es': '<p>Debes tener al menos 16 años para crear una cuenta, o más si así lo exige la ley del lugar donde vives.</p>',
 'zh': '<p>你必须年满 16 周岁才能创建账户；如果你所在地的法律要求更高年龄，则须达到该年龄。</p>',
 'ko': '<p>계정을 만들려면 만 16세 이상이어야 하며, 거주 지역의 법률이 더 높은 연령을 요구하는 경우 그 연령 이상이어야 합니다.</p>',
 'ja': '<p>アカウントを作成するには 16 歳以上である必要があります。お住まいの地域の法律でそれより高い年齢が定められている場合は、その年齢以上である必要があります。</p>',
 'de': '<p>Du musst mindestens 16 Jahre alt sein, um ein Konto zu erstellen, oder älter, wenn das Recht an deinem Wohnort dies vorschreibt.</p>',
 'fr': "<p>Vous devez avoir au moins 16 ans pour créer un compte, ou plus si la loi de votre lieu de résidence l'exige.</p>",
 'pt-br': '<p>Você precisa ter pelo menos 16 anos para criar uma conta, ou mais, se a lei do lugar onde você mora exigir.</p>',
 'it': "<p>Per creare un account devi avere almeno 16 anni, o un'età superiore se la legge del paese in cui vivi lo richiede.</p>"},

'<p>To close your account, email us from the address on the account. Closing it does not delete anything on your computer.</p>': {
 'es': '<p>Para cerrar tu cuenta, escríbenos desde la dirección de correo electrónico de la cuenta. Cerrarla no borra nada de tu ordenador.</p>',
 'zh': '<p>如需注销账户，请使用账户中的电子邮件地址给我们发送邮件。注销账户不会删除你电脑上的任何内容。</p>',
 'ko': '<p>계정을 해지하려면 계정에 등록된 이메일 주소로 당사에 메일을 보내 주세요. 계정을 해지해도 컴퓨터에 있는 것은 아무것도 삭제되지 않습니다.</p>',
 'ja': '<p>アカウントを閉鎖するには、アカウントに登録しているメールアドレスから当社にメールでご連絡ください。アカウントを閉鎖しても、お客様のパソコン上のものは何も削除されません。</p>',
 'de': '<p>Um dein Konto zu schließen, schreib uns eine E-Mail von der Adresse des Kontos. Das Schließen löscht nichts auf deinem Computer.</p>',
 'fr': "<p>Pour fermer votre compte, écrivez-nous depuis l'adresse associée au compte. Sa fermeture ne supprime rien sur votre ordinateur.</p>",
 'pt-br': '<p>Para encerrar sua conta, envie um e-mail a partir do endereço da conta. O encerramento não apaga nada do seu computador.</p>',
 'it': "<p>Per chiudere il tuo account, scrivici dall'indirizzo email associato all'account. La chiusura non elimina nulla sul tuo computer.</p>"},

'<p>Kapture Pro is not available to buy yet. Before free trials or paid plans become available, we will publish their terms on this page, including prices, renewal, cancellation and refunds. Those terms will apply only to trials and purchases made after they are published.</p>': {
 'es': '<p>Kapture Pro aún no está a la venta. Antes de que haya pruebas gratuitas o planes de pago disponibles, publicaremos sus términos en esta página, incluidos los precios, la renovación, la cancelación y los reembolsos. Esos términos solo se aplicarán a las pruebas y compras realizadas después de su publicación.</p>',
 'zh': '<p>Kapture Pro 目前尚未开放购买。在免费试用或付费方案推出之前，我们会在本页面公布相关条款，包括价格、续订、取消和退款。这些条款仅适用于其公布之后开始的试用和进行的购买。</p>',
 'ko': '<p>Kapture Pro는 아직 구매할 수 없습니다. 무료 체험 또는 유료 요금제를 제공하기 전에 가격, 갱신, 해지, 환불을 포함한 관련 약관을 이 페이지에 게시합니다. 해당 약관은 게시된 이후에 시작한 체험과 구매에만 적용됩니다.</p>',
 'ja': '<p>Kapture Pro はまだ購入できません。無料トライアルまたは有料プランの提供を開始する前に、価格、更新、解約、返金を含むそれらの条件をこのページに掲載します。それらの条件は、掲載後に開始されたトライアルおよび行われた購入にのみ適用されます。</p>',
 'de': '<p>Kapture Pro kann noch nicht gekauft werden. Bevor kostenlose Testphasen oder kostenpflichtige Tarife verfügbar werden, veröffentlichen wir ihre Bedingungen auf dieser Seite, einschließlich Preisen, Verlängerung, Kündigung und Erstattungen. Diese Bedingungen gelten nur für Testphasen und Käufe, die nach ihrer Veröffentlichung erfolgen.</p>',
 'fr': "<p>Kapture Pro n'est pas encore disponible à l'achat. Avant que des essais gratuits ou des formules payantes ne deviennent disponibles, nous publierons leurs conditions sur cette page, notamment les prix, le renouvellement, la résiliation et les remboursements. Ces conditions s'appliqueront uniquement aux essais et aux achats effectués après leur publication.</p>",
 'pt-br': '<p>O Kapture Pro ainda não está à venda. Antes que testes gratuitos ou planos pagos fiquem disponíveis, publicaremos os termos deles nesta página, incluindo preços, renovação, cancelamento e reembolsos. Esses termos se aplicarão somente a testes e compras feitos depois da publicação.</p>',
 'it': '<p>Kapture Pro non è ancora acquistabile. Prima che siano disponibili prove gratuite o piani a pagamento, pubblicheremo su questa pagina i relativi termini, compresi prezzi, rinnovo, annullamento e rimborsi. Tali termini si applicheranno solo alle prove e agli acquisti effettuati dopo la loro pubblicazione.</p>'},

'<p>Please do not misuse our websites or services, interfere with them or with other people&rsquo;s use of them, or try to get around any limits or security measures. If you do this seriously or repeatedly, we may suspend or close your account. Unless the law, security or the nature of the misuse prevents it, we will tell you first.</p>': {
 'es': '<p>Te pedimos que no hagas un uso indebido de nuestros sitios web o servicios, que no interfieras con ellos ni con su uso por parte de otras personas y que no intentes eludir ningún límite ni medida de seguridad. Si lo haces de forma grave o reiterada, podemos suspender o cerrar tu cuenta. Salvo que la ley, la seguridad o la naturaleza del uso indebido lo impidan, te avisaremos antes.</p>',
 'zh': '<p>请勿滥用我们的网站或服务，请勿干扰它们或干扰他人对它们的使用，也请勿试图规避任何限制或安全措施。如果你的此类行为情节严重或屡次发生，我们可能会暂停或关闭你的账户。除非法律、安全原因或滥用行为的性质不允许，我们会事先通知你。</p>',
 'ko': '<p>당사의 웹사이트나 서비스를 오용하거나, 서비스 또는 다른 사람의 서비스 이용을 방해하거나, 제한 또는 보안 조치를 우회하려고 하지 마세요. 이러한 행위가 심각하거나 반복되는 경우 당사는 계정을 정지하거나 해지할 수 있습니다. 법률, 보안 또는 오용의 성격상 불가능한 경우가 아니라면 사전에 알려 드립니다.</p>',
 'ja': '<p>当社のウェブサイトやサービスを不正に利用したり、その運営や他の人による利用を妨げたり、制限やセキュリティ対策を回避しようとしたりしないでください。そうした行為が重大な場合または繰り返し行われた場合、当社はお客様のアカウントを停止または閉鎖することがあります。法律、セキュリティ、または不正利用の性質上できない場合を除き、事前にお知らせします。</p>',
 'de': '<p>Bitte missbrauche unsere Websites oder Dienste nicht, störe weder sie noch ihre Nutzung durch andere und versuche nicht, Beschränkungen oder Sicherheitsmaßnahmen zu umgehen. Tust du dies schwerwiegend oder wiederholt, können wir dein Konto sperren oder schließen. Sofern Gesetz, Sicherheit oder die Art des Missbrauchs dem nicht entgegenstehen, informieren wir dich vorher.</p>',
 'fr': "<p>Merci de ne pas utiliser abusivement nos sites ou nos services, de ne perturber ni leur fonctionnement ni leur utilisation par d'autres personnes, et de ne pas tenter de contourner les limites ou les mesures de sécurité. Si vous le faites de manière grave ou répétée, nous pouvons suspendre ou fermer votre compte. Sauf si la loi, la sécurité ou la nature de l'abus l'empêche, nous vous en informerons au préalable.</p>",
 'pt-br': '<p>Pedimos que você não use indevidamente nossos sites ou serviços, não interfira neles nem no uso que outras pessoas fazem deles e não tente contornar limites ou medidas de segurança. Se você fizer isso de forma grave ou repetida, podemos suspender ou encerrar sua conta. A menos que a lei, a segurança ou a natureza do uso indevido impeçam, avisaremos você antes.</p>',
 'it': "<p>Ti chiediamo di non fare un uso improprio dei nostri siti web o servizi, di non interferire con essi o con l'uso che ne fanno altre persone e di non cercare di aggirare limiti o misure di sicurezza. Se lo fai in modo grave o ripetuto, potremo sospendere o chiudere il tuo account. Salvo che la legge, la sicurezza o la natura dell'uso improprio lo impediscano, ti avviseremo prima.</p>"},

'<p>We are responsible for loss you suffer that is a foreseeable result of our breaking these terms or failing to use reasonable care and skill. We are not responsible for loss that was not foreseeable.</p>': {
 'es': '<p>Somos responsables de las pérdidas que sufras que sean una consecuencia previsible de que incumplamos estos términos o de que no actuemos con una diligencia y una pericia razonables. No somos responsables de las pérdidas que no fueran previsibles.</p>',
 'zh': '<p>对于因我们违反本条款或未尽合理的谨慎和技能而给你造成的可预见损失，我们承担责任。对于不可预见的损失，我们不承担责任。</p>',
 'ko': '<p>당사는 당사가 본 약관을 위반하거나 합리적인 주의와 기술을 다하지 않은 결과로 사용자가 입은 손해 중 예견 가능한 손해에 대해 책임을 집니다. 예견할 수 없었던 손해에 대해서는 책임을 지지 않습니다.</p>',
 'ja': '<p>当社は、当社が本規約に違反したこと、または合理的な注意と技能をもって行動しなかったことの予見可能な結果としてお客様が被った損失について責任を負います。予見できなかった損失については責任を負いません。</p>',
 'de': '<p>Wir haften für Schäden, die du erleidest und die eine vorhersehbare Folge davon sind, dass wir gegen diese Bedingungen verstoßen oder nicht mit angemessener Sorgfalt und Sachkenntnis handeln. Für Schäden, die nicht vorhersehbar waren, haften wir nicht.</p>',
 'fr': "<p>Nous sommes responsables des pertes que vous subissez lorsqu'elles sont une conséquence prévisible d'un manquement de notre part à ces conditions ou d'un défaut de soin et de compétence raisonnables. Nous ne sommes pas responsables des pertes qui n'étaient pas prévisibles.</p>",
 'pt-br': '<p>Somos responsáveis pelas perdas que você sofrer que sejam consequência previsível do descumprimento destes termos por nossa parte ou de não termos agido com cuidado e competência razoáveis. Não somos responsáveis por perdas que não eram previsíveis.</p>',
 'it': '<p>Siamo responsabili delle perdite che subisci e che sono una conseguenza prevedibile della nostra violazione di questi termini o del nostro mancato impiego di ragionevole cura e competenza. Non siamo responsabili delle perdite non prevedibili.</p>'},

'<p>Nothing in these terms excludes or limits our responsibility where the law does not allow it, including for death or personal injury caused by our negligence, for fraud, or for your legal rights as a consumer.</p>': {
 'es': '<p>Nada de lo dispuesto en estos términos excluye ni limita nuestra responsabilidad cuando la ley no lo permite, incluida la responsabilidad por muerte o lesiones personales causadas por nuestra negligencia, por fraude o en relación con tus derechos legales como consumidor.</p>',
 'zh': '<p>在法律不允许排除或限制责任的情况下，本条款的任何内容均不排除或限制我们的责任，包括因我们的过失导致的死亡或人身伤害、欺诈，以及你作为消费者的法定权利。</p>',
 'ko': '<p>본 약관의 어떠한 내용도 법률상 허용되지 않는 범위에서 당사의 책임을 배제하거나 제한하지 않습니다. 여기에는 당사의 과실로 인한 사망 또는 신체 상해, 사기, 소비자로서 사용자가 갖는 법적 권리에 대한 책임이 포함됩니다.</p>',
 'ja': '<p>本規約のいかなる規定も、法律上認められない範囲で当社の責任を除外または制限するものではありません。これには、当社の過失による死亡または身体の傷害、詐欺、および消費者としてのお客様の法的権利に関する責任が含まれます。</p>',
 'de': '<p>Nichts in diesen Bedingungen schließt unsere Haftung aus oder beschränkt sie, wo das Gesetz dies nicht erlaubt, insbesondere für Tod oder Körperverletzung infolge unserer Fahrlässigkeit, für Betrug oder hinsichtlich deiner gesetzlichen Rechte als Verbraucherin oder Verbraucher.</p>',
 'fr': "<p>Rien dans ces conditions n'exclut ni ne limite notre responsabilité lorsque la loi ne le permet pas, notamment en cas de décès ou de dommage corporel causé par notre négligence, en cas de fraude, ou au regard de vos droits légaux en tant que consommateur.</p>",
 'pt-br': '<p>Nada nestes termos exclui ou limita nossa responsabilidade quando a lei não permite, inclusive por morte ou lesão corporal causada por nossa negligência, por fraude ou em relação aos seus direitos legais como consumidor.</p>',
 'it': '<p>Nulla in questi termini esclude o limita la nostra responsabilità nei casi in cui la legge non lo consente, anche per morte o lesioni personali causate da nostra negligenza, per frode o per i tuoi diritti di consumatore previsti dalla legge.</p>'},

'<p>If you use Kapture for a business, we are not liable to you for loss of profit, business or business opportunity.</p>': {
 'es': '<p>Si usas Kapture con fines empresariales, no somos responsables ante ti por la pérdida de beneficios, de negocio o de oportunidades de negocio.</p>',
 'zh': '<p>如果你将 Kapture 用于商业用途，我们不对你的利润损失、业务损失或商业机会损失承担责任。</p>',
 'ko': '<p>사업 목적으로 Kapture를 사용하는 경우, 당사는 이익, 사업 또는 사업 기회의 손실에 대해 책임을 지지 않습니다.</p>',
 'ja': '<p>お客様が事業のために Kapture を利用する場合、当社は逸失利益、事業の損失、または事業機会の損失について責任を負いません。</p>',
 'de': '<p>Wenn du Kapture geschäftlich nutzt, haften wir dir gegenüber nicht für entgangenen Gewinn, entgangene Geschäfte oder entgangene Geschäftschancen.</p>',
 'fr': "<p>Si vous utilisez Kapture à des fins professionnelles, nous ne sommes pas responsables envers vous des pertes de bénéfices, d'activité ou d'opportunités commerciales.</p>",
 'pt-br': '<p>Se você usa o Kapture para fins comerciais, não somos responsáveis perante você por lucros cessantes nem pela perda de negócios ou de oportunidades de negócio.</p>',
 'it': "<p>Se usi Kapture per un'attività professionale, non siamo responsabili nei tuoi confronti per perdita di profitti, di affari o di opportunità commerciali.</p>"},

'<p>Kapture saves files to your own computer. Keep backups of files that matter to you.</p>': {
 'es': '<p>Kapture guarda los archivos en tu propio ordenador. Haz copias de seguridad de los archivos que te importen.</p>',
 'zh': '<p>Kapture 会将文件保存到你自己的电脑上。请为重要文件做好备份。</p>',
 'ko': '<p>Kapture는 파일을 사용자의 컴퓨터에 저장합니다. 중요한 파일은 백업해 두세요.</p>',
 'ja': '<p>Kapture はファイルをお客様自身のパソコンに保存します。大切なファイルはバックアップを取っておいてください。</p>',
 'de': '<p>Kapture speichert Dateien auf deinem eigenen Computer. Erstelle Sicherungskopien der Dateien, die dir wichtig sind.</p>',
 'fr': '<p>Kapture enregistre les fichiers sur votre propre ordinateur. Conservez des sauvegardes des fichiers qui comptent pour vous.</p>',
 'pt-br': '<p>O Kapture salva os arquivos no seu próprio computador. Faça backup dos arquivos que são importantes para você.</p>',
 'it': '<p>Kapture salva i file sul tuo computer. Conserva copie di backup dei file importanti per te.</p>'},

'<p>If you are not happy with something, <a href="mailto:hello@kaptapp.com">email us</a>. We acknowledge complaints within 5 working days and aim to resolve them within 30 days. We do not currently use an alternative dispute resolution scheme. Citizens Advice (UK) or your local consumer organisation can tell you about your options.</p>': {
 'es': '<p>Si no estás satisfecho con algo, <a href="mailto:hello@kaptapp.com">escríbenos</a>. Acusamos recibo de las reclamaciones en un plazo de 5 días hábiles y procuramos resolverlas en un plazo de 30 días. Actualmente no recurrimos a ningún sistema de resolución alternativa de litigios. Citizens Advice (UK) o la organización de consumidores de tu zona pueden informarte sobre tus opciones.</p>',
 'zh': '<p>如有任何不满意之处，请<a href="mailto:hello@kaptapp.com">给我们发送邮件</a>。我们会在 5 个工作日内确认收到投诉，并力求在 30 天内解决。我们目前不使用替代性争议解决机制。Citizens Advice (UK) 或你当地的消费者组织可以告诉你有哪些选择。</p>',
 'ko': '<p>불만 사항이 있으면 <a href="mailto:hello@kaptapp.com">이메일</a>로 알려 주세요. 당사는 영업일 기준 5일 이내에 불만 접수를 확인하고 30일 이내 해결을 목표로 합니다. 현재 당사는 대체적 분쟁 해결 제도를 이용하지 않습니다. Citizens Advice (UK) 또는 거주 지역의 소비자 단체에서 선택할 수 있는 방법을 안내받을 수 있습니다.</p>',
 'ja': '<p>ご不満な点がある場合は、<a href="mailto:hello@kaptapp.com">メールでご連絡ください</a>。苦情は 5 営業日以内に受領を確認し、30 日以内の解決を目指します。現在、裁判外紛争解決（ADR）制度は利用していません。お客様が取り得る手段については、Citizens Advice (UK) またはお住まいの地域の消費者団体にご相談いただけます。</p>',
 'de': '<p>Wenn du mit etwas nicht zufrieden bist, <a href="mailto:hello@kaptapp.com">schreib uns eine E-Mail</a>. Wir bestätigen den Eingang von Beschwerden innerhalb von 5 Arbeitstagen und bemühen uns, sie innerhalb von 30 Tagen zu lösen. Derzeit nutzen wir kein Verfahren zur alternativen Streitbeilegung. Citizens Advice (UK) oder deine örtliche Verbraucherorganisation kann dich über deine Möglichkeiten informieren.</p>',
 'fr': '<p>Si quelque chose ne vous convient pas, <a href="mailto:hello@kaptapp.com">écrivez-nous</a>. Nous accusons réception des réclamations sous 5 jours ouvrés et nous efforçons de les résoudre sous 30 jours. Nous n\'avons actuellement recours à aucun dispositif de règlement extrajudiciaire des litiges. Citizens Advice (UK) ou votre association locale de consommateurs peut vous renseigner sur les options qui s\'offrent à vous.</p>',
 'pt-br': '<p>Se você não estiver satisfeito com algo, <a href="mailto:hello@kaptapp.com">envie um e-mail para nós</a>. Confirmamos o recebimento das reclamações em até 5 dias úteis e procuramos resolvê-las em até 30 dias. No momento, não utilizamos nenhum mecanismo alternativo de resolução de disputas. O Citizens Advice (UK) ou o órgão de defesa do consumidor da sua região podem informar você sobre suas opções.</p>',
 'it': '<p>Se qualcosa non ti soddisfa, <a href="mailto:hello@kaptapp.com">scrivici via email</a>. Confermiamo la ricezione dei reclami entro 5 giorni lavorativi e cerchiamo di risolverli entro 30 giorni. Al momento non aderiamo ad alcun sistema di risoluzione alternativa delle controversie. Citizens Advice (UK) o l\'associazione dei consumatori della tua zona possono informarti sulle opzioni a tua disposizione.</p>'},

'<p>We may update these terms, for example when Kapture Pro becomes available or the law changes, and we change the date at the top when we do. If a change materially affects your account, we tell you by email at least 30 days before it takes effect.</p>': {
 'es': '<p>Podemos actualizar estos términos, por ejemplo cuando Kapture Pro esté disponible o cambie la ley, y cuando lo hacemos cambiamos la fecha que figura al principio. Si un cambio afecta de forma sustancial a tu cuenta, te lo comunicamos por correo electrónico al menos 30 días antes de que entre en vigor.</p>',
 'zh': '<p>我们可能会更新本条款，例如在 Kapture Pro 推出或法律发生变化时；更新时，我们会修改页面顶部的日期。如果某项变更对你的账户有重大影响，我们会在变更生效前至少 30 天通过电子邮件通知你。</p>',
 'ko': '<p>당사는 Kapture Pro 출시나 법률 변경 등의 경우 본 약관을 업데이트할 수 있으며, 이때 상단의 날짜를 변경합니다. 변경 사항이 사용자의 계정에 중대한 영향을 미치는 경우, 시행 최소 30일 전에 이메일로 알려 드립니다.</p>',
 'ja': '<p>当社は、Kapture Pro の提供開始時や法律の改正時などに本規約を更新することがあり、その際はページ上部の日付を変更します。変更がお客様のアカウントに重大な影響を与える場合は、発効の 30 日以上前にメールでお知らせします。</p>',
 'de': '<p>Wir können diese Bedingungen aktualisieren, etwa wenn Kapture Pro verfügbar wird oder sich die Rechtslage ändert, und ändern dann das Datum oben auf der Seite. Wirkt sich eine Änderung wesentlich auf dein Konto aus, informieren wir dich mindestens 30 Tage vor ihrem Inkrafttreten per E-Mail.</p>',
 'fr': '<p>Nous pouvons mettre à jour ces conditions, par exemple lorsque Kapture Pro deviendra disponible ou que la loi changera, et nous modifions alors la date indiquée en haut de la page. Si une modification affecte de manière importante votre compte, nous vous en informons par e-mail au moins 30 jours avant son entrée en vigueur.</p>',
 'pt-br': '<p>Podemos atualizar estes termos, por exemplo quando o Kapture Pro ficar disponível ou a lei mudar, e, quando fazemos isso, alteramos a data no topo da página. Se uma alteração afetar de forma relevante sua conta, avisamos você por e-mail com pelo menos 30 dias de antecedência da entrada em vigor.</p>',
 'it': '<p>Possiamo aggiornare questi termini, ad esempio quando Kapture Pro sarà disponibile o quando cambia la legge, e in tal caso modifichiamo la data in alto. Se una modifica incide in modo sostanziale sul tuo account, te lo comunichiamo via email almeno 30 giorni prima che entri in vigore.</p>'},

'<p>These terms are governed by the law of England and Wales. If you live in Scotland or Northern Ireland, you can also bring proceedings in your local courts. If you live in the European Union, you keep the protection of the mandatory consumer laws of your country and can bring proceedings in its courts.</p>': {
 'es': '<p>Estos términos se rigen por la legislación de Inglaterra y Gales. Si vives en Escocia o en Irlanda del Norte, también puedes iniciar acciones judiciales ante los tribunales de tu lugar de residencia. Si vives en la Unión Europea, conservas la protección que te otorgan las leyes imperativas de protección de los consumidores de tu país y puedes iniciar acciones judiciales ante sus tribunales.</p>',
 'zh': '<p>本条款受英格兰和威尔士法律管辖。如果你居住在苏格兰或北爱尔兰，也可以在当地法院提起诉讼。如果你居住在欧盟，你仍受你所在国家强制性消费者保护法律的保护，并可以在该国法院提起诉讼。</p>',
 'ko': '<p>본 약관은 잉글랜드 및 웨일스 법률을 준거법으로 합니다. 스코틀랜드 또는 북아일랜드에 거주하는 경우 거주지 법원에 소송을 제기할 수도 있습니다. 유럽연합에 거주하는 경우 거주 국가의 강행적 소비자보호법에 따른 보호를 계속 받으며, 해당 국가의 법원에 소송을 제기할 수 있습니다.</p>',
 'ja': '<p>本規約はイングランドおよびウェールズの法律に準拠します。スコットランドまたは北アイルランドにお住まいの場合は、お住まいの地域の裁判所に訴訟を提起することもできます。欧州連合にお住まいの場合は、お住まいの国の強行法規である消費者保護法による保護を引き続き受けられ、その国の裁判所に訴訟を提起することができます。</p>',
 'de': '<p>Für diese Bedingungen gilt das Recht von England und Wales. Wenn du in Schottland oder Nordirland lebst, kannst du auch vor den Gerichten an deinem Wohnort klagen. Wenn du in der Europäischen Union lebst, behältst du den Schutz der zwingenden Verbraucherschutzgesetze deines Landes und kannst vor dessen Gerichten klagen.</p>',
 'fr': "<p>Ces conditions sont régies par le droit de l'Angleterre et du pays de Galles. Si vous résidez en Écosse ou en Irlande du Nord, vous pouvez également engager une procédure devant les tribunaux de votre lieu de résidence. Si vous résidez dans l'Union européenne, vous conservez la protection des dispositions impératives du droit de la consommation de votre pays et pouvez engager une procédure devant ses tribunaux.</p>",
 'pt-br': '<p>Estes termos são regidos pela lei da Inglaterra e do País de Gales. Se você mora na Escócia ou na Irlanda do Norte, também pode propor ações nos tribunais locais. Se você mora na União Europeia, mantém a proteção das leis imperativas de defesa do consumidor do seu país e pode propor ações nos tribunais desse país.</p>',
 'it': "<p>Questi termini sono regolati dalla legge di Inghilterra e Galles. Se vivi in Scozia o in Irlanda del Nord, puoi anche agire in giudizio davanti ai tribunali locali. Se vivi nell'Unione europea, conservi la protezione delle norme imperative sui consumatori del tuo paese e puoi agire in giudizio davanti ai suoi tribunali.</p>"},

'<p class="legal-foot">KUMO STUDIO LIMITED &middot; Company number 08453597 &middot; Registered office: Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>': {
 'es': '<p class="legal-foot">KUMO STUDIO LIMITED &middot; Número de registro 08453597 &middot; Domicilio social: Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>',
 'zh': '<p class="legal-foot">KUMO STUDIO LIMITED &middot; 公司编号 08453597 &middot; 注册办公地址：Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>',
 'ko': '<p class="legal-foot">KUMO STUDIO LIMITED &middot; 회사 번호 08453597 &middot; 등록 사무소: Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>',
 'ja': '<p class="legal-foot">KUMO STUDIO LIMITED &middot; 会社番号 08453597 &middot; 登記上の事務所：Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>',
 'de': '<p class="legal-foot">KUMO STUDIO LIMITED &middot; Registernummer 08453597 &middot; Eingetragener Sitz: Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>',
 'fr': '<p class="legal-foot">KUMO STUDIO LIMITED &middot; Numéro d\'immatriculation 08453597 &middot; Siège social&nbsp;: Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>',
 'pt-br': '<p class="legal-foot">KUMO STUDIO LIMITED &middot; Número de registro 08453597 &middot; Sede social: Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>',
 'it': '<p class="legal-foot">KUMO STUDIO LIMITED &middot; Numero di registrazione 08453597 &middot; Sede legale: Office 2, Tweed House, Park Lane, Swanley, Kent, BR8 8DT, England</p>'},

'These Kapture Pro terms are part of these terms in every language version of this page.': {
 'es': 'Estos términos de Kapture Pro forman parte de estos términos en todas las versiones de esta página. Por ahora solo están disponibles en inglés.',
 'zh': '以下 Kapture Pro 条款是本条款在各语言版本中的组成部分，目前仅提供英文版。',
 'ko': '아래 Kapture Pro 약관은 모든 언어 버전의 이 약관에 포함되며, 현재 영어로만 제공됩니다.',
 'ja': '以下の Kapture Pro の条件は、すべての言語版の本規約の一部です。現在は英語でのみ提供しています。',
 'de': 'Die folgenden Bedingungen für Kapture Pro sind in jeder Sprachfassung dieser Seite Teil dieser Bedingungen. Sie sind derzeit nur auf Englisch verfügbar.',
 'fr': "Les conditions de Kapture Pro ci-dessous font partie de ces conditions dans toutes les versions linguistiques de cette page. Elles ne sont pour l'instant disponibles qu'en anglais.",
 'pt-br': 'Os termos do Kapture Pro abaixo fazem parte destes termos em todas as versões de idioma desta página. Por enquanto, estão disponíveis apenas em inglês.',
 'it': 'I termini di Kapture Pro qui sotto fanno parte di questi termini in ogni versione linguistica di questa pagina. Per ora sono disponibili solo in inglese.'},
}

# The Kapture Pro section is generated from the backend's pro_terms.json by
# tools/sync_pro_terms.py; its translations live in t_pro_terms.py.
from t_pro_terms import PRO, NOTICE_TRANSLATED
TERMS.update(PRO)
TERMS['These Kapture Pro terms are part of these terms in every language version of this page.'] = {
    **TERMS['These Kapture Pro terms are part of these terms in every language version of this page.'], **NOTICE_TRANSLATED}
