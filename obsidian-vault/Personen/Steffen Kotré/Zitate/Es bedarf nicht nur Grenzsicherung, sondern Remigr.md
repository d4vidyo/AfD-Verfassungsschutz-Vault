---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2025-01-23
topic: Menschenwürde
page_bfv: 906
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 23.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Es bedarf nicht nur Grenzsicherung, sondern Remigration. [...] Abschiebung im großen Stil und Brot, Bett und Seife. Das heißt keinen einzigen Euro mehr für jemanden, der abgelehnt ist, der nicht in unserem Land sein darf und der sich auch sonst wie hier bei uns nicht integriert. Und dieses Programm gibt es nur mit der AfD. Aber wenn wir jetzt gucken, wie die Medien darauf reagieren, dann sind immer andere schuld, aber nur nicht die, die hier diese Leute ins Land gelassen haben. Dann sind es mal die Männer, die schuld sein sollen. Nein, es liegt nicht daran, dass es Männer sind, sondern Leute aus kulturfremden Räumen, die von fast Kriminellen in den Behörden und in der Bundesregierung hier reingelassen worden sind. Und es liegt auch nicht daran, dass sie jung sind. Denn Deutsche machen sowas nicht. Deutsche stechen keine kleinen Kinder ab, um es ganz klar zu sagen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 906

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