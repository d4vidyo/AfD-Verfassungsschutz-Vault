---
type: zitat
speaker: "[[René Bochmann]]"
date: 2023-02-22
topic: Menschenwürde
page_bfv: 172
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[René Bochmann]] vom 22.2.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Auch ein deutscher Pass oder eine doppelte Staatsangehörigkeit können darüber nicht hinwegtäuschen, dass die fremden Kulturkreise immer mehr Raum ergreifen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 172

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