---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2022-06-29
topic: Menschenwürde
page_bfv: 208
source: Facebook
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 29.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der sogenannte Brain-Drain geht in immer größerer Geschwindigkeit voran. Allein im Jahr 2021 haben etwa eine Million Einwohner ihre Heimat für immer verlassen, während laut dem statistischen Bundesamt zeitgleich rund 1,1 Millionen nichtdeutsche Staatsbürger einwanderten. [...] Gleichzeitig verlassen die Leistungsträger unserer Gesellschaft ihre Heimat in immer größerer Zahl. Sie werden zu Flüchtlingen vor einer Politik, die ihnen ihre Existenzgrundlage nimmt und sie über Gebühr mit Abgaben und Steuern belastet. Ersetzt werden sie dem statistischen Bundesamt nach vor allem durch Syrer, Rumänen und Afghanen. Diese stellten 2021 die Haupteinwanderungsgruppe dar.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 208

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