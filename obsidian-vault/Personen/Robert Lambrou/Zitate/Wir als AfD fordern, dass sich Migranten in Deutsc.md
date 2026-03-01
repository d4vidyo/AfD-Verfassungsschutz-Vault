---
type: zitat
speaker: "[[Robert Lambrou]]"
date: 2025-02-20
topic: Menschenwürde
page_bfv: 885
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Robert Lambrou]] vom 20.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir als AfD fordern, dass sich Migranten in Deutschland integrieren, ja assimilieren und keine Parallelgesellschaften aufbauen. [...] Und liebe Freunde... und das ist das Wichtigste: Wir von der AfD fordern ein Ende, ein sofortiges Ende dieser völlig unverantwortlichen und staatsgefährdenden Masseneinwanderung. Es muss Schluss sein!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 885

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