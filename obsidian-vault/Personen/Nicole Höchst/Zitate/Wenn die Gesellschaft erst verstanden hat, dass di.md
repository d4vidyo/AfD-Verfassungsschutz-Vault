---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-12-06
topic: Demokratieprinzip
page_bfv: 539
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 6.12.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wenn die Gesellschaft erst verstanden hat, dass die derzeitigen Nöte und Probleme geschaffen wurden, damit die von langer Hand erdachten 'Lösungen' eingesetzt werden können, dann wird sie anfangen, die abgrundtiefe Bösartigkeit derer zu begreifen, die das Ganze orchestrieren und davon profitieren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 539

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