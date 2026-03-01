---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-04-25
topic: Menschenwürde
page_bfv: 475
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 25.4.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Das Ziel ist die Unterwerfung unter den Islam. Noch haben wir die Möglichkeit zur Umkehr. Jetzt muss unserer Toleranz ein Ende gesetzt werden, wenn wir in unserem eigenen Land wieder Herr über unsere Kultur, Tradition und Identität sein wollen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 475

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