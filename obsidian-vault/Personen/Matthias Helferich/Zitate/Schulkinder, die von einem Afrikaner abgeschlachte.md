---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2022-12-05
topic: Menschenwürde
page_bfv: 322
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 5.12.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Schulkinder, die von einem Afrikaner abgeschlachtet werden, Gruppenvergewaltigungen in U-Bahnstationen, Terrorwarnungen auf Weihnachtsmärkten: Wer weiterhin in der Politik für Massenzuwanderung eintritt, ist nicht Mitbewerber, er ist Feind.“

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 322

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