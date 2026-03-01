---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-07-24
topic: Nationalsozialismus
page_bfv: 684
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 24.7.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Man rettet und verteilt das Steuergeld im Weltretter-Wahn und der kollektiv-historischen Zwangsneurose an den Rest der Welt und vergisst mit voller Absicht das eigene Volk, die eigenen Deutschen, seine Nächsten. Die Herrschaft der Schlechtesten in Deutschland hilft allen Völkern auf dieser Welt aufopferungsvoll und mit ewigen historischen Schuldkult, überweist gerne Mal 10 Milliarden deutsches Steuergeld nach Indien aus vermeintlichen Klimaschutzgründen und lässt die eigenen Bürger im zerstörten Ahrtal alleine, um wiederum von Indien überteuertes Gas und Öl zu kaufen, welches diese wiederum aus Russland beziehen! Das ist die Idiotenherrschaft in Deutschland in Reinform, meine Damen und Herren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 684

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