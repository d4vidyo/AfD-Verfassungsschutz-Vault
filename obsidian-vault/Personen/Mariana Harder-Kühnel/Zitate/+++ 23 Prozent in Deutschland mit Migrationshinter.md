---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2023-03-06
topic: Menschenwürde
page_bfv: 183
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 6.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>+++ 23 Prozent in Deutschland mit Migrationshintergrund: Die Ampel schafft sich ein neues Volk! +++ [...] Die Bundesregierung dürfte über diese Zahlen dennoch erfreut sein. Wer vom alten Volk nicht mehr gewählt wird, wählt sich einfach selbst ein neues. Gelockt wird dieses mit Blitzeinbürgerungen und unendlicher Partizipation am Sozialstaat.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 183

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