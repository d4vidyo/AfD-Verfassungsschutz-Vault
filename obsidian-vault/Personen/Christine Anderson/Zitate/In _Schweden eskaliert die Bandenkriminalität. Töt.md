---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2023-01-23
topic: Menschenwürde
page_bfv: 272
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 23.1.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>In #Schweden eskaliert die Bandenkriminalität. Töten oder getötet werden ist das Motto im kriminellen #Migranten-Sumpf. #Stockholm ist nur die Blaupause dessen, was #Deutschland und der #EU droht, wenn #Migration ohne Grenzen fortgesetzt wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 272

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