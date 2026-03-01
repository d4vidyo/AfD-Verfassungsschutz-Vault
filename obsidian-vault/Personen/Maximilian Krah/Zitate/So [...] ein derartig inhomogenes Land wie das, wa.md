---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-01-15
topic: Menschenwürde
page_bfv: 250
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 15.1.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>So [...] ein derartig inhomogenes Land wie das, was wir jetzt geworden sind, ohne gemeinsames kollektives Bewusstsein, ohne gemeinsame Identität, ist immer ein kriminelles, gewalttätiges und unsolidarisches Land. Und die Politik kann darauf nur antworten – wenn sie das nicht schafft, die Homogenität wiederherzustellen und das [...] soll ja neuerdings verfassungswidrig sein, das zu wollen – indem sie es entweder laufen lässt und akzeptiert, dass es No-Go-Areas gibt und dass man eben zweimal im Jahr die Stadt anzündet, wie in Brüssel, oder indem der Staat repressiv wird. Und das ist eben das, worauf wir uns einstellen müssen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 250

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