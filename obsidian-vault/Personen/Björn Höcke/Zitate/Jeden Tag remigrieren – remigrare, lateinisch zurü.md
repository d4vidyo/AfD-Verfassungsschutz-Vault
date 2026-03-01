---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-04-11
topic: Menschenwürde
page_bfv: 428
source: 'Welt TV'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 11.4.2024 veröffentlicht auf: 'Welt TV'
> [!quote] Aussage
>Jeden Tag remigrieren – remigrare, lateinisch zurückwandern – migrieren Menschen zurück in ihrer Heimat. Das ist ein normaler Vorgang. Aber mir geht es vor allen Dingen um die Hochklassifizierten. [...] Ja, mir geht es aber vor allen Dingen um die deutschen Staatsangehörigen, die im Ausland leben, weil sie aus Deutschland geflohen sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 428. TV-Duell gegen Mario Voigt

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