---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-06-30
topic: Menschenwürde
page_bfv: 380
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 30.6.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die bunte & vielfältige Dystopie nimmt Gestalt an: Andauernde Krawalle in Frankreich, erstes Überschwappen auf Brüssel. Die Masseneinwanderung aus fremden Kulturen ist gescheitert, sie zerstört Europa. Aber Ampel & CDU wollen mehr davon.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 380

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