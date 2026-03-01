---
type: zitat
speaker: "[[Carolin Bachmann]]"
date: 2024-01-19
topic: Menschenwürde
page_bfv: 186
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Carolin Bachmann]] vom 19.1.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutsche Staatsbürgerschaft für 'Jeden'! Eben beschloss der Bundestag, gegen die Stimmen der AfD, das neues 'Staatsangehörigkeitsrecht'! GRUND: 'Es besteht aber ein gesamtgesellschaftliches Interesse, dass sich möglichst viele Ausländer, die die rechtlichen Voraussetzungen erfüllen, für eine Einbürgerung entscheiden, um aktiv das gesellschaftliche Zusammenleben mitgestalten zu können.' [Pfeil-Symbol] also wählen und gewählt werden können ! Die Altparteien schaffen sich ein neues Staatsvolk!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 186

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