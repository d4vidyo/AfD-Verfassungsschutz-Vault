---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-10-15
topic: Menschenwürde
page_bfv: 219
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 15.10.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Aber eine Einwanderung, wie sie jetzt die Grüne Katrin Göring-Eckardt fordert, von 400.000 Menschen pro Jahr über 12 Jahre, also 4,8 Millionen [...], das ist keine Einwanderung mehr, das ist Ersetzungsmigration, das ist Großer Austausch, das ist Umvolkung, das wollen wir nicht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 219

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