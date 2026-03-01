---
type: zitat
speaker: "[[Daniel Haseloff]]"
date: 2022-11-01
topic: Menschenwürde
page_bfv: 190
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Daniel Haseloff]] vom 1.11.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Einbürgerung steigt massiv an. Anzahl der Einbürgerungen hat sich seit 2015 vervierfacht! Jeder zweite Neubürger stammt aus Syrien, gefolgt vom Irak und der Ukraine. Der rapide Anstieg der Einbürgerungszahlen kommt einer Verramschung der deutschen Staatsbürgerschaft gleich. [...] Wir stehen gegen die verdeckte Masseneinwanderung, die das humanitäre Anliegen als Hebel nutzt, um die Zusammensetzung unseres Volkes im großen Maßstab zu verändern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 190

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