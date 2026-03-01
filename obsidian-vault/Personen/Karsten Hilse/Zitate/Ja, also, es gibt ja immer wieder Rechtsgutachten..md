---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2023-03-01
topic: Demokratieprinzip
page_bfv: 540
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 1.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ja, also, es gibt ja immer wieder Rechtsgutachten. Leute äußern sich, Völkerrechtler, wie auch immer, die sagen okay, wir sind ein besetztes Land. Wir sind theoretisch nicht, so wie du [Anm.: auf Reichardt bezogen] das gerade gesagt hast, wir sind souverän, zumindest laut Vertrag. Ich persönlich habe keine Nebenabsprachen, Nebengesetze, Nebenvereinbarungen, die sozusagen neben dem Zwei-plus-Vier-Vertrag geschlossen worden sein sollen, je gesehen. Diejenigen, die davon erzählen, behaupten das auch nur, legen das nicht vor, weil es natürlich auch geheime Absprachen sind und so weiter und so fort. Aber reinpraktisch sind wir natürlich, sind natürlich die Amerikaner nicht abgezogen [...], halten hier ihre Militärbasen, von denen sie auch noch es schlechterweise Krieg in Asien führen, also von Ramstein. Von Ramstein werden unter anderem die Drohnen gesteuert, mit denen in Pakistan oder überhaupt in Ostasien dort einfach nur völkerrechtswidrig und rechtswidrig Menschen einfach in einem anderen Land umbringen, mit welcher Begründung auch immer. Und dann kann man schon sagen – ja , natürlich – sind wir besetzt. Wir könnten souverän sein, wenn es eine souverän denkende und souverän handelnde Regierung gäbe. Aber wir haben eben keine souverän handelnde Regierung. Schwachsinn. Also ich werde immer wieder mal zum Beispiel nach dem Morgenthau-Plan gefragt, ob der immer noch sozusagen gilt, ob das jetzt durchgezogen wird. [...] Und dann sag ich immer, diesen Morgenthau-Plan braucht es gar nicht bei dieser Regierung. Es braucht gar keinen Plan. Die sind einfach so, erstens verblödet, dumm und einen dummen Menschen kannst du natürlich viel, viel besser lenken. Und zweitens sind sie natürlich auch angetreten, um eben nicht deutsche Interessen, sondern amerikanische Interessen zu vertreten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 540

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