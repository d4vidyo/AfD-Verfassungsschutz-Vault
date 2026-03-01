---
type: zitat
speaker: "[[Arno Bausemer]]"
date: 2025-01-09
topic: Menschenwürde
page_bfv: 909
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Arno Bausemer]] vom 9.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Vorsitzende hatte dieses Plakat gepostet und soll jetzt wegen angeblichen Rassismus vor Gericht gestellt werden. ,Engpässe im Gesundheitswesen werden nicht durch ,importierte Chirurgen' gelöst. Stoppt den EU-Migrationspakt!' Es muss ja wohl in einer freien Gesellschaft sein, dass man als Opposition die massiv steigende Messer-Kriminalität auch mit drastischen Bildern thematisiert. Egal ob im EU-Parlament oder in unseren nationalen Parlamenten - wir lassen uns von den Verursachern dieses Asyl-Chaos niemals einen Maulkorb verpassen! Von daher teile ich gerne das Bild und unterstütze damit die Partei meines tschechischen Fraktionskollegen Dr. Ivan David.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 909

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