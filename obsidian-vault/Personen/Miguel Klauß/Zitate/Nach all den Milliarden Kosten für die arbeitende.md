---
type: zitat
speaker: "[[Miguel Klauß]]"
date: 2022-08-01
topic: Menschenwürde
page_bfv: 413
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Miguel Klauß]] vom 1.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Nach all den Milliarden Kosten für die arbeitende Bevölkerung muss man sich die Frage stellen, ob wir es uns noch leisten können, Milliarden € für Flüchtlinge im Hartz4 System auszugeben. #Remigration jetzt

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 413

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