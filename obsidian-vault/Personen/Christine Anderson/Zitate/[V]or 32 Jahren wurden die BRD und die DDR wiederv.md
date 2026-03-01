---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2022-11-08
topic: Demokratieprinzip
page_bfv: 602
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 8.11.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>[V]or 32 Jahren wurden die BRD und die DDR wiedervereint. [...] Doch dabei wurden auch wieder neue, unnötige und fahrlässige Wunden in das kollektive Bewusstsein vieler ostdeutscher Bürger geschlagen. Die politischen und wirtschaftlichen Eliten des Westens, machten sich die ehemalige DDR zur Beute. [...] Heute haben unsere Regierung und ihre Erfüllungsgehilfen im politischen Establishment ihre Hände direkt im Spiel, wenn es darum geht, das Geld der Deutschen diesmal auf Nimmerwiedersehen in Richtung EU zu exportieren. Dies alles geschieht heute mit derselben herablassenden Arroganz wie damals. Und wer das nicht möchte, seine berechtigten Sorgen und Kritik über die abgehobene und bürgerfeindliche Politik der deutschen Gegenwart zum Ausdruck bringt, wird als Wutbürger, Verlierer, Schwurbler, Dunkeldeutscher, Verschwörungstheoretiker oder gar gleich als Rechtsradikaler vom Altparteienkomplex beschimpft. Die Vokabeln, mit denen Regierung und medialer Komplex mittlerweile Opposition und Kritiker verunglimpfen, haben sich freilich seit damals etwas geändert, der Geist einer SED wohnt aber auch ihnen wieder inne. Und so stehen sie heute wieder einträchtig beieinander - die längst bekannten und selbstverliebten Vertreter unserer Altparteien - und feiern den 32. Jahrestag unserer Wiedervereinigung, während sie gleichzeitig dabei sind, mit denselben Methoden und Zielsetzungen von damals, eine neue DDR 2.0 entstehen zu lassen. Wer dies erst einmal bemerkt hat, dem ist nicht mehr ernsthaft nach Feiern zumute. Ich bin stolz auf die friedliche Revolution der Ostdeutschen, die unsere gemeinsame Zukunft in einem wiedervereinigten Deutschland erst ermöglichte. Eine Revolution die zeigt, welche Kraft ein Volk entwickeln kann, wenn es den Entschluss gefasst hat, ein diktatorisches Regime in die Knie zu zwingen. [...] Daher möchte ich heute an alle Deutschen appellieren: Lasst uns endlich Rückgrat zeigen! Lasst uns auf die Warnungen aus Ostdeutschland hören! Die Menschen dort besitzen noch feinere Antennen und erkennen aus Erfahrung früher und besser, wenn Unfreiheit und Lüge wieder damit beginnen, ihr hässliches Haupt zu erheben. [...] Feiern wir heute unser geeintes Deutschland. Aber seien wir ab morgen gemeinsam und entschlossen gleich doppelt so wachsam, damit wir den falschen Eliten und ihren politischen Handlangern den Weg zurück zu Unfreiheit und Unterdrückung ein für alle Mal austreiben!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 602

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