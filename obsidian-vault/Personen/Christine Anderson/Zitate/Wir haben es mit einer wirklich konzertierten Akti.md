---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2023-03-25
topic: Menschenwürde
page_bfv: 499
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 25.3.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir haben es mit einer wirklich konzertierten Aktion zu tun, und wir reden hier von wirklich eklatanten Angriffen auf die Freiheit, die Demokratie und die Rechtsstaatlichkeit. Und diese Angriffe, die beziehen sich auf die nationale Souveränität, auf die Volksherrschaft, auf das Selbstbestimmungsrecht der Völker, auf die individuelle Freiheit und auf die Identität, und zwar die Identität, die sich aus einer nationalen Identität speist, aus einer kulturellen Identität speist und sogar die sexuelle Identität – das, was uns im Kern als Menschen ausmacht – noch nicht mal mehr davor machen sie Halt. Wie macht man das nun? Nun, über diverse Institutionen, über diverse Programme, über diverse Gremien. Wenn wir mit dem EU- Parlament oder den EU-Institutionen als solchen beginnen, dann kann ich wirklich sagen, die EU-Institutionen fungieren als Abrissbirne für alle nationalen Staaten, für alle europäischen Völker. Meine Damen und Herren, ich nenne das EU-Parlament immer das größte Irrenhaus der Welt. Die Verstöße gegen die demokratischen Prinzipien, die suchen ihresgleichen. Sie sind aber gewollt. [...] Worum geht es eigentlich unterm Strich? Ja, das ist jetzt wirklich nicht schön. Es geht um die Errichtung eines totalitären Überwachungsstaates, in dem wir alle völlig verarmt und versklavt sind, um uns von einer Gesellschaft bestehend aus freien Individuen in ein Kollektiv zu überführen, in der der Einzelne lediglich noch Teil einer willenlosen, formbaren Masse ist, über das die globalitäre Elite frei verfügen kann. Darauf läuft es hinaus.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 499

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