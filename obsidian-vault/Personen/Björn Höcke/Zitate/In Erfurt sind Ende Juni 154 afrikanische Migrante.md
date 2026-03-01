---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-13
topic: Menschenwürde
page_bfv: 217
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 13.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>In Erfurt sind Ende Juni 154 afrikanische Migranten angekommen. Die sind mit dem Flieger aus Nairobi gekommen und in Erfurt gelandet. 154 Menschen. Aus dem Kongo, aus Tansania, aus Somalia. Und nun fragt ihr euch, wie kann das sein? Wie, die mussten auch nicht mehr zu Fuß durch die Sahara? Und die mussten auch kein Schlepperschiff am Mittelmeer? Oder nee, die sind eingeflogen worden. Und die Grundlage ist der UN-Migrationspakt. Diejenigen unter euch, die vielleicht damals schon politisch wach waren, die können sich dran erinnern. Das ist ein Pakt, der besagt, dass es so etwas wie - nein - Umvolkung nicht gibt. Das dürft ihr nicht sagen. Also die Herren und Damen vom Verfassungsschutz, jetzt mal weghören. Oder jetzt ganz genau hinhören. Also wenn ihr von Umvolkung sprecht, dann kommt ihr in den Verfassungsschutzbericht. Aber ihr dürft die englische Version benutzen, denn die steht so in den Dokumenten der UN und der EU. Nämlich Replacement Migration und Resettlement Migration. Bedeutet eigentlich nichts anderes als Ersetzungsmigration. Das heißt, die UN und die EU, also diese Globalisierungsagenturen, ich nenne die jetzt mal so, die im Auftrag von, naja, wem auch immer unterwegs sind, die analysieren einfach, da sind sterbende Völker, wie das Deutsche, wie die Westeuropäer, sind alle sterbende Völker, seit Jahrzehnten lässt man das schon zu, dass wir immer weniger werden, die Lücken werden immer größer. Da sind Lücken, da haben wir Afrika, die haben einen gewaltigen Geburtsüberschuss, die werden bis zum Mitte des Jahrhunderts, werden ihre Bevölkerungsanzahl wahrscheinlich verdoppelt haben, von jetzt 1,3 auf 2,5, 2,6 Milliarden Menschen. Na, was liegt denn da näher, als einfach mathematisch auszugleichen? Da ist zu viel, da ist zu wenig, dann fliegen wir die halt nach Europa ein. Man fragt nicht, ob diese Menschen zu uns passen. Man fragt nicht, ob sie unsere Werte teilen. Wir wurden nicht gefragt. Und wer hat's gemacht? Wer hat's gemacht? Merkel hat's gemacht. Die CDU hat's gemacht. Also die Truppe, die jetzt unter Mario Voigt, rechts blinkt, ja, als harter Hund steht er auf den Bühnen - nein, er steht gar nicht auf den Bühnen, weil es gar kein Publikum für ihn gibt - aber er versucht in den Talkshows jetzt den harten Hund zu machen. Wir lösen das Migrationsproblem. Alles Symptompolitiker hintenherum kommen die Menschen an und werden hier sofort mit einem Duldungsstatus ausgestattet. Und wenn es gut läuft, sind die in drei Jahren Deutscher. Freunde, nach drei Jahren kann man nach dem reformierten Staatsangehörigkeit Deutscher werden. Nach drei Jahren. Im Jahre 2023 sind über 200.000 Menschen eingebürgert worden, haben diesen Pass bekommen. Über 200.000, die größte Gruppe waren Syrer, die gerade mal fünf, sechs, sieben Jahre hier leben. Die haben den deutschen Pass bekommen. Die Kartellparteien schaffen sich gerade ein neues Volk. Freunde, das müssen wir verhindern, sonst verlieren wir diese Demokratie. Sonst verlieren wir diese deutsche Demokratie.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 217

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