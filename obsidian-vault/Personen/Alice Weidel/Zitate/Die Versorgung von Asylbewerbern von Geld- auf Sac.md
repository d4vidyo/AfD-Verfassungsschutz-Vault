---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2025-01-11
topic: Menschenwürde
page_bfv: 933
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 11.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Die Versorgung von Asylbewerbern von Geld- auf Sachleistungen umstellen, Sozialleistungen für Nicht-Aufenthaltsberechtigte streichen und Rückführung im großen Stil durchführen. Und ich muss Ihnen ganz ehrlich sagen: Wenn es dann Remigration heißen soll, dann heißt es eben RE-MIGRATION.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 933

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