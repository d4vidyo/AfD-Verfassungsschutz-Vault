---
type: zitat
speaker: "[[Robert Teske]]"
date: 2025-01-17
topic: Menschenwürde
page_bfv: 925
source: 'TikTok'
status: Unbewertet
---

# Zitat: [[Robert Teske]] vom 17.1.2025 veröffentlicht auf: 'TikTok'
> [!quote] Aussage
>Deiner Oma droht Altersarmut. Deutschlands Sozialkassen sind leergeplündert. Offene Grenzen, Toleranzbesoffenheit des deutschen Establishments haben dafür gesorgt, dass kein Geld mehr für unsere Großeltern da ist. [...] Im Februar diesen Jahres hast du die Wahl. Altersarmut für Oma und Opa oder Remigration von Illegalen und nicht Integrierbaren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 925

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