---
type: zitat
speaker: "[[Kai Uwe Dettmar]]"
date: 2021-08-20
topic: Menschenwürde
page_bfv: 153
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Kai Uwe Dettmar]] vom 20.8.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die EU hat die Ausbreitung von Waschbären verboten. Begründung: Das invasive Vordringen eines Spezies von einem anderen Kontinent könnte und würde die heimische Tierpopulation beeinflussen und sogar ausrotten. Jetzt einmal scharf nachdenken.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 153

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