---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2024-11-28
topic: Menschenwürde
page_bfv: 888
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 28.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Sie wollen weiter Masseneinwanderung und damit unser Volk, unsere Gemeinschaft schädigen. [...] Liebe Freunde, es ist kein Menschenrecht, in Deutschland zu sein. Und es ist ethisch geboten, diejenigen, die uns Schaden zufügen, wieder außer Landes zu schaffen. Wir werden im großen Stil abschieben. Wir haben Hunderttausende, die wir abschieben müssen, die eben von uns alimentiert werden. Das ist schon, ich würde sagen, fast schon kriminell von der Bundesregierung, dass sie an Leute hier unsere harte Arbeit, das Geld, verteilt, damit sie bleiben, obwohl sie gar nicht berechtigt sind. Ich kann auch nicht nach Polen gehen und sagen, ich will jetzt hier bei euch leben und gebt mir mal Geld. Aber genau das passiert hier hunderttausendfach, wenn nicht gar millionenfach in Deutschland. Und das ist geschuldet eben der linksgrünen Politik für Masseneinwanderung zum Schaden von Deutschland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 888. Videobeitrag

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