---
type: zitat
speaker: "[[Norbert Kleinwächter]]"
date: 2024-05-14
topic: Menschenwürde
page_bfv: 335
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Norbert Kleinwächter]] vom 14.5.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>#Bandenkrieg mit Machete! Das Video einer #Massenschlägerei in Leipzig offenbart, wer dabei war: Augenscheinlich keine ethnischen Sachsen. Die Polizei hatte das zuvor verschwiegen. So wird das letzte Vertrauen in den Staat zerstört: Keine Sicherheit mehr auf der Straße und die Hintergründe unter den Tisch fallen lassen. Dabei ist die Lösung offenkundig: #Täter identifizieren und in ihre Heimat abschieben. Denn Macheten-Fachkräfte wollen wir nicht!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 335

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