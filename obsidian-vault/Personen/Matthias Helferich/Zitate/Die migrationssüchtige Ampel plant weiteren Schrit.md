---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2022-09-28
topic: Menschenwürde
page_bfv: 227
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 28.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die migrationssüchtige Ampel plant weiteren Schritt zur Transformation unseres Volkes [...] Die Regierung perpetuiert somit Merkels-Willkommensstreich: Anstatt ausreisepflichtige Ausländer konsequent abzuschieben, erhalten diese eine Bleibeperspektive. Aus 'illegal' wird 'legal'. [...] Ich werde gegen diesen weiteren Schritt zur 'Großen Transformation' unseres Volkes kämpfen. Versprochen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 227

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