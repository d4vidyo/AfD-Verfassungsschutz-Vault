---
type: zitat
speaker: "[[Peter Felser]]"
date: 2023-04-21
topic: Menschenwürde
page_bfv: 307
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Peter Felser]] vom 21.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Massenschlägereien und Messerangriffe - Meldungen aus dem 'besten Deutschland aller Zeiten' Was die verantwortlichen Politiker aus unserem Land gemacht haben ist unverzeihlich. Kaum ein Tag vergeht, an dem man nicht von neuen Messerangriffen, sexuellen Gewalttaten oder Prügeleien lesen kann. Zum Profil der Täter muss man hier Garnichts sagen. Die Kriminalstatistiken des Bundes sprechen für sich. Allein im Jahr 2022 ist die Gewaltkriminalität um fast 20 Prozent gestiegen. Der Anteil an Ausländern unter den Tatverdächtigen lag bei fast 40 Prozent! Ob ein Migrationshintergrund bei 'deutschen' Tatverdächtigen vorliegt, wird von der Statistik nicht erfasst. [...] Im Bunten Deutschland gehören solche Meldungen inzwischen zum Alltag. Auf diese Gewaltspirale in den deutschen Innenstädten kann es nur eine Antwort geben: harte Strafen und Abschiebungen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 307

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