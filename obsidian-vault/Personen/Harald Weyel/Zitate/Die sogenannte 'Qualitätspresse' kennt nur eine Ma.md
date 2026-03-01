---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2024-09-09
topic: Demokratieprinzip
page_bfv: 558
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom 9.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die sogenannte 'Qualitätspresse' kennt nur eine Marschrichtung, wenn es um die AfD geht. Was ärgert sie noch mehr als die blaue Partei? Medien, die ohne #Zwangsbeitrag eine andere Sicht auf die Dinge präsentieren. #GEZ #rundfunkbeitrag #AUF1 #freilich #compact #jungefreiheit

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 558

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