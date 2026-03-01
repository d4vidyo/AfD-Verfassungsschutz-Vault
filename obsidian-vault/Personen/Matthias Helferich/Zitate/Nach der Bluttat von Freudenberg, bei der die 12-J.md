---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-03-23
topic: Menschenwürde
page_bfv: 271
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 23.3.2023 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Nach der Bluttat von Freudenberg, bei der die 12-Jährige Luise F. mutmaßlich von zwei gleichaltrigen Schulkameradinnen mit mehreren Messerstichen ermordet wurde, wird Deutschland von einer weiteren Gewalttat unter Jugendlichen erschüttert Doch statt in diesem Fall Ross und Reiter klar zu benennen, eröffnet die bundesdeutsche Öffentlichkeit in üblicher Manier eine Scheindebatte um die Herabsetzung des Strafmündigkeitsalters. Ähnlich der hauptsächlich von Migranten ausgelösten Silvesterkrawalle, als man ein allgemeines Böllerverbot forderte, wird auch hier die Problemstellung bewusst verkürzt. wenn auch grundsätzlich eine Herabsetzung vonnöten wäre. Denn zahllose Gewaltdelikte, Silvesterkrawalle, Angriffe auf Lehrer und Kriminalstatistiken machen klar: junge Migranten sind häufig ein Sicherheitsrisiko.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 271

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