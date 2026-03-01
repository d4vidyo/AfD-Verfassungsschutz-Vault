---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-06-17
topic: Demokratieprinzip
page_bfv: 596
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 17.6.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Noch nie seit der Gründung der Bundesrepublik gab es so viele oder so abrupte Vorhaben in die Freiheitsrechte der Menschen einzuschreiten und so viele diktatorische Gesetzgebungsverfahren von oben. [...] Ich will noch mal darauf hinweisen: Es gibt viele andere kleine Hinweise noch, wo man sehen kann, wir haben eine Entwicklung, die tatsächlich uns Sorgen machen muss, dass wir zurück in die Diktatur gehen. [...] Und deshalb sage ich: Liebe Leute, werdet wach, währet den Anfängen. Wer in der Demokratie schläft, der wird in der Diktatur erwachen. Und deshalb muss der heutige Tag uns Mahnung sein, dass die Freiheit und die Demokratie keine Geschenke sind. Je länger eine Person oder je länger auch eine Partei an der Macht ist, desto größer wird ihr Verlangen, diese Macht dauerhaft zu behalten. Und das funktioniert am Ende nur durch die Schwächung und durch die Unterdrückung der Menschen, durch die Schwächung und Unterdrückung der Opposition. Und in diesem Stadium, in diesem Stadium, Schwächung der Menschen, Schwächung der Opposition, befinden wir uns derzeit. Es war seit 1945 im Westen oder auch seit 1989 bei uns im Osten - noch nie sind wir so nah an sozialistische Verhältnisse herangekommen wie jetzt, siebzig Jahre nach der Niederschlagung dieses ersten großen Volksaufstandes. [...] Kämpfen wir für ein Deutschland, in dem das Volk tatsächlich wieder der Souverän ist, indem nach einem langen Arbeitsleben ein schöner und würdiger Lebensabend wartet, ein Deutschland, in dem sich Leistungen und Arbeit wieder lohnen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 596

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