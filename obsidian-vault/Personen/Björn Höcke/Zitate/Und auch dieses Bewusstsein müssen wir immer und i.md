---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-05-21
topic: Menschenwürde
page_bfv: 505
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 21.5.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und auch dieses Bewusstsein müssen wir immer und immer wieder jeden Tag reaktivieren: Freunde – die US-Amerikaner sind nicht unsere Feinde, die Russen sind nicht unsere Feinde, die Ukrainer sind nicht unsere Feinde. Diese Völker werden auch stellenweise fremdbestimmt. [...] Und ich kann den Amerikanern nur wünschen, dass sie sich endlich von ihrem Tiefen Staat befreien, von einem globalistischen Establishment befreien und mit uns zusammen auf die Seite der Freiheit treten und diese Welt wieder sicher und schön machen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 505

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