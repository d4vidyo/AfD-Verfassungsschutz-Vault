---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-05-16
topic: Menschenwürde
page_bfv: 305
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 16.5.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Man kennt es: Sogenannte Geflüchtete messern in der Öffentlichkeit Mitmenschen nieder und schnell steht fest: Es liegt kein religiöses oder politisches Tatmotiv vor. Es handelt sich auf KEINEN Fall um einen Terrorakt! Im Gegenteil - der Täter ist psychisch krank und im Grunde genommen auch nicht voll schuldfähig. \<Bild\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 305

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