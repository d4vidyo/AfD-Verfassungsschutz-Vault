---
type: zitat
speaker: "[[Rainer Rothfuß]]"
date: 2025-02-13
topic: Menschenwürde
page_bfv: 928
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Rainer Rothfuß]] vom 13.2.2025 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Und da geht es nicht nur um die Abschiebung schwerer Straftäter, sondern auch um die Rückführung vieler Hunderttausender, die kaum integrierbar sind in unsere Wirtschafts- und Sozialsysteme, es sei denn, es handelt sich um die sozialen Sicherungssysteme.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 928

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