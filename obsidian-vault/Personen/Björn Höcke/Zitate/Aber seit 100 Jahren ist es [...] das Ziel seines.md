---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-10-03
topic: Demokratieprinzip
page_bfv: 547
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 3.10.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Aber seit 100 Jahren ist es [...] das Ziel seines Landes, ein deutsch-russisches Zusammengehen zu verhindern, weil die Gefahr bestünde, das etwas entsteht, das sogar den globalen Machtanspruch der USA zurückweisen könnte. Und nun sind wir zum dritten Mal seit Beginn des letzten Jahrhunderts gegen unsere Interessen und gegen die Vernunft gegen Rußland aufgestellt [...]. Zum dritten Mal seit Beginn des letzten Jahrhunderts stehen auf dem europäischen Kontinent Nationen und Völker gegeneinander, obwohl nichts näher läge, als zusammenzuarbeiten und die USA mit ihrem primitiven Sendungsbewußtsein aus Europa fernzuhalten [...]! Es ist entsetzlich: Wir werden von einer raumfremden Macht und einer fremdbestimmten Bundesregierung in einen Krieg hineingetrieben, der nicht der unsere ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 547

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