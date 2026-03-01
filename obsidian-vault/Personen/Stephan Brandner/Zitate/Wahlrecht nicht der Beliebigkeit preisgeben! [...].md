---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2023-09-19
topic: Menschenwürde
page_bfv: 185
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 19.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wahlrecht nicht der Beliebigkeit preisgeben! [...] ,Es überrascht wenig, dass ausgerechnet die SPD die Wahlen für Flüchtlinge öffnen will - schließlich kommen kaum noch Bürger auf die Idee, das Kreuz am Wahltag bei dieser Partei zu machen. Dieser verzweifelte Versuch, Wahlstimmen aus dem Ausland zu rekrutieren, würde aber sogar bei Umsetzung nach hinten losgehen. Letztendlich lässt der Vorschlag nur erkennen, welcher Plan hinter der massenhaften Aufnahme von Ausländern steckt: die SPD will sich ihr Wahlvolk einkaufen, auf Kosten unseres Sozialstaats päppeln und für den eigenen Machterhalt platzieren. Das werden wir zu verhindern wissen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 185

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