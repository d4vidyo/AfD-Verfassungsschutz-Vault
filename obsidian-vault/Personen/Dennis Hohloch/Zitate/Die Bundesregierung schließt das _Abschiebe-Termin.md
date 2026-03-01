---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2023-01-30
topic: Menschenwürde
page_bfv: 292
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 30.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Bundesregierung schließt das #Abschiebe-Terminal am Flughafen BER. Man kontrolliert nicht, wer kommt. Man lässt jeden rein. Man schiebt Straftäter nicht ab. Man toleriert Messermänner. Man nimmt Tote in Kauf.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 292

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