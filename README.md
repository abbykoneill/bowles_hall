# Bowles Hall website

A redesign of the Bowles Hall Residential College site, hosted on GitHub Pages.

## Editing

Pages live in `src/pages/`, and the shared header and footer live in `src/layout.html`.
Edit those, then rebuild the HTML files at the repo root:

```bash
python3 build.py
```

Each page starts with a comment setting its title, description and which nav item is current:

```html
<!-- title: Apply · Bowles Hall | description: One sentence. | nav: apply -->
```

Styles are in `styles.css`; photos, headshots, newsletters and blog images are in `assets/`.

## Preview locally

```bash
python3 -m http.server 8000
```

Photos, text and newsletters come from the original Bowles Hall site. Online donations go to the Foundation's Donorbox page.
