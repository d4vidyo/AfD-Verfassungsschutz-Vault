---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2024-05-10
topic: Nationalsozialismus
page_bfv: 689
source: 'Freilich-Magazin'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 10.5.2024 veröffentlicht auf: 'Freilich-Magazin'
> [!quote] Aussage
>Deutschland wurde von der Hitlermacht befreit, um es unter die Herrschaft der Besatzer zu stellen. Und in den ersten Monaten war auch diese Besatzung Unrecht, denn wie will man die zahlreichen Verbrechen der Besatzungstruppen von den Rheinwiesenlagern bis zu den Vergewaltigungen im Osten anders bezeichnen? [...] Der 8. Mai: Tag der Besatzung und Teilung Deutschlands. Die Teilung endete 1990. aber noch stehen 38.000 amerikanische Soldaten auf dem deutschen Boden. [...] Ein Gedenken an den 8. Mai sollte deshalb in die Vergewisserung münden, dass es heute darauf ankommt, die Befreiung zu vollenden und echte Souveränität zu erlangen. Das ist das Vermächtnis des 8. Mai.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 689

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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