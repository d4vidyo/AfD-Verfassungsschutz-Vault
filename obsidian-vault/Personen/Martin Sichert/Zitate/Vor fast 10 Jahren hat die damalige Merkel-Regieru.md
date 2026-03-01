---
type: zitat
speaker: "[[Martin Sichert]]"
date: 2024-05-07
topic: Menschenwürde
page_bfv: 370
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Martin Sichert]] vom 7.5.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Vor fast 10 Jahren hat die damalige Merkel-Regierung unser Land Invasoren aus dem Nahen Osten freigegeben. Erstmals in der Geschichte hat ein Land Eroberern nicht nur Tür und Tor eröffnet, sondern sie mit Unterkünften und Geld der eigenen Bevölkerung ausgestattet. Folge: Terror, Gewalt und Bevölkerungsersetzung. [...] Es ist höchste Zeit für eine Politik, die an der Grenze feindselige Invasoren stoppt und sie gar nicht erst ins Land lässt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 370

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