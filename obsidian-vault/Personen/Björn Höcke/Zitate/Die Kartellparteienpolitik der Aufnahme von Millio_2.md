---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-23
topic: Menschenwürde
page_bfv: 925
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 23.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Kartellparteienpolitik der Aufnahme von Millionen illegaler Immigranten aus fremden Kulturen zerstört den im Grundgesetz beschriebenen Souverän und Staat. Sie ist in der Tat verfassungswidrig und extremistisch! Als ich vor einigen Jahren in ,Nie zweimal in den denselben Fluß' den fortgeschrittenen Prozeß des deutschen Staatszerfalls beschrieb, führte ich zu möglichen Gegenmaßnahmen aus: ,Neben dem Schutz unserer nationalen und europäischen Außengrenzen wird ein groß angelegtes Remigrationsprojekt notwendig sein. Und bei dem wird man, so fürchte ich, nicht um eine Politik der ,Wohltemperierten Grausamkeit', wie es Peter Sloterdijk sagte, herumkommen. Das heißt, dass sich menschliche Härten und unschöne Szenen nicht immer vermeiden lassen werden.' Und ich mahnte, was oft unterschlagen wird, aus meiner ethischen Verantwortung heraus im folgenden Satz an: ,Man sollte daher so human wie irgend möglich, aber auch so konsequent wie nötig vorgehen.' Ich setzte damit bewußt einen Kontrapunkt zur damaligen Bundeskanzlerin Merkel, die den Migrantentsunami über Deutschland hinweggehen ließ, weil sie die unschönen Bilder an der Bundesgrenze fürchtete. Ich tat es, wohl wissend, Opfer von Haß und Hetze durch das polit-mediale Establishment zu werden, weil ich ahnte, wie grausam die Folgen für Deutschland werden würden. Die Bluttat von Aschaffenburg steht für diese grausamen Folgen. [...] Trump weiß, es gibt kein internationales Recht, das das Recht eines souveränen Volkes brechen könnte, selbst darüber zu entscheiden, mit wem es Zusammenleben will und mit wem nicht. Die unschuldigen Opfer der immigrationsbedingten Gewalt in Deutschland werden nicht mehr lebendig werden. Und die Toten von Aschaffenburg werden nicht die letzten gewesen sein. Trotzdem haben die Menschen in Deutschland am 23. Februar die Möglichkeitden fatalsten Irrweg der deutschen Nachkriegsgeschichte zu beenden - den der identitäts- und staatsauflösenden Politik der offenen Grenzen. Es ist Zeit für Deutschland!

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Die Kartellparteienpolitik der Aufnahme von Millio]]

**SPIEGEL-Notiz:** Gutachten Seite: 925

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