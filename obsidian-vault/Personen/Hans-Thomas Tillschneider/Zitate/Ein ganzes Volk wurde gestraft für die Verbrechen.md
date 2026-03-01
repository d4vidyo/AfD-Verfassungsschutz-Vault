---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2023-09-18
topic: Menschenwürde
page_bfv: 519
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 18.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ein ganzes Volk wurde gestraft für die Verbrechen einer Parteioligarchie, als wäre es selbst durch deren Unrechtsherrschaft allein noch nicht gestraft genug gewesen. [...] Groß war sicherlich die Schuld, aber gnadenlos auch die Strafe – so gnadenlos, daß die Strafe die Schuld gleich welcher Art bis in den letzten Winkel gesühnt und ausgetilgt hat. Wir können das Büßerhemd ein- für allemal ablegen und erhobenen Hauptes allen Völkern dieser Welt gegenübertreten und all diejenigen munter vor den Kopf stoßen, die unsere deutsche Schuld niemals getilgt wissen wollen, und zwar nicht, weil es ihnen um Gerechtigkeit ginge, sondern im Gegenteil, weil es ihnen einzig und allein darum geht, uns in maßloser Verdammung niederzuhalten – oder schlimmer noch – weil es gebrochene Geister sind, die sich nur noch in der Selbsterniedrigung gefallen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 519

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