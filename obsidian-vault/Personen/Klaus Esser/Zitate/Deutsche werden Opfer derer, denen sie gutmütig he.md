---
type: zitat
speaker: "[[Klaus Esser]]"
date: 2022-07-28
topic: Menschenwürde
page_bfv: 139
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Klaus Esser]] vom 28.7.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Deutsche werden Opfer derer, denen sie gutmütig helfen wollten! Eine Auswertung des BKA hat ergeben, dass legale und illegale Asylzuwanderer weit mehr Gewaltverbrechen an Deutschen begehen als andersherum. Das Missverhältnis wird sowohl bei Tötungsdelikten als auch bei Sexualverbrechen und anderen Gewalttaten offenkundig. Würde zusätzlich noch differenziert, wie lange Täter mit deutschem Pass bereits die Staatsbürgerschaft besitzen, wäre das Bild wahrscheinlich noch eindringlicher.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 139

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