---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2022-11-25
topic: Menschenwürde
page_bfv: 267
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 25.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gewalt gegen Frauen: Unsere feministische Außenministerin macht sich seit Wochen stark für Frauenrechte im Iran, sie steht fest an der Seite der Demonstranten. Aber genauso, wie ihr ihre deutschen Wähler egal sind, so wenig interessiert sie, dass die Gewalt gegen Frauen in Deutschland seit 2015 dramatisch zugenommen hat. [...] Die Gründe für die Rückkehr primitiver Frauenverachtung liegen auf der Hand: Wir haben eine Masseneinwanderung aus Regionen in denen Frauen wie Dreck behandelt werden. Sie sind verfügbare Sklavinnen, Menschen zweiter Klasse, die man im Kindesalter zwangsverheiraten kann, die man auch mal aus Gründen der Ehre ermorden darf.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 267

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