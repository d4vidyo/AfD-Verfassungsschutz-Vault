---
type: zitat
speaker: "[[Lars Schieske]]"
date: 2023-04-27
topic: Sonstiges
page_bfv: 746
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Lars Schieske]] vom 27.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Jetzt erst recht! Der politisch gesteuerte #Verfassungsschutz befindet sich auf einem #lrrweg und dies ist äußerst besorgniserregend. Deutschlands größtes patriotisches #Bürgernetzwerk 'Ein Prozent' macht sich für all jene stark, die ihre #Heimat nicht kampflos einer politischen Elite von #Ideologen überlassen wollen. Es ist an der Zeit, dass jeder von uns Position bezieht und sich für das deutsche #Volk einsetzt. [...] Tritt auch du in den #Widerstand ein! [...] #fördermitglied

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 746

**Verfassungsschutz Kategorisierung:** Sonstiges.

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