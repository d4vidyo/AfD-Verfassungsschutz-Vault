---
type: zitat
speaker: "[[Pascal Pfannes]]"
date: 2025-01-11
topic: Menschenwürde
page_bfv: 938
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Pascal Pfannes]] vom 11.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Es ist absolut richtig, dass wir hier keine Pauschalisierung vornehmen sollten. Eine Pauschalisierung wäre zu sagen:,Diese und diese Religion, die hindern wir an der Ausübung'. Dass wir da uns gegen die Glaubensfreiheit in dem einen oder anderen Bereich aussprechen würden. Das tun wir aber nicht. Die islamische Religionsausübung ist nicht dadurch eingeschränkt, wenn wir sagen:,Wir lassen nicht mehr diese islamischen Herrschaftssymbole in unseren Städten zu: der Muezzinruf und das Minarett.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 938

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