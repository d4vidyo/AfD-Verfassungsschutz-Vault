---
type: zitat
speaker: "[[Nicolaus Fest]]"
date: 2022-09-09
topic: Menschenwürde
page_bfv: 432
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicolaus Fest]] vom 9.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Warum kritisiert die EU Polen und Ungarn, sagt aber nichts zur Verfolgung, Tötung und Diskriminierung sexueller Minderheiten in fast allen afrikanischen Ländern? Ich weiß es nicht, aber ich vermute, die links-woke Truppe um Ursula von der Leyen tut sich leichter damit, zivilisierte Weiße zu kritisieren als schwerverbrecherische Farbige.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 432

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