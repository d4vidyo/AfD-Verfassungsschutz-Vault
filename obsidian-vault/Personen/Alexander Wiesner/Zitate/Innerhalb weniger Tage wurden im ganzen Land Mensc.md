---
type: zitat
speaker: "[[Alexander Wiesner]]"
date: 2024-06-14
topic: Menschenwürde
page_bfv: 292
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Alexander Wiesner]] vom 14.6.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Innerhalb weniger Tage wurden im ganzen Land Menschen von Migranten mit Messern angegriffen und teils lebensgefährlich verletzt. Das sind die Folgen einerkatastrophalen Migrationspolitik! Wir brauchen eine konsequente Remigrations-Kampagne!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 292

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