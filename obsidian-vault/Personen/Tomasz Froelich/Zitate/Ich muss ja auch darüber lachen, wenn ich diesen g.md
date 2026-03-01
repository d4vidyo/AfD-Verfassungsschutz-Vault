---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2023-07-20
topic: Menschenwürde
page_bfv: 151
source: 'Rede, im Youtube Livestream per AfD TV'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 20.7.2023 veröffentlicht auf: 'Rede, im Youtube Livestream per AfD TV'
> [!quote] Aussage
>Ich muss ja auch darüber lachen, wenn ich diesen ganzen Schwachsinn lese, schwule Kängurus, transsexuelle Vögel etc. Das mag alles ganz lustig klingen, aber wir dürfen das alles nicht auf die leichte Schulter nehmen, denn diese ganze links-woke Identitätspolitik, die richtet sich gegen alles, was uns als Zivilisation definiert. Sie richtet sich gegen die Familie, gegen unser Geschlecht, gegen unsere ethnokulturelle Identität, gegen unseren Glauben, gegen unser Volk, gegen das wahre, gegen unser Europa. Man will uns unserer Wurzeln berauben und uns zu bloßen Konsumenten, zu nützlichen Idioten, zu leicht steuerbaren Einheitsmenschen formen. [...] Und wenn man uns dann vorwirft, dass wir ein anderes Deutschland wollen, dann sage ich: ja, exakt so ist es. Wir wollen ein anderes Deutschland. Wir wollen ein ganz anderes Deutschland. Wir wollen ein Deutschland, in dem wir stolz unsere schwarz-rot-goldene Flagge schwenken dürfen statt die des Regenbogens. [...] Ein Deutschland, in dem wir das Eigene lieben, statt es dem Fremden zu opfern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 151

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