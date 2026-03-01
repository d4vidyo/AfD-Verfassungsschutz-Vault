---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2022-12-08
topic: Sonstiges
page_bfv: 829
source: 'YouTube; Schnellroda'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 8.12.2022 veröffentlicht auf: 'YouTube; Schnellroda'
> [!quote] Aussage
>Nonkonformität ist ja da das Stichwort, und ich habe die JA natürlich immer als, klar, Unterstützung für die Partei gesehen und als Bewegung auf der Straße. Und das soll sie ja auch sein, diese Jugendorganisation. Wir preschen voran und wir bringen die PS auf die Straße. Das hat man jetzt auch gerade wieder bei der AfD-Demo in Berlin gesehen, am 8. Oktober. Da ist die JA geschlossen aufgetreten und hat wahrscheinlich den, ja, wohl stabilsten Block gebildet, möchte ich es mal nennen. Aber was auch mein Ziel ist, ich möchte auch tatsächlich neue Mandatsträger aus den Reihen der JA rekrutieren. Denn diese lagerübergreifende, dieses lagerübergreifende Verständnis, was bei uns herrscht, das ist ein Kriterium dafür, warum neue Mandatsträger aus den Reihen der JA kommen sollten, aber auch die fachliche Expertise. Lebensalter ist nicht immer ein Indikator für fachliches Wissen oder für fachliche Expertise. Wir haben hervorragende junge Menschen in unseren Reihen, die top ausgebildet sind und die auch schon Berufserfahrung haben. Und es gibt viele, viele Beispiele im Bundestag oder in den Landtagen, wo junge Menschen wirklich reüssieren. Und man darf ja immer nicht vergessen, dass unsere stärkste Wählerschicht bei den Wahlprognosen, ebenfalls jetzt in den neuen Bundesländern, liegt nun mal zwischen 18 und 45 Jahren, also Menschen, die mitten im Berufsleben stehen, die Steuern zahlen. Und das muss natürlich auch bei den Mandatsträgern dann irgendwann abgebildet werden. Also das ist für mich auch ein ganz klarer Auftrag, mehr junge Menschen in die Mandate zu bekommen. Ich möchte nicht, dass wir die nächste Altparteien-Jugendorganisation werden, die nur noch Mandatsträger nachzieht, klar. Aber es müssen deutlich mehr junge Leute in die Mandate kommen, gepaart mit dem Straßenkampf, nenne ich es mal. [...] Ich würde mir mehr junge Menschen wünschen, die sich in dieser Partei engagieren, vor allem auch auf kommunaler Ebene. Ich breche das immer gern runter auf meinen Kreisverband. Wir hatten 2019 30 Mitglieder. Wir sind jetzt bei 150. Wenn man mit einer jungen Truppe engagiert für seine Region arbeitet, dann kann man diese Partei auch nach vorne bringen und vor allem in breiteren Bevölkerungsschichten verankern. Die AfD muss frischer werden. Die AfD muss auch ein bisschen, ich nenne es jetzt mal cooler werden, damit man bei jungen Menschen auch eine breite, eine breite Unterstützung erfährt. Aber ich bin mir sicher, dass das in den nächsten Jahren passieren wird, wenn wir dann eben auch diese jungen Leute in die Mandate bringen und in die erste Reihe stellen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 829

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