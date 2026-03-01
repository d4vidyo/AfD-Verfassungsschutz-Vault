---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2024-04-06
topic: Demokratieprinzip
page_bfv: 560
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 6.4.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Diese Partei [Anm.: SPD] und dieser Rundfunk, die das Tag für Tag tun, haben keine Überzeugungen. Davon bin ich überzeugt. Sie betreiben Machterhalt und sie nutzen dabei jedes Mittel, das ihnen in die Hände kommt. Sie nutzen den Inlandsgeheimdienst, um ihn auf unschuldige Bürger loszuschicken. Sie nutzen die Macht über ihren Einfluss im öffentlich-rechtlichen Rundfunk, um Andersdenkende zu stigmatisieren. Und, meine Damen und Herren, Sie haben aus unserer Demokratie einen Parteienstaat gemacht. Und diesen Parteienstaat lehne ich grundsätzlich ab. [...] Wir müssen diesen Parteienstaat abschaffen und es schaffen, dieses Land wieder nach vorne zu bringen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 560

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