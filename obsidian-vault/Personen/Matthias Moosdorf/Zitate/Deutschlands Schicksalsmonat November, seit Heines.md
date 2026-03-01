---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2023-11-21
topic: Demokratieprinzip
page_bfv: 584
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 21.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschlands Schicksalsmonat November, seit Heines 'Wintermärchen' geschichtsbelastet wie kein anderer, wird zum politischen Grabstein einer Regierung, die es so seit Adolf Nazi niemals wieder gab. [...] Dass diese Regierung eine von strukturellen Verfassungsbrechern ist, haben wir nun amtlich. [...] Und heute sind sich die Kleptokraten ohne ökonomisches Grundwissen bereits einig: Die Ausrufung einer weiteren Notlage für das Jahr 2023 fortfolgend, soll es richten. [...] Auf der Suche nach vergleichbarer Apokalypse muss man bis Weimar zurückgehen. Notstand, Rezession, explodierende Preise, Verarmung, wechselnde Regierungen. In diesem Kontext ist es fast folgerichtig, dass die Verbrecher ihre Kritiker zu verfolgen trachten und die einzige Partei, die ihnen seit ihrem Bestehen den Spiegel vor die Fratze hält, am liebsten verbieten möchten. Aber keine Angst: Noch ist Thomas Haldenwang kein Hermann Göring. Die Demokratie wird das diesmal überleben - und zwar mit unserer Hilfe!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 584

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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