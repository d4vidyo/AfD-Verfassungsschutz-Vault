---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-06-23
topic: Sonstiges
page_bfv: 828
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 23.6.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wir lassen uns nicht verleumden, erst recht nicht von einer politisch instrumentalisierten Behörde. Wir wehren uns! Nach jahrelangen Anfeindungen wissen wir, wie wichtig es ist, uns nicht von außen gegeneinander ausspielen zu lassen. Es ist der neue Zusammenhalt, der die AfD jetzt mit guten Umfrageergebnissen belohnt. Nun braucht die Junge Alternative unsere Unterstützung! Spenden Sie großzügig für das Gerichtsverfahren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 828

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