---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-07-30
topic: Menschenwürde
page_bfv: 211
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 30.7.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir haben von Anfang an vor den Folgen der Migration in unser Land gewarnt. Mit der AfD an der Regierung hätte es nie die Morde, Terrorangriffe, Vergewaltigungen und Ersetzungsmigration gegeben, die jetzt Deutschland in Angst und Schrecken versetzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 211

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