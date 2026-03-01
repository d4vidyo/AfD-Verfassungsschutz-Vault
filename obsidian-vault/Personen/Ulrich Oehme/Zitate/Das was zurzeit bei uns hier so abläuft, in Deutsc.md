---
type: zitat
speaker: "[[Ulrich Oehme]]"
date: 2023-06-19
topic: Demokratieprinzip
page_bfv: 604
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Ulrich Oehme]] vom 19.6.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Das was zurzeit bei uns hier so abläuft, in Deutschland, in Europa, ist für mich ein sozioökonomisches, soziosozialistisches Experiment. Glauben sie mir, ich weiß was Sozialismus bedeutet. Sozialismus ist Kollektivismus statt Individualismus, ist Gleichheit statt Vielfalt, ist die Abschaffung von Privateigentum. Klaus Schwab hat uns schon gesagt: 'lhr werdet nichts besitzen und ihr werdet glücklich sein'. Es bedeutet Angriff auf die Familie, denn die Familie ist der Hort der Geborgenheit und der Staat hat wenig Zugriff [...] Alles ist im Kampf gegen die Familie. [...] Zwischen dem 17. Juni '53 und '89 sind einige Jahrzehnte vergangen. Und von 89 bis jetzt sind wieder einige Jahrzehnte vergangen. Und wir müssen feststellen, wir haben uns im Kreis gedreht. Wir haben eine 360 Gradwendung gemacht. Wieder haben wir Planwirtschaft, Verbote, Spaltung der Gesellschaft. Nein das brauchen wir nicht. Was wir brauchen [...] das ist Einheit, das ist Freiheit. 'Teile und herrsche' ist das System des Totalitarismus. Wenn wir einig sind, wenn Deutschland sich einigt, wenn der 17. Juni wieder der Feiertag der Deutschen wird, der Tag, der vom Volk kommt, der auf derStraße seine Opfer gefunden hat, der erlitten, der erkämpft wurde. Dann werden die jetzigen Machthaber keine Macht mehr über uns haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 604

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