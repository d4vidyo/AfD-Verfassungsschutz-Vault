---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-10-20
topic: Sonstiges
page_bfv: 707
source: 'YouTube, Kanal "Michael Michael Wittwer 2.0"'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 20.10.2024 veröffentlicht auf: 'YouTube, Kanal "Michael Michael Wittwer 2.0"'
> [!quote] Aussage
>Liebe Freunde, PEGIDA war immer die große Schwester von Zukunft Heimat. Und in diesen Jahren zwischen Merkels Grenzöffnung und dem Corona-Regime, da waren Cottbus, aber da war vor allem Dresden ein Leuchtturm, ein Leuchtturm der Freiheit in Deutschland, ein Leuchtturm für alle, denen Heimat, Freiheit und Tradition irgendetwas bedeuten. Und wir wären doch erstickt in diesen Jahren, hätte PEGIDA nicht das Fenster aufgestoßen, hätte PEGIDA das Fenster nicht weit aufgestoßen. Und die Bundesverdienstkreuze, die ein unwürdiger Bundespräsident unwürdigen Funktionären verteilt, die es nicht verdient haben, hier namentlich genannt zu werden, die landen auf dem Schrottplatz der Geschichte. Aber an PEGIDA wird man sich noch in Jahrzehnten erinnern. An PEGIDA wird man sich in Jahrzehnten erinnern, wenn wir Deutschland aus den Trümmern wieder aufgebaut haben, in die CDU, SPD und Grüne dieses Land geführt haben. Liebe Freunde, ich sagte es, wir wären erstickt ohne die PEGIDA-Demos und ich wäre nicht der Vorsitzende der Landtagsfraktion der AfD im Landtag Brandenburg ohne PEGIDA, Vorsitzender einer Fraktion, die jetzt in der vergangenen Woche erstmals mit einer Sperrminorität in den Landtag einzog und verhindern kann, dass die Verfassung künftig willkürlich geändert wird. Und liebe Freunde, ich sage es hier in Dresden mit Freude und mit vollem Bewusstsein, nirgendwo mehr als in Brandenburg, meine lieben Sachsen, ist PEGIDA Teil des AfD-Wahlerfolgs! [...] Und unsere historische Aufgabe besteht nicht darin, irgendwelche Regierungsmehrheiten zu haben, sondern Deutschland als Staat der Deutschen zu erhalten und wo er verloren gegangen ist, wiederherzustellen. Nichts weniger ist unsere historische Aufgabe. Und nur diese Aufgabe kann der Maßstab unseres Handelns und unseres Erfolges sein. Und wenn ich von wir spreche, dann meine ich eben nicht nur die AfD. Ich meine die Bürgerbewegung, ich meine euch von PEGIDA, ich meine den Straßenprotest, ich meine die alternativen Medien und ich meine den vorpolitischen Raum. Wir alle gehören zusammen und nur wenn wir zusammen handeln, dann werden wir unserer historischen Verantwortung gerecht werden. [...] Und liebe Freunde, in diesem Sinne, in diesem Sinne Teil des AfD-Erfolgs zu sein, das ist das größte Verdienst von PEGIDA. Und damit, liebe Freunde, habt ihr euch ein bleibendes Denkmal gesetzt. Ich bin traurig über euren Abschied, aber noch mehr bin ich euch dankbar, denn ihr habt uns Hoffnung gegeben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 707

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