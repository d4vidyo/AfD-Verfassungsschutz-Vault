---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-10-31
topic: Menschenwürde
page_bfv: 260
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 31.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>RACIAL PROFILING KANN LEBEN RETTEN! Gestern hat die Polizei in Berlin auf ihre Erfahrung gesetzt und per 'verdachtsunabhängiger Personenkontrolle aufgrund des Erscheinungsbildes' wahrscheinlich einen Terroranschlag verhindert. Im Klartext: Sie haben einen typischen '2015er' ins Visier genommen. Haben sie Asiaten oder Osteuropäer – von denen es am Bahnhof sicherlich auch genügend zur Auswahl gab – kontrollieren wollen? Nein, denn sowohl Kriminelle als auch Terroristen weisen oft ähnliche Profile auf. Die Polizei hat hier auf statistische Erkenntnisse gesetzt und Schlimmeres verhindert. Daher – Racial Profiling eignet sich zur Stärkung der inneren Sicherheit in Deutschland. Es ist doch klar, wer meist die Tätergruppen sind; was in der Politik aktuell fehlt, ist nur der Wille, die eigene Bevölkerung zu schützen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 260

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