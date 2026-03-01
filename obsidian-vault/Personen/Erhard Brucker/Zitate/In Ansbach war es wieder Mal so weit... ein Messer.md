---
type: zitat
speaker: "[[Erhard Brucker]]"
date: 2022-09-09
topic: Menschenwürde
page_bfv: 478
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Erhard Brucker]] vom 9.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>In Ansbach war es wieder Mal so weit... ein Messermoslem verbreitete im Auftrag der Religion des Friedens seinen Missionssauftrag. Die lokale Presse und Polizei überprüfen bereits ob das Motiv des Allahu Akbarschreiers irgendwas mit dem Islams zu tun haben könnte .... wahrscheinlich handelt es sich aber wie immer um einen psychisch kranken Einzeltäter... dem so gut wie nichts passieren würde ( wenn ihm in diesem Fall die Polizei nicht seinen sehnlichsten Wunsch erfüllt hätte und er nun bei 72 Huris sitzt), während man Islamkritiker schon mal für 6 Monate einsperren kann ... irres Deutschland !

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 478

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