---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2022-10-19
topic: Menschenwürde
page_bfv: 268
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 19.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wir brauchen endlich eine Abschiebeoffensive. Deutschland darf nicht länger Hort psychisch auffälliger 'Einzeltäter' sein, die offensichtlich tickende Zeitbomben sind, sondern muss die Sicherheit der Bürger in den Vordergrund rücken. Das sind wir vor allem den vielen Opfern der Migrationspolitik seit 2015 schuldig.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 268

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