---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-06-01
topic: Nationalsozialismus
page_bfv: 680
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom Juni 2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und eine der wichtigsten Aufgaben, vielleicht sogar die allerwichtigste muss sein, unserem Volk wieder ein natürliches Selbstbewusstsein und Selbstvertrauen, einen gesunden Nationalstolz zurückzugeben. Beides wurde unter den Trümmern einer jahrzehntelangen Schuldhaftigkeit verschüttet. Und diese Trümmer müssen wir endlich beiseite räumen. Ich träume mit vielen von euch den Traum eines souveränen, freien, selbstbestimmten deutschen Volkes, das seine Geschicke wieder selber in die Hand nimmt.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Juni 2022

**SPIEGEL-Notiz:** Gutachten Seite: 680

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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