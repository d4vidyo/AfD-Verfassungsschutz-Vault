---
type: zitat
speaker: "[[Carlo Clemens]]"
date: 2021-08-01
topic: Menschenwürde
page_bfv: 377
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Carlo Clemens]] vom August 2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wer sich den Koalitionsvertrag der Ampel näher anschaut, könnte auf den Gedanken kommen, dass es die Einwanderungswelle 2015 mit all ihren Folgen für Deutschland und seine Bürger nie gegeben hätte. Der Koalitionsvertrag nimmt nicht im Entferntesten Rücksicht auf Terror, Ausländerkriminalität, gesellschaftliche und kulturelle Aufnahmekapazitäten und die zunehmende Islamisierung. Stattdessen: Noch mehr Migration, noch mehr angebliche 'Vielfalt', noch mehr Einbürgerungen. Spätestens jetzt wird Deutschland zur Siedlungsregion für die Dritte Welt.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: August 2021

**SPIEGEL-Notiz:** Gutachten Seite: 377. abweichendes Datum in der zugehörigen Fußnote: 27.11.2021

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