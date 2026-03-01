---
type: zitat
speaker: "[[Markus Frohnmaier]]"
date: 2022-08-03
topic: Demokratieprinzip
page_bfv: 539
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Markus Frohnmaier]] vom 3.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ein über hundert Jahre alter Trick des angelsächsischen Imperialismus besteht darin, die Kooperation (um es höflich auszudrücken) kleiner Staaten mit ihm als nationale Souveränität und Selbstbestimmungsrecht zu verkaufen. Müssen wir im Jahr 2022 wirklich noch darauf reinfallen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 539. Repost ohne Originalquelle

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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