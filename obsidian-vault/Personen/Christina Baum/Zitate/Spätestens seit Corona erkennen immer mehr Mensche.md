---
type: zitat
speaker: "[[Christina Baum]]"
date: 2023-10-21
topic: Menschenwürde
page_bfv: 200
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 21.10.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Spätestens seit Corona erkennen immer mehr Menschen, dass die Welt kopfsteht, dass wir von Politikern und Medien belogen und betrogen werden, dass sie uns wie in Orwells Roman 1984 die Lüge als Wahrheit und die Wahrheit als Lüge verkaufen wollen. [...] Sie wollen durch den Bevölkerungsaustausch mittels Massenmigration, die europäischen Völker abschaffen. Und das ist keine Verschwörungstheorie, sondern Realität!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 200

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