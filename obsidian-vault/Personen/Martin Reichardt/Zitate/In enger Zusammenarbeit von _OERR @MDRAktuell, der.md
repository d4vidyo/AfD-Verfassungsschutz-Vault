---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2024-02-08
topic: Sonstiges
page_bfv: 722
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 8.2.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>In enger Zusammenarbeit von #OERR @MDRAktuell, der linken Lügen- & Agitationsplattform #Correctiv wird Zensur umgesetzt und schöngeredet! Als Scheinlegitimation gilt noch eine Petition, die ca. 100000 Zeichner hat! [Deutschland-Flagge] wird immer mehr zur linken Gesinnungsdiktatur! Man muss nicht alles teilen, was @COMPACTMagazin schreibt, aber dieses Vorgehen ist ein Schlag gegen die Presse- & Meinungsfreiheit!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 722

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