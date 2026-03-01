---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-07-30
topic: Menschenwürde
page_bfv: 508
source: 'Podiumsdiskussion'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 30.7.2022 veröffentlicht auf: 'Podiumsdiskussion'
> [!quote] Aussage
>George Soros hat mit seinen Methoden, mit seinem Institut, mit seinen Netzwerken die Ukraine gedreht. Das wissen wir alle. Er hat den Leuten den Kopf verrückt gemacht. Die Erlösung läge im Westen und hat die Ukraine gedreht. Und damit wurde sozusagen die Ursache geschaffen für den Konflikt, den wir jetzt sehen und Russland war nicht in der Lage, ähnlich subtil und hintergründig zu arbeiten. [...] Also was Russland lernen muss, ist, dass es den Methoden, den Schutz des George Soros auf gleicher Ebene Paroli bietet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 508

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