---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2024-09-23
topic: Menschenwürde
page_bfv: 409
source: 'Pressekonferenz'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 23.9.2024 veröffentlicht auf: 'Pressekonferenz'
> [!quote] Aussage
>Ich meine, Herr Springer hat es ja richtigerweise gesagt. Wir reden hier über die Jugend, auch die hat einen sehr tollen Wahlkampf hier in Brandenburg mit geleistet, auch im Übrigen in den anderen Landtagswahlkämpfen, und auch sie hat ein Recht ausgelassen zu feiern. Ja, und ich meine, es wurde ja erst schon gesagt, sie haben ein Lied gesungen, was in keinster Weise in irgendeiner Art verboten ist oder auf einem irgendeinem Index steht. [...] Es ist die Jugend, die auch beteiligt war, die auch gestern bei der Wahlfeier mit dabei war und ich sehe da aktuell zumindest nichts Anstößiges.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 409. Im Fließtext des Gutachtens ist auch von einem Interview die Rede.

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