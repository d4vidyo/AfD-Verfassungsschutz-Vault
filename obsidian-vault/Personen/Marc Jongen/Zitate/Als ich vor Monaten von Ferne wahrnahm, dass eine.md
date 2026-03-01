---
type: zitat
speaker: "[[Marc Jongen]]"
date: 2023-12-22
topic: Sonstiges
page_bfv: 774
source: 'Sezession'
status: Unbewertet
---

# Zitat: [[Marc Jongen]] vom 22.12.2023 veröffentlicht auf: 'Sezession'
> [!quote] Aussage
>Als ich vor Monaten von Ferne wahrnahm, dass eine Aktivistengruppe am Bonner Hauptbahnhof einen Regenbogen Zebrastreifen mit den Farben Schwarz Rot Gold überklebt hat, auch ein vom links-grünen Stadtrat in Düsseldorf installiertes arabisches Straßenschild in Karl-Martell-Straße umbenannt hat, da dachte ich: jawohl, so muss sie sein, eine – horribile dictu – Antifa von rechts. Oder sollte man sagen, eine Antiglob. Kreativ, provokativ, gewaltlos, die Linken mit deren eigenen Waffen schlagend und dabei nebenbei deren ganze Heuchelei bloßstellend. Als dann vor wenigen Tagen der Antrag in den AfD-Bundesvorstand kam, diese Gruppe, die Revolte Rheinland, auf die Unvereinbarkeitsliste der Partei zu setzen und zur Begründung die Verwendung der Odal Rune als Zeichen der Bewegung angeführt wurde, die schon der 7. SS-Freiwilligen-Division als Erkennungszeichen diente und seither immer wieder von rechtsextremen Gruppen benutzt worden ist, da war mein erster Gedanke – warum?! Warum nur müssen Akteure und Aktivisten im patriotischen Bereich immer wieder mit vollkommen kontaminierter Symbolik aus der düstersten Zeit deutscher Geschichte hantieren? Warum diese Anspielungen, diese Uneindeutigkeiten? Ist es mangelnde Geschichtskenntnis, eine pubertäre Lust an der Maximalprovokation, oder schlicht und einfach Dummheit? Dass ein tatsächliches Einverständnis mit dem historischen Vorbild besteht, dem die frivole Anspielung gilt, möchte ich ausschließen. Fest steht, dass der Bundesvorstand einer Partei, die mittlerweile in Deutschland weit über 10 Millionen Wähler repräsentiert und auf der die ganze Hoffnung dieses wachsenden Teils unseres Volkes ruht, dass sie das Ruder noch einmal herumreißt und verhindert, dass unser Land vollständig den Bach runtergeht – die zugleich aber von einer links-grünen Übermacht, die sich den Staat und seine Institutionen zur Beute gemacht hat, existenziell bedroht wird –, gar nicht anders handeln kann, als eine klare Trennungslinie zwischen sich und einer solchen Himmelfahrtstruppe zu ziehen. [...] Es gibt ein Paralleluniversum, in dem gewaltlose patriotische Aktionen nicht als Zeichen von Rechtsextremismus gebrandmarkt werden, in dem es umgekehrt nicht ohne rechtliche Konsequenzen bleibt, etwa die erneute Bombardierung Dresdens durch Bomber Harris zu verlangen. In dem 'Deutschland verrecke!' als Hassrede gilt und nicht eine objektive Tatsachenfeststellung zur Kriminalitätsrate von Migranten. In dem, vor allem, das Zeigen von Symbolik gleich welcher Couleur (vor allem patriotischer Couleur) nicht als schlimmer erachtet wird als das Begehen schlimmster Gewaltverbrechen, solange diese von angeblich Schutzsuchenden begangen werden. In solch einem Paralleluniversum – früher nannte man es die Normalität – wäre es dem Bundesvorstand einer patriotischen Partei möglich, sich Aktivisten mit Verirrung im Bereich der politischen Symbolik zur Brust zu nehmen und nach der Korrektur selbiger das Ganze als Dumme-Jungen-Streich abzuhaken und zur Tagesordnung überzugehen. In dem Universum fast totaler links-grüner Hegemonie, in dem wir aber tatsächlich aktuell noch leben, ist mit unverfrorenen Doppelstandards, mit vollkommen pervertierten Beurteilungsmaßstäben und vor allem mit dem unbedingten Willen zur maximalen Repression bis hin zum Parteiverbot der patriotischen Opposition und der Vernichtung der bürgerlichen Existenz ihrer Mitglieder jederzeit zurechnen. [...] Und es geht bei solchen Entscheidungen, um auch diesem oft kolportierten Missverständnis noch entgegenzuwirken, nie darum, dem Verfassungsschutz zu gefallen. Das ist unmöglich, denn er ist (bis auf weiteres) ein weisungsgebundenes Instrument der politischen Kräfte, die uns Übelstes wollen. Es geht einzig und allein um unsere Argumentation gegenüber den Gerichten, deren zumindest Rest-Unabhängigkeit wir idealtypisch unterstellen müssen, wenn wir uns im deutschen politischen System überhaupt noch sinnvoll bewegen wollen. Entscheidungen wie die jüngst zu treffende gehören zu den unangenehmsten und undankbarsten eines Bundesvorstands. Jeder Einzelfall will genau abgewogen sein, es gibt keine Pauschalkriterien. Der Schutz der Partei – und damit des Landes – vor Gefahren, die der Vorstand nicht kontrollieren und noch weniger verantworten kann, muss aber immer dessen oberste Handlungsmaxime sein. Dagegen zu verstoßen kann kurzfristige (persönliche) Vorteile bringen. Der Schaden für die Partei und damit indirekt auch für ihr Vorfeld würde langfristig dafür umso größer sein.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 774

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