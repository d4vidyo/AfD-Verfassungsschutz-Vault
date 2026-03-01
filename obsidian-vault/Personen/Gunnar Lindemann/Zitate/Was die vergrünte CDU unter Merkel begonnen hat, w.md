---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2023-06-04
topic: Demokratieprinzip
page_bfv: 572
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 4.6.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Was die vergrünte CDU unter Merkel begonnen hat, wird von der gegenwärtigen Linksaußen-Regierung konsequent fortgesetzt: Sie brechen deutsches Asylrecht in dem Wissen, dass es niemanden gibt, der sie daran hindern wird. Die deutsche Justiz sowieso nicht und auch von internationalen Institutionen ist kein Widerstand zu erwarten. Der deutsche Wähler wird erkennen müssen, dass die alten Parteien sich dazu verschworen haben, unser geltendes Recht mit Füßen zu treten. Wenn er dies nicht akzeptieren will, bleibt ihm nur eine Chance: Die einzige Partei zu wählen, die sich dieser verschworenen Gemeinschaft von Politgangstern entgegenstellt. Auch wenn er nicht mit allem einverstanden ist, was die AfD sagt oder tut - auf eines kann sich jeder Deutsche verlassen: Die AfD wird deutsche Interessen vertreten und geltendes Recht konsequent umsetzen. Immer. Zu jeder Zeit und gegen jeden Widerstand.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 572

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