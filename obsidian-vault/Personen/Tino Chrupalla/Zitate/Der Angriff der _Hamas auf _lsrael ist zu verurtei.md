---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2023-10-11
topic: Menschenwürde
page_bfv: 529
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 11.10.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der Angriff der #Hamas auf #lsrael ist zu verurteilen. Ich trauere um alle Kriegstote. Jetzt müssen die Staaten der Region auf Deeskalation setzen, um einen Flächenbrand abzuwenden. Diplomatie ist das Gebot der Stunde. Eine tragfähige Lösung für alle Seiten muss das Ziel sein!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 529

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