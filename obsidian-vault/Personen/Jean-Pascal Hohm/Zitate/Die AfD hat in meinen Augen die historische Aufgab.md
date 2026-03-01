---
type: zitat
speaker: "[[Jean-Pascal Hohm]]"
date: 2024-03-25
topic: Menschenwürde
page_bfv: 162
source: 'Heimatkurier'
status: Unbewertet
---

# Zitat: [[Jean-Pascal Hohm]] vom 25.3.2024 veröffentlicht auf: 'Heimatkurier'
> [!quote] Aussage
>Die AfD hat in meinen Augen die historische Aufgabe, Deutschland als Heimat der Deutschen zu bewahren. Wer will, dass Deutschland als Land der Deutschen eine Zukunft hat, muss AfD wählen. Mit dieser Botschaft werde ich in den Wahlkampf gehen und ich bin optimistisch, dass der Selbstbehauptungswille - besonders in unserer Region - noch groß genug ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 162

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