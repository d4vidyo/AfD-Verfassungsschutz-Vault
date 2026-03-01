---
type: zitat
speaker: "[[Martin Renner]]"
date: 2024-07-09
topic: Nationalsozialismus
page_bfv: 679
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 9.7.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Diese Art 'Musterdemokraten' verteidigen unsere Demokratie mit allen Mitteln und seien diese noch so faschistisch. Schön und wichtig, dass es Euch CDU-Musterdemokraten gibt. Ihr müsst Euch jetzt halt nur noch überlegen, wo 'das totale Auslöschen' stattfinden soll - in Auschwitz oder in Bergen-Belsen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 679

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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