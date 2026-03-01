---
type: zitat
speaker: "[[Beatrix von Storch]]"
date: 2024-10-05
topic: Menschenwürde
page_bfv: 463
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Beatrix von Storch]] vom 5.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Alle afghanischen Frauen bekommen Asyl- weil ihre afghanischen Männer alle grausam sind? Und dann kommen die Männer über Familiennachzug? Das hat mit dem #Islam zu tun. Der #EuGH will uns offenkundig kaputt machen, also: islamisieren. Was für ein IRRSINN. #nurnochAfD Wir steigen da aus. Es reicht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 463

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