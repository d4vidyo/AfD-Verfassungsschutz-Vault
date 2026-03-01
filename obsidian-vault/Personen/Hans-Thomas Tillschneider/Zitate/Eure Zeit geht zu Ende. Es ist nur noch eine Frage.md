---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-11-14
topic: Demokratieprinzip
page_bfv: 609
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 14.11.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Eure Zeit geht zu Ende. Es ist nur noch eine Frage der Zeit, bis euer Regime endet.

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