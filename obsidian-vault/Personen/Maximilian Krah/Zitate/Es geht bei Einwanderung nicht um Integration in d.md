---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-04-09
topic: Menschenwürde
page_bfv: 169
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 9.4.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Es geht bei Einwanderung nicht um Integration in die deutsche Kulturgemeinschaft, es geht um ihre Zerstörung [...]. Und das ist auch folgerichtig weil diese Kultur eben nicht beliebig auf Andere übertragbar ist, sondern das Produkt kollektiver Evolution.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 169

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