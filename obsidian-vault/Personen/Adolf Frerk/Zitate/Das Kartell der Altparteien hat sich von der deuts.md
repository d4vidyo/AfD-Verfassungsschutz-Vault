---
type: zitat
speaker: "[[Adolf Frerk]]"
date: 2022-06-16
topic: Menschenwürde
page_bfv: 175
source: 'https;//afd-kleve.de'
status: Unbewertet
---

# Zitat: [[Adolf Frerk]] vom 16.6.2022 veröffentlicht auf: 'https;//afd-kleve.de'
> [!quote] Aussage
>Das Kartell der Altparteien hat sich von der deutschen Kulturnation verabschiedet und versucht, die multikulturelle Willensnation einzuführen. Die autochthonen Deutschen haben auf ihren eigenen historischen und kulturellen Hintergrund zu verzichten. Wer sich da sträubt, ist ein Ausländerfeind, ein Rassist oder ganz einfach ein Staatsfeind, worüber Herr Haldenwang befindet. Die Vergabe der deutschen Staatsbürgerschaft soll nur noch von der Zustimmung des Einzelnen zum Wortlaut der Verfassung abhängen. In diesem Sinn hat Frau A. Merkel 2015 die deutschen Grenzen für die ganze Welt geöffnet. [...] Das deutsche Volk soll endlich seine ererbte Identität zugunsten der Migrationsgesellschaft aufgeben. [...] Der Bevölkerungsaustausch ist zum Staatsziel geworden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 175

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