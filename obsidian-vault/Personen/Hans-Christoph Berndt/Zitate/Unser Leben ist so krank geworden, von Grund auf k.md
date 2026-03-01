---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-08-21
topic: Menschenwürde
page_bfv: 123
source: 'Interview mit AUF1'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 21.8.2024 veröffentlicht auf: 'Interview mit AUF1'
> [!quote] Aussage
>Unser Leben ist so krank geworden, von Grund auf krank geworden, dass wir lange brauchen werden, bis wir wirklich wieder gesunde und normale Verhältnisse haben. Und die politische Macht alleine kann es nicht richten, aber politische Macht ist notwendig, um diese Prozesse in Gang zu setzen und zu fördern und zu beschleunigen. Deswegen wollen wir politische Macht, nicht weil es um das Ministerium geht. Uns geht es darum, dass wir wieder als Deutsche in Deutschland im Frieden mit uns selbst leben können. Und es wird es nur mit uns geben, eine solche Politik.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 123

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