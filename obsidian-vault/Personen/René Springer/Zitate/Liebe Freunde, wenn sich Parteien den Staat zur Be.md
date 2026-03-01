---
type: zitat
speaker: "[[René Springer]]"
date: 2021-08-22
topic: Demokratieprinzip
page_bfv: 608
source: 'Rede'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 22.8.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Liebe Freunde, wenn sich Parteien den Staat zur Beute machen, wenn Grundrechte willkürlich außer Kraft gesetzt werden, wenn die Gewaltenteilung nur noch auf dem Papier existiert, dann nennt man das in allen Sprachen dieser Welt Tyrannei. Es ist einfache und absolute Tyrannei und sie mag noch so mild daherkommen, sie bleibt Tyrannei und sie nimmt uns die Freiheit.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 608

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