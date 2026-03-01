---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-12-20
topic: Menschenwürde
page_bfv: 209
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 20.12.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Diese #Ersatzmigration muß ein Ende finden, damit wir in Deutschland wieder in Sicherheit leben können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 209

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