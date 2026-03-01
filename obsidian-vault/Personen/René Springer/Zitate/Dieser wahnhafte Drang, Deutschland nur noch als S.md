---
type: zitat
speaker: "[[René Springer]]"
date: 2023-03-12
topic: Menschenwürde
page_bfv: 367
source: 'Heimatkurier'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 12.3.2023 veröffentlicht auf: 'Heimatkurier'
> [!quote] Aussage
>Dieser wahnhafte Drang, Deutschland nur noch als Siedlungsgebiet für fremde Völker zu betrachten und dieses überhebliche Sendungsbewusstsein, der ganzen Welt das eigene Übel aufzuzwingen, wird gern mit superhumanistischen Begründungen kaschiert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 367

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