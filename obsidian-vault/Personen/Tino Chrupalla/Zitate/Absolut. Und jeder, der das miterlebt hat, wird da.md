---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2024-01-21
topic: Demokratieprinzip
page_bfv: 598
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 21.1.2024 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Absolut. Und jeder, der das miterlebt hat, wird das bestätigen. Nun sagen viele Politiker, das darf man nicht und äh, kann man nicht vergleichen. Das kann man sehr wohl vergleichen. Wenn man die Sprechverbote, die Meinungsverbote, wenn man auch teilweise die Arbeitsverbote, die es ja gibt, wie Menschen aus dem öffentlichen Dienst gedrängt werden, nur weil sie AfD-Mitglied sind, oder wenn sie Positionen vertreten, das erleben Sie ja ähnlich in der Medienlandschaft, wenn man Positionen vertritt, die einfach nicht regierungskonform sind, ist man ganz schnell Rechtsextremist, schlimmstenfalls noch Nazi.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 598

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