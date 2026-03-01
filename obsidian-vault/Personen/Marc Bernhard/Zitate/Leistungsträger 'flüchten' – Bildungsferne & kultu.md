---
type: zitat
speaker: "[[Marc Bernhard]]"
date: 2022-07-04
topic: Menschenwürde
page_bfv: 388
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marc Bernhard]] vom 4.7.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Leistungsträger 'flüchten' – Bildungsferne & kulturfremde Migranten wandern ein! Wenn nicht gerade zufällig ein G7-Gipfel drei Tage lang für sichere Grenzen sorgt dann nimmt die ungebremste Massenmigration nach Deutschland ihren Lauf. […] Eingewandert sind überwiegend Bevölkerungsgruppen, die von den Altparteien als 'Fachkräfte' oder 'Ortskräfte' bezeichnet werden. Studien belegen, dass diese Migrantenkategorie eine lebenslange Nettobelastung für die Volkswirtschaft darstellt, ganz zu schweigen davon, dass sie nicht ansatzweise den Fachkräftemangel beheben könnten!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 388

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