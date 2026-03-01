---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-12-14
topic: Menschenwürde
page_bfv: 880
source: 'Podiumsdiskussion'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 14.12.2024 veröffentlicht auf: 'Podiumsdiskussion'
> [!quote] Aussage
>Ja und ich hab immer ein bisschen Bauchschmerzen genau bei diesem Thema, mit der direkten Demokratie, die ja in der Schweiz wunderbar funktioniert, aber du kommst aus Nordrhein-Westfalen und es gibt in Nordrhein-Westfalen Schulklassen, da ist nicht ein einziges Kind mehr wirklich deutsch, da haben wir eine riesen Einwanderung aus dem muslimischen Kulturkreis und da hab ich einfach die Sorge – bei uns in Brandenburg ist das überhaupt kein Problem – da habe ich zum Beispiel die Sorge: Was ist denn, wenn diejenigen einfach mal ein Gesetz initiieren: "Es darf kein Schweinefleisch mehr an Schulen geben" oder "Lehrerinnen müssen verschleiert werden". Die hätten dann im Prinzip ja die Mehrheit, das bereitet mir so ein bisschen Bauchschmerzen. [...] Dann wäre dann Remigration wahrscheinlich wieder der Schlüssel.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 880

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