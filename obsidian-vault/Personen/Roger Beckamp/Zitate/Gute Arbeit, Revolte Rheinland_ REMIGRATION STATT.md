---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2023-03-27
topic: Sonstiges
page_bfv: 777
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 27.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gute Arbeit, Revolte Rheinland: REMIGRATION STATT UNTERWERFUNG! In der vergangenen Woche wurde international über Deutschlands erstes arabisches Straßenschild in der Ellerstraße in Düsseldorf berichtet. Damit diese Unterwerfungsgeste der Stadt Düsseldorf nicht unbeantwortet bleibt, äußerten die Aktivisten von Revolte Rheinland ihren Unmut in friedlichen Protest. Weiterhin fordern sie geschlossene Grenzen und Remigration statt Unterwerfung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 777

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