---
type: zitat
speaker: "[[Eva Maria Schneider-Gärtner]]"
date: 2022-06-09
topic: Menschenwürde
page_bfv: 326
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Eva Maria Schneider-Gärtner]] vom 9.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Diese Tat erschüttert uns zutiefst und macht uns fassungslos. Vor allem die üblichen Reaktionen in Politik und Medien, welche die grausame Amokfahrt eines Täters mit Migrationshintergrund mit einer vermeintlichen 'psychischen Erkrankung' zu relativieren versuchen und den unmittelbaren Zusammengang mit einer unkontrollierten Masseneinwanderung systematisch verleugnen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 326

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