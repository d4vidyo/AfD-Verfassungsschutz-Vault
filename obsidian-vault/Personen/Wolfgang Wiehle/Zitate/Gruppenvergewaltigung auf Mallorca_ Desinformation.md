---
type: zitat
speaker: "[[Wolfgang Wiehle]]"
date: 2023-07-17
topic: Menschenwürde
page_bfv: 144
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Wolfgang Wiehle]] vom 17.7.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gruppenvergewaltigung auf Mallorca: Desinformation durch deutsche Medien! Fünf Passdeutsche wurden auf Mallorca verhaftet - Verdacht: Gruppenvergewaltigung! Alle Tatverdächtigen haben Migrationshintergrund. Sie bringen den Namen Deutschlands international in Verruf. [...] Das ist ein Armutszeugnis und zeigt Scheuklappen auf, die einerseits für das deutsche Opfer unwürdig sind, andererseits die Diskussion um eine gescheitere Integration sowie eine zu schnelle Vergabe der Staatsbürgerschaft im Keim ersticken (sollen). Desinformation scheint vielen Medien in Fleisch und Blut übergegangen zu sein. Wer steckt dahinter und versucht, die Probleme zu verschleiern? Die Wahrheit muss auf den Tisch! \<Bild Als 'Deutsche' bezeichnet man die Verhafteten. Formal korrekt, und dennoch Desinformation!\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 144

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