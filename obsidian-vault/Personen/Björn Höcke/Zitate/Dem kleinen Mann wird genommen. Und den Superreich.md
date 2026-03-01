---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-03-30
topic: Nationalsozialismus
page_bfv: 692
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 30.3.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Dem kleinen Mann wird genommen. Und den Superreichen wird gegeben. Es geht darum, das Geld aus euren Taschen rauszuholen und denen zu geben, die schon mehr als genug haben. Dieser Politikansatz wird von jeder dieser Altparteien genau so gewollt. Und genauso umgesetzt. Er ist schändlich, er ist verwerflich, er ist volksschädlich und Volksschädigung muss endlich enden, liebe Freunde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 692

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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