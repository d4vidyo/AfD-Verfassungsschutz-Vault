---
type: zitat
speaker: "[[René Springer]]"
date: 2023-04-26
topic: Sonstiges
page_bfv: 839
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 26.4.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Keine der betroffenen Organisationen [Anm.: JA, IfS, EinProzent] ist rechtsextrem. Es geht darum, den Höhenflug der AfD zu stoppen. Dieser verzweifelte Schritt macht das "Schwert" #Verfassungsschutz nur noch stumpfer. Wenn unser Rechtsstaat noch funktioniert, werden Gerichte diese Entscheidung aufheben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 839

**Verfassungsschutz Kategorisierung:** Sonstiges.

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