---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-09-16
topic: Demokratieprinzip
page_bfv: 552
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 16.9.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Zwei Jahre später, 1949, wurde dann die NATO gegründet, von der niemand anders als ihr erster Generalsekretär höchstselbst so treffend gesagt hat, der Zweck sei, die Amerikaner drinnen, die Russen draußen und die Deutschen unten zu halten. Die Amerikaner drinnen in Europa, die Russen draußen, die Deutschen unten. Und das ist bis heute das Programm der NATO. Preußen dagegen, Preußen dagegen bedeutet, dass die Deutschen oben, die Russen drinnen und die Amerikaner draußen sind. Preußen bedeutet: Raus aus der NATO!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 552

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