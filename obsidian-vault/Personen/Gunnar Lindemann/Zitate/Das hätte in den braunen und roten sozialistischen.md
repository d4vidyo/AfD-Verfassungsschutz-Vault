---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2022-08-27
topic: Demokratieprinzip
page_bfv: 623
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 27.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das hätte in den braunen und roten sozialistischen Diktaturen der Vergangenheit nicht besser gelöst werden können. Offenbar will das bunte Regime hier vorsorgen und im Fall der befürchteten Energieproteste ein Mittel zur Hand haben, den Souverän seiner Grundrechte zu berauben. Merken Sie sich diejenigen, die diese Willkürmaßnahmen im Bundestag durchwinken. Diese Leute haben sich von Demokratie und Rechtsstaatlichkeit endgültig verabschiedet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 623

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