# Gera index.html a partir de src.html, embutindo as imagens de assets/ em base64.
import base64, re, sys
def uri(p): return 'data:image/png;base64,' + base64.b64encode(open(p,'rb').read()).decode()
s = open('src.html', encoding='utf-8').read()
s = s.replace('{{LOGO}}', uri('assets/logo.png')).replace('{{LOGO_BRANCA}}', uri('assets/logo-branca.png')).replace('{{ICONE}}', uri('assets/icone.png'))
open('index.html', 'w', encoding='utf-8').write(s)
if len(sys.argv) > 1:  # versão sem <html>/<head>/<body> para a prévia
    a = re.sub(r'(?s)^<!doctype html>\s*<html[^>]*>\s*<head>\s*<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', '', s)
    a = a.replace('</head>\n<body>\n', '\n', 1).replace('</body>\n</html>\n', '')
    open(sys.argv[1], 'w', encoding='utf-8').write(a)
print('ok', len(s)//1024, 'KB')
