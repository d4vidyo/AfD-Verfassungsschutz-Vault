---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-06-12
topic: Menschenwürde
page_bfv: 175
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 12.6.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Anstelle der deutschen Kultur, Tradition, Identität soll der Multikulti-Vielfaltsstaat nach dem Vorbild der USA oktroyiert werden, aber mit einem über Jahrhunderte geprägtem Volk auf dem Staatsgebiet und ohne Leitkultur oder Patriotismus [...] und wir Deutschen - wie schon jetzt in den Großstädten im Westen zu sehen - jeden Tag aufs neue aushandeln dürfen, wie viel wir von unserem zivilisatorischen Denken abgeben und jeden Tag aufs Neue von der archaischen Dominanz mancher Zuwanderer als bereichert ansehen dürfen. [...] Hier soll nur die einhellige Meinung des Establishments herrschen, das seine Kinder auf die Privatschulen schickt und Im sicheren Villenviertel mit hohen Mauern, Sicherheitsdienst in homogener Gesellschaft lebt, dass wir unsere ewige Schuld reinwaschen müssen, indem wir den Rest der Welt hier aufnehmen und immer mehr Asyltouristen reinwinken, bis der Sozialstaat komplett abgeschafft ist und Deutschland zum bunten identitätslosen Nachkriegsexperiment verkommt [...]. [...] Wie Sie sehen, es ist ja eben die neue Glaubensfrage des 21. Jahrhunderts in einer Gesellschaft, die tief zersplittert und historisch gebrochen nach der Erlösung sucht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 175

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