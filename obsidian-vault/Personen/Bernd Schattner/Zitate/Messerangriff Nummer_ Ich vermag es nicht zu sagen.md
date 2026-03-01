---
type: zitat
speaker: "[[Bernd Schattner]]"
date: 2022-11-07
topic: Menschenwürde
page_bfv: 294
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Bernd Schattner]] vom 7.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Messerangriff Nummer? Ich vermag es nicht zu sagen. Es sind einfach zu viele. Zigtausende Messerangriffe in den letzten Monaten und Jahren. [...]. Die Barbarei tobt und Polizei und Medien sehen vorsätzlich angestrengt weg. Man mag sich gar nicht vorstellen, was diese Menschen im Falle eines längeren Stromausfalls, eines Blackouts, anrichten, wenn Polizei und Rettungskräfte nicht gerufen werden können... Zum Schutz unserer Bürger und zur Wahrung unserer Identität dürfen wir uns nicht damit abfinden, dass das jetzt die neue Kultur ist, mit der wir bereichert werden sollen. Diese Abschlachtungsszenen dürfen keine Normalität werden. Die Bundesregierung muss endlich dafür sorgen, dass es für kriminelle Ausländer keinerlei Anreize mehr gibt zu uns zu kommen. Harte Strafen müssen schnell und konsequent durchgesetzt werden - die Kuscheljustiz gegenüber Ausländern muss ein Ende haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 294

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