---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2025-02-08
topic: Nationalsozialismus
page_bfv: 979
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 8.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und ich bin froh, dass diese Menschen sich zu uns stellen, häufig sogar mutiger sind, weil sie nicht durch die Schuldkultmühlen des Establishments getrieben wurden und uns auch animieren zu sagen:'Kämpft um unsere gemeinsame Heimat. Wir stehen an eurer Seite.'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 979

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