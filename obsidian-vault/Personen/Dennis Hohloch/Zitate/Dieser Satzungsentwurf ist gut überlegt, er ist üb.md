---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2025-01-12
topic: Sonstiges
page_bfv: 865
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 12.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Dieser Satzungsentwurf ist gut überlegt, er ist über ein Jahr vorbereitet und fand seinen Anstoß in einer Diskussion des Bundesvorstandes und des Vorstandes der Jungen Alternative vor über einem Jahr. Er sieht vor, dass die Junge Alternative oder die neue Jugendorganisation mit der Partei näher zusammenwachsen. Das bedeutet auf der einen Seite, dass man der Jugendorganisation mehr Möglichkeiten bieten muss: finanziell, strukturell und personell. Eine professionelle Jugendorganisation braucht genau diese Möglichkeiten. Eine professionelle Partei auf der anderen Seite braucht allerdings auch Sicherheit. Sicherheit, dass Personen, die sich innerhalb dieser Jugendorganisation bewegen und Politik machen, kein Schindluder mit unserer Partei treiben. Und das hat nichts mit einem Generalverdacht zu tun, das ist völlig normal in jeder Beziehung. Man braucht Sicherheit, um gemeinsam zusammen arbeiten zu können und dementsprechend ist es notwendig, die neue Jugendorganisation zusammen in die Partei zu integrieren und gleichzeitig unter die Schiedsgerichtsbarkeit der Partei zu stellen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 865

**Verfassungsschutz Kategorisierung:** Sonstiges.

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