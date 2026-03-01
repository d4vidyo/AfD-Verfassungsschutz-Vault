---
type: zitat
speaker: "[[Bernd Schattner]]"
date: 2022-10-19
topic: Menschenwürde
page_bfv: 294
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Bernd Schattner]] vom 19.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Es ist gefährlich geworden in Deutschland. Messerangriffe gehören quasi zur Tagesordnung. Kandel. Würzburg. Ludwigshafen. Zwei Menschen mussten gestern ihr Leben geben, weil unsere Regierung stur an der Politik der offenen Grenzen festhält. Wer seine Grenzen nicht kontrolliert, riskiert den Import tickender Zeitbomben! [...] Es wirkt, als habe sich Deutschland an Messermorde gewöhnt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 294

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