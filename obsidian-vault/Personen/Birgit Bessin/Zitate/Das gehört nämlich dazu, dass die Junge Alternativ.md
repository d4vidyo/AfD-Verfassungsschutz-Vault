---
type: zitat
speaker: "[[Birgit Bessin]]"
date: 2022-06-03
topic: Sonstiges
page_bfv: 827
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Birgit Bessin]] vom 3.6.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Das gehört nämlich dazu, dass die Junge Alternative auch in Brandenburg immer mit dabei ist, die Junge Alternative ist bei uns im Landesvorstand kooptiert. Die jungen Leute gehören einfach dazu, denn die Zukunft gehört nun mal den jungen Leuten. [...] Unsere jungen Leute gehören nicht ausgegrenzt, sondern unterstützt und mitgenommen, so dass wir uns gegenseitig unterstützen. Wir brauchen die jungen Leute, die die jungen Wähler ansprechen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 827

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