---
type: zitat
speaker: "[[Klaus Gagel]]"
date: 2025-01-14
topic: Demokratieprinzip
page_bfv: 968
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Klaus Gagel]] vom 14.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Während des vergangenen Wochenendes wurde in Riesa auf unserem Bundesparteitag über die Kanzlerkandidatur unserer Spitzenkandidatin Alice Weidel ab- und mit großer Mehrheit dafür gestimmt. Die AfD stellt damit erstmals einen Kanzlerkandidaten. Die deutschen Bevölkerung hat damit nun auch endlich Aussicht auf eine potentielle Kanzlerin, die tatsächlich deutsche Interessen vertritt. Und dies ist auch bitter notwendig. Nach über zwanzig Jahren antideutscher Politik der Altparteien steht unser Land so schlecht da wie noch nie in der jüngeren Geschichte der Bundesrepublik.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 968

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