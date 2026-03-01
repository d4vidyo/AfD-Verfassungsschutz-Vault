---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2022-06-22
topic: Menschenwürde
page_bfv: 416
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 22.6.2022 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Ausländer an Straftaten mit Schusswaffen überproportional beteiligt +++ [...] Laut Mitteilung des Innenministeriums sind in der Polizeilichen Kriminalstatistik für das Berichtsjahr 2021 nahezu 8.000 Schusswaffenstraftaten erfasst. Fast jede dritte Tat, bei der mit einer Schusswaffe gedroht worden ist, ist von einem Ausländer begangen worden. Und das obwohl der Ausländeranteil in Deutschland lediglich bei 13 Prozent liegt. Fremde sind damit bei Straftaten mit Schusswaffen, wie auch in vielen weiteren Deliktfeldern, überproportional tatverdächtig. Unsere Antwort darauf? Remigration!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 416

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