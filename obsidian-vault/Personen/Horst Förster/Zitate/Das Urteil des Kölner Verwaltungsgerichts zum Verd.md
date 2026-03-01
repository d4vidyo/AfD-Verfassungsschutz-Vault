---
type: zitat
speaker: "[[Horst Förster]]"
date: 2022-03-10
topic: Menschenwürde
page_bfv: 128
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Horst Förster]] vom 10.3.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das Urteil des Kölner Verwaltungsgerichts zum Verdachtsfall AfD fußt auf einer Fehlinterpretation des Grundgesetzes, indem es darauf abstellt, dass ein ethnischer Volksbegriff mit dem Grundgesetz nicht vereinbar sei. [...] Der ethnische Volksbegriff stört [...] auf dem Weg in die multikulturelle Gesellschaft, die mehr oder weniger zur Staatsdoktrin erhoben wird. Also wird dem ethnischen Volksbegriff angedichtet, er grenze notwendigerweise alles Fremde aus, was natürlich nicht stimmt. Diese Fehlinterpretation ist aber notwendig, um über Fremdenfeindlichkeit die Argumentationskette zu extrem bzw. extremistisch zu schließen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 128

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