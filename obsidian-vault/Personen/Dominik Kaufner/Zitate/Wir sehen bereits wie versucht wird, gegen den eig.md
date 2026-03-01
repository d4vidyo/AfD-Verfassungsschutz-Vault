---
type: zitat
speaker: "[[Dominik Kaufner]]"
date: 2023-02-11
topic: Menschenwürde
page_bfv: 187
source: 'www.freilich-magain.com'
status: Unbewertet
---

# Zitat: [[Dominik Kaufner]] vom 11.2.2023 veröffentlicht auf: 'www.freilich-magain.com'
> [!quote] Aussage
>Wir sehen bereits wie versucht wird, gegen den eigentlichen Souverän, das deutsche Volk, zu putschen und die ethnische Wahl als entscheidenden Machtfaktor ins Spiel zu bringen, indem man jedem Illegalen die Staatsbürgerschaft hinterherwirft, um die eigene Wählerbasis zu erweitern und diesen Kurs unumkehrbar zu machen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 187

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