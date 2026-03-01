---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-06-30
topic: Menschenwürde
page_bfv: 269
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 30.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Sommer, Sonne, Badespaß. Wie schon in den Wochen zuvor kam es auch am vergangenen Sonntag zu einer Massenschlägerei in einem Freibad in Berlin-Neukölln. Dabei sollen mehrere Kinder andere Badegäste mit Wasserpistolen bespritzt haben. Das Ganze eskalierte in der Warteschlange einer Rutsche. Nachdem sich eine junge Frau gegen die übergriffigen Kinder zu Wehr setzte, mischte sich ein mittelalter Mann ein, der ihr kurzerhand das Nasenbein mit einer Wasserpistole brach. Hach, diese südländische Lebensfreude!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 269

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