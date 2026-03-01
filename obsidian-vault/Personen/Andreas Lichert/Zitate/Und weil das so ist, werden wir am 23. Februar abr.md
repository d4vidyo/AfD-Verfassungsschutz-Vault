---
type: zitat
speaker: "[[Andreas Lichert]]"
date: 2025-01-01
topic: Nationalsozialismus
page_bfv: 983
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Andreas Lichert]] vom 1.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und weil das so ist, werden wir am 23. Februar abräumen. Und weil wir die beste Kandidatin haben. Du bist nicht nur die Kanzlerin der Herzen und der Hirne. Am 23. Februar wirst du die Kanzlerin aller Deutschen! Alice für Deutschland!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 983

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