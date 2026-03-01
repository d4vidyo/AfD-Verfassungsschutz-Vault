---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-12-02
topic: Menschenwürde
page_bfv: 216
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 2.12.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Seine Heimat, liebe Freunde, verliert man nicht nur durch Flucht und Vertreibung, seine Heimat verliert man auch dadurch, dass man zur Minderheit im eigenen Land wird. [...] Wenn ich durch unsere Städte gehe, dann denke ich immer: das, was ich hier sehe, müsste ich eigentlich mit dem Begriff Umvolkung beschreiben können, aber Umvolkung darf ich nicht sagen. [...] Umvolkung darf man nicht mehr sagen, aber replacement migration [...] oder resettlement migration [...], das darf man sagen und das kann man vielleicht auch ins Deutsche übersetzen. [...] Wir Deutschen sollen ersetzt werden, liebe Freunde, und das dürfen wir nicht zulassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 216

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