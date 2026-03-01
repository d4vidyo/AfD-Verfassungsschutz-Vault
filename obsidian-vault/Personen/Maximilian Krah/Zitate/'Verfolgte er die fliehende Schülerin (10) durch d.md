---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-07-15
topic: Menschenwürde
page_bfv: 381
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 15.7.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>'Verfolgte er die fliehende Schülerin (10) durch den ganzen Zug' – und keiner half? Die Einwanderung zerstört das Land. Eine Dystopie beginnt, wenn wir nicht schleunigst die Notbremse ziehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 381. Reaktion auf einen Artikel des Heimatkuriers

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