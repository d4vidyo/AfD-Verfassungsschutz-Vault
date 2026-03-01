---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2024-02-14
topic: Demokratieprinzip
page_bfv: 631
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 14.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Hier ist vor kurzem was passiert, was aus meiner Sicht absolut demokratiefeindlich ist. [...] Wenn man Veranstaltungen unterdrückt, ohne dass die Menschen, die da auftreten wollen, strafrechtlich relevant geworden sind. Volksverhetzungen, Aufrufe zur Gewalt. Nichts Strafrechtliches, nur weil einem die Meinung nicht gefällt, dann ist das das Gegenteil von Demokratie, dann sind das Stadträte, die Demokratie unterdrücken. Dann sind das Demokratiefeinde. [...] Das geht von links bis grün, bis SPD, bis zur CDU. Wer so etwas macht, wer die Meinungsfreiheit und die Freiheit des Wortes unterdrückt, das ist ein Demokratiefeind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 631

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