---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2023-09-23
topic: Menschenwürde
page_bfv: 417
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 23.9.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ich bin strikt gegen eine Obergrenze beim Thema #Migration. Jeder Fremde mehr in diesem Land ist einer zu viel. Wir brauchen eine stringente #Remigration von denen, die hier sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 417

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