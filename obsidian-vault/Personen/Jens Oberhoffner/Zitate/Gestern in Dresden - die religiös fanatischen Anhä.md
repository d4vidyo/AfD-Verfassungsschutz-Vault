---
type: zitat
speaker: "[[Jens Oberhoffner]]"
date: 2024-04-11
topic: Menschenwürde
page_bfv: 465
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jens Oberhoffner]] vom 11.4.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gestern in Dresden - die religiös fanatischen Anhänger des Islam untermauern ihren Herrschaftsanspruch. Auch in den ostdeutschen Bundesländern macht sich diese Gefahr immer weiter breit. Darüber täuscht auch keine staatlich verordnete Ablenkungsmedienkampagne á la Correctiv und ,Nie wieder ist jetzt' mehr hinweg. Die Faktenlage ist eindeutig - man muss nur mit offenen Augen und klarem Verstand durch das Land gehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 465

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