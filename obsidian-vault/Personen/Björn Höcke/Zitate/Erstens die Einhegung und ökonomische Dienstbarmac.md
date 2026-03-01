---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-05-01
topic: Demokratieprinzip
page_bfv: 545
source: 'ZUERST Magazin'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom Mai 2022 veröffentlicht auf: 'ZUERST Magazin'
> [!quote] Aussage
>Erstens die Einhegung und ökonomische Dienstbarmachung Deutschlands durch die 'europäische Integration'[...]. Zweitens durch die Massenmigration und Multikulturalisierung, um das neu entflammte Gemeinschaftsgefühl der Deutschen abzuwürgen und fremdenfeindliche Tendenzen anzustacheln, die wiederum eine willkommene Vorlage für den dritten Angriff bildeten: den damals ausgerufenen, gnadenlosen 'Kampf gegen rechts'. Der war natürlich nur vordergründig gegen obskure extremistische Kleinstgruppen, aber vor allem gegen jede nationale Regung gerichtet.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Mai 2022

**SPIEGEL-Notiz:** Gutachten Seite: 545

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