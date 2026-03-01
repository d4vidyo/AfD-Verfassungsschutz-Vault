---
type: zitat
speaker: "[[Martin Renner]]"
date: 2022-07-30
topic: Menschenwürde
page_bfv: 243
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 30.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Alle diese Parteien unseres Parteienstaates haben sich zusammengeschlossen zur 'Neuen Einheitspartei Deutschlands' (NED) [...] vereint im gleichen ideologischen, den Bürger unterdrückenden Fieberwahn. Wir befinden uns inmitten einer aggressiven Bevölkerungs- und Kulturreform. Alles, was nicht der schon vielen, vielen Jahren praktizierten obskuren, globalistischen, universalistischen Staatsideologie entspricht, wird durch die an allen Schalthebeln unserer Republik sitzenden Kulturmarxisten gnadenlos plattgemacht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 243

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