---
type: zitat
speaker: "[[Marc Jongen]]"
date: 2021-10-29
topic: Menschenwürde
page_bfv: 245
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Marc Jongen]] vom 29.10.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Und genau darauf läuft diese Distanzierungs- und Abwertungsmentalität gegenüber dem Eigenen hinaus: auf die kulturelle Selbstabschaffung. [...] Die hier zum Ausdruck kommende Verachtung für das Eigene wird maßgeblich von den links- grünen Kreisen getragen, die voraussichtlich die nächste Bundesregierung bilden werden. Sie können mit Deutschland, seiner Kultur, seinen Menschen und seiner Geschichte 'nichts anfangen' (O-Ton Robert Habeck) und streben eine geschichtslose 'multikulturelle und diverse Gesellschaft' an. In dieser Gesellschaft soll möglichst nichts mehr an deutsche Kultur und Geschichte erinnern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 245

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