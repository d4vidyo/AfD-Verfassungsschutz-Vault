---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2022-08-03
topic: Demokratieprinzip
page_bfv: 609
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 3.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ampel'-Regime siedelt 200 Afghanen um! Mittlerweile werden von der buntesten Regierung aller Zeiten sogar sogenannte afghanische 'Ortskräfte' nach Buntland ausgeflogen, die bereits vor ihrem Abflug einräumten, dass sie nie in Gefahr waren und nur 'ein besseres Leben' wollen. Die Umsiedlung von Teilen der afghanischen Bevölkerung ist insofern kein humanitärer Akt, sondern eine Art Kriegserklärung an den deutschen Steuerzahler

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 609

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