---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2023-09-02
topic: Menschenwürde
page_bfv: 173
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 2.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Es ist die strukturelle Asozialität und penetrante Unverschämtheit linker Migrantenvertreter, die das gesellschaftliche Klima in vergiftet! [Deutschland] gehört den [Deutschen], so wie die [Türkei] den [Türken] gehört! Naika Foroutan ist ein Beispiel für völlig misslungene Integration! Es ist der asoziale linke Irrglaube, dass der Gast, dem Gastgeber am Ende sagen dürfe, dass eigentlich das Haus auch dem Gast gehört!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 173

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