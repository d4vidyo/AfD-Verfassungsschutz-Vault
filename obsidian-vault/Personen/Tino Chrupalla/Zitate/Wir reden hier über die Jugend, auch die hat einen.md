---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2024-09-23
topic: Sonstiges
page_bfv: 841
source: 'Pressekonferenz'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 23.9.2024 veröffentlicht auf: 'Pressekonferenz'
> [!quote] Aussage
>Wir reden hier über die Jugend, auch die hat einen sehr tollen Wahlkampf gemacht hier in Brandenburg mitgeleistet, auch im Übrigen in den anderen Landtagswahlkämpfen, und auch sie hat das Recht, ausgelassen zu feiern. Ja, und ich meine, es wurde ja erst schon gesagt, sie haben ein Lied gesungen, was in keinster Weise, in irgendeiner Art verboten ist oder auf einem, irgendeinem Index steht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 841

**Verfassungsschutz Kategorisierung:** Sonstiges.

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