# Generates the Next.js files from original.html without changing any markup, CSS or JS.
import re, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s = (root/'scripts'/'original.html').read_text(encoding='utf-8')
css = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
body = re.search(r'<body>(.*)</body>', s, re.S).group(1)
m = re.search(r'<script>(.*?)</script>\s*$', body, re.S)
js = m.group(1); markup = body[:m.start()]
(root/'public'/'app.js').write_text(js, encoding='utf-8')
(root/'app'/'original-styles.js').write_text('const css = ' + json.dumps(css, ensure_ascii=False) + ';\nexport default css;\n', encoding='utf-8')
(root/'app'/'original-markup.js').write_text('const markup = ' + json.dumps(markup, ensure_ascii=False) + ';\nexport default markup;\n', encoding='utf-8')
print('css', len(css), 'markup', len(markup), 'js', len(js))
