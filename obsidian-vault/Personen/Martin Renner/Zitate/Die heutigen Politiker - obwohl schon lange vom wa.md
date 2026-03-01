---
type: zitat
speaker: "[[Martin Renner]]"
date: 2021-11-11
topic: Menschenwürde
page_bfv: 371
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 11.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die heutigen Politiker - obwohl schon lange vom wahren christlichen Glauben abgefallen - benutzen regelmäßig die Mantelteilung des Heiligen um Barmherzigkeitund Nächstenliebe gegenüber den in unser Land hereinbrechenden Migranten von den Bürgern einzufordern. Aber dieser Ansatz ist grundsätzlich verlogen, schief und in die Irre führend. [...] Auch und gerade in Zeiten der Invasoren-Problematik der neuerlich hierher Hereindrängenden. Mitmenschlichkeit ist und bleibt eine individuelle Angelegenheit und kein staatlich aufgeplusterter und durch Scheinargumente vorgetragener Popanz, der die christlich begründete Pflicht zur Eigenvorsorge und Eigenverantwortung des Individuums, seiner Familie und auch seiner Gemeinde - auch Subsidiarität genannt - negiert und auch zerstören will. Aus welchen Gründen auch immer.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 371

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