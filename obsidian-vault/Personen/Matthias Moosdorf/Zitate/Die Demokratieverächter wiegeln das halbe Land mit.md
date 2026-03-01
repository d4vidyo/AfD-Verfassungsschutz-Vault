---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2024-02-02
topic: Demokratieprinzip
page_bfv: 605
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 2.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Demokratieverächter wiegeln das halbe Land mit ihren Lügen auf und was? Die AfD verliert 1 Prozent in den Umfragen im Bund. In manchen Ländern gewinnt sie noch dazu? So ist es, die Menschen lassen sich von dieser Regierung und ihren Stasi-Helfern nicht mehr für dumm verkaufen. Wir werden weiterwachsen, Wahlen gewinnen und dieses Land aufräumen. Jetzt einfach weiter unsere Alternativen kommunizieren und die unsäglichen Vaterlandsverräter ihre Fehler weitermachen lassen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 605

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