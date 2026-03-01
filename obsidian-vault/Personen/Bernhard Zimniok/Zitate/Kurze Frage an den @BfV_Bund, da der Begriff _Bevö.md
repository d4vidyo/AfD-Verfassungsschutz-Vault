---
type: zitat
speaker: "[[Bernhard Zimniok]]"
date: 2022-02-12
topic: Menschenwürde
page_bfv: 200
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Bernhard Zimniok]] vom 12.2.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Kurze Frage an den @BfV_Bund, da der Begriff #Bevölkerungsaustausch als Verschwörungstheorie gebrandmarkt wird: Wie darf man diesen Austausch denn nennen, wenn jeden Monat eine Kleinstadt einwandert und gleichzeitig die Deutschen weniger werden? #Weltkrieg

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 200

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