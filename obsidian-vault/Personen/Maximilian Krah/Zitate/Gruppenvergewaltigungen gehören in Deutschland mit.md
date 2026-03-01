---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-10-04
topic: Menschenwürde
page_bfv: 342
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 4.10.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gruppenvergewaltigungen gehören in Deutschland mittlerweile zum Alltag. Berlin, Görlitzer Park erst letzte Woche. Und gleichzeitig will der von der CDU geführte Senat immer noch mehr Afghanen direkt ins Land holen, obwohl es genau diejenigen sind, die am wenigsten damit umgehen können, dass hier in Deutschland Frauen selbstbewusst sind, sich alleine durch die Stadt bewegen, einen eigenen Willen haben. Typisch CDU. Sie hat die Grenze geöffnet und sie will noch weitere Probleme ins Land holen. Gruppenvergewaltigungen gab es früher in Deutschland nicht. Gruppenvergewaltigung darf es in Deutschland nicht geben. Deshalb ist es wichtig, die Grenzen zuzumachen, Sexualstraftäter konsequent abzuschieben und vor allen Dingen die Parteien abzustrafen, die dafür gesorgt haben, dass unser schönes Vaterland zum Shithole verkommt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 342

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