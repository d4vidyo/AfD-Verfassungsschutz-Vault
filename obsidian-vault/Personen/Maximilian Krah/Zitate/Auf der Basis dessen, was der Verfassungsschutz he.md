---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-04-27
topic: Menschenwürde
page_bfv: 176
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 27.4.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Auf der Basis dessen, was der Verfassungsschutz heute zum Volk zum Besten gegeben hat, lässt sich kein Staat machen, zumindest kein demokratischer. Denn ohne eine Homogenität kann es kein Gemeinwohl geben, nur Teilinteressen. Abstrakte Rechtsprinzipien reichen nicht aus.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 176

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