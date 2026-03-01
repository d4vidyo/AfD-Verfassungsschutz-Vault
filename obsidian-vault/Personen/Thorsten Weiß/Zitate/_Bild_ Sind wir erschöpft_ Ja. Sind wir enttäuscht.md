---
type: zitat
speaker: "[[Thorsten Weiß]]"
date: 2025-01-19
topic: Menschenwürde
page_bfv: 892
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Thorsten Weiß]] vom 19.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>\<Bild\> Sind wir erschöpft? Ja. Sind wir enttäuscht? Sehr. Dürfen wir deshalb aufgeben? Nein. Vor allem der 3. und 4. Generation sage ich: Dieses Land ist auch Euer unser Land. Kämpft dafür. Demographie wird Fakten schaffen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 892

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