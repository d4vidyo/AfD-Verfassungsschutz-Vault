---
type: zitat
speaker: "[[Maximilian Krah]]"
date: Nicht Verfügbar
topic: Menschenwürde
page_bfv: 350
source: 'Youtube, Deutschland Kurier'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom None veröffentlicht auf: 'Youtube, Deutschland Kurier'
> [!quote] Aussage
>Ein Land, das offen für alle ist, ist nicht ganz dicht. Ein Land, das jeden hereinnimmt, importiert so viele Probleme, dass es nicht mehr imstande ist, seiner alltäglichen Aufgaben zu lösen. [...] Oder wir erkennen, dass diese Entwicklung schädlich ist, dass diese Einwanderung nicht nützt, sondern schadet. Dass sie aus Deutschland Bunt-Land macht und dass Bunt ein Synonym ist für eine Müllhalde. Dass multikulturell multikriminell ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 350

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