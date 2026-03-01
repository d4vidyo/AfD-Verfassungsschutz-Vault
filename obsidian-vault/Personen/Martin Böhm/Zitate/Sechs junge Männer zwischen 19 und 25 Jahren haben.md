---
type: zitat
speaker: "[[Martin Böhm]]"
date: 2024-04-16
topic: Menschenwürde
page_bfv: 373
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Böhm]] vom 16.4.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Sechs junge Männer zwischen 19 und 25 Jahren haben mutmaßlich zwei 14-jährige Mädchen in der Rostocker Innenstadt vergewaltigt. Die beiden Opfer beschrieben die Täter als Ausländer !! [Messer-Emoji] Hier wird ein Machtanspruch zelebriert, wie er sonst nur in Kriegsgebieten an der Tagesordnung ist. Sie verachten unser Land, und sie zeigen es, indem sie unsere Kinder schänden. Vergewaltigung ist seit Tausenden von Jahren eine Waffe im Krieg. Dieses »Vorgehen« liefert eine Erklärung für das, was seit 2015 in Deutschland passiert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 373

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