---
type: zitat
speaker: "[[Rüdiger Lucassen]]"
date: 2024-02-15
topic: Sonstiges
page_bfv: 854
source: 'Heimatkurier'
status: Unbewertet
---

# Zitat: [[Rüdiger Lucassen]] vom 15.2.2024 veröffentlicht auf: 'Heimatkurier'
> [!quote] Aussage
>Mein Antrag richtet sich nicht an die erneute Diffamierung unserer Partei durch den sogenannten Verfassungsschutz. Mir geht es um den richtigen Umgang der AfD mit diesem Angriff auf unsere Parteijugend. [...] Wenn wir jetzt anfingen, unsere eigene Parteijugend im Stich zu lassen, verspielten wir damit unsere Glaubwürdigkeit. Mehr noch: Unser Bekenntnis für Deutschland würde die moralische Grundlage verlieren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 854

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