---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-10-30
topic: Demokratieprinzip
page_bfv: 629
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 30.10.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wer die Bundesrepublik Deutschland im Brustton der Überzeugung als Demokratie (Volksherrschaft) bezeichnet, lebt entweder von ihr oder ist nicht im Vollbesitz seiner geistigen Kräfte. Diese harte Aussage ist mit Blick auf das, was wir hierzulande vorfinden richtig und wichtig: Gebrochene Gewaltenteilung, Kartellbildung der Altparteien, Parteibuchgerichte, staatliche und halbstaatliche Propagandaproduktion, Herrschaft der politischen Korrektheit, Geheimdiensteinsatz gegen friedliche Opposition, Eingriff von in- ausländischen NGOs in den Meinungsbildungsprozeß, Mediatisierung und Manipulation des Volkes, ja, letztlich Zerstörung des Demos (Volkes) durch Multikulturalisierung...

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 629

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