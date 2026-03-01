---
type: zitat
speaker: "[[Beatrix von Storch]]"
date: 2023-01-23
topic: Menschenwürde
page_bfv: 462
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Beatrix von Storch]] vom 23.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>+ + + Massenhafte Einbürgerung von muslimischen Migranten + + + 2022 ließen sich bei uns am häufigsten Syrer einbürgern (über 19.000). Nach Angaben des Statistischen Bundesamtes ließen sich auch noch über 12.000 Türken einbürgern. Das entspricht pro Jahr einer deutschen Kleinstadt, und wenn man dann an den Familiennachzug denkt, hat man schon eine neue muslimische Großstadt in Deutschland. Jedes Jahr. Viele dieser Personengruppe interessieren vor allem: die deutschen Sozialleistungen. So entstehen, von Rot-Grün gewollt, von der FDP geduldet, immer größere und stärkere Parallelgesellschaften, die mit unserer Demokratie und unserem Rechtsstaat oft aber auch gar nichts zu tun haben wollen. Was das bedeutet, hat man an Silvester gesehen. Wir müssen diese fatale Entwicklung endlich stoppen und rückgängig machen, sonst leben wir bald nicht mehr in der Bundesrepublik Deutschland, sondern in der Islamischen Republik Deutschland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 462

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