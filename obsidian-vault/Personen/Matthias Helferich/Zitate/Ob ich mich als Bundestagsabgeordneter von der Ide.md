---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-10-27
topic: Sonstiges
page_bfv: 783
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 27.10.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Ob ich mich als Bundestagsabgeordneter von der Identitären Bewegung distanziere? Immerhin sagen die obersten Schlapphüte, dass die ganz böse sind. Da muss der SPIEGEL jemand anderes fragen, aber seht selbst!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 783. geteilt von Jan Wenzel Schmidt

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