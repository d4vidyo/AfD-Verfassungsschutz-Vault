---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-12-21
topic: Sonstiges
page_bfv: 766
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 21.12.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Nicht alle Parteifreunde haben diese Erkenntnisse verinnerlicht. Der eine oder andere braucht vielleicht noch einen Denkanstoß, damit sie sich unserer tatsächliche Situation bewußt zu machen. Es ist Weihnachtszeit. Vielleicht freut sich der eine oder andere über ein gutes Buchgeschenk. Ich hätte da eine Empfehlung...

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 766

**Verfassungsschutz Kategorisierung:** Sonstiges.

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