---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2021-11-16
topic: Nationalsozialismus
page_bfv: 675
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 16.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>'Ampel' zeigt ihr totalitäres Gesicht! 3G im öffentlichen Personen(nah)verkehr [...] Am 24. März 1942 hatten die braunen Sozialisten im damaligen 'Großdeutschen Reich' verfügt, dass Juden keine öffentlichen Verkehrsmittel mehr benutzen dürfen. Heute, nicht einmal 80 Jahre später, kommt die Koalition der bunten Sozialisten auf eine ähnliche Idee. Jetzt sind die 'Ungeimpften' fällig. Damals wie heute geschah und geschieht das alles natürlich nur zu 'unserem' Besten. Damals wie heute wurde und wird eine bestimmte Bevölkerungsgruppe stigmatisiert, öffentlich beschimpft und entrechtet. Wenn diese faschistoiden Pläne der 'Ampel' umgesetzt werden, ist die Büchse der Pandora endgültig geöffnet. Dann haben die Buntsozialisten einem Teil der Bevölkerung offiziell den Krieg erklärt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 675

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