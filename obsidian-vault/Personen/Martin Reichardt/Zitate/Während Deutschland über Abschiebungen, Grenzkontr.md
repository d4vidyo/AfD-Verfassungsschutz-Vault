---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2024-10-01
topic: Menschenwürde
page_bfv: 191
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 1.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Während Deutschland über Abschiebungen, Grenzkontrollen und Migrantengewalt diskutiert, holt die Ampel zu einem weiteren Schlag gegen die deutsche Bevölkerung aus. Im sogenannten 'Partizipationsgesetz', soll eine verpflichtende Quote für 'Personen mit Migrationsgeschichte oder Diskriminierungserfahrung bei Bundesgerichten und Behörden' festgeschrieben werden. Es ist ein weiterer Baustein im Gesellschaftsumbau, den die 'Fortschrittskoalition' in den letzten Monaten ihrer Deutschlandzerstörung, vorantreibt. [...] Und wir Deutschen müssen uns darauf einstellen, dass nicht mehr deutsch in unseren Amtsstuben gesprochen wird. Wenn es dann zu Verständigungsproblemen kommt, sind wir diejenigen, die nicht gut integriert sind in der schönen neuen Welt, die die Ampel schaffen will. Die Quote, die da geschaffen werden soll, ist auch eine Benachteiligung einheimischer Bewerber, denn bis diese Quote erreicht wird, werden zunächst Migranten eingestellt. Die 'Migranten-Quote' dokumentiert eindrucksvoll den ganzen Wahnsinn und die nicht enden wollende Ideologie der 'Vielfalt', die unser Land zerstört. Nur die AfD kann und will diese Deutschlandzerstörer stoppen! Es wird Zeit, dass wir uns unser Land zurückholen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 191

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