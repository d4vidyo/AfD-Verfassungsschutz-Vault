---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2023-04-01
topic: Demokratieprinzip
page_bfv: 614
source: 'Compact'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom April 2023 veröffentlicht auf: 'Compact'
> [!quote] Aussage
>Ich will nochmal an die Corona-Zeit erinnern. Da haben ja die Abgeordneten - außer uns - das Grundgesetz letztendlich mit Füßen getreten. Man hat so viel Angst eingejagt, dass jetzt alle sterben, wenn wir das nicht tun, wenn wir nicht die Versammlungsfreiheit einschränken, wenn wir nicht einschränken, dass die Leute draußen spazieren gehen dürfen. Das haben viele schon vergessen! Man durfte teilweise nicht mal raus und sich auf eine Bank setzen, um ein Buch zu lesen! Das muss man sich mal reinziehen. Da ist für mich die Tür zum Faschismus aufgestoßen. Ich weiß es nicht, ob es Faschismus wird. Sobald ich mit dem Begriff irgendwo hantiere, erzählen mir vermeintlich kluge Leute: Du weißt ja gar nicht, was Faschismus ist, und dann schicken sie mir irgendwelche Links von Wikipedia und kaprizieren das dann letztendlich nur auf Italien oder NS-Deutschland - nur das sei dann echter Faschismus! Dabei sind wir, zumindest in der Zeit der Corona-Politik, ziemlich nah dran gewesen.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: April 2023

**SPIEGEL-Notiz:** Gutachten Seite: 614

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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