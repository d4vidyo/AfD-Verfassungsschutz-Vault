---
type: zitat
speaker: "[[Irmhild Boßdorf]]"
date: 2023-06-24
topic: Menschenwürde
page_bfv: 248
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Irmhild Boßdorf]] vom 24.6.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir wollen kein Heimweh in den eigenen Städten haben, wenn wir durch Köln, wenn wir durch Dortmund, Wiesbaden oder mittlerweile auch durch Dresden gehen. Wir wollen, dass unsere Heimat Deutschland das Land der Deutschen bleibt. Wir wollen, dass Europa der Kontinent der Europäer bleibt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 248

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