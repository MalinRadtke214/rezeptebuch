# Unser Rezeptebuch

Gemeinsame Rezeptsammlung. Jedes Rezept ist eine eigene Markdown-Datei unter `rezepte/<kategorie>/`.

## Konventionen

- **Dateiname:** Kleinbuchstaben, Bindestriche, keine Umlaute, z. B. `apfelkuchen-mit-quark.md`
- **Vorlage:** `_vorlage.md` kopieren und ausfüllen
- **Kopfbereich (YAML):** Titel, Kategorie, Menge, Zeiten, Tags, Quelle
- **Zutaten:** eine Zeile pro Zutat, `- <Menge> <Einheit> <Zutat>`; bei mehreren Komponenten Unterüberschriften (`### Teig`, `### Füllung`)
- **Zubereitung:** nummerierte Schritte; Wartezeiten als `⏱ <Dauer>` am Ende des Schritts markieren (z. B. `⏱ 55 min`) – daraus werden beim Kochen Timer
- **Fotos:** nur eigene Fotos, abgelegt unter `rezepte/<kategorie>/bilder/<rezeptname>-1.jpg` und im Kopfbereich unter `fotos:` eingetragen
- **Notizen:** eigene Erfahrungen und Änderungen unter `## Notizen`, gern mit Datum

## Kochmodus

Im Claude-Chat „<Rezept>, Kochmodus“ schreiben: Claude zeigt das Rezept als interaktive Oberfläche mit Schritt-für-Schritt-Anleitung und Timern. Details in `KOCHMODUS.md`.

## Oberfläche zum Durchsuchen

Mobile Ansicht mit Suche, Kategorien, Fotos und abhakbaren Zutaten: https://claude.ai/artifact/F5yhzNEi14sHFyAf8P1S51

- Code: `app/template.html` (Oberfläche) und `app/build.py` (liest alle Rezepte ein und erzeugt `app/rezeptebuch.html` mit eingebetteten Daten und Fotos)
- Neu bauen: `python3 app/build.py` (benötigt Pillow); die erzeugte Datei wird nicht eingecheckt
- Die Seite ist ein Schnappschuss: Nach neuen oder geänderten Rezepten neu bauen und unter derselben Adresse neu veröffentlichen

## Kategorien

`backen` · `hauptgerichte` · `beilagen` · `suppen` · `desserts` · `fruehstueck`

## Tags (Vorschläge)

`vegetarisch` · `vegan` · `schnell` (unter 30 min) · `meal-prep` · `gaeste` · `sommer` · `winter`
