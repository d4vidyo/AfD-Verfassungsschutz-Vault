---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-10-25
topic: Sonstiges
page_bfv: 709
source: 'YouTube, Kanal Schnellroda'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 25.10.2024 veröffentlicht auf: 'YouTube, Kanal Schnellroda'
> [!quote] Aussage
>Ja, das bewegt mich sehr. Mich hat vor allem erst mal bewegt, als ich kam. Der Dritte im Bunde, Musketier war ja immer Wolfgang Taufkirch, der Bayer. [...] Er hat mir gesagt, ab heute wird gekämpft und Wolfgang, wir unterstützen das, wo wir können. Und ansonsten PEGIDA ist etwas, also ich glaube, in dieser Zeit zwischen der Merkels Grenzöffnung und dem Corona-Regime, da hat PEGIDA etwas geleistet, was wir gar nicht genug würdigen können. [...] PEGIDA hat es doch deutlich gemacht mit diesen zehntausenden Demonstranten, die sich schon gegen die Islamisierung des Abendlandes gerichtet haben. [...] Das war eine ganz große politische und therapeutische Tat von PEGIDA. [...] Wir, also wir in Brandenburg sowieso, mir war das immer bewusst, dass wir als Partei nur ein kleiner Teil sind und wenn wir, wenn wir unser Land retten wollen, dass wir das breite Umdenken brauchen und deswegen Vorfeld, Umfeld, alternative Medien, Metapolitik und sowas und Bürgerbewegung unverzichtbar sind und wir nur ein kleiner Teil sind mit der parlamentarischen Arbeit. Das war uns in Brandenburg immer ziemlich bewusst, das war eigentlich auch Kalbitz glaube ich bewusst. Das war in Brandenburg ziemlich unumstritten. Und wir sagen das, insofern hat schon Lutz Bachmann absolut recht, wenn er sagt, diese Wahlerfolge sind eben auch zum ordentlichen Teil PEGIDA zuzuschreiben, ist gar keine Frage. Wir sind uns dessen bewusst, deswegen werde ich immer mit Hochachtung von den PEGIDA-Leuten sprechen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 709

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