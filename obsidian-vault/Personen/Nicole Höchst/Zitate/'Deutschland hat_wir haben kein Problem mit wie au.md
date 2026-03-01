---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2022-11-10
topic: Menschenwürde
page_bfv: 316
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 10.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>'Deutschland hat/wir haben kein Problem mit wie auch immer gearteter Fremdenfeindlichkeit, wir haben ein Problem mit feindlichen Fremden und einer Regierung, die zu Toleranzerzwingungszwecken mittlerweile über 1 Milliarde Euro aufwendet'. [...] Umgekehrt wird ein Schuh draus: wer bemäntelt, verharmlost und das Problem von sich weg weist, liefert in Wahrheit die Bürger ihren Schlächtern aus.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 316

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