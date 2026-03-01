---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-24
topic: Demokratieprinzip
page_bfv: 967
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 24.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Die Kartellparteienpolitiker, die haben Deutschland, obwohl wir noch gar nicht im Krieg stehen, Gott sei Dank noch nicht im Krieg stehen mit Russland, sie haben Deutschland in den letzten Jahren und Jahrzehnten zu einem killing field im Frieden gemacht. [...] Die Deutschen sind in den letzten Jahren und Jahrzehnten vom politmedialen Establishment in Deutschland in Angst und Schuld gehalten worden. Und wenn sie nicht langsam wach werden, wenn sie nicht langsam den aufrechten Gang lernen, dann wird von ihnen schon in Bälde nichts mehr übrig sein [...]. Ich kann die Namen nicht mehr aufzählen, die unschuldig in den letzten Jahren ums Leben gekommen sind durch eine verfehlte Politik der offenen Grenzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 967

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