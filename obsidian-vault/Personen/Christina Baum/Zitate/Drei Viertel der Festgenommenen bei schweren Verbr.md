---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-09-23
topic: Menschenwürde
page_bfv: 136
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 23.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Drei Viertel der Festgenommenen bei schweren Verbrechen wie Mord, Totschlag, Vergewaltigung und sexueller Nötigung hatten einen deutschen Paß mit Migrationshintergrund. Die einfache Lösung: Eine solche Erfassung wird einfach nicht mehr durchgeführt. Somit werden die deutschen Jugendlichen seit August plötzlich krimineller und brutaler und das Märchen von 'alle Menschen sind gleich' kann zumindest für die rot-rot-grüne Wählerschaft mit rosaroter Brille noch aufrechterhalten werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 136

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