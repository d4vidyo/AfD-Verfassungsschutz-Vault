---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2025-02-07
topic: Menschenwürde
page_bfv: 909
source: 'Redebeitrag'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 7.2.2025 veröffentlicht auf: 'Redebeitrag'
> [!quote] Aussage
>Aber die gesamte Diskussion da fiel von Seiten der etablierten Politik nicht ein einziges Mal die Frage nach Einwanderung, nach Gruppenvergewaltigung von Deutschen durch Migrantengruppen, nichts. [...] Und da sage ich euch ganz deutlich, die Analyse der Gründe ist ganz einfach: Wenn ich Hunderttausende und Millionen aus Kulturen hole, in denen Frauen nichts gelten, in denen sie noch gesteinigt werden, wenn sie irgendwo den falschen Mann angeguckt haben, dann muss ich mich nicht wundern, dass in Deutschland das Leben für Frauen und Mädchen unsicherer wird. Und da haben sich diese ganzen Linken und die Union in einer Weise versündigt an unseren Frauen und an unseren Mädchen. Das werden wir ihnen nicht durchgehen lassen und ich werde es ihnen auch im Familienausschuss immer und immer wieder sagen. Es sind nicht die Männer. Es sind die Männer, die wir hierhergeholt haben und die hier nicht hergehören, weil sie ein frauenverachtendes Weltbild haben. Und es ist umgekehrt eben auch nicht so, dass es ein generelles Problem zwischen Frauen und Männern gibt, sondern es ist ein im Wesentlichen importiertes Problem.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 909

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