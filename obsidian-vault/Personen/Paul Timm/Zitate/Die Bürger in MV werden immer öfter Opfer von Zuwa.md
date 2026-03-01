---
type: zitat
speaker: "[[Paul Timm]]"
date: 2023-01-22
topic: Menschenwürde
page_bfv: 144
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Paul Timm]] vom 22.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Bürger in MV werden immer öfter Opfer von Zuwanderergewalt. Viele der Asylbewerber, Zuwanderer und Passdeutsche mit Migrationshintergrund sind entweder nicht fähig oder nicht willens, sich zu integrieren. [...] Die Ampel in Berlin und Rot-Rot in Schwerin haben die Kontrolle über die Zuwanderer verloren. Wohlgemerkt: es geht nicht um Ukrainer, welche unserer Kultur in weiten Teilen nahe sind. Es geht um Kopftuch-Apologeten, Messermänner und neuerdings auch Brandstifter aus den islamisch geprägten Ländern der Erde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 144

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