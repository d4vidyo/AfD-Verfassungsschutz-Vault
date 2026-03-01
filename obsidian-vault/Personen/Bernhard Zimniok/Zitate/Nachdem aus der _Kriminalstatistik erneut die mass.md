---
type: zitat
speaker: "[[Bernhard Zimniok]]"
date: 2024-04-09
topic: Menschenwürde
page_bfv: 411
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Bernhard Zimniok]] vom 9.4.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Nachdem aus der #Kriminalstatistik erneut die massive Migrantenkriminalität hervorgeht, kommen wieder die üblichen Forderungen, vor allem nach mehr Polizei und Überwachung. Ergo soll das bewusste (!) Versagen der Altparteien in der Migrationspolitik den weiteren Ausbau des Überwachungsstaats rechtfertigen. Das muss jeder Demokrat ablehnen. Es ist doch offensichtlich, was das Problem ist: die Massenmigration von Kulturfremden. Die Folgen sind ebenso offensichtlich: Grenzen endlich dicht machen und millionenfach abschieben. Wir brauchen eine drastische Reform der Migrationspolitik, die u. a. ein Ende des Individualrechts auf Asyl beinhaltet. Nur so wird man diesem Problem Herr. Das ist lange bekannt, die Altparteien verweigern diese Lösungen aber trotzdem. Daher: #AfD wählen - oder untergehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 411

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