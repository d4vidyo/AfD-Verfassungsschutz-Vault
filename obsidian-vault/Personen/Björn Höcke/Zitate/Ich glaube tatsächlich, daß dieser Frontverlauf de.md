---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-10-03
topic: Demokratieprinzip
page_bfv: 546
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 3.10.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ich glaube tatsächlich, daß dieser Frontverlauf der bedeutendste der Gegenwart ist: [...]. Dieses Regenbogenimperium mit den USA als Kernland und der BRD als wichtigstem Brückenkopf in Europa ist es, das die Zerstörung der Nation durch Masseneinwanderung forciert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 546

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