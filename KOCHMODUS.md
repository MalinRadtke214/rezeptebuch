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
   - **Zutaten:** jede Zutat einzeln mit Menge und Einheit. Einheiten: g, kg, ml, l, TL → tsp, EL → tbsp, Prise → pinch. Zählbares (Eier, Äpfel, Päckchen) ohne Einheit, das Zählwort steht im Namen. Gleichnamige Zutaten aus verschiedenen Komponenten unterscheiden, z. B. „Zucker (Boden)“ und „Zucker (Füllung)“.
   - **Schritte:** ein Widget-Schritt pro nummeriertem Schritt, mit kurzem Titel (z. B. „Teig rühren“) und den Zutaten als Verweis im Text, damit Mengen beim Skalieren mitwandern.
   - **Timer:** Jede Markierung `⏱ <Dauer>` wird zum Timer des Schritts (z. B. `⏱ 55 min` → 3300 s, `⏱ 3 h` → 10800 s). Schritte mit erkennbarer Wartezeit ohne Markierung (Vorheizen, Ruhen) bekommen einen sinnvollen Timer, sofern die Datei eine Zeit nennt.
   - **Notizen:** Inhalt von `## Notizen` und die benötigten Utensilien.
4. **Begleiten:** Während des Kochens knapp auf Fragen antworten (Ersatzzutaten, „ist der Teig so richtig?“). Die Rezeptdatei bleibt im Kochmodus unverändert.
5. **Nach dem Kochen:** Fragen, ob Erfahrungen oder Änderungen unter `## Notizen` ergänzt werden sollen (mit Datum), und das erst nach Zustimmung committen.

## Ton

Kurz und praktisch – am Herd wird auf dem Handy mitgelesen.
