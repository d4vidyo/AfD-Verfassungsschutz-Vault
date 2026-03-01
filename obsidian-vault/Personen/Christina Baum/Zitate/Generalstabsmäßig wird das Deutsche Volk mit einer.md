---
type: zitat
speaker: "[[Christina Baum]]"
date: 2021-12-27
topic: Demokratieprinzip
page_bfv: 620
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 27.12.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Generalstabsmäßig wird das Deutsche Volk mit einer mehr als zweifelhaften, oft unwirksamen, dafür häufig schädlichen #Injektion vergewaltigt. [...] Diese #Regierung samt #Scheinopposition führen eine Art #Krieg der unheimlichen Art gegen das eigene #Volk.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 620

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