---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-04-12
topic: Menschenwürde
page_bfv: 491
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 12.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das Weitergeben der Flamme, wie Sie es in der Burschenschaft pflegen, ist die Antithese zur globalistischen Agenda, zum ,Great Reset', zum großen Austausch. Wenn wir unsere Heimat nachhaltig schützen wollen, dann müssen wir sie von der Wurzel her bewahren. Die Deutsche Burschenschaft und der heutige Reichsgründungskommers leisten dazu einen wichtigen Beitrag.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 491

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