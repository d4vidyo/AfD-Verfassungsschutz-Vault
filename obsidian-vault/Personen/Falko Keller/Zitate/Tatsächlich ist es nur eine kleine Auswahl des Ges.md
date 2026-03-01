---
type: zitat
speaker: "[[Falko Keller]]"
date: 2021-05-12
topic: Menschenwürde
page_bfv: 523
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Falko Keller]] vom 12.5.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Tatsächlich ist es nur eine kleine Auswahl des Gesindels, dass Merkel und Co seit Jahren einschleusen. Weiterhin ist es ein Zeichen, dass die jüdische und muslimische Religion voller Hass ist, und hier nichts verloren hat

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 523

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