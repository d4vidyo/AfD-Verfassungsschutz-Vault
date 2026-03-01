---
type: zitat
speaker: "[[Michael Adam]]"
date: 2023-01-13
topic: Menschenwürde
page_bfv: 155
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Michael Adam]] vom 13.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Staat wird nicht umhinkommen, Integrationsverweigerung unter Strafe zu stellen. Bei genauem Hinsehen ist diese Strafandrohung allein schon deshalb erforderlich, damit wir nicht in den Zwang geraten, in Zukunft doch über Ausbürgerungen nachdenken zu müssen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 155

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