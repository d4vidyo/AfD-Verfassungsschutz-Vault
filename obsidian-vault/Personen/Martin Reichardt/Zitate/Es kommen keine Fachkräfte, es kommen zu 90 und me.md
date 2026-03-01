---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2025-02-07
topic: Menschenwürde
page_bfv: 910
source: 'Redebeitrag'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 7.2.2025 veröffentlicht auf: 'Redebeitrag'
> [!quote] Aussage
>Es kommen keine Fachkräfte, es kommen zu 90 und mehr Prozent Leute, die hier in die Sozialsysteme einwandern und die [...] vielleicht im Niedriglohnsegment irgendwo [...] noch gerade so vielleicht ihren Lebensunterhalt verdienen können. [...] Wir kriegen nicht nur keine Fachkräfte, sondern wir kriegen Messerkriminalität, 36.000 Messerangriffe, wir kriegen Dutzende von Morden, wir kriegen jeden Tag zwei Gruppenvergewaltigungen und das alles für einen Gegenwert an Fachkräften von quasi null. [...] Da kann man wohl schwer von einer deutschen Fremdenfeindlichkeit sprechen. Ich sehe da eher die Zahlen, die von einer offensichtlich importierten Inländerfeindlichkeit sprechen lassen müssten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 910. Gehört zum Zitat vom 7.2.2025

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