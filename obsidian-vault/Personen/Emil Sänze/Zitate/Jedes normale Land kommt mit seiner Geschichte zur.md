---
type: zitat
speaker: "[[Emil Sänze]]"
date: 2021-10-10
topic: Menschenwürde
page_bfv: 149
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Emil Sänze]] vom 10.10.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Jedes normale Land kommt mit seiner Geschichte zurecht, bewältigt diese zur Not, aber die Eliten unseres Landes leben davon, dass es kein Verzeihen für ein historisches Ausnahme-versagen geben soll [...] Weil keine Hinwendung zu einer Zukunft unserer Nation geben soll, wir die 'Bewältigung' ewig und die VERZEIHUNG verweigert. Sie brauchen schließlich, wo sie die Einheimischen nicht zufriedenstellen können und wollen, ein anderes Klientel, ein anderes Staatsvolk, das sie dann 'deutsch' nennen. Dieses Klientel imaginieren sie dankbar und nach ihrem Bilde formbar. Bis sie – heute schon – merken, dass dieses von den Eliten großzügig adoptierte Volk (während man das eigene, historisch gewachsene Staatsvolk tagtäglich rituell VERSTÖSST, um seinen politischen Wünschen nicht folgen zu müssen) dann doch mit aller Berechtigung seine Identität bewahrt hat [...] Wenn das Grundgesetz sagt, alle Staatsgewalt geht vom Volke aus - dann kann die Staatsgewalt von Ideologen zu ihren Zwecken nur dann autark gehandhabt werden, wenn dieses Staatsvolk zu einem Zustand gebracht wurde, in dem es infolge völliger ethnischer Inhomogenität keine Identität finden, kein politisches Bewußtsein konsolidieren und keinen politischen Willen mehr äußern kann. [...] Dies geschieht de facto durch einen Austausch der Bevölkerung über Zuwanderung und Geburtenraten, so dass eine Politik, die kein Deutschland will, am Ende etwas anderes erhält, das sie vielleicht will und das sie dann Deutschland nennt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 149

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