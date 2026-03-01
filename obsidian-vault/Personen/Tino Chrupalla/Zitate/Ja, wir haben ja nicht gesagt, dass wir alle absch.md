---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2024-09-23
topic: Menschenwürde
page_bfv: 409
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 23.9.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Ja, wir haben ja nicht gesagt, dass wir alle abschieben wollen. [...] Bitte, eine Überspitzung eines Textes, den auch noch so zu bezeichnen, dass wir damit meinen, alle abzuschieben. Wir wollen die abschieben, die in diesem Land nichts zu suchen haben. Das haben wir ja immer wieder deutlich gemacht und das sind diejenigen, die nicht bleibeberechtigt sind, die ja auch keinen Asylgrund mehr haben, und da reden wir ja auch von 250.000 mindestens. Also das ist der Grund, warum wir sagen, dass die sofort abgeschoben gehören.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 409

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