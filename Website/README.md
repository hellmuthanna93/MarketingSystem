# Website — annahellmuth.com (static)

Static HTML mirror of [annahellmuth.com](https://annahellmuth.com/), living in `anna-hellmuth/`.

## Preview

From the **repo root**:

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080/website/anna-hellmuth/](http://localhost:8080/website/anna-hellmuth/)

## Styling

Pages import the shared brand system:

- `brand/tokens.css`
- `brand/typography.css` (Source Serif 4 via Google Fonts)
- `brand/components.css`

Site-specific layout and sections: `anna-hellmuth/assets/css/index.css`

Edit colors only in `brand/tokens.css`. See `brand/DESIGN.md` for the full reference.

## Pages

| File | Route |
|------|--------|
| `index.html` | Home |
| `counseling.html` | Psychological counseling |
| `lifecoaching.html` | Life coaching |
| `about.html` | About |
| `contact.html` | Contact |
| `impressum.html` | Legal notice |
| `privacy-policy.html` | Privacy policy |

Assets: `anna-hellmuth/assets/images/`
