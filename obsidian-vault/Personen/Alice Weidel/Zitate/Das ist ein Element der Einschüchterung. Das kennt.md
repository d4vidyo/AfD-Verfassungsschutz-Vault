---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2025-02-01
topic: Demokratieprinzip
page_bfv: 957
source: 'Videoeinspieler'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 1.2.2025 veröffentlicht auf: 'Videoeinspieler'
> [!quote] Aussage
>Das ist ein Element der Einschüchterung. Das kennt man aus der DDR, dann ist man da gleich nach Hohenschönhausen geschafft worden. Ich kann nur jedem empfehlen, sich das mal anzugucken, was die mit den Menschen, mit Regimekritikern, die Honecker als Faschisten bezeichnet hat, was man mit den Menschen in Hohenschönhausen gemacht hat.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 957

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