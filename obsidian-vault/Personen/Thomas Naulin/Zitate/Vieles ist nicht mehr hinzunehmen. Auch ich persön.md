---
type: zitat
speaker: "[[Thomas Naulin]]"
date: 2022-09-08
topic: Demokratieprinzip
page_bfv: 626
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Thomas Naulin]] vom 8.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Vieles ist nicht mehr hinzunehmen. Auch ich persönlich habe vor Richtern gesessen die nicht auf so einem Stuhl sitzen dürften. Diese rückgratlosen Marionetten müssen zur Verantwortung gezogen werden! Ich hoffe diesen Herbst erhebt sich das Volk und jagt dieses ganze verlogene Pack endlich zum Teufel!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 626

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