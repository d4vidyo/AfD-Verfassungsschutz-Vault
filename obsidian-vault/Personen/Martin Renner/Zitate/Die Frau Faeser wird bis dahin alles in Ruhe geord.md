---
type: zitat
speaker: "[[Martin Renner]]"
date: 2022-07-18
topic: Demokratieprinzip
page_bfv: 579
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 18.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Frau Faeser wird bis dahin alles in Ruhe geordnet haben. Sie wird Meldestellen und Beruhigungsstätten für die darob aufgebrachten Menschen eingerichtet haben. Sie sucht nur noch nach einem gut klingenden Namen, da sie den Begriff 'Gulag' aus nachvollziehbaren Gründen nicht verwenden will. Ich frage jetzt für einen Freund: Werden diese bürgerlichen 'Beruhigungsstätten' für die unzählig vielen asozialen, also aufgewachten 'Un'bürger, dezentral in den Bundesländern eingerichtet? Oder zentral irgendwo in unserem Bundesstaat? Verwaltungstechnisch wäre die 2. Alternative sicher die einfachere und kostengünstigere Lösung. Sehr verehrte Frau Faeser, sollten Sie noch Berater für die Organisation oben genannter 'Beruhigungsstätten' benötigen, wenden Sie sich gerne an mich. Ich habe mich zeitlebens mit kommunistischen - auch nationalsozialistischen - Gulags und Konzentrationslager und den damit verbundenen Unrechtsregimen beschäftigt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 579

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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