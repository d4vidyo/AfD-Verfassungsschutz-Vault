---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2025-02-02
topic: Demokratieprinzip
page_bfv: 960
source: 'Internetseite'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 2.2.2025 veröffentlicht auf: 'Internetseite'
> [!quote] Aussage
>Da schickst du dein kleinen zweijährigen Jungen morgens in die Kita und siehst ihn nicht lebend wieder, weil ein Monster, das nicht mehr hätte im Land sein dürfen, dein Augenlicht ausgelöscht hat. [...] Was für ein Skandal! Alle Menschen mit totrotgrüner Gesinnung heucheln nun wieder Anteilnahme und spucken den Opfern und ihren Familien im nächsten Augenblick ins Gesicht, indem Sie zu Demonstrationen gegen all die politischen Kräfte aufrufen, die die Menschen in diesem Land vor solchen monströsen Gewalttaten und die gegen das deutsche Volk gerichtete Migrationswaffe schützen wollen. Sie machen am Rande dieser Demos Selfies mit selbstzufriedenem Lächeln und sagen so jedem Menschen in Deutschland, dass Ihnen die Morde und das Metzeln völlig egal sind. Sie demonstrieren nicht gegen die Mörder oder die fehlgeleitete Migrationspolitik. Sie zeigen der großen Mehrheit der jüngst Befragten, die sich ein Ende der entztlichen und folgenschweren Migrationspolitik wünschen, den ausgestreckten Mittelfinger. Bitte erklären Sie ihren Wählern endlich, dass sie gar nicht gewillt sind, die Wähler und ihre Kinder ernsthaft zu schützen. Erklären Sie, dass Sie ihre hart erarbeiteten Steuergelder an Sozialmigranten und feindliche Fremde umverteilen möchte. Sie sind in Wahrheit empathielose, politische Geisterfahrer und die Totengräber des Vertrauens der Menschen in diesen Staat und seine Organe. Und sie gehen dabei über Leichen: Die unrühmliche Mehrheit des Deutschen Bundestages hat am Freitag den CDU Zuwanderungsbegrenzungsgesetzentwurf abgelehnt, den sich 69 Prozent der Befragten wünschten laut "Tagesspiegel" wünschten. Das alles macht die Menschen unfassbar wütend, denn sie sehen, welche Parteien auf die Mord- und Vergewaltigungsopfer der Masseneinwanderung spucken. [...] In Wahrheit ist die Brandmauer keine Heldentat. Sie ist weit entfernt davon. Sie ist so etwas wie die Garantie auf ein Dauerabo auf Regierungsbeteiligung der Deutschland feindlich gesinnten parlamentarischen Minderheit. Mit Demokratie hat diese Brandmauer nichts zu tun. Mit Grabsteinen, Deutschlandvernichtung, Krieg, Armut und Elend leider eine ganze Menge.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 960

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