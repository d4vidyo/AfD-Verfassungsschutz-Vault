---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-05-05
topic: Menschenwürde
page_bfv: 169
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 5.5.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Menschen sind nicht beliebig verschiebbar. Kultur und Prägung können (zum Glück) nicht beliebig ausgetauscht werden. Wer Afrika einwandern lässt, ersetzt nicht deutsche Fachkräfte, sondern wird afrikanisch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 169

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