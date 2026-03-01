---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-18
topic: Menschenwürde
page_bfv: 917
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 18.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Herr Merz, Herr Spahn, Herr Söder, ihr habt euch schuldig gemacht, weil ihr die Multikulturalisierung dieses Landes, die Deformation dieses Landes ohne Widerspruch über euch ergehen habt lassen, aus machtpolitischen Gründen, weil ihr in eurer Partei ja noch was werden wolltet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 917. Gehört zur Rede vom 18.1.2025

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