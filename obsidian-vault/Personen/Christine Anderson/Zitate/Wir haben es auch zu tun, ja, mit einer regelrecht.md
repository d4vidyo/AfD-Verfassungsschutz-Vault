---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2023-03-25
topic: Menschenwürde
page_bfv: 386
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 25.3.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir haben es auch zu tun, ja, mit einer regelrechten Dekonstruktion unserer Gesellschaft. Und jetzt spreche ich von dem Import von Millionen von kulturfremden, jungen, wehrfähigen Männern. Genau die kommen jetzt, und da kann man wirklich sagen: Auf dem Altar von Toleranz und Nächstenliebe wird unsere gleichberechtigte, offene, demokratische Gesellschaft geopfert. [...] Na ja, und dann waren sie halt mal da, ne? Die Flüchtlinge, die Goldstücke, unsere Rente sollten sie ja bezahlen. [...] Aber der absolute Hammer, das muss ich wirklich sagen, war, als ich gelesen habe: 'Kurse zum richtigen Benutzen der Toilette'. Und da habe ich dagesessen, da habe ich gedacht: 'Was – noch nicht mal scheißen können sie. Aber meine Rente wollen sie bezahlen, im Leben nicht!' Und deswegen, meine Damen und Herren, auch bei diesem Thema bleibt es dabei: Es ist noch kein Meister vom Himmel gefallen und aus dem Asylanten-Himmel werden erst recht keine fallen. Das steht fest.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 386

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