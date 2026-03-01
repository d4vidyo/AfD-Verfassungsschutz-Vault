---
type: zitat
speaker: "[[Stephan Protschka]]"
date: 2024-02-22
topic: Demokratieprinzip
page_bfv: 581
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Stephan Protschka]] vom 22.2.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>All diese Dinge wiederholen sich heute. Doch es ist nicht die AfD, die dafür verantwortlich ist. Es sind die Sozialisten der SPD und ihre Koalitionspartner, die Grünen und die FDP. Wir sind nicht das Problem, wir sind die Lösung! Deshalb überlege dir gut, mit wem und wogegen du auf die Straße gehst. Denn 1933 ist näher, als du denkst!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 581. es wird ein Bild aus dem vorherigen Post kommentiert

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