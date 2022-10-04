from datetime import date
import markdown
import os

SOURCE_MD = 'source/index.md'

HTML_TEXT_TEMPLATE = """
<!doctype html>
<html>
  {head}
  {body}
</html>
"""

HeadText = """
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <title>Addison Hu</title>

    <link rel="stylesheet" href="stylesheets/styles.css">
    <link href="https://fonts.googleapis.com/css?family=Bitter|Raleway" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    <!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>
"""

BODY_TEXT_TEMPLATE = """
  <body>
    <div class="wrapper">
      {header}
      {section}
      {footer}
    </div>
  </body>
"""

HEADER_TEXT_TEMPLATE = """
      <header>
        <h1>Addison Hu</h1>
        <!--- <p>{position}<br>{organization}</p> --->
         <p>
         <a href="{headshot_url}">
             <img
             alt=""
             title="{headshot_text}"
             class="avatar"
             style="border-radius: 5px"
             height="230"
             src="{headshot}"
             width="230" />
         </a>
         </p>
        <p><b>contact: <a class="email" href='{mail_href}'>{mail}</a></b></br>
        <b>cv:</b> <a href="{cv}">download pdf</a><br>
        <b>github:</b> <a href="https://github.com/huisaddison">repositories</a><br>
      </header>
"""

FOOTER_TEXT_TEMPLATE = """
      <footer>
        <p><small>
	    Last Updated: {today}.
        <a href="{source}">Source.</a>
      </footer>
"""

HeaderText = HEADER_TEXT_TEMPLATE.format(
    position        = 'PhD Student<br>&emsp;'
                      'Advisor: Ryan Tibshirani<br>'
                      'Statistics & Machine Learning',
    organization    = 'Carnegie Mellon University',
    cv              = 'pdfs/AddisonHu_CV.pdf',
    headshot_url    = '',
    headshot_text   = 'with my bicycle',
    headshot        = 'img/autumn-bicycle.jpg',
    mail_href       = r'mail&#116;o&#58;&#109;a&#37;&#54;9&#108;%40hu&#105;' +
                      r'saddiso%&#54;E&#46;c&#111;m',
    mail            = r'mail&#64;&#104;&#117;i&#115;a&#100;di&#115;&#111;&#110;&' +
                      r'#46;com',
)

FooterText = FOOTER_TEXT_TEMPLATE.format(
    generate_script = 'generate_html.py',
    source          = SOURCE_MD,
    today           = date.today().strftime('%Y %B %d'),
)

SECTION_TEXT_TEMPLATE = """
    <section>
    {section}
    </section>
"""

section_html = ''

with open(SOURCE_MD, 'r', encoding='utf-8') as f:
    text = f.read()
    section_html += markdown.markdown(text)

SectionText = SECTION_TEXT_TEMPLATE.format(
    section     = section_html,
)

BodyText = BODY_TEXT_TEMPLATE.format(
    header      = HeaderText,
    section     = SectionText,
    footer      = FooterText,
)
HtmlText = HTML_TEXT_TEMPLATE.format(
    head    = HeadText,
    body    = BodyText,
)

if os.path.isfile('index.html'):
    os.rename('index.html', 'index.html.old')

with open('index.html', 'w') as f:
    f.write(HtmlText)
