---
type: zitat
speaker: "[[Gunnar Beck]]"
date: 2022-08-12
topic: Menschenwürde
page_bfv: 208
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gunnar Beck]] vom 12.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Während die EU-Gesamtbevölkerung das zweite Jahr in Folge zurückging, wurden Bevölkerungsrückgänge nur in 10 Mitgliedstaaten gemeldet. Deutschlands Bevölkerung wächst rasant. Deutschland hat im letzten Jahr netto 228.195 Deutsche verloren, aber netto 310.228 Migranten hinzugewonnen. Das ist ein Drittel aller Migranten in der EU. Mit dem Begriff Ersatzmigration müssen wir vorsichtig sein, aber die Daten sprechen für sich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 208

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