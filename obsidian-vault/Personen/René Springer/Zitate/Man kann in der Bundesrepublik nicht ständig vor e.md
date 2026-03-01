---
type: zitat
speaker: "[[René Springer]]"
date: 2024-12-04
topic: Demokratieprinzip
page_bfv: 953
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 4.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Man kann in der Bundesrepublik nicht ständig vor einem angeblichen Untergang der Demokratie warnen, gezielt die Opposition bekämpfen und dann in ein anderes Land reisen, um dort den Sturz einer demokratisch gewählten Regierung zu unterstützen. Kartellpolitiker wie Roth sind der Inbegriff der Altparteien-Heuchelei und einer fremdinteressengesteuerten Außenpolitik.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 953

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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