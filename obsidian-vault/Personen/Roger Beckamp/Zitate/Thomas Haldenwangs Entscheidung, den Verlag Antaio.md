---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2024-06-19
topic: Sonstiges
page_bfv: 762
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 19.6.2024 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Thomas Haldenwangs Entscheidung, den Verlag Antaios als 'gesichert rechtsextrem' einzustufen, erinnert doch ein wenig an Ray Bradburys dystopischen Roman 'Fahrenheit 451'. In 'Fahrenheit 451' geht es um eine Gesellschaft, in der Bücher verboten sind und VS-Schlapphüte - Verzeihung - "Feuerwehrmänner beauftragt sind, diese zu verbrennen, um unabhängiges & kritisches Denken zu unterdrücken und die Bevölkerung zu kontrollieren. Ähnlich dazu könnte die Einstufung des Verlags Antaios als ein Versuch gesehen werden, dissidente Positionen zu überwachen und zu unterdrücken. [...] Auf diesen Schock hin: Bestellen Sie doch beim Verlag Antaios!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 762

**Verfassungsschutz Kategorisierung:** Sonstiges.

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