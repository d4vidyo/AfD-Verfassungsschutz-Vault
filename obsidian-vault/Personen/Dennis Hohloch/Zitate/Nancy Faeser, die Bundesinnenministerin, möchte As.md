---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2023-09-20
topic: Menschenwürde
page_bfv: 185
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 20.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Nancy Faeser, die Bundesinnenministerin, möchte Asylbewerbern das Wahlrecht geben. [...] Diesen Menschen möchte sie jetzt auch noch unser verbrieftes Grundrecht, das Wahlrecht, geben, und zwar auf kommunaler Ebene. Heißt erstmal klein an fangen, und irgendwann dann das Wahlrecht auf Landesebene für den Landtag, dann für den Bundestag und dann hat man sich sein neues Wahlvolk geschaffen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 185

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