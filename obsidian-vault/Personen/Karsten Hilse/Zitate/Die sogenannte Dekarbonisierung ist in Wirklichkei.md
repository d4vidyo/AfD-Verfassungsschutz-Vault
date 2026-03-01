---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2024-02-22
topic: Demokratieprinzip
page_bfv: 637
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 22.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die sogenannte Dekarbonisierung ist in Wirklichkeit eine Deindustrialisierung Deutschlands. Und diese sukzessive Zerstörung Deutschlands erfolgt auch nicht aus Dummheit, sondern in böswilliger Absicht. Wie jeder normaldenkende Bürger in Deutschland weiß, haben die meisten Grünen Kommunisten weder einen Berufs- noch einen Studienabschluss und laufen Ihnen und Ihresgleichen wie geistig minderbemittelte Claqueure hinterher. Sie sind von Hass auf Deutschland zerfressen und haben zum Ziel, unser Deutschland bis zur Unkenntlichkeit zu transformieren, gelenkt von Sozialisten aus Brüssel und Washington, seiner Seele, seiner Identität und seiner Wirtschaftskraft beraubt. Die einzige Partei, die Ihnen bei der Umsetzung Ihres perfiden Plans noch im Weg steht, ist die AfD.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 637

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