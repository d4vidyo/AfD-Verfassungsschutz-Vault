---
type: zitat
speaker: "[[Jurij Kofner]]"
date: 2024-09-06
topic: Sonstiges
page_bfv: 791
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jurij Kofner]] vom 6.9.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ich bin rechts-LIBERTÄR. Aus gutBÜRGERLICHEM Hause. Mit MIGRATIONSHINTERGRUND. So sehe ich auch meine Rolle In der #AfD. Aber verdammt nochmal, die @IBDeutschland gehört RUNTER von der Unvereinbarkeitsliste! Die #IB hätte auch niemals drauf sein sollen. Das ist ein Relikt der feigen Meuthen-Ära der AfD. Die IB ist genau so wenig rassistisch, wie die AfD. Sie vertritt richtige und absolut normale Standpunkte: Bewahrung der eigenen #ldentität, #Ethnopluralismus, #Multipolarität. Die VS-Einstufung der IB ist genau so haltlos, wie bei der AfD. Die AfD und die IB, als eine bedeutender und aktiver (im Gramsci-Sinne) Akteur des patriotischen Vorfeldes, sollten offen und eng zusammenarbeiten. #Privatmeinung

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 791

**Verfassungsschutz Kategorisierung:** Sonstiges.

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