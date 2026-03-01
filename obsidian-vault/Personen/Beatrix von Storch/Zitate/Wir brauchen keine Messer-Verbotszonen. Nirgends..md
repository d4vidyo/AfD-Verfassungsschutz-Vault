---
type: zitat
speaker: "[[Beatrix von Storch]]"
date: 2024-11-28
topic: Menschenwürde
page_bfv: 913
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Beatrix von Storch]] vom 28.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir brauchen keine Messer-Verbotszonen. Nirgends. Wir brauchen nur weniger von diesen Messer-Männern, die ständig mit einem Messer durch die Gegend laufen, in unserem Land.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 913

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