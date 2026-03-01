---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2024-01-17
topic: Menschenwürde
page_bfv: 194
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 17.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Bis zu 5 Millionen Ausländer können nach dem neuen Ampel-Staatsangehörigkeitsrecht Deutsche werden. Mehrfachstaatsangehörigkeiten möglich. Der Bevölkerungsaustausch ist eine rechte Verschwörungstheorie [Clown- Emoji]

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 194

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