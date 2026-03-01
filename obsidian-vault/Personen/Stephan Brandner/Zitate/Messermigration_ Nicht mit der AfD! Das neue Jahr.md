---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2023-03-08
topic: Menschenwürde
page_bfv: 289
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 8.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Messermigration? Nicht mit der AfD! Das neue Jahr ist erst wenige Wochen alt und schon waren die Zeitungen voll von Schlagzeilen zu Messermorden und -angriffen. [...] Wir alle wissen, dass diese Entwicklung verhältnismäßig neu ist. Vor 2015 hat das Messer als Tatmittel, wie es in der offiziellen Statistik heißt, wohl kaum eine Rolle gespielt. Jahrelang mussten wir als AfD darum kämpfen, dass die Statistik der Messerattacken überhaupt durch offizielle Stellen geführt wird. denn nur, wenn umfassende Kenntnisse vorhanden sind, lassen sich die Ursachen der Messerattacken überhaupt bekämpfen. Sogenannte 'Junge Männer‘ aus dem Ausland, die angeblich nach Schutz und Frieden in Deutschland suchen, den sie in ihrer Heimat nicht finden konnten, sorgen sogar in unserem ruhigen und beschaulichen Ostthüringen für Angst und Schrecken. [...] Mit Angst in den Zug einzusteigen, weil man an die schrecklichen Morde von Brokstedt denken muss? Erinnerungen an das verheerende Messergemetzel von Gera, das einen jungen Mann für immer gezeichnet hat? An mir gehen diese Schlagzeilen nicht spurlos vorbei. Die Grenzen müssen kontrolliert und geschützt werden und nicht jeder darf ungehindert in unser Land, in unsere Sozialsysteme einwandern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 289

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