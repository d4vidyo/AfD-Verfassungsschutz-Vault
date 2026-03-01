---
type: zitat
speaker: "[[Michael Adam]]"
date: 2023-01-13
topic: Menschenwürde
page_bfv: 273
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Michael Adam]] vom 13.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>An dieser Stelle sei ein tagesaktuelles und sehr trauriges Beispiel der Folge der Kulturfremdheit einiger deutscher Staatsbürger angeführt: Ein 17-jähriger, kulturfremder Deutscher erstach vor einigen Tagen seine Lehrerin mit einem Messer, weil er sich von ihr ungerecht behandelt fühlte. Diese Tat war und ist mit der deutschen Kultur in mehrfacher Hinsicht nicht vereinbar: Die offenkundig sinnlose Tötung von Menschen widerspricht dem christlichen Menschenbild, dessen Wertekanon zu den Grundlagen unserer abendländisch geprägten deutschen Kultur gehört. Auch sind gewaltsame Auseinandersetzungen unter der Verwendung von Messern der deutschen Kultur fremd und erscheinen der Mehrheitsgesellschaft zu Recht (noch) als abstoßend. Nicht zuletzt ist die Gewalt gegen Frauen in unserer Kultur mit Recht geächtet. All dies scheint dem kulturfremden deutschen Täter nicht bekannt gewesen zu sein oder wahrscheinlicher: Es war ihm egal.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 273

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