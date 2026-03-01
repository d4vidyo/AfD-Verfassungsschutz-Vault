---
type: zitat
speaker: "[[Christian Blex]]"
date: 2025-02-15
topic: Menschenwürde
page_bfv: 912
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christian Blex]] vom 15.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Sie haben afrikanische, arabische Armutszuwanderung, komplett kulturfremd - Messerzuwanderung - in unser Land gelassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 912

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