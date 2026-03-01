---
type: zitat
speaker: "[[Peter Boehringer]]"
date: 2022-07-29
topic: Demokratieprinzip
page_bfv: 623
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Peter Boehringer]] vom 29.7.2022 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Es ist wahnsinnig, welche monströsen Lügen möglich waren und sind und wie viele Menschen und Verbände mitmachen. [...] Was auch erschreckend war die letzten zweieinhalb Jahre, und das war glaube ich in dieser Form auch einmalig und erstmalig so, dass man weltweit [...] diese Volksverdummung durchsetzen konnte, weltweit. Das ist schon erstaunlich und erheblich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 623

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