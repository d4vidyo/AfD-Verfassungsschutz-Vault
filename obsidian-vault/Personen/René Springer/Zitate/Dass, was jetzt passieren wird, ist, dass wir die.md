---
type: zitat
speaker: "[[René Springer]]"
date: 2024-12-17
topic: Sonstiges
page_bfv: 861
source: 'Phoenix'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 17.12.2024 veröffentlicht auf: 'Phoenix'
> [!quote] Aussage
>Dass, was jetzt passieren wird, ist, dass wir die Jugendorganisation im Grunde stärken, sie wird größer werden, sie wird mehr Mitglieder haben, sie wird auch besser finanziell ausgestattet werden. Und insofern ist das eigentlich eine win-win-Situation für alle Beteiligten nämlich für die heutigen Jugendlichen, die sich [...] in der JA engagieren, aber eben auch für die Bundes-AfD, die jetzt ein Konzept hat, das die Junge Alternative auch schützt vor der übergriffigen Nancy Faeser. Denn wir wissen ja, mit Verbotsforderungen wird ja um sich geworfen. [...] Wir wollen verhindern, dass eine übergriffige Innenministerin unsere Jugendorganisation verbietet. Und jetzt haben wir sie unter den Schutzschirm der Partei genommen, und insofern ist das für alle ein großartiger Erfolg.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 861

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