---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-06-17
topic: Demokratieprinzip
page_bfv: 603
source: 'Gast-Kommentar auf www.info-direkt-eu'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 17.6.2023 veröffentlicht auf: 'Gast-Kommentar auf www.info-direkt-eu'
> [!quote] Aussage
>Doch ihr Opfergeist war vergebens, wenn wir zulassen, dass sich die heutige Tyrannis zwar in bunte Farben hüllt, aber gleichsam düster gegen Andersdenkende vorgeht. Wenn all jenes Aufbegehren, welches den Geist des 17. Junis atmet - sei es der Widerstand gegen das Corona-Regime oder die anhaltende Ersetzungsmigration - ungestraft, so wie damals als faschistisch abgetan wird. Wenn erfolgreiche Oppositionspolitiker in Schauprozessen angeklagt werden, weil sie lediglich mit Worten für eine bessere Heimat streiten; ja dann wird es Zeit für ein neuerliches Aufbegehren. Dann müssen sich die Schwachen erneut verbinden und die Machtfrage stellen. Dann muss sich der demokratische Widerstand wieder unter Schwarz- Rot-Gold versammeln.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 603

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