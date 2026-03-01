---
type: zitat
speaker: "[[Thomas Herrig]]"
date: 2023-08-21
topic: Menschenwürde
page_bfv: 524
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Thomas Herrig]] vom 21.8.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Türken haben Deutschland wieder aufgebaut, Afrikaner wiedervereinigt und eine andere Minderheit, die wir fast ausgerottet haben, regiert dieses Land.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 524

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