---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2023-01-07
topic: Menschenwürde
page_bfv: 321
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 7.1.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Unkontrollierte Masseneinwanderung importiert Gewalt, Kriminalität und destabilisiert die Aufnahmegesellschaft. Unser Rechtsstaat, unsere Art zu leben und unsere Werte sind ernsthaft in Gefahr.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 321

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