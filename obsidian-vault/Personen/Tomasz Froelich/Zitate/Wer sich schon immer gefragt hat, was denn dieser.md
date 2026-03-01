---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2023-11-18
topic: Menschenwürde
page_bfv: 201
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 18.11.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wer sich schon immer gefragt hat, was denn dieser ominöse #Bevölkerungsaustausch eigentlich so ist, der dürfte heute mit einem Blick auf die Zuschauerränge im Berliner Olympiastadion beim Länderspiel zwischen #Deutschland und der #Türkei eine Antwort erhalten haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 201

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