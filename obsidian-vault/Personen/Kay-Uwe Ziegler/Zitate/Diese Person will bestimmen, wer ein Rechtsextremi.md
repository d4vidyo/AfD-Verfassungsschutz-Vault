---
type: zitat
speaker: "[[Kay-Uwe Ziegler]]"
date: 2024-02-15
topic: Demokratieprinzip
page_bfv: 630
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Kay-Uwe Ziegler]] vom 15.2.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Diese Person will bestimmen, wer ein Rechtsextremist ist und was eine Verhöhnung des Staates darstellt! DIE DIKTATUR BEGINNT JETZT! [...] In ihrem Umfeld werden Menschen, die nicht geimpft sind oder an zwei statt 170 Geschlechter glauben, als rechtsextrem bezeichnet. Faesers Behörde kann nun wirklich jeden willkürlichen Vorwand nehmen, um Menschen zu überwachen und zu diskriminieren. Unser Rechtsstaat wird in aller Öffentlichkeit demontiert. Ein antidemokratisches, dystopisches Szenario, das nur Ihr mit Eurer Stimme verhindern könnt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 630

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