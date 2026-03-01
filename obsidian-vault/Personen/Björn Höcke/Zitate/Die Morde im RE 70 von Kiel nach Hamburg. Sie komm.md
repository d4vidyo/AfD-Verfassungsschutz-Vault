---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-01-26
topic: Menschenwürde
page_bfv: 361
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 26.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Morde im RE 70 von Kiel nach Hamburg. Sie kommen als ‚Schutzsuchende‘, sie bleiben als Straftäter. [...] Versprochen wurden uns ‚Fachkräfte‘, bezahlen tun wir überwiegend Sozialtouristen, die darüber hinaus viel zu oft eine Gefahr für unsere Gesellschaft, ja - mit Blick auf die letzten Silvesterkrawalle - sogar für die Stabilität des Staates sind. [...] Klar ist: Mit dem Staatsversagen schreitet der Staatsverfall voran.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 361

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