---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2024-05-10
topic: Nationalsozialismus
page_bfv: 689
source: 'Freilich-Magazin'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 10.5.2024 veröffentlicht auf: 'Freilich-Magazin'
> [!quote] Aussage
>Für die deutsche Armee freilich war der 8. Mai eine Niederlage. Jeder Soldat will den Krieg, in dem er kämpft, gewinnen. Die Politik interessiert ihn nicht. Er ist ein Arbeiter im Kriegshandwerk. Er trifft keine Entscheidungen, er empfängt Befehle. Wird er missbraucht, trifft ihn keine oder nur eine sehr reduzierte und spezielle Verantwortung. Die durch das Hitlerregime missbrauchte Wehrmacht war am 8. Mai besiegt worden. [...] Der 8. Mai: Tag der militärischen Niederlage.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 689

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