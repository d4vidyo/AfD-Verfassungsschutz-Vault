---
type: zitat
speaker: "[[Stefan Möller]]"
date: 2025-01-18
topic: Demokratieprinzip
page_bfv: 959
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Stefan Möller]] vom 18.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Dieser Staat ist repressiv geworden und zwar ziemlich unverblümt. Wenn man beispielsweise jetzt die Forderung von Nancy Faeser anguckt, dass Polizisten entlassen werden, nur weil sie in der falschen Partei sind. Oder wenn wir anschauen, dass diese Woche ein Soldat entlassen worden ist aus dem Knast, der dort reingekommen ist, weil er sich nicht hat impfen lassen, weil er keine Lust hatte, eine experimentelle Impfung zu ertragen. Das ist Deutschland 2024 und das ist Deutschland noch 2025 und das müssen wir ändern. Denn das, was diese Politiker, unsere Konkurrenten, unsere [Anm.: zeigt Anführungsstriche] Demokratie nennen, das ist gar nicht unsere Demokratie, sondern das, was sie meinen, ist deren Macht. Es geht um deren Macht. Denn mit Demokratie hat das alles nicht viel zu tun, für Demokratie reicht‘s nicht, dass man wählen gehen kann, das gibt’s auch in Staaten, die nicht demokratisch sind. Denn dazu muss es auch entsprechend fair zugehen. Da gehört ne ganze Menge mehr dazu.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 959

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