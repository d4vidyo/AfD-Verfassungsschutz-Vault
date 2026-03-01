---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2025-02-08
topic: Menschenwürde
page_bfv: 895
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 8.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und auch wenn wir uns überlegen, dass die Staatsangehörigkeit schon nach fünf Jahren übertragen werden soll. [...] Und natürlich führt das dazu, dass sich der Charakter unseres Volkes verändert. Aber ich glaube, das wollen die etablierten Parteien. Sie wissen, dass wir sie nicht mehr wählen werden, und deshalb wollen sie uns austauschen. Und das werden wir nicht zulassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 895

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