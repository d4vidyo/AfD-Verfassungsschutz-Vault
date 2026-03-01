---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2023-11-30
topic: Menschenwürde
page_bfv: 227
source: 'Beitrag auf info-direkt.eu'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 30.11.2023 veröffentlicht auf: 'Beitrag auf info-direkt.eu'
> [!quote] Aussage
>Trotz einer dramatischen Haushaltskrise und etlicher Kommunen, die aufgrund des Migrationsdrucks finanziell einbrechen, setzt die Bundesregierung ihre linksgrün-ideologischen Projekte unbeirrt fort. Ihre geplante Einbürgerungsreform würde das Gesicht Deutschlands für immer verändern und stellt damit einen weiteren großen Schritt in Richtung einer unumkehrbaren Abschaffung unseres Landes dar. Die Transformation in eine bunte Multi-Minoritäten-Gesellschaft wäre damit endgültig besiegelt. [...] Entgegen dem unverantwortlichen Ampel-Vorhaben soll nach Ansicht der AfD nur derjenige Teil unserer Schicksalsgemeinschaft werden dürfen, der bereit ist, auch in Krisenzeiten zu Deutschland zu stehen, und sich mit unserer Kulturnation voll identifiziert. Nur wer sich eindeutig für uns entscheidet, soll die deutsche Staatsbürgerschaft erlangen dürfen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 227

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