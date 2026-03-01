---
type: zitat
speaker: "[[Enrico Komning]]"
date: 2022-12-07
topic: Menschenwürde
page_bfv: 352
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Enrico Komning]] vom 7.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Kein Menschenleben mehr für rot-grüne MultiKulti-Träume! Wieder einmal trifft es Unschuldige, in diesem Fall zwei Mädchen, wieder einmal wird seitens der Systemmedien alles versucht, die Umstände der Tat zu verschweigen oder wenigstens zu verschleiern. [...] Für ihre menschen- und gesellschaftsfeindliche Multi-Kulti Ideologie instrumentalisieren Altparteien und Systemmedien seit Jahren die unzähligen Opfer krimineller Migranten. Der Preis, den die beiden Mädchen in Illerkirchberg bezahlt haben - die eine mit ihrem Leben, die andere mindestens mit ihrer Gesundheit - ist endgültig zu hoch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 352

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