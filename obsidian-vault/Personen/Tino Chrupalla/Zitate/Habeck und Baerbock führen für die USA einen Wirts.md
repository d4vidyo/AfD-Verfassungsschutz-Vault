---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2022-08-28
topic: Demokratieprinzip
page_bfv: 537
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 28.8.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Habeck und Baerbock führen für die USA einen Wirtschaftskrieg gegen die eigene Bevölkerung, gegen unser Land und das ist die Wahrheit. Das sind die wahren Kriegstreiber, liebe Freunde. [...] Robert Habeck vertritt eine Agenda, die durch und durch radikal ist. [...] Perspektivisch muss aber Europa seine Verteidigung wieder in die eigenen Hände nehmen. Das muss es sein. Es muss souverän sein und auch Deutschland muss an seiner Souveränität arbeiten. Das sehen wir doch aktuell, dass wir das in vielen Bereichen eben nicht sind. Dass wir von außen manipuliert werden. Dass wir von außen gesagt bekommen, was wir sagen und wir nicht machen dürfen. Und das muss aufhören, liebe Freunde. Wir brauchen unsere Interessen und ein souveränes Deutschland. [...] Die Grünen nutzen diesen Wirtschaftskrieg für eine Transformation unseres Landes und genau das ist die Absicht, was dahintersteht. Wirtschaftlich, gesellschaftlich, politisch. Leidtragende sind die Bürger, die Mittelständler, die Handwerker und alle, die Interessen über Ideologie stellen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 537

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