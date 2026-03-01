---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2023-09-18
topic: Menschenwürde
page_bfv: 519
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 18.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wenn einem 52jährigen Mann ein Flugblatt nachgetragen wird, in dem er als Schüler vor 35 Jahren darüber phantasiert haben soll, Vaterlandsverräter ins KZ zu schicken, dann ist das, was wir heute zu kritisieren haben, nicht die unbeholfene Provokation des pubertären Gernegroß von einst, sondern das schäbige Aufblasen einer solchen jugendlichen Verirrung, um draus Kapital zu schlagen. [...] Und deshalb stürzen sie sich auf Flugblätter, die dumme Jungen vor 35 Jahren verbreitet haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 519

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