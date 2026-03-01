---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2023-11-20
topic: Nationalsozialismus
page_bfv: 688
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 20.11.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Nur ein verschwindend geringer Teil der Wehrmachtssoldaten [hat] Verbrechen verübt. Unsere Urgroßväter und unsere Großväter waren keine Verbrecher!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 688

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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