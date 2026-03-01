---
type: zitat
speaker: "[[Jean-Pascal Hohm]]"
date: 2024-03-02
topic: Menschenwürde
page_bfv: 184
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Jean-Pascal Hohm]] vom 2.3.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Es gibt ein Thema, was uns alle beschäftigt und wenn ich an Infoständen aktiv bin, dann ist es auch das Thema, was den Menschen unter den Nägeln brennt. Und das ist der Bevölkerungsaustausch, das ist die massive Migrationspolitik, die in diesem Land stattfindet, die uns zu Fremden im eigenen Land macht, die uns hier austauscht und das wollen wir nicht. Wir als AfD sind die Partei der Deutschen. Wir sind die, die wollen, dass Deutschland das Land der Deutschen bleibt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 184

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