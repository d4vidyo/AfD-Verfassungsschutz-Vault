---
type: zitat
speaker: "[[Andreas Galau]]"
date: 2023-09-07
topic: Menschenwürde
page_bfv: 220
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Andreas Galau]] vom 7.9.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Liebe Freunde, wenn ich hier an dieser Stelle das böse U-Wort verwenden würde - könnt ihr jetzt mal drüber nachdenken was ich damit meine - wäre mir der nächste Eintrag im Verfassungsschutzbericht sicher. Möglicherweise wird sogar der Staatsanwalt juckig wegen Hassrede oder Volksverhetzung oder so. Es ist ja in unserem besten Rechtsstaat aller Zeiten mittlerweile schwierig, die Realität rechtskonform zu beschreiben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 220

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