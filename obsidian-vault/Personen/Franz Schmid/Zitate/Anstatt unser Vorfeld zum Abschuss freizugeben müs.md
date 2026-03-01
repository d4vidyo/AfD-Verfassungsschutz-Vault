---
type: zitat
speaker: "[[Franz Schmid]]"
date: 2023-07-12
topic: Sonstiges
page_bfv: 790
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Franz Schmid]] vom 12.7.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Anstatt unser Vorfeld zum Abschuss freizugeben müssen wir es stärken! Die mutigen Aktivisten von @WiderstandB, @Wackre_Schwaben, @lederhosen_rvlt und co sind keine Extremisten! Aktionspläne braucht es in diesem Land gegen Linksterrorismus und für Remigration! Nicht gegen patriotische Aktionsgruppen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 790

**Verfassungsschutz Kategorisierung:** Sonstiges.

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