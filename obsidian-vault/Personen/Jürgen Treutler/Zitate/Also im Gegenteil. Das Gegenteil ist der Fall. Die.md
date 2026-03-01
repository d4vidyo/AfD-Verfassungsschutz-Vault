---
type: zitat
speaker: "[[Jürgen Treutler]]"
date: 2024-09-26
topic: Demokratieprinzip
page_bfv: 645
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jürgen Treutler]] vom 26.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Also im Gegenteil. Das Gegenteil ist der Fall. Die haben ja einen Antrag eingebracht zur Geschäftsordnung. Sie wollten das durchsetzen und ich habe das dann verhindert, weil die wollten quasi sofort die Wahl durchführen. Dass nicht nach bisherigen Gegebenheiten, sondern jede Fraktion jemanden vorschlagen kann. Und es war ja auch im Beifall zu sehen, dass sich dann wieder alle auf einen Kandidaten vereinigt hätten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 645

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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