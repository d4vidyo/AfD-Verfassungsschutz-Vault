---
type: zitat
speaker: "[[Udo Stein]]"
date: 2024-08-26
topic: Menschenwürde
page_bfv: 451
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Udo Stein]] vom 26.8.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Europa feiert ,Vielfalt‘ - der Islam ein Schlachtfest Es passiert immer und immer wieder, nun auch in der berühmten ,Messerstadt‘ Solingen. Während der woke, blinde, blümchenwerfende Westen seine eigene Tolleranz und Vielfalt feiert, lacht sich der radikale Islam ins Fäustchen und dankt für die Schäfchen, die sich selbst zur Schlachtbank führen. Der Staat ist hier eindeutig mitschuld, wenn eine Abschiebung nicht stattfindet, weil die Person nicht anzutreffen ist! Es ist unfassbar! Wie viele Menschen müssen noch sterben, ehe wir endlich eine klare Kante zeigen und konsequent und unbarmherzig gegen jeden Gesellschaftsschädling und Freiheitsfeind vorgehen? \<Bild Europa feiert ,Vielfalt‘ - der Islam ein Schlachtfest\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 451

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