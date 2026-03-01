---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2024-01-17
topic: Menschenwürde
page_bfv: 184
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 17.1.2024 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Lächerliches Rückführungsgesetz. Jeder soll Deutscher werden. Man schafft sich ein neues Volk.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 184

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