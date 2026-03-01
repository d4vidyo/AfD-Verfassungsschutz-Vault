---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2022-07-17
topic: Menschenwürde
page_bfv: 119
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 17.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Frauenfußball befindet sich qualitativ zwar mehrere Klassen unter dem herkömmlichen Männerfußball, allerdings muss man unsere Frauenmannschaft loben, dass sie im Gegensatz zur durchmultikulturalisierten männlichen Söldnertruppe noch eine echte deutsche (!) Nationalmannschaft (!) ist. Von demher repräsentieren uns die Mädels mehr als es ,die Mannschaft' tut.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 119

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