---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2023-11-20
topic: Menschenwürde
page_bfv: 277
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 20.11.2023 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Lebensrealität der meisten Einheimischen: Massenmigration bedeutet nicht gemütliches Beisammensein bei Schach und Wein! [...] Berlin, 31. Dezember 2022, 23:54 Uhr: Der 38-jährige Kurt, der das ganze Jahr über im Schichtdienst arbeitet, um seine Familie durchzubringen, freut sich schon seit Langem auf ein friedliches Neujahrfest. Doch als er draußen die Lage erkundet, wird er statt feiernder Familien und Feuerwerke von Macheten-Mutombo und Böller-Bilal überrascht, die gerade Sprengkörper auf die Feuerwehr werfen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 277

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