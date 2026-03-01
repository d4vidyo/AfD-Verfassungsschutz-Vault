---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-07-18
topic: Menschenwürde
page_bfv: 239
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 18.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Zu dieser Aussage stehe ich heute mehr denn je, denn die anhaltende, massenhafte Zuwanderung von Menschen aus aller Herren Länder wird nun wirklich für jeden täglich im öffentlichen Raum sichtbarer. Deren Folgen sind genau diejenigen, die in der Definition vom Genozid beschrieben werden. [...] Dabei handelt es sich um Verbrechen, die zusammengenommen einem Volk oder einer Volksgruppe die Lebensgrundlagen entziehen, Ein Verbrechen, dass über kurz oder lang also zur Vernichtung der Existenz des Volkes oder der Volksgruppe führen sollten. Die massive Reduktion des deutschen Bevölkerungsanteils in den nächsten Generationen im eigenen Land verglich ich deshalb nach der obigen Definition mit einem schleichenden Völkermord durch genau diese hauptsächlich von den Grünen betriebene, inzwischen aber von alle Altparteien mitgetragene, Migrationspolitik.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 239

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