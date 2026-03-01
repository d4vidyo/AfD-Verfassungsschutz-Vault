---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2022-03-08
topic: Menschenwürde
page_bfv: 132
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 8.3.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Kein verfassungsmäßiges Werkzeug wie das der Passvergabe wird heute so unverhohlen politisch eingesetzt. Mit ihm entfaltet sich die ganze Destruktivität – durchaus im Sinne von Zersetzung – eines Weges, der an seinem Ende erklärtermaßen keine Nationalstaaten mehr dulden will, der Europa homogenisieren und zu einem globalen Siedlungsgebiet abwirtschaftet, in dem zwar 'kein Mensch mehr illegal' ist, aber auch sonst kein Stein mehr auf dem anderen gelassen wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 132

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