---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-06-05
topic: Menschenwürde
page_bfv: 143
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 5.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Beim Betrachten des Fotos allerdings müsste man der Richtigkeit halber von einer "Passdeutschen Fußballnationalmannschaft" sprechen. Gibt es tatsächlich so wenig talentierte "Eingeborene"?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 143

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