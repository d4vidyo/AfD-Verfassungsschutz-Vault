---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-07-09
topic: Menschenwürde
page_bfv: 402
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 9.7.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Wir brauchen dringend eine Abschiebekultur! Wir sind nicht das Sozialamt der Welt. Wir sind nicht der historische Müllhaufen für alle Verbrechen dieser Welt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 402

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