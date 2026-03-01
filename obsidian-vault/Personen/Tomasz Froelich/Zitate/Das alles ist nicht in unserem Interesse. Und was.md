---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2023-07-30
topic: Demokratieprinzip
page_bfv: 568
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 30.7.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Das alles ist nicht in unserem Interesse. Und was mich besonders aufregt, das ist die Heuchelei der Kartellparteien, die diese Politik vorantreiben. Sie sind feige, verlogen und gefährlich. [...] Denn diese EU ist so tief im woken Sumpf versunken, dass sie als ernstzunehmender außenpolitischer Faktor ausscheidet. Sie suhlt sich in einer Dekadenz, die man bestenfalls noch als linksliberale Wohlstandsverwahrlosung bezeichnen könnte.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 568

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