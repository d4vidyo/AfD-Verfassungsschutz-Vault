---
type: zitat
speaker: "[[Stephan Protschka]]"
date: 2024-02-22
topic: Demokratieprinzip
page_bfv: 580
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Stephan Protschka]] vom 22.2.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>\<Bild 1933 darf sich nicht wiederholen! Bürger wurden von den Nationalsozialisten diffamiert Andersdenkende wurden verraten Die Medien wurden kontrolliert Meldestellen wurden eingerichtet Das Volk wurde gespalten Parteien wurden verboten\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 580

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