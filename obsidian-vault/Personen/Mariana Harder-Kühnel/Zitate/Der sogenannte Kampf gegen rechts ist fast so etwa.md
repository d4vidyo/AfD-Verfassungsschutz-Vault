---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2024-02-16
topic: Demokratieprinzip
page_bfv: 628
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 16.2.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Der sogenannte Kampf gegen rechts ist fast so etwas wie eine Art Ersatzreligion geworden und in diesen Tagen erreicht er so langsam hoffentlich sein Endstadium und hat weite Teile der deutschen Öffentlichkeit in eine Art Wahnzustand versetzt. Ja, die Leute merken gar nicht mehr, dass das, was getrieben wird, eigentlich schon den Charakter eines autoritären Regimes angenommen hat. Erst wollte man uns als AfD politisch stellen, das hat irgendwie nicht so richtig funktioniert und weil man uns politisch nicht stellen konnte, greift man eben nun zu immer härteren Bandagen. Ja, sogar über ein Verbot der AfD wird offen gesprochen, die Verzweiflung muss da tatsächlich sehr, sehr groß sein und mit demokratischen Standards hat das alles längst nichts mehr zu tun.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 628

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