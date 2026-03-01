---
type: zitat
speaker: "[[Dirk Spaniel]]"
date: 2024-03-16
topic: Menschenwürde
page_bfv: 468
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Dirk Spaniel]] vom 16.3.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die links-grün-bunte Propaganda will Deutschland als ursprüngliche und eigenständige Nation und Kulturgemeinschaft durch die seit Jahren politisch forcierte Verdrängungsmigration quasi auslöschen -zur Bedeutungslosigkeit marginalisieren. Auf allen Kanälen werden die Bürger tagaus, tagein pausenlos mit dem Mantra von Vielfalt, Toleranz und Weltoffenheit malträtiert. Dabei sind die Mehrheit der Deutschen gegen diese Demutsgesten und Lichtergirlanden...

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 468

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