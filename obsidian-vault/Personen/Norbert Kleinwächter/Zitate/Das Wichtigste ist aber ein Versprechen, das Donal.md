---
type: zitat
speaker: "[[Norbert Kleinwächter]]"
date: 2024-11-06
topic: Menschenwürde
page_bfv: 945
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Norbert Kleinwächter]] vom 6.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Das Wichtigste ist aber ein Versprechen, das Donald Trump gegeben hat und für das er natürlich immer als Verschwörungstheoretiker gebrandmarkt wurde. Das Versprechen lautet nämlich, diesen Deep State auszuhöhlen. Trump hat oft vom Deep State gesprochen, hat oft von Akteuren gesprochen, die im Endeffekt die Zügel in der Hand halten und sozusagen die Politiker sogar noch dominieren. Und hier ist die historische Aufgabe, den Beweis zu erbringen, dass es diesen Deep State tatsächlich gibt und die Akteure hinter Schloss und Riegel zu bringen. Wir sehen ja ihr Wirken auch in Europa. Wir sehen es in der parlamentarischen Versammlung des Europarats beispielsweise, in der ich auch bin, wo wir dann sehen, dass in den europäischen Gerichtshof für Menschenrechte lauter Richter gewählt werden sollen, die aus George Soros Open Society Foundation kommen. Also diese ganze Philanthropie, die ein Bill Gates machen, die ein George Soros machen und so weiter, die haben politischen Einfluss auch in Europa. Trump sagt, das ist ein Deep State, der im Endeffekt die Politik dominiert außerhalb der demokratischen Institutionen. Trump hat nun als US-Präsident meiner Ansicht nach die Pflicht, genau diesen Deep State absolut auszuradieren. Denn es kann nicht sein, dass es außerhalb der demokratischen Institutionen, außerhalb der demokratischen Wahlen noch irgendwas gibt, was eigentlich die Politik leitet. Und wenn wir diesen Deep State los sind, wenn wir diese Philanthropie los sind, wenn es die tatsächlich gibt mit ihrem negativen Einfluss, mit ihrem antidemokratischen Gehabe, dann haben wir auch in Europa wieder eine bessere Chance auf Demokratie und freie Entfaltung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 945

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