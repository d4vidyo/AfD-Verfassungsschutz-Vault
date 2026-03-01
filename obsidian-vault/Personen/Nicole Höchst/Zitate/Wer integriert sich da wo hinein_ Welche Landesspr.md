---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-08-29
topic: Menschenwürde
page_bfv: 475
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 29.8.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wer integriert sich da wo hinein? Welche Landessprache und Kultur herrschen da vor? Ist das die Zukunft Deutschlands, die wir unseren Kindern hinterlassen wollen? Unterwerfung, Koran und Scharia inklusive?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 475

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