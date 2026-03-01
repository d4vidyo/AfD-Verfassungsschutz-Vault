---
type: zitat
speaker: "[[Eric Engelhardt]]"
date: 2025-01-12
topic: Sonstiges
page_bfv: 866
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Eric Engelhardt]] vom 12.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Der Antrag, der hier im Raum steht, ist weder im Interesse noch der Wille der Jungen Alternative. Richtig ist, dass man sich grundsätzlich für einen Reformprozess ausgesprochen hat. Dieser Antrag ist aber keine Reform, keine Verbesserung, sondern eine Abgliederung und letztlich eine Vernichtung der Jungen Alternative.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 866

**Verfassungsschutz Kategorisierung:** Sonstiges.

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