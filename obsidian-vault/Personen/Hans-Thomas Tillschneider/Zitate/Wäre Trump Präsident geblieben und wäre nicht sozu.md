---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-07-30
topic: Menschenwürde
page_bfv: 509
source: 'Podiumsdiskussion'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 30.7.2022 veröffentlicht auf: 'Podiumsdiskussion'
> [!quote] Aussage
>Wäre Trump Präsident geblieben und wäre nicht sozusagen diese giftige Sprechpuppe der Globalisten, Biden, Präsident geworden, hätten wir in der Ukraine keinen Krieg gesehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 509

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