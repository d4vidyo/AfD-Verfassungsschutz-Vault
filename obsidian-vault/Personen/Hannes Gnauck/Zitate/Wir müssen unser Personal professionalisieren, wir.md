---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2024-07-05
topic: Sonstiges
page_bfv: 815
source: 'YouTube; AfD TV'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 5.7.2024 veröffentlicht auf: 'YouTube; AfD TV'
> [!quote] Aussage
>Wir müssen unser Personal professionalisieren, wir müssen Schulungen abhalten für die Mitglieder, weil in der JA sind eben auch die zukünftigen Mandatsträger der Partei engagiert. Und es geht ja immer darum, bei Wahlen maximale Erfolge zu erreichen und dann eben auch unsere Mandatsträger irgendwann mal in Regierungsverantwortung zu bringen. Und auch das ist eine Aufgabe der Jugendorganisation, eben diese jungen Mandatsträger heranzuführen, zu schulen, weiterzubilden und dann in die AfD einfließen zu lassen, damit sie dann irgendwann mal für den Landtag, für den Bundestag oder für ein kommunales Amt kandidieren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 815

**Verfassungsschutz Kategorisierung:** Sonstiges.

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