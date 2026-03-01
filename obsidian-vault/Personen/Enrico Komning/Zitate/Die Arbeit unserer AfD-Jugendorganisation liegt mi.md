---
type: zitat
speaker: "[[Enrico Komning]]"
date: 2022-10-28
topic: Sonstiges
page_bfv: 827
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Enrico Komning]] vom 28.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Arbeit unserer AfD-Jugendorganisation liegt mir sehr am Herzen. Die Aktivitäten und Aktionen der Junge Alternative Mecklenburg-Vorpommern haben sich in den letzten Monaten hervorragend entwickelt. Die Teilnahme der Jungs und Mädels an regionalen aber auch bundesweiten Aktionen sind ebenso präsent wie die kreative Protestgestaltung an öffentlichen Orten. Ich habe deshalb letzte Woche einen Fördermitgliedsantrag gestellt. Ordentliches Mitglied darf ich ja leider altersbedingt nicht mehr sein.

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