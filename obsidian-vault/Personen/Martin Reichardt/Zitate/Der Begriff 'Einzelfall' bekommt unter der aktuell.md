---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2023-09-05
topic: Menschenwürde
page_bfv: 290
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 5.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Begriff 'Einzelfall' bekommt unter der aktuellen Regierung eine neue traurige Bedeutung. Auch wenn sich die Tat im Juni dieses Jahres ereignet hat, zeigt sie nur einmal mehr wie die Sicherheit auf deutschen Straßen zu definieren ist - nämlich als unsicher. Dank weltfremder, von Ideologie getriebener Willkommenskultur, die darauf ausgerichtet ist ein Land, unser Land, von innen heraus zu zerstören.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 290

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