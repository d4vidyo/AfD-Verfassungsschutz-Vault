---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-23
topic: Demokratieprinzip
page_bfv: 967
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 23.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Beileidsbekundungen der Kartellparteienpolitiker sind flach, hohl und stereotyp. Entweder ist das ihrer Empathielosigkeit geschuldet oder dem Wissen, daß sie durch die Politik der offenen Grenzen, die sie alle bis heute mittragen, große Schuld auf sich geladen haben. Als bezeichnend und gleichzeitig beschämend empfand ich den Beitrag der CDU-Spitzenfunktionärin Julia Klöckner auf X. Sie schrieb: ,Es sind immer wieder Männer. Nicht Frauen. #Aschaffenburg‘ Wahrscheinlich um von der Jahrhundertschuld der CDU abzulenken, scheut diese Dame nicht davor zurück, Männer gegen Frauen auszuspielen und unsere Gesellschaft auch noch in dieser Hinsicht zu polarisieren. Um es nochmal deutlich auszusprechen: Die Kartellparteienpolitik der Aufnahme von Millionen illegaler Immigranten aus fremden Kulturen zerstört den im Grundgesetz beschriebenen Souverän und Staat. Sie ist in der Tat verfassungswidrig und extremistisch! [...] Trump weiß, es gibt kein internationales Recht, das das Recht eines souveränen Volkes brechen könnte, selbst darüber zu entscheiden, mit wem es zusammenleben will und mit wem nicht. Die unschuldigen Opfer der immigrationsbedingten Gewalt in Deutschland werden nicht mehr lebendig werden. Und die Toten von Aschaffenburg werden nicht die letzten gewesen sein. Trotzdem haben die Menschen in Deutschland am 23. Februar die Möglichkeit den fatalsten Irrweg der deutschen Nachkriegsgeschichte zu beenden - den der identitäts- und staatsauflösenden Politik der offenen Grenzen. Es ist Zeit für Deutschland!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 967

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