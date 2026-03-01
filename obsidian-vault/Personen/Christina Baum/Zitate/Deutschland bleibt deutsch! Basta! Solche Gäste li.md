---
type: zitat
speaker: "[[Christina Baum]]"
date: 2021-02-03
topic: Menschenwürde
page_bfv: 114
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 3.2.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschland bleibt deutsch! Basta! Solche Gäste lieben die Grünen besonders. Dieser junge Mann soll in Syrien seinen Beitrag für sein Volk leisten. Er wird dort dringend gebraucht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 114

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