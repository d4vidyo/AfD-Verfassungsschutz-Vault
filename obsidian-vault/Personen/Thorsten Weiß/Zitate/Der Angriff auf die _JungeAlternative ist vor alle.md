---
type: zitat
speaker: "[[Thorsten Weiß]]"
date: 2024-02-06
topic: Sonstiges
page_bfv: 837
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Thorsten Weiß]] vom 6.2.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der Angriff auf die #JungeAlternative ist vor allem ein Angriff auf die #AfD. Jetzt heißt es zusammenstehen, Fördermitglied werden, spenden und unterstützen. Unsere Parteijugend muss sich auf uns verlassen können! #jetzterstrecht

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 837

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