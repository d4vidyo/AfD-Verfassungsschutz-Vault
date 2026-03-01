---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-12-02
topic: Menschenwürde
page_bfv: 354
source: 'YouTube, Der blaue Kanal'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 2.12.2022 veröffentlicht auf: 'YouTube, Der blaue Kanal'
> [!quote] Aussage
>Die innere Sicherheit erodiert nicht erst seit gestern, sondern schon seit Jahrzehnten. [...]. Aber die innere Sicherheit zerfällt auch, weil dieses Land seit den 60er Jahren, beginnend in Westdeutschland, zielgerichtet multikulturalisiert worden ist. [...]. Und dann haben wir seit 2015 nochmal 3,5 Millionen Zuwanderer aus außereuropäischen Kontexten hinzubekommen, die wiederum nicht unsere Werte leben können oder leben wollen. [...] Gruppenvergewaltigung, Messermorde [...] das ist die neue Normalität im besten Deutschlands aller Zeiten. [...] Nicht jeder Zuwanderer ist ein Krimineller, aber mit Blick in die Polizeistatistiken [...] kann ich zusammenfassen, dass die Multikulturalisierung Deutschlands die Multikriminalisierung Deutschlands nach sich gezogen hat.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 354

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