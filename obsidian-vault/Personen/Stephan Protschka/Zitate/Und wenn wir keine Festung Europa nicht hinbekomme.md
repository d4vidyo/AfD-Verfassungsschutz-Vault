---
type: zitat
speaker: "[[Stephan Protschka]]"
date: 2023-02-22
topic: Menschenwürde
page_bfv: 363
source: 'Rede politischer Aschermittwoch, Osterhofen'
status: Unbewertet
---

# Zitat: [[Stephan Protschka]] vom 22.2.2023 veröffentlicht auf: 'Rede politischer Aschermittwoch, Osterhofen'
> [!quote] Aussage
>Und wenn wir keine Festung Europa nicht hinbekommen, dann müssen wir eine Festung Deutschland bauen, meine Damen und Herren. Das ist unser Land und es muss jedem bewusst sein. [...] Aber liebe Syrer, geht doch nach Hause. [...] Wir haben seit 2015 einen Zuwachs von über vier Millionen Menschen. Wir können keinen Fachkräftemangel mehr haben. Was ist denn 2015 gekommen: Raketenwissenschaftler, Ärzte, Mediziner, Krankenschwestern und was ist alles gekommen... Ingenieure. Wo sind die ganzen Leute? Keiner will arbeiten von denen. [...] Sollte es vielleicht so weit kommen wie in Lörrach - Lörrach ist Ihnen ein Begriff, Baden-Württemberg - da werden Mieter aus städtischen Wohnungen rausgeworfen, um für die Migranten Platz zu machen. Die Deutschen müssen Platz machen, damit die Migranten Platz haben. Ist das unser Land? Wollen wir das? Ich will so was nicht, meine Damen und Herren. [Rufe aus Publikum:‚Abschieben!‘] Das ist eine... - ja, Abschieben ist die einzige Möglichkeit! [...] Die Leute, die im Cafe sitzen und auf Eure Kosten Kaffee trinken, das sind die sogenannten Flüchtlinge. Nein, stopp - Fachkräfte hat man sie früher noch genannt. Das sind die Fachkräfte, die wissen, wie man vom Arbeitsamt, vom Sozialamt Geld bekommt. Aber die wissen nicht, wie ein Hammer oder Fäustling ausschaut, schon gar nicht, wie der Schraubenzieher oder wie Arbeit ausschaut.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 363

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