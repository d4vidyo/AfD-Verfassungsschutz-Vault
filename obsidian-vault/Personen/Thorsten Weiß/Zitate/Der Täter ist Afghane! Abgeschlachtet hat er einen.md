---
type: zitat
speaker: "[[Thorsten Weiß]]"
date: 2025-01-22
topic: Menschenwürde
page_bfv: 927
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Thorsten Weiß]] vom 22.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der Täter ist Afghane! Abgeschlachtet hat er einen 2-jährigen Jungen. Millionenfache Remigration jetzt! #Aschaffenburg

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 927

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