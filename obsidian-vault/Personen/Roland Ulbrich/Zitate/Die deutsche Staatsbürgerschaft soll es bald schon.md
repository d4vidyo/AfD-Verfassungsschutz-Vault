---
type: zitat
speaker: "[[Roland Ulbrich]]"
date: 2022-12-09
topic: Menschenwürde
page_bfv: 140
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Roland Ulbrich]] vom 9.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die deutsche Staatsbürgerschaft soll es bald schon als Begrüßungsgeschenk geben. Was für die grünen Deutschland-Zerstörer zwei unschätzbare Vorteile hat: Man schafft sich neue Wählergruppen. Und 'reduziert' gleichzeitig die Ausländer-Kriminalität - zumindest optisch. Denn jeder eingebürgerte Killer ist in der Statistik ein 'deutscher' Straftäter. So ergibt das Mantra der Woke-Fanatiker 'Deutsche machen das auch' sogar einen Sinn.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 140

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