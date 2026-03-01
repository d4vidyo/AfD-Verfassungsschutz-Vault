---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2023-09-19
topic: Menschenwürde
page_bfv: 186
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 19.9.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Hier kann man sehen, warum das Establishment darum bemüht ist, Worte zu kriminalisieren, die darauf hindeuten, es würde in [Deutschlandflaggen-Symbol] ein Austausch des Souveräns stattfinden. Die @spdde arbeitet mit Hochdruck daran, ihre Wähler aus Kreisen weit jenseits der einheimischen Bevölkerung zu gewinnen. Sie arbeitet damit an der Marginalisierung der einheimischen Bürger. Hier wäre ein echter @BfV_Bund gefordert. #FaeserRuecktritt #Wahlen

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 186

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