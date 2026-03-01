---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2025-01-03
topic: Menschenwürde
page_bfv: 928
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 3.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Was soll denn die Antwort sein auf all das Blut von Einheimischen, was in unseren Innenstädten fließt? Die Antwort kann nur lauten: Remigration, millionenfache Remigration!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 928

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