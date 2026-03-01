---
type: zitat
speaker: "[[Emil Sänze]]"
date: 2022-10-14
topic: Menschenwürde
page_bfv: 475
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Emil Sänze]] vom 14.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Köln gibt sich auf?! Religionsfreiheit oder Machtdemonstration des politischen Islam? [...] Der Muezzin rief: ,Allah ist der Allergrößte (4mal). Ich bezeuge, dass es keinen Gott außer Allah gibt (2mal). Ich bezeuge, dass Muhammad der Gesandte Allahs ist (2mal). Kommt her zum Gebet (2mal). Kommt her zum Heil (2mal). Allah ist der Allergrößte (2mal). Es gibt keinen Gott außer Allah.' Toleranz hört sich ganz anders an. Die Europäer verhinderten vor Wien die Islamisierung Europas, jetzt werden wir ohne Gegenwehr über Einwanderung islamisiert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 475

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