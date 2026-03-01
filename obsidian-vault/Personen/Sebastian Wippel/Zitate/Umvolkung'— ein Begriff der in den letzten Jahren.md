---
type: zitat
speaker: "[[Sebastian Wippel]]"
date: 2021-11-05
topic: Menschenwürde
page_bfv: 222
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Wippel]] vom 5.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Umvolkung'— ein Begriff der in den letzten Jahren rasant an Bedeutung dazugewonnen hat. Er soll die Folgen beschreiben, die eine zunehmende Masseneinwanderung auf ein Volk, ja eine ganze Nation hat. Er warnt vor drastischen Veränderungen der Bevölkerungsstruktur durch massive Zuwanderung aus kultur- und geographisch fremden Ländern. [...] Linke, pseudoliberale FPDler und Mainstream-CDU-Politiker behaupten hingegen seit Jahren, dass es sich bei der 'Umvolkung' lediglich um eine Verschwörungstheorie, ja, einen rechten Kampfbegriff handele, der rein gar nichts mit der Wirklichkeit zu tun habe — auch wenn die Migrationszahlen der letzten Jahre hochgerechnet etwas komplett anderes aussagen. Linke Propagandisten stehen sogar selbst dazu, dass sie eine solche Umvolkung vorantreiben wollen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 222

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