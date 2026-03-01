---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-08-27
topic: Sonstiges
page_bfv: 730
source: 'COMPACT'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 27.8.2022 veröffentlicht auf: 'COMPACT'
> [!quote] Aussage
>Die AfD und ihr Umfeld brauchen Medien, die uns nicht mit schlechter Absicht, sondern mit guter journalistischer Neutralität gegenübertreten. [...] Wir müssen endlich aufhören, uns von Kräften, die auf der Seite des Volkes stehen, zu distanzieren! Wir müssen uns von dem ständigen Distanzieren distanzieren! Wir müssen mit Leichtigkeit und Offenheit herantreten an neue Partner, wir müssen lernen, uns zusammenzuschließen, anstatt uns spalten zu lassen. Und hier kommt wieder das COMPACT-Magazin ins Spiel. Keine Zeitschrift bildet so sehr die volle Breite und den vollen Facettenreichtum des Widerstandes ab. COMPACT ist das parteiübergreifende Leitmedium des Widerstandes gegen die volksfeindliche Politik der Altparteien. Deshalb habe ich mich sehr über diese Einladung gefreut - denn die hier gelebte Offenheit für alle Strömungen des Widerstandes ist genau die Grundhaltung, die wir brauchen, wenn wir politischen Erfolg haben wollen und irgendwann nicht nur regieren, sondern auch wirklich etwas verändern wollen in diesem Land!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 730

**Verfassungsschutz Kategorisierung:** Sonstiges.

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