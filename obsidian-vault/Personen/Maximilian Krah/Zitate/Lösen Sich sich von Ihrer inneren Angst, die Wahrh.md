---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2024-01-29
topic: Menschenwürde
page_bfv: 116
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 29.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Lösen Sich sich von Ihrer inneren Angst, die Wahrheit auszusprechen! Natürlich ist Korruption korreliert mit Kultur und Kultur mit Ethnie. Empirisch belegbar. Ja, die Linken wollen nicht, dass die Realität ausgesprochen wird. Aber soll ich deshalb der Lüge folgen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 116

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