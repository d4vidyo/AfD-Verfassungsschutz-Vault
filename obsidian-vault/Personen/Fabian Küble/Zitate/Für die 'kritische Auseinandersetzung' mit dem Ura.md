---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2024-09-10
topic: Nationalsozialismus
page_bfv: 682
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 10.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Für die 'kritische Auseinandersetzung' mit dem Uraltkapitel aus Annodazumal haben wir ja die Linken mit ihrem Schuldkult. Eine Rechte braucht das nicht. Weder im positiven noch im negativen Sinne.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 682

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