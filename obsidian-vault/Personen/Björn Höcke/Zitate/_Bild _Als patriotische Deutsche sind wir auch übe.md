---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-08-04
topic: Menschenwürde
page_bfv: 507
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 4.8.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Bild "Als patriotische Deutsche sind wir auch überzeugte Europäer. Wir wollen die EU als Projekt globalistischer Eliten überwinden und einen neuen Bund europäischer Nationen gründen: Kulturelle Vielfalt in wehrhafter Einheit ist das Ziel!" Der Landesvorsitzende der AfD-Thüringen, Björn Höcke, anlässlich der AfD-Europawahlversammlung in Magdeburg www.deutschlandkurier.de\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 507. Bild stammt ursprünglich vom Deutschland-Kurier. Höcke hat es auf seiner Facebook-Seite geteilt.

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