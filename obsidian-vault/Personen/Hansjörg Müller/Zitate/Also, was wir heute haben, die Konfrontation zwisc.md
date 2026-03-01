---
type: zitat
speaker: "[[Hansjörg Müller]]"
date: 2022-11-12
topic: Nationalsozialismus
page_bfv: 676
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hansjörg Müller]] vom 12.11.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Also, was wir heute haben, die Konfrontation zwischen den USA und Russland, ist eine ganz alte Geschichte, in der wir Deutsche auch schon zweimal unter die Räder gekommen sind. Und dann verstehen jetzt vielleicht auch einige hier, warum wir Deutsche, die wir doch ein patriotisches Verständnis haben, heute seelisch auf der Seite der Russen stehen in diesem großen globalen Konflikt. Weil die Russen inzwischen von den gleichen dunklen Mächten zum Opfer gemacht wurden wie wir in zwei Weltkriegen. Wir wurden zweimal in Weltkriege getrieben, die wir nicht wollten. Und genau so wurden die Russen jetzt sind den Krieg gegen die Ukraine getrieben, den sie auch nicht wollten. Und das ist der historische Zusammenhang. [...] Aber es geht noch weiter zurück. [...] Die Wolfowitz-Doktrin ist von 1991, als der damalige Verteidigungsminister Wolfowitz genau das schon gesagt hat: es geht jetzt darum, den Zusammenbruch der Sowjetunion dahingehend auszunutzen, die NATO bis an die russische Grenze zu erweitern und im Endeffekt Russland zu zerschlagen. Und damit schlägt sich der Bogen wieder zu dem, was ich am Anfang gesagt habe: Wolfowitz ist ein Wanderer zwischen den Welten, zwischen amerikanischer Regierung und Weltbank, zwischen amerikanischer Regierung und Federal Reserve Bank, das ist diese Privatbank, die den US-Dollar herausgibt. Jetzt sind wir wieder genau bei dem Punkt, dass diese Leute keine Ruhe geben, solange es eigenständige, souveräne Staaten gibt, die außerhalb ihrer Diktatur des US-Dollars Handel treiben wollen. Und da war halt 1914 und 1939 das Deutsche Reich im Weg. 1941 war Japan im Weg. Und 2022 ist Russland im Weg.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 676

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