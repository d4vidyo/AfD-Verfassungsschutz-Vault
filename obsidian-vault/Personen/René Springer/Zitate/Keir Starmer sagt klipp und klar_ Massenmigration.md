---
type: zitat
speaker: "[[René Springer]]"
date: 2024-12-01
topic: Menschenwürde
page_bfv: 890
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 1.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Keir Starmer sagt klipp und klar: Massenmigration und offene Grenzen sind ein globalistisches Experiment, und ihre verheerenden Folgen sind keine Irrtümer etablierter Politik, sondern Teil einer bewusst verfolgten Agenda. Erstmals gibt damit ein westlicher Staatsmann - zudem ein linksliberaler – zu, dass die Ersetzungsmigration einem Plan folgt und kein Versagen darstellt. Welche Konsequenzen sind daraus zu ziehen? Diese Frage wird in Zukunft unseren Kontinent prägen! Die Antwort kann nur lauten: Remigration, Remigration und nochmals Remigration!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 890

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