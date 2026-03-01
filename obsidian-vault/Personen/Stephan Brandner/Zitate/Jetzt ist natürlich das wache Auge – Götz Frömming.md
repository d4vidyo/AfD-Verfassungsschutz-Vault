---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2024-09-13
topic: Nationalsozialismus
page_bfv: 695
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 13.9.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Jetzt ist natürlich das wache Auge – Götz Frömming ist ja zuständig für Social Media in unserer Fraktion. [...] Da können wir uns jetzt hier keinen Fauxpas erlauben, ne?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 695

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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