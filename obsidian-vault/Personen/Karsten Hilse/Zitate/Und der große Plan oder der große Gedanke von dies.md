---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2024-08-11
topic: Menschenwürde
page_bfv: 242
source: 'Interview mit Deutschland-Kurier'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 11.8.2024 veröffentlicht auf: 'Interview mit Deutschland-Kurier'
> [!quote] Aussage
>Und der große Plan oder der große Gedanke von diesen, früher hätte man gesagt Philanthropen, aber das sind ja keine Philanthropen, das sind ja keine Menschenfreunde. Es sind Leute, die letztendlich denken, die müssten die Welt irgendwie formen in ihrem Sinne. Und die denken einfach, wenn sich alle Rassen irgendwie durchmischen, dann gibt es keine Probleme mehr auf der Erde. Und das soll erfolgen. Aber das erfolgt ja nur in Richtung, ich sage jetzt mal, des 'weißen' Siedlungsgebietes. Es ist ja nicht so, dass irgendwie nach unten, dass es im 'Contract for Migration' drinsteht, dass eben Weiße in Afrika siedeln sollen oder Weiße in Südamerika oder in Südostasien siedeln sollen, um letztendlich diese Durchmischung da voranzubringen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 242

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