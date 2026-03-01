---
type: zitat
speaker: "[[Paul Timm]]"
date: 2022-12-27
topic: Menschenwürde
page_bfv: 333
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Paul Timm]] vom 27.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Auch sieben Jahre nach dem Beginn des Asylansturmes auf Deutschland haben wir jeden Tag mit Asylbewerbern, kriminellen Ausländern und Abzuschiebenden zu kämpfen. Deutschland hat keinen Platz mehr. Der Berliner Görlitzer Park ist ein Drogenparadies für nigerianische Mafiosi. Der Schweriner Marienplatz ist Schauplatz von Messerstechereien unter Ausländern. Vergewaltigungen und Tötungsdelikte durch Ausländer sind zur tragischen Normalität_geworden. Der Mord in Illerkirchberg an einem 14-jährigen Mädchen markiert einen weiteren Grabstein der irren Zuwanderungspolitik, welcher die CDU damals den Weg geebnet hat und die linke Ampel freudig weiterführt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 333

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