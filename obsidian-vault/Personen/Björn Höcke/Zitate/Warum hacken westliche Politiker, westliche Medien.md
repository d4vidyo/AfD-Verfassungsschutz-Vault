---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-10-03
topic: Demokratieprinzip
page_bfv: 547
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 3.10.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Warum hacken westliche Politiker, westliche Medien [...] regelmäßig auf Ländern wie Rußland, Ungarn und Serbien herum? [...] liegt es vielleicht daran, daß sich diese Länder und ihre Staatslenker gegen die Veralberung der Tradition und Geschichte entschieden haben, gegen die ungebremste Einwanderung, gegen die Transformation ihrer Völker in eine gesichtslose Masse von perfekt durchmaterialisierten Konsumfaschisten? Ist es dieser Widerstand, der den 'neuen Westen', den alten klassisch-liberalen gibt es zu meinem Leidwesen nicht mehr, so provoziert?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 547

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