---
type: zitat
speaker: "[[Daniel Freiherr von Lützow]]"
date: 2021-08-22
topic: Menschenwürde
page_bfv: 480
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Daniel Freiherr von Lützow]] vom 22.8.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und wir alle selber wissen: Man hat Tschetschenen ins Land geholt. Jeder der zu Ostzeiten aufgewachsen ist, weiß, was Tschetschenien ist. Das sind Islamisten vom Feinsten. Das sind nicht Leute, die dem islamischen Glauben angehören, da muss man ja auch unterscheiden, sondern das sind Islamisten, die bereit sind, für ihren Glauben in den Tod zu gehen. Genau das gleiche ist mit den Afghanen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 480

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