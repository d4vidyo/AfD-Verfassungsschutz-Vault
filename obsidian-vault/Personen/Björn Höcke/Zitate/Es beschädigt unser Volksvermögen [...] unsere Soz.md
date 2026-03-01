---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-12-02
topic: Menschenwürde
page_bfv: 365
source: 'YouTube, Der blaue Kanal'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 2.12.2022 veröffentlicht auf: 'YouTube, Der blaue Kanal'
> [!quote] Aussage
>Es beschädigt unser Volksvermögen [...] unsere Sozialversicherungssysteme einfach für Millionen unqualifizierte Zuwanderer zu öffnen, die direkt in die Sozialversicherungssysteme einwandern, sie also mehr oder weniger zur Plünderung freizugeben. Und das vor allen Dinge vor dem Hintergrund, dass Millionen Alte, die dieses Land aufgebaut haben [...] in Altersarmut versinken.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 365

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