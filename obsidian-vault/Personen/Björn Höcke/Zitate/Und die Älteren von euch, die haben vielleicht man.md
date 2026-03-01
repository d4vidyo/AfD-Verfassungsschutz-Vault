---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Menschenwürde
page_bfv: 148
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und die Älteren von euch, die haben vielleicht manchmal auch so ein wenig ostalgische Gefühle. Also nicht nostalgische Gefühle, sondern ostalgische Gefühle. Und versteht mich jetzt nicht falsch, wir sind uns einig darüber, dass die DDR ein Unrechtsstaat war und dass sie eine Diktatur war. [...] Aber als Privatperson konnte man in diesem Staat innere Sicherheit erleben. Man konnte in diesem Staat soziale Sicherheit erleben. Man konnte in diesem Staat gelebte Nachbarschaft erleben. Und man durfte in einem deutschen Staat als Deutscher leben. [...] Und alles das steht heute in der Bundesrepublik Deutschland des Jahres 2024 zur Disposition. Alles das, was die Älteren von euch an der DDR dann vielleicht doch im Privaten geschätzt haben. Die innere Sicherheit zerfällt, der Sozialstaat wird zur Plünderung freigegeben. Unser Volk ist mittlerweile im gefährlichen Maße multikulturalisiert und überfremdet und droht zur Minderheit im eigenen Land zu werden. Wir verlieren gerade unsere Heimat, liebe Freunde! Und Heimat verliert man nicht nur durch Flucht und Vertreibung, wie das meine Großeltern erleiden mussten und eure Großeltern und Eltern erleiden mussten. Heimat verliert man auch dadurch, dass man zur Minderheit im eigenen Land wird. Und auf diesem schlechten Weg sind wir gerade unterwegs. Aber diesen Weg werden wir für Thüringen und Sachsen morgen beenden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 148

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