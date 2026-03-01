---
type: zitat
speaker: "[[Dominik Kaufner]]"
date: Nicht Verfügbar
topic: Menschenwürde
page_bfv: 203
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Dominik Kaufner]] vom None veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Gleichzeitig ist der Bevölkerungsaustausch in manchen Klassen fast abgeschlossen. In einer Generation werden wir vielerorts eine Minderheit im eigenen Land sein. Wir können hier wie durch ein Fenster in die Zukunft sehen. Wenn wir jetzt nicht gegensteuern, dann haben wir den Kampf um unsere Heimat verloren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 203

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