---
type: zitat
speaker: "[[Jan Nolte]]"
date: 2025-02-01
topic: Menschenwürde
page_bfv: 918
source: 'Redebeitrag'
status: Unbewertet
---

# Zitat: [[Jan Nolte]] vom 1.2.2025 veröffentlicht auf: 'Redebeitrag'
> [!quote] Aussage
>Das deutsche Volk ist in Not und es gibt viele Deutsche, die haben keine vier Jahre mehr. In diesen vier Jahren werden doch wieder Menschen durch vollziehbare Ausreisepflichtige umgebracht werden. [...] Ja, und ich hätte dann gerne, dass Robert Habeck mal zu den Schülern geht, zu den vielen Schülern, die vor laufenden Kameras von Migrantengangs verprügelt und gedemütigt wurden. [...] Die sollen zu den Eltern des 13-jährigen Finn fahren, den man auf einem Kieler Schulhof ins Herz gestochen hat, oder die sollen zu den Eltern hier in Wiesbaden fahren, des neunjährigen Jungen, den wollten zwei Migranten zwingen, einen brennenden Böller in den Mund zu nehmen. Meine Damen und Herren, wir versinken in Barbarei und Gewalt. Das ist keinen Tag länger auszuhalten. [...] Und es ist extrem, hier über Jahre eine Massenmigration durchzuführen, die Deutschland nachhaltig verändert, auch aus demografischen Gründen, die dazu führt, dass wir Parallelgesellschaften im Land haben, die dazu führt, dass die Sicherheitslage immer schlechter wird, unter denen das Sozialsystem kollabiert, ohne dass irgendjemand das deutsche Volk jemals gefragt hätte, wollt ihr eigentlich, dass Deutschland sich in dieser Art und Weise nachhaltig verändert?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 918

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