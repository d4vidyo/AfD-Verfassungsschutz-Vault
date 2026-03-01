---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2024-08-25
topic: Menschenwürde
page_bfv: 235
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 25.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Vielfalt bedeutet [...] Multikulti und was bedeutet Multikulti? Multikulti bedeutet Traditionsverlust, Identitätsverlust, Verlust der Heimat, Mord, Totschlag, Raub und Gruppenvergewaltigungen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 235

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