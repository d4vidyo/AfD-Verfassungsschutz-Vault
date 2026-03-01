---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2022-06-29
topic: Sonstiges
page_bfv: 826
source: 'YouTube; Irfan Peci'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 29.6.2022 veröffentlicht auf: 'YouTube; Irfan Peci'
> [!quote] Aussage
>Zum Verhältnis zur Jungen Alternative. Also das ist wirklich jetzt ein Bundesvorstand, der definitiv sich von vornherein schon für die JA ausgesprochen hat. Die haben erkannt, dass wir also auch die Zukunft dieser Partei sind, dass wir die Zukunft dieses Landes sind und dass wir garantiert, also es wird ganz sicher gefördert werden, und dass wir auch, Tino Chrupalla hat es ja auch in seiner Rede angekündigt, dass die Jugend also durch Schulungen, durch Seminare, durch Presse- und Öffentlichkeitsschulungen halt gefördert werden, und ich blicke da wirklich sehr positiv in die Zukunft.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 826

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