---
type: zitat
speaker: "[[Daniel Halemba]]"
date: 2024-11-01
topic: Menschenwürde
page_bfv: 363
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Daniel Halemba]] vom 1.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Migration aus Nahost / Afrika ist ein Nettoverlust für uns. Das weiss jeder. Wir dürfen uns jetzt nicht nur um viele Alte, sondern auch um viele versorgungshungrige Migranten kümmern. Die Einwanderung hat unsere Probleme noch verschlimmert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 363

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