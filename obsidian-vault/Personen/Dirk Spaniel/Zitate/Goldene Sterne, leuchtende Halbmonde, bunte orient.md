---
type: zitat
speaker: "[[Dirk Spaniel]]"
date: 2024-03-05
topic: Menschenwürde
page_bfv: 468
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Dirk Spaniel]] vom 5.3.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Goldene Sterne, leuchtende Halbmonde, bunte orientalische Ramadan-Laternen, riesige verschnörkelte Schriftzüge ,Happy Ramadan'. Wieder einmal wird auf Kosten der Steuerzahler ausländischen Integrationsverweigerern gehuldigt. Wir als AfD werden solche grünen Gesten der Unterwerfung verhindern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 468

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