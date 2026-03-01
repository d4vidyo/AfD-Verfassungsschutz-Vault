---
type: zitat
speaker: "[[Andreas Lichert]]"
date: 2025-02-01
topic: Menschenwürde
page_bfv: 898
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Andreas Lichert]] vom 1.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und liebe Pressevertreter, Hefte raus! Die Grundrechte und insbesondere die Meinungsfreiheit sind für uns nicht verhandelbar! Und da können sich die Altparteien noch so sehr hinter dem Inlandsgeheimdienst verstecken. Und die Regierung kann noch so viel Angst vor Majestätsbeleidigung haben. Das wird uns in unserem Weg nicht erschüttern. Und jetzt muss ich noch mal kurz ein bisschen technisch werden, aber das muss jeder hier im Raum verstanden haben, was gewissermaßen die juristische Figur ist, mit der unsere Verfolgung durch den Inlandsgeheimdienst überhaupt nur gerechtfertigt werden soll. Es ist der ethnische Volksbegriff, weil wir angeblich die deutsche Staatsbürgerschaft nur an bestimmte Ethnien-Abstammungen knüpfen wollen. Und das wäre tatsächlich so: Würden wir das wollen, stünde nicht mehr der einzelne Mensch, das Individuum im Vordergrund, sondern seine Gruppenzugehörigkeit und das wäre tatsächlich eine Verletzung der Menschenwürde, eine Verletzung von Artikel 1 des Grundgesetzes. Das Problem ist nur, das ist eine Lüge, eine blanke Lüge. Die Beschlusslage der Partei ist eindeutig. Jeder soll die Chance haben, Deutscher zu werden. Aber am Ende einer gelungenen Integration und nicht als Blankoscheck vorneweg durch Blitzeinbürgerung. Ich konnte das Geraune fast schon hören. ,Das sagt er ja jetzt nur so. Das ist ein Feigenblatt. Das muss er jetzt sagen.' Nein, muss ich nicht. Stattdessen will ich was anderes sagen. Ich meine das nämlich von ganzem Herzen. Denn mit Ausländern, die nach Deutschland kommen und mit uns gemeinsam an einer guten Zukunft Deutschlands und seiner Bürger bauen wollen, mit denen haben wir viel mehr gemeinsam als mit den Deutschland-Abschaffern in den Altparteien. Ganz egal wie lang der deutsche Stammbaum ist. Dankeschön! Und weil das so ist, werden wir am 23. Februar abräumen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 898

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