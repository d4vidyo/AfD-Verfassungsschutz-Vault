---
type: zitat
speaker: "[[Katrin Ebner-Steiner]]"
date: 2021-07-10
topic: Menschenwürde
page_bfv: 327
source: 'Redebeitrag in Memmingen'
status: Unbewertet
---

# Zitat: [[Katrin Ebner-Steiner]] vom 10.7.2021 veröffentlicht auf: 'Redebeitrag in Memmingen'
> [!quote] Aussage
>Ja liebe Freunde, es waren Rote und Grüne, die Lohndumping in Deutschland zur neuen Normalität gemacht haben, und Union und FDP haben mitgemacht und dieses System weitergegeben. EU-Freizügigkeit, Westbalkanregelung, EU und UN Migrationspakt und natürlich Merkels-Millionenheer oft Un- und Geringqualifizierter setzen den Arbeitsmarkt weiter unter Druck. [...] Statt uns Bürger zu gängeln, sollten Söder, Laschet, wie sie denn alle in ihrem bequemen Regierungssesseln heißen, endlich damit anfangen, unsere Frauen und Mädchen vor Mord, Totschlag und Gruppenvergewaltigungen durch Migranten zu schützen. Ja, vielleicht sollten sie endlich damit anfangen, die Wahrheit anzuerkennen. Dass ihre Politik der offenen Grenzen nichts anderes ist als die größte Katastrophe der deutschen Nachkriegsgeschichte. Denn mittlerweile ist es vielfach nachgewiesen, dass wir von Anfang an Recht hatten: Hätten die Regierenen da oben in Berlin auf uns gehört, dann hätten wir vielleicht viele Tausende Menschenleben retten können. [...] Der Moslem, der in Würzburg Johanna, Christiane und Steffi - und diese Namen sind nicht nur Namen, sie stehen für eine Geschichte und es hätte genauso gut zum Beispiel meine Mutter treffen können, ihre Tochter oder ihre Großmutter - diese drei Frauen wurden totgestochen und mehrere Menschen wurden schwer verletzt. Und dieser Moslem war nichts anderes als ein Merkel-Flüchtling. In Deutschland werden heute Menschen mit Beilen und Samurai-Schwertern getötet und Kinder vor Züge gestoßen. Aber wir sollen das alles hinnehmen als kleine Nebeneffekte, einer angeblich positiven Entwicklung. Denn laut den Regierenden brauchen wir ja Migration für unseren Arbeitsmarkt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 327

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