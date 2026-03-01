---
type: zitat
speaker: "[[Petr Bystron]]"
date: 2022-12-19
topic: Sonstiges
page_bfv: 724
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Petr Bystron]] vom 19.12.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Das COMPACT-Team trägt hier alle bekannten Fakten und Indizien für eine Täterschaft – und überraschenderweise liegen die Beweise nicht auf der Seite Russlands, wie uns das durch die Mainstream-Medien anfangs ohne jegliche Belege nahegelegt wurde, sondern es verhärtet sich der Verdacht, dass dieser Angriff von einer befreundeten Macht verübt wurde. [...] Die Wahrheit würde das Staatswohl gefährden. Was für ein Staatswohl ist das denn? Womöglich eins, das darauf aufgebaut ist, dass wir alle in einer Lüge leben müssen! Deswegen ist es eine große Leistung vom Team COMPACT. Diese Dokumentation deckt auf nicht nur Fakten zur Zerstörung von Nord Stream, sondern auch das totale Versagen der journalistischen Kaste in Deutschland. Denn bei so einer Situation müssten tatsächlich alle investigativen Medien recherchieren, hart dranbleiben und uns die Wahrheit präsentieren. Und das tut hier nur das COMPACT-Magazin. Kompliment dafür!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 724

**Verfassungsschutz Kategorisierung:** Sonstiges.

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