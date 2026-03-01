---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2024-02-13
topic: Sonstiges
page_bfv: 745
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 13.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>In Gedenken an die Opfer der Bombenangriffe auf Dresden [...] Wir vergessen nicht, dass ein wichtiger Teil unserer Identität durch die Zerstörung unserer Städte ausradiert werden sollte. Wir vergessen sie nicht, die tausenden Menschen, die so grausam ihr Leben ließen. Und wir vergessen auch nicht das Leid, das ihre Familien bis heute ertragen müssen. An dieser Stelle möchten wir uns auch bei EinProzent bedanken, die mit ihrer wichtigen Aktion gestern ein Zeichen gegen das Vergessen gesetzt haben und zeigen, dass auch 79 Jahre später die Erinnerung nicht verblasst ist

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 745

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