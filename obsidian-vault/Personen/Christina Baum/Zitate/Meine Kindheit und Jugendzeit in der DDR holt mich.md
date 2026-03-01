---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-01-26
topic: Demokratieprinzip
page_bfv: 595
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 26.1.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Meine Kindheit und Jugendzeit in der DDR holt mich ein. Damals mussten wir dem Kommunismus und den Bonzen huldigen und zujubeln und den Klassenfeind verteufeln. [...] Ich habe ein Déjà-vu. Die DDR 2.0 ist auferstanden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 595

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