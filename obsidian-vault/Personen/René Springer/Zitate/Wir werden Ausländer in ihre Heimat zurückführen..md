---
type: zitat
speaker: "[[René Springer]]"
date: 2024-01-10
topic: Menschenwürde
page_bfv: 419
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 10.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir werden Ausländer in ihre Heimat zurückführen. Millionenfach. Das ist kein #Geheimplan. Das ist ein Versprechen. Für mehr Sicherheit. Für mehr Gerechtigkeit. Für den Erhalt unserer Identität. Für Deutschland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 419

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