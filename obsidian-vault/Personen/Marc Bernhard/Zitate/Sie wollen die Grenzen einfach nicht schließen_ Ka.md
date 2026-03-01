---
type: zitat
speaker: "[[Marc Bernhard]]"
date: 2025-01-31
topic: Demokratieprinzip
page_bfv: 965
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Marc Bernhard]] vom 31.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Sie wollen die Grenzen einfach nicht schließen: Kartellparteien zerstören Deutschland! Das heutige pseudo-"demokratische" Schauspiel ist vorbei. Angesichts der täglichen Messerübergriffe, Gruppenvergewaltigungen und Toten war dieses Gerangel mehr als nur unwürdig für unser Parlament. Nicht die Sicherheit und das Leben der Menschen, sondern "Brandmauern" und Wahlkampftaktik spielen für die Kartellparteien offenkundig die wichtigste Rolle. Das "Zustrombegrenzungsgesetz" hat bloß rein kosmetischen Charakter, doch nicht einmal diesen minimalen Schritt sind die Deutschlandzerstörer bereit, zu gehen. Die absurde Debatte über dieses Gesetz beweist, dass die Altparteien unsere Grenzen nicht schützen wollen. Grüne, FDP, SPD, Linke und CDU sind klar unwählbar. Diese Antidemokraten haben heute eindrücklich unter Beweis gestellt, dass sie nicht das Wohle Deutschlands und das der Bürger im Sinne haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 965

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