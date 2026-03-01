---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2024-08-16
topic: Menschenwürde
page_bfv: 238
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 16.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Es geht nicht mehr um das Wohl des deutschen Volkes, sondern es geht darum, dass wir verschwinden, dass wir als Deutsche verschwinden, dass die Franzosen als Franzosen verschwinden, dass die Polen als Polen verschwinden. Das kann man an vielen Dingen ablesen. Unsere Grenze wird ja nicht mehr geschützt, unsere deutsche Sprache wird verhunzt, wir haben das Gendern, die Traditionen werden geschliffen. Und zu uns kommen Menschen aus aller Herren Länder und auch Terroristen. [...] Und das zeigt – das zeigt, dass wir, liebe Freunde, hier quasi verdünnt werden sollen, dass aus Europa hier ein Transitgebiet gemacht werden soll mit Menschen aus aller Herren Länder. Sie wollen nämlich unsere Nationalität schleifen, damit sie uns besser im Griff haben oder weil sie meinen, sie wollen eine Eine-Welt-Regierung irgendwann schaffen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 238

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