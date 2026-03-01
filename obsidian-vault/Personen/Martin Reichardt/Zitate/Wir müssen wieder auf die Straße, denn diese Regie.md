---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2023-04-16
topic: Demokratieprinzip
page_bfv: 639
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 16.4.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Wir müssen wieder auf die Straße, denn diese Regierung der linken und grünen Deutschland-Hasser, sie hat ihr Ziel vor Augen, und es ist die Zerstörung unseres Landes, die Zerstörung unserer Gesellschaft, die Zerstörung unserer Kultur, die Vernichtung unseres Eigentums und die Zerstörung unseres Wohlstands. Und dagegen stehen wir gemeinsam auf, Frau Baerbock, wir lassen uns von ihnen nicht kaputtmachen. Wir erleben die Zerstörung all dessen, was Generationen aufgebaut haben. Wir erleben die atemberaubend schnelle Vernichtung dessen, was unserer Väter und Großväter hier wieder aufgebaut haben. Das Land, das unsere Heimat ist. Dieses Land soll uns von den Linksgrünen genommen werden. Liebe Freunde, wir haben es bereits mehrfach gesagt, Deutschland ist zu einem rot-grünen Irrenhaus geworden, regiert von Sozialisten von einer aus Amerika gesteuerten pädophilen, grünen Clique von Lügnern und Lebenslauffälschern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 639

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