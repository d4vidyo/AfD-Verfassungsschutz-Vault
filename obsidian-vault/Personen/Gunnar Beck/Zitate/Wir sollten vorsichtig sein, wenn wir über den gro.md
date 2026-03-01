---
type: zitat
speaker: "[[Gunnar Beck]]"
date: 2022-08-13
topic: Menschenwürde
page_bfv: 179
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Beck]] vom 13.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir sollten vorsichtig sein, wenn wir über den großen Austausch #GreatReplacement sprechen, aber die Propagandavideos des @Europarl_DE senden eine ganz klare Botschaft

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 179

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