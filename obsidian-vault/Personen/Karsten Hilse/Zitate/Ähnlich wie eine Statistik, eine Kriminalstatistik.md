---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2023-03-01
topic: Menschenwürde
page_bfv: 346
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 1.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ähnlich wie eine Statistik, eine Kriminalstatistik, dass dort auch überdimensioniert prozentual, bestimmte Bevölkerungsgruppen vertreten sind. [...] Ich sage jetzt mal zwanzig Prozent vielleicht Migranten in Deutschland und der prozentuale Anteil zumindest an Gewaltverbrechen ist also bedeutend höher, als diese zwanzig Prozent. Gruppenvergewaltigungen gab es vor 2015 gab es praktisch nicht. Und dort ist also der Anteil an Migranten oder Menschen mit Migrationshintergrund eben aus einem bestimmten Kulturkreis kommend, überdimensional hoch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 346

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