---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-09-26
topic: Demokratieprinzip
page_bfv: 645
source: 'www.welt.de'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 26.9.2024 veröffentlicht auf: 'www.welt.de'
> [!quote] Aussage
>Ich werde jetzt nicht aus meinem strategischen Nähkästchen plaudern. Sie können sicher sein, dass wir als AfD Thüringen eine sehr weitreichende strategische Planung haben. Selbst wenn Jürgen Treutler seinen Wahlkreis nicht gewonnen hätte, wäre unser Abgeordneter Wolfgang Lauerwald Alterspräsident geworden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 645

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