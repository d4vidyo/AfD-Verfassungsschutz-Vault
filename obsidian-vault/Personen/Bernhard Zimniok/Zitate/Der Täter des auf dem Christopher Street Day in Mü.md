---
type: zitat
speaker: "[[Bernhard Zimniok]]"
date: 2022-09-05
topic: Menschenwürde
page_bfv: 340
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Bernhard Zimniok]] vom 5.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Täter des auf dem Christopher Street Day in Münster ermordeten ,Transmanns‘ Malte C. wurde gefasst. Es handelt sich um einen tschetschenischen Asylbewerber, der der Polizei wegen Gewaltdelikten bereits bekannt war. [...] Erneut hat die Asyl- und Migrationspolitik der Linksgrünen also ein Opfer gefordert. [...] Fakt ist: Die linksgrüne Migrations- und Asylpolitik tötet. Immer und immer wieder.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 340

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