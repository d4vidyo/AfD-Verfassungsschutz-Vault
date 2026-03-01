---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2022-07-23
topic: Demokratieprinzip
page_bfv: 592
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 23.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das Ziel dieser neuen Sprachpolizei ist klar: Den Bürgern wird signalisiert, dass sie unter Beobachtung stehen, dass kritische politische Äußerungen erfasst und gesammelt werden. [...] Die Regierung setzt also, auch wenn kein juristisches Vergehen vorliegt, auf Einschüchterung - auf totalitäre Methoden, wie wir sie z.B. aus der DDR kennen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 592

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