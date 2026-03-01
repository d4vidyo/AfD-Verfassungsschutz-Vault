---
type: zitat
speaker: "[[Dirk Spaniel]]"
date: 2024-08-07
topic: Menschenwürde
page_bfv: 288
source: 'dirkspaniel.de'
status: Unbewertet
---

# Zitat: [[Dirk Spaniel]] vom 7.8.2024 veröffentlicht auf: 'dirkspaniel.de'
> [!quote] Aussage
>Und täglich grüßt der Messermann Das Messer als Vorbote des zivilisatorischen Zusammenbruchs [...] Die kulturelle Bereicherung und Vielfalt der Gewalt lässt und erschaudern. [...] Und der Haifisch, der hat Zähne Und die trägt er im Gesicht Und Mohammed, der hat ein Messer Doch das Messer sieht man nicht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 288. als Gedicht verfasst

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