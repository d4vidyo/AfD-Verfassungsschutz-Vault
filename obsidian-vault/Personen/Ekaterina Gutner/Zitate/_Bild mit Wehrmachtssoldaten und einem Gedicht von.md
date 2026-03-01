---
type: zitat
speaker: "[[Ekaterina Gutner]]"
date: 2023-12-24
topic: Nationalsozialismus
page_bfv: 671
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Ekaterina Gutner]] vom 24.12.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Bild mit Wehrmachtssoldaten und einem Gedicht von Thilo Scheller\> "Einmal im Jahr, in der heiligen Nacht, verlassen die toten Soldaten die Wacht, die sie für Deutschlands Zukunft stehen. Sie kommen nach Haus, nach Art und Ordnung zu sehen, schweigend treten sie ein in den festlichen Raum – den Tritt der genagelten Stiefel, man hört ihn kaum – sie stellen sich still zu Vater und Mutter und Kind, aber sie spüren, daß sie erwartete Gäste sind. Es brennt für sie eine rote Kerze am Tannenbaum, es steht für sie ein Stuhl am gedeckten Tisch, es glüht für sie im Glase dunkel der Wein. Und in die Weihnachtslieder, gläubig und frisch, stimmen sie fröhlichen Herzens mit ein. Hinter dem Bild mit dem Stahlhelm dort an der Wand steckt ein Tannenzweig mit silbernem Stern. Es duftet nach Tannen und Äpfel und Mandelkern, und es ist alles wie einst – und der Tod ist so fern. – Wenn dann die Kerzen am Lichtbaum zu Ende gebrannt, legt der tote Soldat die erdverkrustete Hand jedem der Kinder leise aufs junge Haupt: Wir starben für euch, weil wir an Deutschland geglaubt. Einmal im Jahr, nach der heiligen Nacht, beziehen die toten Soldaten wieder die ewige Wacht." Liebe Patrioten, egal aus welchem Land, ich wünsche euch ein besinnliches Weihnachtsfest, das leider nicht bei allen fröhlich wird. Von daher poste ich hier dieses Gedicht. Es ist allen gewidmet, die in den letzten 2 Jahren den Kriegen zum Opfer fielen. Seien wir dem Allmächtigen dankbar, dass Er auf uns aufpasste und wir heute zusammen mit unseren Liebsten beim Kerzenlicht am geschmückten Tannenbaum sitzen können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 671

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