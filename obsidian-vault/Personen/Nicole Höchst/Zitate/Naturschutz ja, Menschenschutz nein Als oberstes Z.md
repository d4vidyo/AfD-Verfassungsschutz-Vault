---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2022-11-27
topic: Menschenwürde
page_bfv: 168
source: 'Beitrag auf journalistenwatch.com'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 27.11.2022 veröffentlicht auf: 'Beitrag auf journalistenwatch.com'
> [!quote] Aussage
>Naturschutz ja, Menschenschutz nein Als oberstes Ziel stehen immer Naturschutz und Tierschutz. Vom Schutz der Menschen liest man selten. [...] Mir ist die Brenzligkeit, bei sozialen Phänomenen Vergleiche zur Biologie anzustellen, durchaus bewusst, wie auch die Tatsache, dass die entsprechende Bildsprache von den Nationalsozialisten in menschenverachtender und volksverhetzender Weise gebracht wurden, um 'Rassen' oder 'Minderwertige' zu diffamieren. Nichts liegt mir ferner, als hier irgendwelche Anleihen zu nehmen [...]. Und doch ist das Bild von den 'invasiven Arten', welches das offizielle Vokabular im Tierschutzzusammenhang darstellt, mit Blick die Bedrohung unsere kulturelle und ethnische Identität durchaus geeignet, um auf ein immer drängenderes Problem deutlich zu machen. Denn der Einwanderungspolitik der Bundesregierung – schon der alten unter Merkel, aber erst recht der Ampel – geht es, um im Bild zu bleiben, genau darum, Angestammte, als quasi 'einheimische Arten', zu verdrängen. Und ja: In letzter Konsequenz wird sogar die mögliche Gefahr ihrer perspektivischen Ausrottung in Kauf genommen. Ist es im besten Deutschland aller Zeiten allerdings überhaupt noch erlaubt, sich hier aufdrängende Parallelen zu ziehen? Sei's drum.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 168

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

---
## Meine Auswertung:

**Meine Bewertung:** `INPUT[inlineSelect(option(Unbewertet), option(Legitim), option(Fragwürdig), option(Nicht legitim), defaultValue(Unbewertet)):status]`

_Mein Kommentar:_ 


---
# Nächste Aussage:
```dataview
TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
FROM "Personen"
WHERE type = "zitat" and status = "Unbewertet" AND file.name != this.file.name
SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
LIMIT 10
```