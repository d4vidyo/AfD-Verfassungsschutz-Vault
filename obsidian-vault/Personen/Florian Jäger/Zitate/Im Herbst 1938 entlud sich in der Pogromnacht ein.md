---
type: zitat
speaker: "[[Florian Jäger]]"
date: 2021-12-06
topic: Menschenwürde
page_bfv: 525
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Florian Jäger]] vom 6.12.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Im Herbst 1938 entlud sich in der Pogromnacht ein sogenannter Volkszorn gegen Juden im Deutschen Reich. Jüdische Geschäfte wurden geplündert, Synagogen in Brand gesteckt und unzählige Juden wurden misshandelt und ermordet. Jedoch war dieser 'Volkszorn' nicht so spontan ausgebrochen, wie die nationalsozialistische Propagandamaschienerie behauptete. Aktuell wird nach bekanntem Muster ein Sündenbock für das katastrophale Politversagen der Regierenden gesucht und Söder hat ihn gefunden. Es ist der 'Ungeimpfte'.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 525

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