---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2024-12-11
topic: Menschenwürde
page_bfv: 920
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 11.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Polizei ist völlig überfordert, der Autoverkehr bricht teilweise zusammen. So sieht es aus, wenn ein ehemals stabiles Land in #Parallelgesellschaften zersplittert. Wo sich die respektlosen Gäste von einst mittlerweile zu den neuen Herren aufschwingen & machen, was sie wollen. Es ist nicht nur der Jubel zum Sturz von #Assad, es ist auch eine #Machtdemonstration gegenüber den schwachen Deutschen. Allerdings: Assad ist jetzt weg & damit auch euer Fluchtgrund! Geht nach Hause, feiert dort & vor allem: baut euer Land wieder auf! Ich wünsche gute Heimreise! #Remigration

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 920

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