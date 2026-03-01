---
type: zitat
speaker: "[[Nils Hartwig]]"
date: 2022-06-25
topic: Menschenwürde
page_bfv: 372
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Nils Hartwig]] vom 25.6.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Auch in Westdeutschen, eher provinziellen Kleinstädten beginnt eine immer offenere und aggressivere Landnahme durch afrikanische Zuwanderer. Afrikaner prägen längst das Stadtbild. Unser Volk kann nur mit einer Politik der Null- Zuwanderung überleben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 372

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