---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-03-30
topic: Menschenwürde
page_bfv: 504
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 30.3.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Was würde er [Anm.: Otto von Bismarck] seinem deutschen Volk sagen? [...] Er würde zunächst einmal darauf hinweisen – mit Blick auf Deutschland, mit Blick auf dieses verlotterte politische Establishment – Deutschland, meine lieben Mitbürger, Deutschland ist ein unterwandertes, ein fremdbestimmtes, ein nicht souveränes Land. [...] Er würde darauf hinweisen, dass fast sämtliche Regierungsvertreter in Berlin irgendwie mal in den letzten Jahren und Jahrzehnten in den sogenannten transatlantischen Netzwerken unterwegs waren. [...] Und da hat man ihnen vielleicht die Reste an Patriotismus aberzogen, man hat sie in die globalistische Denkweise vor allen Dingen US-amerikanischer Eliten hineingenommen, mitgenommen, integriert. Man hat sie transformiert, um sie dann als globalistische Sprechpuppen, als Marionetten zurückzuschicken in ihr Land.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 504

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