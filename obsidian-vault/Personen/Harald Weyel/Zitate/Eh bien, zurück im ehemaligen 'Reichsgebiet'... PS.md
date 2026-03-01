---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2023-09-01
topic: Nationalsozialismus
page_bfv: 691
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom 1.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Eh bien, zurück im ehemaligen 'Reichsgebiet'... PS: Ob nun Rückkehrversuche über Gottard Tunnel oder Paß: Überall schaffen es dilettierende 'gewerbliche Verkehrsteilnehmer' ihre Fahrzeuge trocken zu fahren oder ihre Anhänger umzukippen! PPS: So schon auf der Hinfahrt ein poln. Kleinlaster. Dergleichen sollte doch sofort in allfällige neue #Reparationsverhandlungen einbezogen werden, oder?!!! ;))

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 691

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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