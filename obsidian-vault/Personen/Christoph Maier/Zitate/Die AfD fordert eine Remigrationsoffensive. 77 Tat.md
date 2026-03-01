---
type: zitat
speaker: "[[Christoph Maier]]"
date: 2022-08-18
topic: Menschenwürde
page_bfv: 415
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christoph Maier]] vom 18.08.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die AfD fordert eine Remigrationsoffensive. 77 Tatverdächtige eines Gewaltdelikts in Memmingen konnte die Polizei im Jahr 2021 ermitteln. Darunter befinden sich 35 nichtdeutsche Tatverdächtige. Damit sind Ausländer fast für die Hälfte aller Gewaltdelikte in der Stadt verantwortlich! Personen, die einen deutschen Pass besitzen, aber einen Migrationshintergrund haben, werden in den Statistiken der deutschen Bevölkerung zugerechnet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 415

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