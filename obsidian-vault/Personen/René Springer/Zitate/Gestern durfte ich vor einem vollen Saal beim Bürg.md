---
type: zitat
speaker: "[[René Springer]]"
date: 2023-03-22
topic: Menschenwürde
page_bfv: 198
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 22.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gestern durfte ich vor einem vollen Saal beim Bürgerdialog der AfD-Bundestagsfraktion in Frankfurt (Oder) über meine parlamentarische Arbeit und die aktuellen Probleme in unserem Land - wie zum Beispiel absurd niedrige Renten - sprechen. Wie so häufig in den vergangenen Tagen ging es auch um den stattfindenden Bevölkerungsaustausch sowie den Krieg in der Ukraine. Beides muss beendet werden!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 198

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