---
type: zitat
speaker: "[[Christina Baum]]"
date: 2023-10-20
topic: Menschenwürde
page_bfv: 445
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 20.10.2023 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Wir haben durch diese Massenmigration diese Menschen jetzt hier bei uns, auf unseren Straßen, in unseren Häusern. Und für mich war immer klar, dass das zu Konflikten führen wird eines Tages. Es sind einfach verschiedene Kulturen, es sind verschiedene Religionen, die aufeinandertreffen. Und das kann auf die Dauer meiner Meinung nach nicht gut gehen. [...] Und wir haben ja schon wirklich, ganz speziell seit 2015, so viele Tote auf unseren Straßen. [...] Und wir sehen das eigentlich jeden Tag, lesen wir von irgendwelchen Messeangriffen, von irgendwelchen mindestens auch Raubüberfällen, aber eben auch von Tötungsdelikten. Also, wenn ich daran denke, dass das wirklich irgendwie dazu führen sollte, jetzt dieser Konflikt, dass noch mehr Muslime in unser Land kommen, also dann wird mir wirklich angst und bange, ganz speziell als Frau. [...] Wir sollten gelernt haben, auch aus den furchtbaren Folgen der zwei Weltkriege, gerade für unser Volk und für unser Land, dass wir versuchen sollten, wirklich auch in jeder Hinsicht in Frieden mit den anderen Nationen zu leben. [...] Also ich bin wirklich absolut gegen eine Islamisierung Deutschlands. Aber ich bin nicht der Meinung, dass wir anderen Völkern, anderen Religionsgemeinschaften vorschreiben sollten, wie sie zu leben haben. Sie können gern dort in ihren Ländern so leben, wie sie es seit Jahrtausenden tun. Ich möchte sie nicht in Deutschland haben. Ich möchte nicht, dass unsere Tradition, unsere Werte verloren gehen oder von anderen sozusagen erobert werden. Und das ist der einzige Grund, weshalb ich jetzt gegen die Islamisierung bin. Ich bin aber nicht prinzipiell gegen arabische Länder oder gegen arabische Völker. Das ist der absolute Unterschied. Die haben genauso ihr Recht, in ihren Traditionen zu leben, wie wir das wollen. Ich möchte auch nicht von diesen eben hier in Deutschland bevormundet werden, ich möchte so leben, wie meine Vorfahren schon immer gelebt haben

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 445

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