---
type: zitat
speaker: "[[Enxhi Seli-Zacharias]]"
date: 2025-01-20
topic: Menschenwürde
page_bfv: 906
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Enxhi Seli-Zacharias]] vom 20.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Schon wieder Messertote. Schon wieder ein afghanischer Täter. Und schon wieder stirbt ein Kind. Wann rafft es der letzte Horst, dass die unzivilisierten #Messermörder fast ausnahmslos aus arabsichen Ländern importiert wurden?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 906

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