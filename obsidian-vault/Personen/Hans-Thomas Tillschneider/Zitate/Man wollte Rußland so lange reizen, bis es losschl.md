---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2023-01-13
topic: Demokratieprinzip
page_bfv: 553
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 13.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Man wollte Rußland so lange reizen, bis es losschlägt, um dann mit dem Finger auf den Aggressor zu zeigen. Allerdings denke ich auch, daß die meisten Angehörigen unserer Marionetten-Regierungen in diese Strategie nicht eingeweiht waren. Wozu auch, wenn sie die ihnen zugedachte Rolle auch so spielen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 553

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