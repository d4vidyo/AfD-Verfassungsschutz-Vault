---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-03-30
topic: Menschenwürde
page_bfv: 492
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 30.3.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>So wir stellen die Frage: Cui Bono? Wem nützt es? Wem nützt diese Corona Pandemie, diese Corona-Plandemie? Dem globalistischen Establishment, das gerade um sein Überleben kämpft. Denkt an das, was ich eingangs gesagt habe, Great Reset. Sie müssen irgendwie die Kontrolle behalten, die zu entgleiten droht. [...] Erst kommt die digitale Identität der Impfausweis wird auch digitalisiert, er ist Teil der digitalen Identität. Dann kommt die digitale Währung, und dann haben wir den gläsernen Bürger, der total überwacht ist. Und wenn ihr euch da nicht impfen lasst, beziehungsweise gentherapieren lasst, dann bekommt ihr eben kein Geld mehr. Das ist der Hintergedanke. Denn die Gentherapie, die von den Regierungen von ihr in Medien postuliert wird, ist letztlich nur dazu da, um eure Gefügigkeit auszutesten. Um eure Regierungstreue auszutesten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 492

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