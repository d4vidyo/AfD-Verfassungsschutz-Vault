---
type: zitat
speaker: "[[Gunnar Beck]]"
date: 2022-08-24
topic: Menschenwürde
page_bfv: 150
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Beck]] vom 24.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Biologie und Medizin lehren uns, Lebewesen unterscheiden sich weitestgehend aufgrund ihrer genetischen Ausstattung. Nur bei der menschlichen Intelligenz macht die linke 'Wissenschaft' eine Ausnahme. Sonderbar, nicht?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 150

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