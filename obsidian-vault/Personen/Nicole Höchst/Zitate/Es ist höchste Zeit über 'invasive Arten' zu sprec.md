---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2022-11-27
topic: Menschenwürde
page_bfv: 168
source: 'Beitrag auf journalistenwatch.com'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 27.11.2022 veröffentlicht auf: 'Beitrag auf journalistenwatch.com'
> [!quote] Aussage
>Es ist höchste Zeit über 'invasive Arten' zu sprechen, denn schließlich ist selbst aus der Sicht der EU-Kommission 'die Verbreitung invasiver, gebietsfremder Arten – sowohl Tiere als auch Pflanzen – einer der Hauptfaktoren für den Verlust der biologischen Vielfalt. Diese Tiere und Pflanzen können nicht nur zu ökologischen und wirtschaftlichen Schäden führen, sondern auch Krankheiten übertragen, Gesundheitsprobleme verursachen oder zu Verlusten in der Landwirtschaft führen.' Im schlimmsten Fall können einheimische Arten komplett ausgerottet werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 168

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