---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-12-02
topic: Menschenwürde
page_bfv: 239
source: 'Beitrag auf christina-baum.berlin'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 2.12.2022 veröffentlicht auf: 'Beitrag auf christina-baum.berlin'
> [!quote] Aussage
>Die Zahl der indigenen Deutschen sinkt seit Jahren, während die Zahl der Ausländer beständig steigt. [...] Dass der Deutsche im eigenen Land zur aussterbenden Rasse gehört, dafür sorgt die Bundesregierung verstärkt mit illegaler Massenmigration, schnellster Einbürgerung und loser Rundumversorgung. Auf kurz oder lang werden wir Deutsche also zur Minderheit in unserer angestammten, seit vielen Jahrhunderten von unseren Vorfahren bewohnten Heimat werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 239

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