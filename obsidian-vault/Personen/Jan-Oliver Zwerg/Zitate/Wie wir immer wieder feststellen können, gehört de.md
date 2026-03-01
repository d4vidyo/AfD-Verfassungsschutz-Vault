---
type: zitat
speaker: "[[Jan-Oliver Zwerg]]"
date: 2023-10-23
topic: Menschenwürde
page_bfv: 458
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Jan-Oliver Zwerg]] vom 23.10.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wie wir immer wieder feststellen können, gehört der Islam nicht zu Deutschland. [...] Er gehört in den Orient. [...] Der Islam ist nicht friedlich. [...] Wir sehen es auch, er äußert sich überall auf der Welt mit Aggression, mit Terror und wir haben bei uns in Deutschland ständig diese Stellvertreterkriege. [...] Die Massenmigration aus Arabien und Afrika bedeuten eben Import von Gewalt. [...] Ja, wir haben uns die Falschen ins Land eingeladen, deswegen haben wir jetzt die Clanstrukturen, wir haben eine hohe Kriminalität. [...] Für alles ist Geld da. Wir merken, dass quasi alle möglichen Vereine, auch für islamische Vereine, die kriegen also noch vom Staat in Größenordnung Geld, Unterstützung, damit sie uns terrorisieren können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 458

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