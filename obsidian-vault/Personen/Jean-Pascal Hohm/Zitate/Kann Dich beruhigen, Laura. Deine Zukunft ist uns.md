---
type: zitat
speaker: "[[Jean-Pascal Hohm]]"
date: 2023-05-07
topic: Menschenwürde
page_bfv: 384
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jean-Pascal Hohm]] vom 7.5.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Kann Dich beruhigen, Laura. Deine Zukunft ist uns nicht egal. Darum kämpfen wir auch mit aller Entschlossenheit gegen die fortschreitende Überfremdung unserer gemeinsamen Heimat.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 384

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