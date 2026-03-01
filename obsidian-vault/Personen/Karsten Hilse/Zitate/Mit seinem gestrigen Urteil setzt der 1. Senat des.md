---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2021-12-01
topic: Rechtsstaatsprinzip
page_bfv: 659
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 1.12.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Mit seinem gestrigen Urteil setzt der 1. Senat des Bundesverfassungsgerichts unser Grundgesetz in großen Teilen faktisch außer Kraft. Die grundgesetzlich garantierten Freiheitsrechte, welche als Abwehrrechte gegen den Staat, vor allem in Krisensituationen, in das Grundgesetz geschrieben wurden und auch noch mit einer Ewigkeitsklausel versehen sind, haben praktisch aufgehört zu existieren. Mit der Verkündung des Urteils begann auch die Diskussion für einen allgemeinen Impfzwang. Alle, die diese Entwicklung prognostizierten, wurden als Verschwörungstheoretiker diffamiert. Was gestern noch als absurde Behauptung bezeichnet wurde, ist heute Realität. Was heute als absurd und nie und nimmer eintretbar oder denkbar erscheint, wird die Realität von morgen sein, wenn nicht endlich ALLE, die sich gegen die Aushebelung unserer freiheitlich demokratischen Grundordnung wenden, von ihrem Recht auf Widerstand Gebrauch machen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 659

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Rechtsstaatsprinzip.

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