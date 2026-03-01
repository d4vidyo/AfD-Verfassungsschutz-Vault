---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2023-07-09
topic: Menschenwürde
page_bfv: 287
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 9.7.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Messerkriminalität zum Beispiel. Es ist uns in unserer Kultur völlig unbekannt. Das gab es nicht. Das Phänomen gibt es bei uns nicht. Das gibt es in den Kulturkreisen in Afrika und im Nahen Osten, um es mal ganz klar zu sagen. Und wenn Sie diese Leute aus gewaltbereiten Gesellschaften in ihr Land lassen, die auf eine freiheitlich... Ich sag jetzt auch mal eine gleichberechtigte - Frauen und Männer sind hier gleichberechtigt - auf eine Gesellschaft stoßen, die diese Werte teilt. Ja, dann kommt es zu einem Clash, Clash of Cultures. [...] Ich glaube, dass das umkehrbar ist, wenn die AfD möglichst schnell jetzt in Regierungsverantwortung kommt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 287

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