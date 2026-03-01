---
type: zitat
speaker: "[[Thomas Dietz]]"
date: 2023-05-10
topic: Demokratieprinzip
page_bfv: 585
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Thomas Dietz]] vom 10.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Dass ausgerechnet in Deutschland Jahrzehnte nach der Bücherverbrennung Menschen mit 'falscher' Meinung wieder reihenweise zensiert, schikaniert, entmenschlicht und verhetzt werden, dass Buchhändler wieder Bücher sortieren, um politisch 'unreine' Bücher aus dem Sortiment zu halten, ist unerträglich. Die Denk- und Verhaltensmuster haben sich leider, anders als erhofft, nur wenig geändert - nur die Erscheinungsformen und vor allem die Lackierung sind andere.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 585

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