---
type: zitat
speaker: "[[Sebastian Wippel]]"
date: 2023-11-11
topic: Menschenwürde
page_bfv: 141
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Wippel]] vom 11.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gewalt gegen Polizisten erreicht neues Allzeithoch – Ein importiertes Problem! [...] Insgesamt 30,1 Prozent aller Tatverdächtigen bei Gewalttaten gegen Polizisten waren Ausländer - passdeutsche Migrationshintergründler sind hierbei natürlich noch nicht miterfasst.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 141

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