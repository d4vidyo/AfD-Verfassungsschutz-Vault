---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-07-16
topic: Menschenwürde
page_bfv: 210
source: 'www.heimatkurier.at'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 16.7.2023 veröffentlicht auf: 'www.heimatkurier.at'
> [!quote] Aussage
>Angesichts der staatlich betriebenen Ersetzungsmigration, die bereits heute dazu führt, dass unser Land immer weniger Heimat ist, kann sich niemand mehr ins Neutrale flüchten. Die Frage ist unausweichbar: Deutschland aufgeben oder um das Erbe unserer Vorfahren kämpfen? Und damit für jeden Einzelnen: Teil des Problems zu sein oder der Lösung? Politik ist wieder da, als Kampf um die eigene kollektive Existenz.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 210

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