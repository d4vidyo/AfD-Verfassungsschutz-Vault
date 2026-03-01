---
type: zitat
speaker: "[[Gereon Bollmann]]"
date: 2024-06-11
topic: Menschenwürde
page_bfv: 349
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gereon Bollmann]] vom 11.6.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Grafik\> 7000 Gruppenvergewaltigungen in 10 Jahren Zuvor unbekannte Verbrechen traurige Realität in Deutschland durch Masseneinwanderung

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 349

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