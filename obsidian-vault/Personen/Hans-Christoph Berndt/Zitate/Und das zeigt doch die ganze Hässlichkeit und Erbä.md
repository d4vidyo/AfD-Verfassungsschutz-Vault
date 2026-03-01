---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-12-30
topic: Demokratieprinzip
page_bfv: 954
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 30.12.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und das zeigt doch die ganze Hässlichkeit und Erbärmlichkeit dieser späten BRD. Die ganze Hässlichkeit und Erbärmlichkeit der Lage, in die uns CDU, SPD, FDP und Grüne gebracht haben. [...] Ja, wir haben es in diesem Jahr noch nicht geschafft, die Vorherrschaft dieser Altparteien zu brechen. Aber liebe Freunde, wir sind sehr dicht davor. Und gerade nach den Wahlen im Osten in diesem Sommer und nachdem, wie es sich jetzt in diesen Parlamenten entwickelt hat, ist doch dieses Parteienkartell dabei, sein Ansehen zu verspielen, seine Legitimation zu verspielen. Bei jedem, der auch nur halbwegs neutral die Sache sieht, haben diese Parteien doch offenkundig ihre Glaubwürdigkeit verloren. [...] Elon Musk sagt wiederholt "Nur die AfD kann Deutschland retten!" . Nur die AfD kann Deutschland retten. Und das Kartell von Staatsparteien und Staatsmedien bekommt Schnappatmung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 954

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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