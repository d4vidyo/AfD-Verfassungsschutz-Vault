---
type: zitat
speaker: "[[Sebastian Koch]]"
date: 2022-06-15
topic: Menschenwürde
page_bfv: 348
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Koch]] vom 15.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Offene Grenzen und Toleranz. Mir kann so etwas nicht passieren - ich habe ein stereotypisches Gedankengut in mir und denke immer wenn ich so ne Meute sehe, dass die eh nur randalieren und Frauen begrabschen bis hin zu einer Gruppenvergewaltigung, weshalb ich sofort beim ersten Anschein von schwarzen Wolken am Horizont weggefahren wäre. Man fragt sich bei solchen Meldungen immer wieder, warum so viele Menschen Ressentiments entwickeln...

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 348

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