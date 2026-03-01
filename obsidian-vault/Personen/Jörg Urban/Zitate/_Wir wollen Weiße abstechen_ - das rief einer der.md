---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-11-25
topic: Menschenwürde
page_bfv: 324
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 25.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>"Wir wollen Weiße abstechen" - das rief einer der 20 jungen, mit Messern bewaffneten Migranten, die bei einem Dorffest im französischen Crepol einen 16-Jährigen ermordeten und 16 weitere Personen verletzten. Es ist der vorläufige Höhepunkt einer Stimmungsmache gegen weiße Menschen, die sich in Europa breitmacht. Ob 'Black Lives Matter‘-Aktivisten, die historische Denkmäler zerstören oder Medien und Wissenschaftler, die die europäische Geschichte auf ihre dunklen Seiten reduzieren wollen - sie alle schüren rassistischen Hass gegen Menschen mit weißer Hautfarbe, Einen Hass, der zum Morden bereit ist. Es gilt jetzt unsere Bürger zu schützen. Gegen die anti-weißen Hassprediger, egal ob Black Lives Matter oder linke Ideologen, muss konsequent vorgegangen werden. Migranten mit rassistischen Einstellungen müssen unverzüglich abgeschoben werden. Die deutsche Politik muss die Sicherheit ihrer Bürger gewährleisten. Und nicht wie die Altparteien Hass und Mord in unser Land importieren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 324

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