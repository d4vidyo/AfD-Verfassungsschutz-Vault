---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023
topic: Menschenwürde
page_bfv: 117
source: '"Politik von rechts. Ein Manifest", Schnellroda 2023'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 2023 veröffentlicht auf: '"Politik von rechts. Ein Manifest", Schnellroda 2023'
> [!quote] Aussage
>Rechte Politik bekennt sich zum Volk, das ist mehr als die Gemeinschaft der Staatsbürger. [...] Volk ist Schicksal. Volk ist Realität. [...] Eine Gemeinschaft, die ehrlich und rechtstreu ist, die vertraut und Vertrauen gewährt, ist einer solchen, die derlei nicht praktiziert, überlegen. Der ehrliche Einzelne ist aber in einer Gesellschaft der Unehrlichen hoffnungslos verloren. Deshalb sind Anstand, Ehrlichkeit und Vertrauen nur zu gewinnen, wenn Völker in ihrem ethnischen Substrat Bestand haben, wenn ihre positiven Eigenschaften durch die Homogenität der ebenso Geprägten zum Vorteil aller werden, statt daß sie dem Einzelnen im unbarmherzigen Selbstbehauptungskampf unter Fremden zum Nachteil gereichen. Ohne den Schutzraum des Volkes verschwindet deshalb jede Eigentümlichkeit und Liebenswürdigkeit; ja alles, was den Kampf ums nackte Überleben übersteigt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 117

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