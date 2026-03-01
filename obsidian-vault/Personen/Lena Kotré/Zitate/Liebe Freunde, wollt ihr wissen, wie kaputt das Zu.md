---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-10-06
topic: Menschenwürde
page_bfv: 463
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 6.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Liebe Freunde, wollt ihr wissen, wie kaputt das Zuwanderungssystem in Deutschland wirklich ist? Der Europäische Gerichtshof hat entschieden, dass Frauen aus Afghanistan allein aufgrund ihres Geschlechts einen Anspruch auf Asyl in der Europäischen Union haben. Die Bundesregierung plant ja auch schon, Afghaninnen hierher zu holen. Ja, die Situation der Frauen vor Ort ist fatal, aber genau das ist der fundamentale Islam, genau das ist die Scharia und genau das ist auch der Grund, warum wir hier in Deutschland uns immer wieder vehement gegen die schleichende Islamisierung in der Gesellschaft einsetzen. Wir wollen diese Zustände hier nicht, verdammt noch mal. Ist das so schwer zu verstehen? Wir Frauen in Deutschland sind durch die Islamisierung ebenfalls gefährdet. Wir sind stark gefährdet, indem immer weiter seit 2015 kontinuierlich junge Männer hierherkommen, aus Kulturkreisen, die nicht kompatibel mit dem unseren sind. [...] Ja, den Frauen sollte geholfen werden, allerdings vor Ort, in den Kulturkreisen rund um Afghanistan, wo sie zu Hause sind, wo sie sozialisiert sind. Das kann hier in Deutschland nicht erfolgen. Wir haben ja noch ein weiteres Problem, wenn wir die Frauen aus Afghanistan her holen. Und zwar den Familiennachzug. Auf einmal haben wir 20-köpfige Familien hier, alle kommen hierher. Ehemänner, Söhne, alle die, die dort in diesen frauenfeindlichen Kreisen, in diesen frauenfeindlichen Kulturen sozialisiert wurden, kommen hierher und implementieren ihr Frauenbild immer weiter in die Gesellschaft. Wir deutschen Frauen sind dann die Leidtragenden. Das darf nicht sein. Wir müssen uns immer wieder gegen diese schleichende Islamisierung stellen. Ich kann es nur noch einmal sagen. Die AfD ist die einzige Partei, die sich noch für die Rechte der Deutschen und für die Rechte der deutschen Frauen im Übrigen hier in diesem Land einsetzen. Wir sind gegen eine Islamisierung. Wir sind gegen das Implementieren islamistischen Gedankengutes in unsere Gesellschaft. Und deshalb dürfen wir es nicht hinnehmen, dass Islamisten aus anderen Ländern hier Einzug halten dürfen. Ich sage es noch einmal. Die Frauen aus Afghanistan müssen in ihren Kulturkreisen bleiben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 463

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