---
type: zitat
speaker: "[[Gerhard Schenk]]"
date: 2025-02-12
topic: Demokratieprinzip
page_bfv: 962
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gerhard Schenk]] vom 12.2.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Zensur, Hausdurchsuchungen, Druck am Arbeitsplatz. Die Opposition ist einem immensen Verfolgungsdruck ausgesetzt. Nur so können anscheinend die Altparteien ihren Kurs der wirtschaftlichen und kulturellen Zerstörung weiterfortsetzen. Absicht? Unvermögen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 962

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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