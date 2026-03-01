---
type: zitat
speaker: "[[Birgit Bessin]]"
date: 2022-06-03
topic: Menschenwürde
page_bfv: 401
source: 'None'
status: Unbewertet
---

# Zitat: [[Birgit Bessin]] vom 3.6.2022 veröffentlicht auf: 'None'
> [!quote] Aussage
>Forderung einer „Abschiebeoffensive“ in einer Rede

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 401

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