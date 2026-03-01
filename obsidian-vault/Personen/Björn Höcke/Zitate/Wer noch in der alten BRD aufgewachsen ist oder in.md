---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-12-21
topic: Menschenwürde
page_bfv: 882
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 21.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wer noch in der alten BRD aufgewachsen ist oder in der DDR, der wird sich eingestehen müssen, daß er sein Heimatland nicht wiedererkennen kann. Alle Gewißheiten sind in Frage gestellt, alles ist ins Rutschen geraten: Wo sind unsere Werte, wo unsere Vertrauensgemeinschaft, wo ist das Deutschland, auf das die Welt bewundernd schaute? Wir müssen eingestehen: von ihm, von uns ist kaum noch etwas da. Reicht die Restsubstanz noch, um neu zu beginnen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 882

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