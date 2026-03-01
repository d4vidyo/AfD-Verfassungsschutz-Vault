---
type: zitat
speaker: "[[Peter Boehringer]]"
date: 2023-01-08
topic: Menschenwürde
page_bfv: 385
source: 'freilich-magazin.com'
status: Unbewertet
---

# Zitat: [[Peter Boehringer]] vom 8.1.2023 veröffentlicht auf: 'freilich-magazin.com'
> [!quote] Aussage
>Hier wurde natürlich seit Jahrzehnten unglaublich viel kaputtgeschlagen - ich unterstelle hier ganz klar ABSICHT der linken Kulturmarxisten, obwohl man immer auch alles mit ideologischer Dummheit (woke-ideologische LEERpläne statt naturwissenschaftlicher, faktenorientierter Lehrpläne) erklären könnte; oder mit falschem Moralismus (Zuwanderung von bildungsfernsten Analphabeten und kulturell kaum kompatiblen Menschen).

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 385

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