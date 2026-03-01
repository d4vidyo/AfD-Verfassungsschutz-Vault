---
type: zitat
speaker: "[[Martin Böhm]]"
date: 2024-01-02
topic: Demokratieprinzip
page_bfv: 570
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Böhm]] vom 2.1.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschland 2023 Nicht nur an Silvester: Migranten-Mob regiert die Straße, Kartell- Parteien das ganze Land!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 570

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