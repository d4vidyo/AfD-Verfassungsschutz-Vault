---
type: zitat
speaker: "[[Dominik Kaufner]]"
date: 2024-12-21
topic: Menschenwürde
page_bfv: 929
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Dominik Kaufner]] vom 21.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Mir ist es übrigens vollkommen gleich, ob Ausländer ihren Hass auf uns #Deutsche nun mit dem #lslam oder sonst irgendwie begründen. Die nie enden wollenden Diskussionen um religiöse oder politische Motive, um psychische Störungen, Traumata und ein Gefühl der Fremdheit im Aufnahmeland verstellen den Blick auf eine einfache Wahrheit: Millionenfache #Migration ist das Problem und millionenfache #Remigration ist die Lösung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 929

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