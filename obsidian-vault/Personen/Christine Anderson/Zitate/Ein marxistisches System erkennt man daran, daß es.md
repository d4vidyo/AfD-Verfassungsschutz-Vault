---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2022-08-15
topic: Menschenwürde
page_bfv: 303
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 15.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ein marxistisches System erkennt man daran, daß es die Kriminellen verschont und den politischen Gegner kriminalisiert. (A. Solschenizyn) Marxistisches System? Lächerlich! [Deutschland-Flagge] ist noch besser. Wir verehren Kriminelle! Jetzt alle zusammen: 'Messerstecher Lives Matter'!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 303

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