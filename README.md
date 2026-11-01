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

## Kategorien

`backen` · `hauptgerichte` · `beilagen` · `suppen` · `desserts` · `fruehstueck`

## Tags (Vorschläge)

`vegetarisch` · `vegan` · `schnell` (unter 30 min) · `meal-prep` · `gaeste` · `sommer` · `winter`
