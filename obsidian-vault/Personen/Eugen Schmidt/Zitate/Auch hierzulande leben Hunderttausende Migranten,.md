---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2022-03-25
topic: Menschenwürde
page_bfv: 166
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom 25.3.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Auch hierzulande leben Hunderttausende Migranten, die nicht zu unserer Kultur passen und den Sozialstaat massiv belasten. Die deutsche Identität ist durch die Masseneinwanderung massiv bedroht. [...] Wir [...] hoffen, dass auch bei uns mehr Menschen beginnen, die alles zerstörende Migrationspolitik zu hinterfragen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 166

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

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