---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-09-16
topic: Demokratieprinzip
page_bfv: 552
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 16.9.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Das ist seit eh und je die antideutsche Politik der Unterwerfung unter die Mächte, die aus dem Westen hereindrängen. Das ist die Zerstörung des Rechts im Namen der Menschenrechte. Das ist das Regiment des Regenbogens. Das ist der Globalismus, gepaart mit dem Opportunismus und dem ganz individuellen Egoismus deutscher Fürsten und Altparteifunktionären.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 552

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