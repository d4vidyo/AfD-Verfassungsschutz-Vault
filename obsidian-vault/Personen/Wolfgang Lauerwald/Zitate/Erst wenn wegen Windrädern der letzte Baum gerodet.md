---
type: zitat
speaker: "[[Wolfgang Lauerwald]]"
date: 2024-08-16
topic: Demokratieprinzip
page_bfv: 634
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Wolfgang Lauerwald]] vom 16.8.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Erst wenn wegen Windrädern der letzte Baum gerodet, das letzte Rind und Schwein wegen des Klimas getötet wurde, alle kritischen Medien verboten sind, in fast jeder Familie Messermorde und Vergewaltigungen stattfanden, der Krieg unsere Heimat verwüstete, der letzte Mensch seine Genspritzen unter Zwang verabreicht bekam, das Sozialkreditsystem Menschen entrechtet und ausgestoßen hat, die Opposition verboten und Widerstandskämpfer im Lager interniert wurden, eine weiße Minderheit in Ghettos lebt und eine kleine superreiche Macht-Elite Milliarden von Sklaven beherrscht, erst dann werdet ihr feststellen, dass ihr aus Gleichgültigkeit, Obrigkeitshörigkeit, Untertanengeist, Feigheit oder Dummheit die Freiheit aufgegeben und die Diktatur irreversibel erhalten habt. Ihr liebe Patrioten und Zuhörer, viele von euch haben bereits erkannt, dass die Politik weltweit in Deutschland und auch in Thüringen genau diese Ziele verfolgt. Einiges haben diese Eliten von ihren Plänen schon umgesetzt, der Rest wird noch kommen, auch wenn uns dies schwer vorstellbar erscheint, weil wir nicht so negativ und bösartig denken und handeln können, doch deren finstere Agenda steht. Aber ich will nicht, dass dies alles so kommt. [...] Die Marionetten in Berlin und Thüringen überschlagen sich in Kriegstreiberei und Kriegshetze. Jährlich werden 50 Milliarden Euro für eine unkontrollierte, vollends gescheiterte und lebensbedrohliche illegale Massen- und Messermigration zweckentfremdet. [...] Der Plan, Deutschland zu zerstören, steht. Wenn wir die Regierungen in Thüringen und Berlin nicht aufhalten, ist unser Untergang besiegelt. Wann begreift das endlich der deutsche Michel, der die Kartellparteien wählt, die Parteien wählt, welche Deutschland hassen und abschaffen wollen? Das grenzt doch schon an das Stockholm-Syndrom, oder? [...] Ja, wir können gemeinsam diese Politik der links-grünen Knechtschaft beenden, die uns jeden Tag ärmer, unsicherer und unfreier macht. Die unser hart erarbeitetes Geld für linke Ideologie-Projekte und unsere eigene ideologische Umerziehung verpulvert. [...] Alles für unsere Heimat Thüringen! Für Deutschland alles!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 634

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