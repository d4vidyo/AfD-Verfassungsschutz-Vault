---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2025-01-22
topic: Menschenwürde
page_bfv: 906
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 22.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>DAS SCHLACHTEN GEHT WEITER Die Messerangriffe, die unweigerlich mit der gescheiterten Migrationspolitik zusammenhängen, reißen nicht ab. [...] Mitverantwortlich sind Merkel und alle, die die Invasion unseres Landes ermöglicht haben. [...] Jetzt hilft nur eines: Konsequente Remigration. Wir werden diesen importierten Terror beenden und dafür sorgen, dass unsere Heimat wieder sicher wird. Wir lassen es uns nicht bieten, dass Menschen in unserem Land abgeschlachtet werden!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 906

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