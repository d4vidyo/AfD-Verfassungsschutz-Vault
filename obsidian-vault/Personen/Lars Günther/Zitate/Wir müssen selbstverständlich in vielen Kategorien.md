---
type: zitat
speaker: "[[Lars Günther]]"
date: 2021-11-25
topic: Sonstiges
page_bfv: 794
source: 'Podiumsdiskussion'
status: Unbewertet
---

# Zitat: [[Lars Günther]] vom 25.11.2021 veröffentlicht auf: 'Podiumsdiskussion'
> [!quote] Aussage
>Wir müssen selbstverständlich in vielen Kategorien denken. Der vorparlamentarische Raum auf Metaebene, muss das alles besprochen werden. Wir haben super Leute. Ich nenne da jetzt mal ein Musterbeispiel: Martin Sellner mit seinen Kanälen bei Telegram et cetera. Das ist wirklich eigentlich für jeden Pflichtprogramm, für jeden Jüngeren, für jeden Älteren. Und wir haben ja viele andere. Wir haben, Gott sei Dank, das Compact-Magazin und vieler andere freie Medien. Die sollte man eigentlich auch unterstützen. [...] Bitte unterstützt die Zeitungen 'COMPACT', 'ZUERST!', wie sie alle heißen. Kauft sie, gebt sie weiter. Guckt 'CompactTV' am Tag, bringt was in die sozialen Medien, verstreut es, verteilt es. Denn jeden Tag können wir selber was bewirken und Leute beim Aufwachprozess unterstützen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 794

**Verfassungsschutz Kategorisierung:** Sonstiges.

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