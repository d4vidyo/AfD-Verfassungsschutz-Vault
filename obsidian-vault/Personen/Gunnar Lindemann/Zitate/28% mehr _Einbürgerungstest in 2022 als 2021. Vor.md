---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2023-05-30
topic: Menschenwürde
page_bfv: 221
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 30.5.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>28% mehr #Einbürgerungstest in 2022 als 2021. Vor allem aus #Syrien, #Ukraine, #lrak und #Türkei. Aber eine Umvolkung findet natürlich nicht statt in #Deutschland. Schlafen Sie beruhigt weiter. Gute Nacht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 221

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