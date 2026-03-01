---
type: zitat
speaker: "[[Stephan Protschka]]"
date: 2018-12-05
topic: Menschenwürde
page_bfv: 146
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Stephan Protschka]] vom 5.12.2018 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wenn sich ein #Hund einem #Wolfsrudel anschließt. Ist er dann ein #Wolf oder bleibt er Hund? #Passbeschenkter

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 146

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