---
type: zitat
speaker: "[[Carolin Bachmann]]"
date: 2023-02-14
topic: Menschenwürde
page_bfv: 152
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Carolin Bachmann]] vom 14.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>### SIND WIR IN AFRIKA!?### Blättern im neuen Tchibo Katalog 'Sunday style' führt unvermeidbar zu der Frage, ob denn in Deutschland alle SCHWARZ sind !? Während in Nigeria Models mit heller Haut nicht mehr auf Werbeplakaten zu sehen sind, sogar ein 'Verbot für die Verwendung ausländischer Models und Sprecher für jegliche Werbung'!! besteht, lassen wir DEUTSCHE uns STOLZ und EHRE rauben, ohne uns zu wehren.... WOHIN FÜHRT DIESER WEG, DER NICHT DER UNSERE SEIN KANN?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 152

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