---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-03-20
topic: Menschenwürde
page_bfv: 271
source: 'www.freilich-magazin.de'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 20.3.2023 veröffentlicht auf: 'www.freilich-magazin.de'
> [!quote] Aussage
>Der von Hauptschulen in Problembezirken oder Hauptbahnhöfen zur Dämmerung bekannte Hass von Migranten gegen ethnische, autochthone Deutsche findet hier keinerlei Erwähnung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 271

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