---
type: zitat
speaker: "[[Birgit Bessin]]"
date: 2023-12-15
topic: Menschenwürde
page_bfv: 266
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Birgit Bessin]] vom 15.12.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Nein zu #Kinderehen, (Gruppen)#Vergewaltigungen, #Genitalverstümmelung...Schluss mit der Unterdrückung von Frauen durch unkontrollierte #Massenmigration aus mittelalterlich anmutenden Gesellschaften von kulturfremden Menschen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 266

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