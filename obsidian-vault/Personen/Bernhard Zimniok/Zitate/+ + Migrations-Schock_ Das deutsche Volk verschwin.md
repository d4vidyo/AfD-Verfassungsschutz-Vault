---
type: zitat
speaker: "[[Bernhard Zimniok]]"
date: 2023-06-29
topic: Menschenwürde
page_bfv: 194
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Bernhard Zimniok]] vom 29.6.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>+ + Migrations-Schock: Das deutsche Volk verschwindet! + + Der Bevölkerungsaustausch sei eine Verschwörungstheorie, hört man immer wieder. Erstmals beweist der EU-Abgeordnete Bernhard Zimniok anhand der Daten des Statistischen Bundesamtes in einer interaktiven Karte auf www.demografie-europa.eu/deutschland das Gegenteil: Der Bevölkerungsaustausch ist real, das deutsche Volk droht zu verschwinden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 194

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