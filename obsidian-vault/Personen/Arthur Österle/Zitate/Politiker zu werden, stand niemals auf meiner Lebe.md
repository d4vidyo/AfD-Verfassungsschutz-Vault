---
type: zitat
speaker: "[[Arthur Österle]]"
date: Nicht Verfügbar
topic: Demokratieprinzip
page_bfv: 636
source: 'arthuroesterle.de'
status: Unbewertet
---

# Zitat: [[Arthur Österle]] vom None veröffentlicht auf: 'arthuroesterle.de'
> [!quote] Aussage
>Politiker zu werden, stand niemals auf meiner Lebensagenda. Das Kartell der Altparteien und ihre Handlanger plündern uns und unsere Heimat aus. Das Kartell der Altparteien setzt das Grundgesetz als Waffe gegen uns, gegen unser Volk ein. Das Kartell der Altparteien manipuliert unser Volk oder ignoriert uns einfach. Deshalb fühle ich mich geradezu gezwungen, einzuschreiten - aus purer Notwehr für die Meinen und mein Volk!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 636

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