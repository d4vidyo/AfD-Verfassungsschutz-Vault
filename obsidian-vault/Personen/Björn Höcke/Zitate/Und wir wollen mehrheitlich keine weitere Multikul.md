---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Menschenwürde
page_bfv: 428
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und wir wollen mehrheitlich keine weitere Multikulturalisierung. Nein, wir wollen Remultikulturalisierung und Remigration.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 428. Rede auf Wahlkampfveranstaltung in Erfurt

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