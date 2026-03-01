---
type: zitat
speaker: "[[Stephan Protschka]]"
date: 2021-08-13
topic: Menschenwürde
page_bfv: 527
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Stephan Protschka]] vom 13.8.2021 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ich bin Jetzt ein Mensch zweiter Klasse, ich bin #Ungeimpf. Muss ich jetzt irgend eine Armbinde tragen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 527

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