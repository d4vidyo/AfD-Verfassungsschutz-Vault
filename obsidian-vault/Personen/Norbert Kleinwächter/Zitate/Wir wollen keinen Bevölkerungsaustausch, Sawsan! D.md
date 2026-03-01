---
type: zitat
speaker: "[[Norbert Kleinwächter]]"
date: 2025-01-21
topic: Menschenwürde
page_bfv: 893
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Norbert Kleinwächter]] vom 21.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir wollen keinen Bevölkerungsaustausch, Sawsan! Die #SPD-Politikerin Sawsan Chebli hetzt ihre muslimischen Anhänger zur Übernahme Deutschlands auf:,Demographie wird Fakten schaffen.' Die #Regierung schweigt. Ich nicht:

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 893. gehört zum Video vom 21.1.2025

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