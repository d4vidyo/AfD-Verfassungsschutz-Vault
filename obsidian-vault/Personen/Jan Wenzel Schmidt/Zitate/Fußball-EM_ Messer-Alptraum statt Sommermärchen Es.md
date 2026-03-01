---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2024-06-18
topic: Menschenwürde
page_bfv: 284
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 18.6.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Fußball-EM: Messer-Alptraum statt Sommermärchen Es hat sich seit dem Sommermärchen von 2006 etwas spürbar in Deutschland verändert. Es ist nicht mehr das friedliche Land, in dem die Welt ausgelassen bei Freunden feiert. Die Masseneinwanderung machte aus Deutschland ein Land des Messerterrors. Compact hat alle bisher bekannten 'Einzelfälle‘ aufgelistet. Wie lang wird diese Liste am Ende sein?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 284

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