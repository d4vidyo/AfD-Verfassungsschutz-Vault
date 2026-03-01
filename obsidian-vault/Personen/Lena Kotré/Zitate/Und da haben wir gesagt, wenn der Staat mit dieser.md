---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-09-18
topic: Rechtsstaatsprinzip
page_bfv: 659
source: 'Interview mit Deutschland-Kurier deutschlandkurier.de'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 18.9.2024 veröffentlicht auf: 'Interview mit Deutschland-Kurier deutschlandkurier.de'
> [!quote] Aussage
>Und da haben wir gesagt, wenn der Staat mit dieser Aufgabe nicht fertig wird, wenn er seiner Pflicht nicht nachkommen kann, dann müssen wir über Alternativen nachdenken und eine Alternative ist eben Ausschreibungen zu machen, öffentliche Ausschreibungen an private Abschiebeunternehmen. Wer uns da das beste Konzept vorlegt, der kriegt den Zuschlag und der darf dann im Namen des Staates abschieben.

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