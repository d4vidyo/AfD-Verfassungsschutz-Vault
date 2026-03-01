---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2022-06-23
topic: Demokratieprinzip
page_bfv: 622
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 23.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Unsere Befürchtung ist heute leider war geworden und der "Grundrechte Bezugsschein" - eine Bezeichnung die ich hier als wesentlich treffender erachte - wurde um ein weiteres Jahr bis Juni 2023 verlängert. Ich habe selbstverständlich zusammen mit einigen Mitstreitern dagegen gestimmt, jedoch war dem Durst der Mehrheit der EU-Abgeordneten nach weiteren Möglichkeiten zur Einschränkung von Bürgerfreiheit und Grundrechten nicht mehr beizukommen. [...] Zu sehr hat man Gefallen daran gefunden, den Bürgern unter dem Vorwand der vermeintlichen "Gesundheitsfürsorge" die Grundrechte entziehen und bei regierungsfreundlichem Wohlverhalten ggf. wiedergewähren zu können, ganz so als handle es sich um Privilegien. Genießen Sie einen letzten Sommer der Freiheit. Ist er erst vorbei, wird uns allen wohl ein weiterer pLandemischer (sic) Herbst und Winter vor der Tür stehen! Aber eines ist jetzt schon sicher: Unser Kampf für die Freiheit wird weitergehen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 622

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