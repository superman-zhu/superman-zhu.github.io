# Personal Website — Setup Guide

A single-file portfolio for Jiaqi Zhu. No build step, no dependencies. Double-click `index.html` to preview it in any browser.

## 1. Publish it (get a real URL)

GitHub Pages is free and takes about five minutes. Your account is `superman-zhu`, so:

1. Go to **github.com/new**
2. **Repository name:** `superman-zhu.github.io` — exactly this, including `.github.io`
3. **Visibility:** Public (required for free Pages hosting)
4. Leave *Add README*, *.gitignore*, *license*, and the Copilot prompt untouched
5. Click **Create repository**
6. On the new repo page, click **uploading an existing file**, drag in `index.html` and `cv.pdf`, then **Commit changes**
7. Wait 1–2 minutes and open **https://superman-zhu.github.io**

To update the site later, upload a new `index.html` over the old one.

*(You are only using GitHub as free hosting here — nothing about your code needs to be public, and the site never links to a GitHub profile.)*

### Custom domain (optional)

Buy a domain (Cloudflare or Namecheap, roughly $10/year), then go to **Settings → Pages → Custom domain**, enter it, and add the DNS records GitHub shows you.

### Alternatives

**Vercel** or **Netlify** — sign up, drag the folder onto the page, get a URL in seconds. Both support custom domains.

## 2. What's already filled in

- NYU Shanghai · Class of 2027
- Major: Business and Finance & Data Science
- Email: jz6553@nyu.edu
- LinkedIn: linkedin.com/in/jiaqi-zhu-22a866370
- Sections: **Writing** and **Projects** only
- Accent colour: NYU violet

## 3. What still needs your input

Open `index.html` in any text editor and search for `[EDIT` — four spots.

| Marker | What to change |
|---|---|
| EDIT 1 | Tab title and SEO description |
| EDIT 2 | CV link (see below) |
| EDIT 3 | Your bio — rewrite it in your own voice |
| EDIT 4 | Portrait photo |

Then replace the placeholder text in the Writing entries and Project cards.

### Add your CV

Rename your resume PDF to `cv.pdf` and upload it next to `index.html`. All three CV links on the page already point there.

### Add your photo

Name the image `photo.jpg`, put it in the same folder, then replace:

```html
<div class="portrait">
  <p class="portrait-ph">PHOTO<br>photo.jpg<br>800 × 920 px</p>
</div>
```

with:

```html
<div class="portrait"><img src="photo.jpg" alt="Jiaqi Zhu"></div>
```

### Add a writing entry

Search for `COPY THIS ENTIRE <li>`. Duplicate everything between the `▼▼▼` and `▲▲▲` comments and edit the copy. Delete any link chips (PDF, Slides, Data) you don't need.

### Add a project

Search for `COPY THIS ENTIRE <a class="card">` and do the same. If a project has no link yet, change `<a class="card" href="...">` to `<div class="card">` and the closing `</a>` to `</div>`.

### Change the accent colour

One line near the top of the file:

```css
--accent: #57068c;
```

- `#57068c` NYU violet (current)
- `#7c2d3a` academic crimson
- `#1e3a5f` navy
- `#2d5a4a` forest green

### Host PDFs and other files

Upload them to the same repository alongside `index.html`, then link with `href="paper.pdf"`.

## A note on the internship material

Your resume describes work done at Fullgoal, CCB Principal, and Western Securities. Replicated research reports and internal frameworks generally belong to the firm — check before putting any of it on a public site, and describe methods in general terms rather than posting the code or the reports themselves.

## Built in

Automatic dark mode with a manual toggle that remembers your choice, mobile layout, scroll-reveal animations, reduced-motion support, and visible keyboard focus rings.
