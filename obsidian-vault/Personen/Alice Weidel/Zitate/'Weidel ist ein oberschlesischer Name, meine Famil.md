---
type: zitat
speaker: "[[Alice Weidel]]"
date: Nicht Verfügbar
topic: Nationalsozialismus
page_bfv: 692
source: 'None'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom None veröffentlicht auf: 'None'
> [!quote] Aussage
>'Weidel ist ein oberschlesischer Name, meine Familie väterlicherseits kommt aus Leobschütz. Ich habe mich immer geweigert, nachzuschauen, wie der polnische Name der Stadt lautet, und diese Stadt umzubenennen.'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 692. Der Bericht zitiert die Welt vom 29.7.2024, die wiederum aus "Der Eckart" zitiert. Datum der Originalquelle: 25.7.2024

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