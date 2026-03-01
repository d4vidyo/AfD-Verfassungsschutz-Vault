---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-07-13
topic: Menschenwürde
page_bfv: 115
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 13.7.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Wir dürfen nicht zulassen, dass [...] man zum ,deutschen Volk‘ nicht mehr durch Abstammung gehört sondern durch Übertreten der Landesgrenze und ‚Demokratie’ nicht mehr die Herrschaft des Volkes, sondern Übereinstimmung mit rotgrünen Ideologien ist. Auf Dauer schafft man so eine beliebig manipulier- und korrumpierbare Masse von Individuen, die zudem ausschließlich auf den eigenen Vorteil bedacht ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 115

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