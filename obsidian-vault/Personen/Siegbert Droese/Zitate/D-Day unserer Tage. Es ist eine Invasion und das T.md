---
type: zitat
speaker: "[[Siegbert Droese]]"
date: 2023-09-12
topic: Menschenwürde
page_bfv: 369
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Siegbert Droese]] vom 12.9.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>D-Day unserer Tage. Es ist eine Invasion und das Tag für Tag und Nacht für Nacht. Wer etwas anderes sagt verkennt den Ernst der Lage oder ist ein Scharlatan.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 369

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