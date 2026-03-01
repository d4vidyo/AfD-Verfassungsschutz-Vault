---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2024-11-25
topic: Menschenwürde
page_bfv: 910
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 25.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Mehr als 600 Frauen wurden Silvester 2015 Opfer sexueller Straftaten. Mehrheitlich wurden diese Taten von sogenannten Flüchtlingen verübt. [...] Seitdem hat sich das Leben von Frauen in Deutschland verändert. Gruppenvergewaltigungen, Morde, sind in Deutschland 2024 alltäglich geworden. Keine Frau ist mehr sicher, zu keiner Zeit, an keinem Ort. [...] Aber keiner benennt den Grund, warum die Gewalt gegen Frauen explosionsartig zugenommen hat. Wenn sie es täten, müssten sie ihre Mitschuld eingestehen, denn sie haben massenweise Männer in unser Land geholt, die dem frauenfeindlichen islamistischen Weltbild folgen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 910

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