---
type: zitat
speaker: "[[Roman Kuffert]]"
date: 2024-04-07
topic: Demokratieprinzip
page_bfv: 632
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Roman Kuffert]] vom 7.4.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Zensur, Diffamierung, Repressalien. Schlimmer als in der DDR. Es ist nämlich - da könnte ich die Frage stellen: ein Bevölkerungsaustausch? Weil wir haben im Grunde genommen eins, was wir erleben. Wir haben den Krieg mittels Migrationswaffe gegen uns, gegen das deutsche Volk.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 632

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