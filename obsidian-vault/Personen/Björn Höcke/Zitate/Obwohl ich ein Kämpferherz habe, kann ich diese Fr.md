---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-18
topic: Menschenwürde
page_bfv: 882
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 18.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Obwohl ich ein Kämpferherz habe, kann ich diese Frage gerade nicht zustimmend beantworten. Heute spüre ich nur tiefe Traurigkeit. [...] Der französische Schriftsteller Michel Houellebecq führte vor kurzem in einem Interview aus, daß es zwei Arten von Menschen gibt, nämlich gute und böse. Heute, einen Tag nach #Magdeburg, fällt es mir schwer ihm zu widersprechen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 882

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