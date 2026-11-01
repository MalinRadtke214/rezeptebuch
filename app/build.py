#!/usr/bin/env python3
"""Baut aus rezepte/**/*.md eine eigenständige HTML-Seite (app/rezeptebuch.html).

Aufruf aus dem Repo-Wurzelverzeichnis:  python3 app/build.py [Zieldatei]
(ohne Zieldatei: app/rezeptebuch.html; GitHub Pages baut nach _site/index.html)
Benötigt: Pillow (für das Verkleinern der Fotos).
"""
import base64, io, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REZEPTE = ROOT / "rezepte"
TEMPLATE = ROOT / "app" / "template.html"
OUT = ROOT / "app" / "rezeptebuch.html"
FOTO_MAX = 900  # lange Kante in px für die eingebetteten Fotos


def parse_frontmatter(text):
    meta, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return meta, body
    for line in m.group(1).splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, val = line.split(":", 1)
        val = re.sub(r"\s+#.*$", "", val).strip()
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        meta[key.strip()] = val
    return meta, m.group(2)


def parse_body(body):
    out = {"beschreibung": "", "utensilien": [], "zutaten": [], "schritte": [], "notizen": []}
    h2, group = None, None
    for raw in body.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.startswith("!["):
            continue
        if line.startswith("# "):
            h2 = "_intro"; continue
        if line.startswith("## "):
            h2 = line[3:].strip().lower(); group = None; continue
        if line.startswith("### "):
            if h2 == "zutaten":
                group = {"name": line[4:].strip(), "items": []}
                out["zutaten"].append(group)
            continue
        bullet = re.match(r"^\s*-\s+(.*)$", line)
        num = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if h2 == "_intro" and not out["beschreibung"]:
            out["beschreibung"] = line.strip()
        elif h2 == "utensilien" and bullet:
            out["utensilien"].append(bullet.group(1))
        elif h2 == "zutaten" and bullet:
            if group is None:
                group = {"name": "", "items": []}; out["zutaten"].append(group)
            group["items"].append(bullet.group(1))
        elif h2 == "zubereitung" and num:
            out["schritte"].append(num.group(1))
        elif h2 == "notizen" and bullet:
            out["notizen"].append(bullet.group(1))
    return out


def foto_data_uri(path):
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    im.thumbnail((FOTO_MAX, FOTO_MAX))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def main():
    rezepte = []
    for md in sorted(REZEPTE.rglob("*.md")):
        meta, body = parse_frontmatter(md.read_text(encoding="utf-8"))
        r = parse_body(body)
        fotos = meta.get("fotos") or []
        if isinstance(fotos, str):
            fotos = [fotos] if fotos else []
        r["fotos"] = [foto_data_uri(md.parent / f) for f in fotos if (md.parent / f).exists()]
        tags = meta.get("tags") or []
        r.update({
            "id": md.stem,
            "titel": meta.get("titel") or md.stem,
            "kategorie": meta.get("kategorie") or md.parent.name,
            "menge": meta.get("menge", ""),
            "arbeitszeit": meta.get("arbeitszeit", ""),
            "koch_backzeit": meta.get("koch_backzeit", ""),
            "tags": tags if isinstance(tags, list) else [tags],
            "quelle": meta.get("quelle", ""),
        })
        rezepte.append(r)
    data = json.dumps(rezepte, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/[]", data)
    out = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"{len(rezepte)} Rezepte -> {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    sys.exit(main())
