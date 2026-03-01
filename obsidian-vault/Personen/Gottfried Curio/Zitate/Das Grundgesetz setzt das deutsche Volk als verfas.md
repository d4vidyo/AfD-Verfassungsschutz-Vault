---
type: zitat
speaker: "[[Gottfried Curio]]"
date: 2021-10-30
topic: Menschenwürde
page_bfv: 120
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gottfried Curio]] vom 30.10.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das Grundgesetz setzt das deutsche Volk als verfassungsgebende Gewalt voraus. Wenn das deutsche Volk nicht mehr das deutsche Volk als geschichtlich gewachsene, kulturell (bei allen Binnen-Unterschieden) sich als Einheit auffassende, schicksalsmäßig aneinander gebundene Gemeinschaft ist, sondern nur noch ein aus allen Himmelsrichtungen zusammengewürfelte Menschenansammlung, was bleibt dann noch von dem ursprünglichen Gedanken einer Herrschaft des Volkes in Deutschland? Eine aktivierende Familienpolitik bleibt seit Jahrzehnten aus - stattdessen wird erst unter Rot-Grün, dann unter Merkel und demnächst wieder unter Rot-Grün (mit gelbem Mehrheitsbeschaffer) ein aus allen Fugen geratener, forcierter widerrechtlicher (illegale Immigration) Ausländer-Import unter der Lügen-Formel Flüchtling' betrieben, samt nachfolgender Nicht-Ausweisung, stattdessen aber Ausstattung mit der deutschen Staatsbürgerschaft - die kalte Entmündigung des deutschen Wählers durch rechtsbrechenden Umbau der Wähler-Demographie (alles abgesichert durch gleichgeschaltete Staatsmedien und politisch instrumentalisierten Verfassungsschutz). Versucht wird, den Begriff 'Volk' ideologisch zu verbiegen, um ihn für linke Gesellschaftsexperimente nutzbar zu machen, getreu Merkels Satz: 'Das Volk ist jeder, der hier lebt'. Rechtliche, gesellschaftlich-kulturelle, sprachliche und historische Verständnisse des Volksbegriffs werden abgeräumt durch Einbürgerung eines illegal importierten, nach Millionen zählenden Ausländerheeres, samt auffällig unterschiedlichen demographischen Reproduktionsquoten der angestammten Deutschen gegenüber den illegal ins Land gerufenen Kulturfremden. Auf diese Weise erfolgt eine schleichende Usurpation von Rechtsbegriffen, die Demokratie und Rechtsstaat entkernen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 120

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