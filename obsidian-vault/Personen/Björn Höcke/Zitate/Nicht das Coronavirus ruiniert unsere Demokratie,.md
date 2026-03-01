---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2021-07-10
topic: Menschenwürde
page_bfv: 502
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 10.7.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Nicht das Coronavirus ruiniert unsere Demokratie, nicht das Coronavirus ruiniert unseren Rechtsstaat, nicht das Coronavirus ruiniert unseren Staatshaushalt. Nein, die Corona-Maßnahmen-Politik ruiniert uns. [...] Und DER SPIEGEL, früher mal das Sturmgeschütz der Demokratie, heute das Sturmgeschütz des Establishments ist ja auch ganz federführend beim Herbeischreiben einer todbringenden Pandemie. Und wen wundert es, wenn man annimmt, dass DER SPIEGEL von einem der größten Profiteure der Corona-Maßnahmen-Politik, nämlich Bill Gates, mal 2,3 Millionen Euro Spenden erhalten hat. 'Des Brot ich ess, des Lied ich sing'. So war es immer und so wird es immer bleiben und deswegen brauchen wir ganz dringend endlich eine freie Presse in Deutschland. Corona ist für mich, und ich habe mich jetzt anderthalb Jahre in diesem neuen Politikfeld bewegt, viel gelesen und viel gelernt, ist für mich über weite Strecken eine einzige große Inszenierung. Diesmal wieder fragen: 'Cui bono? Wem nützt es?' Ja, es nützt den schwarzen Amigos, die sich mit dem Maskenverkauf eine goldene Nase verdient haben, aber wem nützt es natürlich aber vor allem nützt es natürlich Big Data und natürlich Big Tech. Also all den Konzernen, die ich jetzt namentlich nicht nennen muss, die durch die Digitalisierung, die durch Corona natürlichen Schub erhalten hat, sich die Taschen richtig vollgemacht hat. [...] Ernst Wolff, der eine oder andere von ihnen von euch kennt ihn vielleicht, ein unermüdlicher Aufklärer, was das Weltfinanzsystem angeht, was die Macht der globalen Geld-Eliten angeht, hat vor einigen Monaten mal eine sehr, sehr gute Rede in Stuttgart gehalten, es könnte jetzt schon ein Jahr her sein bei einer Querdenken-Demonstration. Und er hat die einfache aber richtige überzeitliche Einsicht nochmal wunderbar in Worte gefasst, indem er feststellte: Geld bedeutet Macht. Und noch nie in der Weltgeschichte haben so wenige Menschen so viel Geld und damit so viel Macht in ihren Händen gehalten, wie in der Gegenwart. Auch wenn sich ein George Soros, ein Bill Gates und wie sie alle heißen, obwohl George Soros darf ich gar nicht mehr erwähnen, wenn ich ihn erwähne bin ich schon im sogenannten Verfassungsschutzbericht, [...].Ja, George Soros, Bill Gates und die anderen, die spielen sich immer gerne als Philanthropen auf, das wissen wir, die wollen aber vor allen Dingen die Welt als globale Freihandelszone, die wollen ein entortetes, wurzelloses Individuum, das sie im Profitinteresse überallhin schieben können, um für sie zu arbeiten. Sie wollen keine Kulturen, sie wollen keinen Nationen, sie wollen die One-World und sie wollen am Ende auch eine Weltregierung. Das ist ihr Plan, so erkenne ich das jedenfalls, wenn ich ihre Äußerung zusammenziehe und interpretiere, wenn ich auch ihre schriftlichen Äußerungen lese und zusammenziehe und interpretiere. Und mit dem Vehikel Corona ist dann tatsächlich dieser Vision, die für mich keine Vision ist sondern eine Dystopie, ein Schreckbild, dieser Vision der One-World und der World Governments einen großen Schritt näher gekommen, das müssen wir leider so konstatieren. Es gibt hinhaltenden Widerstand und der ist extrem wichtig. Wir sind in einer schwierigen Phase als Patrioten. Wir haben seit der Entmachtung von Donald Trump wirklich mit einem Frontalangriff des globalistischen Establishments zu tun. [...] Diese Globalisten wollen das Ende von dem, was wir lieben, wofür wir leben und was wir an unsere Kinder weitergeben wollen. Wir allerdings, wir von der AfD, wissen, die Nation ist noch lange nicht am Ende. [...] Da gibt es verschiedene Theorien, die alle nicht bewiesen sind, aber man kann auch dieser Theorie, weil das Wetter sich ständig ändert und nicht beeinflusst werden kann, tatsächlich auch die Transformation der ganzen Welt in Richtung One-World und Weltregierung hin ausrichten und ablaufen lassen. So meine Befürchtung. [...] Wir haben ein Altparteienkartell, das von den Globalisten angeführt wird und das sich inhaltlich mit großen Politikfeldern kaum noch unterscheidet und die [...] drei großen, ideologisch aufgeladenen Politikfelder, deren Handhabung über das Wohl und Wehe unseres Landes entscheidet – die Euro-Rettung, Energiewende und die Einwanderung – in diesen drei großen Politikfeldern sprechen die Altparteien von der umbenannten SED bis zur Merkel-Söder-Laschet-Union mit einer Stimme. Sie sind gleichgeschaltet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 502

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