# GENZTECH DSS – Signage CMS (Next.js)

Original `index.html` ka exact Next.js (App Router) version. Markup, CSS aur JS bina kisi change ke use hue hain.

## Chalane ke liye
```bash
npm install
npm run dev        # http://localhost:3000
# production:
npm run build && npm start
```
Login page: `http://localhost:3000/?login=1` (pehle jaisa — "Open dashboard" button naye tab me yahi URL kholta hai).

## Files
- `app/layout.js` – `<head>` (title, viewport, Google Fonts) + original `<style>` as-is
- `app/page.js` – original body markup + original script load
- `app/original-markup.js` – original `<body>` HTML (unchanged)
- `app/original-styles.js` – original CSS (unchanged)
- `public/app.js` – original `<script>` (unchanged; base64 images isi ke andar hain)
- `scripts/original.html` + `scripts/build-from-html.py` – original HTML update karo to
  `python3 scripts/build-from-html.py` chala do, upar ki teeno files dobara generate ho jayengi.
