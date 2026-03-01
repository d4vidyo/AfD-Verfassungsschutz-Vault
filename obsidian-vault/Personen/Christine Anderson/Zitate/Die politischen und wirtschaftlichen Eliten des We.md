---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2024-10-03
topic: Demokratieprinzip
page_bfv: 591
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 3.10.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die politischen und wirtschaftlichen Eliten des Westens, machten sich die ehemalige DDR zur Beute. [...] Es bedarf nun nicht mehr einer vorgeschalteten Bundesanstalt nach dem Muster einer Treuhand, um unser gemeinsames Volksvermögen aus dem Land zu transferieren. Heute haben unsere Regierung und ihre Erfüllungsgehilfen im politischen Establishment ihre Hände direkt im Spiel, wenn es erneut darum geht, das Geld der Deutschen auf Nimmerwiedersehen - diesmal in Richtung EU - verschwinden zu lassen. Dies alles geschieht heute mit derselben herablassenden Arroganz wie damals. Und wer das nicht möchte, seine berechtigten Sorgen und Kritik über die abgehobene und bürgerfeindliche Politik der deutschen Gegenwart zum Ausdruck bringt, wird als Wutbürger, Verlierer, Schwurbler, Dunkeldeutscher, Verschwörungstheoretiker oder gar gleich als Rechtsradikaler vom Altparteienkartell beschimpft. Die Vokabeln, mit denen Regierung und medialer Komplex mittlerweile Opposition und Kritiker verunglimpfen, haben sich freilich seit damals etwas geändert, der Geist einer SED wohnt aber auch ihnen wieder inne. Und so stehen sie heute wieder einträchtig beieinander - die charakterlosen und selbstverliebten Vertreter unserer Altparteien - und feiern den 34. Jahrestag unserer Wiedervereinigung, während sie gleichzeitig dabei sind, mit denselben Methoden und Zielsetzungen von damals, eine neue DDR 2.0 entstehen zu lassen. Wer dies erst einmal bemerkt hat, dem ist nicht mehr ernsthaft nach Feiern zumute.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 591

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