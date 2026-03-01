---
type: zitat
speaker: "[[Alexander Wiesner]]"
date: 2022-06-03
topic: Menschenwürde
page_bfv: 344
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Alexander Wiesner]] vom 3.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>*Goldstücke sorgen für zwei Einzelfälle pro Tag* [...] Das Vergewaltigungen und sexuelle Übergriffe durch Asyl-Migranten Alltag sind, ist das erschreckende Ergebnis einer verfehlten Politik. Die Duldung von No-go-Areas befeuert diesen verachtenswerten Zustand zudem. Die medial gepriesene ‚feministische‘ Außenpolitik ist ein Wunschdenken der linken Politkamarilla, welche in Realität Wirtschaftsflüchtlingen aus aller Herren Länder nur zum weiteren Zuzug ins Schlaraffenland BRD animiert. Festzuhalten bleibt, dass die frauenfeindlichen und antisemitischen Auswüchse hierzulande das Ergebnis von importierten Heerscharen von überwiegend männlichen Einwanderern aus problematischen Gesellschaften seit 2015 ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 344

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