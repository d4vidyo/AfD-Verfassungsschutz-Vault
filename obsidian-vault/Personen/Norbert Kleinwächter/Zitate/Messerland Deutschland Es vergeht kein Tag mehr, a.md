---
type: zitat
speaker: "[[Norbert Kleinwächter]]"
date: 2024-07-23
topic: Menschenwürde
page_bfv: 292
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Norbert Kleinwächter]] vom 23.7.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Messerland Deutschland Es vergeht kein Tag mehr, an dem kein Messermann in Deutschland wütet. Jetzt hat es Berlin getroffen. Nur Polizei-Schüsse konnten schlimmeres verhindern - Verhältnisse wie in einem Bürgerkriegsland. die wir so früher nur aus schlechten Filmen kannten. Beenden wir diese miese Kino-Vorführung und lassen wir den Vorhang für Ampel und Altparteien fallen. Ohne Applaus und ohne Zugabe. Es reicht!

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