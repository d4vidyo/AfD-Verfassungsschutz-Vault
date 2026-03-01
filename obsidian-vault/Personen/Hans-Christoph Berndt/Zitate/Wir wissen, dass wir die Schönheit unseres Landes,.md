---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-08-11
topic: Menschenwürde
page_bfv: 367
source: 'YouTube, Berlinchen Tinchen'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 11.8.2024 veröffentlicht auf: 'YouTube, Berlinchen Tinchen'
> [!quote] Aussage
>Wir wissen, dass wir die Schönheit unseres Landes, die Kultur unseres Landes [...] denjenigen verdanken, die vor uns gelebt haben, den Mühen und den Künsten unserer Vorfahren. [...] Und weil wir das empfinden, haben wir auch ein Empfinden dafür, dass wir deshalb verpflichtet sind, auch den nachfolgenden Generationen ein Land zu hinterlassen, in dem sie zu Hause sind. In dem sie sich entwickeln können. Ein Land, in dem sie als Deutsche wie Deutsche leben können und in dem sie nicht sich den Speisevorschriften, den Bekleidungsvorschriften und den Ehrvorschriften von irgendwelchen Beduinen unterwerfen müssen, sondern als Deutsche und Europäer leben können. [...] Deutschland ist das Land der Deutschen und Deutschland soll das Land der Deutschen bleiben. Wir wollen, dass unsere Jugend in Deutschland ihre Heimat behält und sich nicht irgendwelchen Zuwanderern unterwerfen muss. [...] Alle anderen Parteien [...] haben sich vom deutschen Volk verabschiedet. Sie haben sich vom deutschen Nationalstaat verabschiedet. Sie wollen, dass wir aufgehen in einer EU und Weltgemeinschaft. Sie wollen Deutschland zum internationalen Siedlungsgebiet machen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 367

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