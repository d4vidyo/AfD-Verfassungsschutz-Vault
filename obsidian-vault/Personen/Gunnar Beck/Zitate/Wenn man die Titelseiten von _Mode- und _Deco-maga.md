---
type: zitat
speaker: "[[Gunnar Beck]]"
date: 2022-08-29
topic: Menschenwürde
page_bfv: 432
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Beck]] vom 29.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wenn man die Titelseiten von #Mode- und #Deco-magazinen, #Kleiderwerbung u. Regierungsbroschüren liest, könnte man meinen, autochtone #Europäer seien ,endangered species' wie Primaten. Doch das wird erst in 25 Jahren so sein, wenn die #Propaganda Früchte trägt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 432

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