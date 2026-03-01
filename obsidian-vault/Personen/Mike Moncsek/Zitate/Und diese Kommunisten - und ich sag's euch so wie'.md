---
type: zitat
speaker: "[[Mike Moncsek]]"
date: 2021-08-19
topic: Demokratieprinzip
page_bfv: 590
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Mike Moncsek]] vom 19.8.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und diese Kommunisten - und ich sag's euch so wie's ist - diese Einheitspartei, die auch heute wieder regiert - alle zusammen, das ist genau die gleiche Situation, die wir '89 hatten. Und wir werden es diesmal selber wieder hier von Sachsen aus machen. Bloß diesmal machen wir's selber. [...] Die Sachsen sind schlau. Wir sind diejenigen, die ein ganzes Regime, eine ganze Regierung demokratisch - ohne Waffen, ohne Gewalt - davongejagt haben. Und so wie's Honecker gegangen ist, wird's auch denjenigen gehen, die uns heute auf der Nase rumtanzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 590

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