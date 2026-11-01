# Kochmodus – Anleitung für Claude

Diese Datei beschreibt, wie Claude sich verhält, wenn jemand im Chat den Kochmodus startet.

## Auslöser

Der Kochmodus startet bei Formulierungen wie:
- „Kochmodus“ oder „<Rezept>, Kochmodus“
- „Lass uns <Rezept> kochen/backen“
- „Führ mich durch <Rezept>“

Ist kein Rezept genannt, fragt Claude nach, welches Rezept gekocht werden soll.

## Ablauf

1. **Rezept finden:** Die passende Datei unter `rezepte/**` auf dem Branch `main` suchen und immer die aktuelle Version lesen (nicht aus dem Gedächtnis).
2. **Menge klären:** Wenn eine abweichende Menge genannt wurde („für 2 Personen“, „halbes Rezept“), entsprechend skalieren. Sonst die Menge aus dem Kopfbereich (`menge`) als Basis nehmen.
3. **Oberfläche zeigen:** Das Rezept als interaktives Rezept-Widget mit Kochmodus darstellen:
   - **Titel** = `titel`; **Beschreibung** = Einleitungssatz; **Portionen** aus `menge` (Kuchen in Springform: 12 Stücke).
   - **Zutaten:** jede Zutat einzeln mit Menge und Einheit. Als Einheit nur g, kg, ml und l verwenden. Löffelmaße und Prisen ohne Einheit angeben und „TL“, „EL“ oder „Prise“ vor den Namen schreiben (Menge 1, Name „TL Zimt“), damit die Oberfläche deutsch bleibt. Zählbares (Eier, Äpfel, Päckchen) ebenfalls ohne Einheit, das Zählwort steht im Namen. Gleichnamige Zutaten aus verschiedenen Komponenten unterscheiden, z. B. „Zucker (Boden)“ und „Zucker (Füllung)“.
   - **Schritte:** ein Widget-Schritt pro nummeriertem Schritt, mit kurzem Titel (z. B. „Teig rühren“) und den Zutaten als Verweis im Text, damit Mengen beim Skalieren mitwandern.
   - **Timer:** Jede Markierung `⏱ <Dauer>` wird zum Timer des Schritts (z. B. `⏱ 55 min` → 3300 s, `⏱ 3 h` → 10800 s). Schritte mit erkennbarer Wartezeit ohne Markierung (Vorheizen, Ruhen) bekommen einen sinnvollen Timer, sofern die Datei eine Zeit nennt.
   - **Notizen:** Inhalt von `## Notizen` und die benötigten Utensilien.
   - **Fotos:** Hat das Rezept eigene Fotos (`fotos:` im Kopfbereich), diese vor dem Rezept-Widget zeigen – ausschließlich die eigenen Fotos, niemals Bilder aus dem Netz oder von der Quellseite. Ohne eigene Fotos wird kein Bild gezeigt.
4. **Begleiten:** Während des Kochens knapp auf Fragen antworten (Ersatzzutaten, „ist der Teig so richtig?“). Die Rezeptdatei bleibt im Kochmodus unverändert.
5. **Nach dem Kochen:** Fragen, ob Erfahrungen oder Änderungen unter `## Notizen` ergänzt werden sollen (mit Datum), und das erst nach Zustimmung committen.

## Ton

Kurz und praktisch – am Herd wird auf dem Handy mitgelesen.

## Fotos hinzufügen

- Fotos werden im Ordner `bilder/` der jeweiligen Kategorie abgelegt: `rezepte/<kategorie>/bilder/<rezeptname>-1.jpg`, `-2.jpg` usw.
- Schickt jemand ein Foto im Chat, verkleinert Claude es (lange Kante max. 1600 px, JPEG), legt es dort ab, trägt es unter `fotos:` im Kopfbereich ein, bindet es unter der Überschrift ein und committet.
- Fotos können auch direkt über GitHub hochgeladen werden; dann den Pfad unter `fotos:` ergänzen.
