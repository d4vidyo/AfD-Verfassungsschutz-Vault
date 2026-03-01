---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2024-04-10
topic: Demokratieprinzip
page_bfv: 542
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 10.4.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wenn wir wirklich souverän werden und uns also von den USA emanzipieren wollen, brauchen wir Partner. Alleine schaffen wir das nicht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 542

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