---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2025-01-08
topic: Sonstiges
page_bfv: 845
source: 'YouTube; Interview mit COMPACTTV'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 8.1.2025 veröffentlicht auf: 'YouTube; Interview mit COMPACTTV'
> [!quote] Aussage
>Es gibt viele Leute, die haben keine Abos bei Info-DIREKT, die haben keine Abos bei COMPACT. [...] Dieses Bewusstsein muss erstmal geschaffen werden und das ist Aufgabe meiner Meinung nach der JA, dass wir dieses Bewusstsein herstellen. Deswegen auch dieser Kongress [Anm.: JA-Bundeskongress im Oktober 2022 in Apolda], dass wir eben dafür sorgen, dass [...] dieses Bewusstsein besteht und wenn das abgeschlossen ist, wenn die Partei versteht, okay, wir brauchen solche Leute, dann kann man auch sagen, okay, vielleicht ist das nicht der Platz, aber unsere Aufgabe ist es gerade, über die Junge Alternative, weil wir da [...] unseren Wirkkreis sozusagen haben in der Partei. Eine andere Form gibt es nicht. Die haben wir ja letztendlich erst angestoßen, dass du sozusagen als COMPACT-Reporter auch auf einem Bundesparteitag oder so vor Ort sein kannst. Ist ja auch darauf zurückzuführen, dass wir uns überhaupt in den letzten Jahren dafür so stark gemacht haben und dass wir nicht aufgehört haben. [...]. Wir konnten nur innerhalb, weil wir halt eben Teil dieser AfD sind, dafür überhaupt das so bewirken.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 845

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