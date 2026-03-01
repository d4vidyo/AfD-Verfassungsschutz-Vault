---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-11-02
topic: Menschenwürde
page_bfv: 401
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 2.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Pulverfass Migration - voll ist voll. In riesengroßen Schritten treibt unsere Regierung die Selbstzerstörung Deutschlands immer weiter voran. Habeck katapultiert uns zurück in die Steinzeit, Lauterbach nimmt uns die Grundrechte und Frau Faeser ersetzt unser deutsches Volk. Die Aufnahmeeinrichtungen sind voll, deutsche Städte ächzen unter dem massiven illegalen Ansturm, vor allem aus Afrika und dem Nahen Osten, und Frau Faeser reibt sich die Hände und schaut einfach weg. [...] Was Deutschland jetzt braucht, ist ein sofortiger Paradigmenwechsel – es muss endlich zu einem Abschiebeland werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 401

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