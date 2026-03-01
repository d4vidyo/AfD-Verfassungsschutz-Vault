---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2023-04-27
topic: Demokratieprinzip
page_bfv: 617
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 27.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Abweichler, ob nun in Corona- oder Genderfragen, bei der Einordnung der Situation in der Ukraine oder der Vereinbarkeit des Islam mit der Europäischen Menschenrechtscharta, sollen mundtot gemacht werden. Das aber ist totalitär, in meinen Augen beginnt hier ein Faschismus, der in seinen Anfängen schon als solcher benannt und bekämpft werden muss. [...] Die moralisierende Dummheit des Verfassungsschutzes - ein institutionalisierter singulärer Anachronismus selbst unter westlich orientierten Staaten - ist nichts als ein Werkzeug zur Unterdrückung von Meinungen und dem dazugehörigen freien Diskurs. Es ist genau der Kampf gegen den vermeintlichen Faschismus, der ihn erst erzeugt. Extremistisch sind die Ziele und Methoden des Verfassungsschutzes - und damit gesichert verfassungsfeindlich. Der Geist der Überwachung, ob nun von Gestapo, Stasi oder Verfassungsschutz exekutiert, schützt unsere Gesellschaft nicht. Er gefährdet sie!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 617

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