---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-10-29
topic: Menschenwürde
page_bfv: 422
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 29.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Dresdner AfD-Anfrage offenbart: Die Betreuung von 219 unbegleiteten minderjährigen Asylsuchenden kostete die Stadt 2023 insgesamt 15,4 Millionen Euro- 70.000 Euro pro Person. Gleichzeitig erzielt die Rückkehrberatung 'kaum Erfolge'. Genug davon! Wir brauchen eine millionenfache Remigration und das erreichen wir am besten durch die Privatisierung der Abschiebungen. Im Landtag Brandenburg werden wir hierzu bald die ersten Schritte unternehmen. Ob in Sachsen oder Brandenburg: Asylmissbrauch stoppen! Unser Geld für unsere Leute!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 422

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