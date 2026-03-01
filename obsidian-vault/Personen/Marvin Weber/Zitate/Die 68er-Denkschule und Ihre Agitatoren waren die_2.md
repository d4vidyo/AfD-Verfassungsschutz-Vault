---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-08-09
topic: Demokratieprinzip
page_bfv: 586
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 9.8.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die 68er-Denkschule und Ihre Agitatoren waren die geistig-reaktionären Nachfolger der Nationalsozialisten. Sie und ihre Post-68er-Nachfolger herrschen in ihrem radikalen Zersetzungswahn gegen die eigene Kultur wie ideologisch vernarbte Nazirichter, die tagtäglich noch nach 75 Jahren die Rache an den eigenen Bürgern planen. [...] Sie, also die Denkschule dar heutigen Grünen konnten durch die Institutionen marschieren und mit Hilfe von RAF-Terror, historischer Erpressung und kollektiver Sippenhaft ein traumatisiertes und ängstliches Volk in den Wahnsinn treiben und beherrschen. Die Multikulti-Abschaffung zum einen und fatale Abschaffung alles Deutschen durch die, die bis heute den Hitlerkult für ihren ewige Zwangsneurose konstruieren und den Rassismus gegen die eigenen zelebrieren, wird jeden Tag schlimmer. Wir müssen uns von Clans beherrschen, von den eingewanderten Kulturen aus den kriminellsten Regionen der Erde jeden Tag aufs Neue beglücken lassen und die westdeutsche Stürmerpresse, die den Antisemitismus durch Germanophobie eingetauscht hat, schweigt, relativiert, inszeniert mit ihrer Wortakrobatik eine neue Normalität. Was für eine kalte, ideologisch vernarbte Führungsschicht dieses polit-medialen Systems, die immer im Sinne des kultur- und staatszersetzenden Globalismus denkt, aber nie an die eigenen Bürger und diese wie Untertanen behandelt. Der größte Verrat aber haben die 'Bürgerlichen' begangen, die sich aus Konformismus, Opportunismus und Machtgier diesem neuen anti-deutschen Totalitarismus nicht nur unterworfen haben, sondern ohne Gegenstimme im Kadavergehorsam diese Doktrin der totalen Zersetzung übernommen haben und bis heute mit ihren Kampf-gegen-Rechts-Gesetzen die eigenen Bürger für Freiwild ihrer Antifa-Schlägertrupps erklären und die Meinungsfreiheit in Feudalherrenart radikal verachten. Die geistigen Erben der Nazis fordern Brandbomben auf Dresden, brennende Deutschlandflaggen, Umvolkung und Kanthölzer gegen den freien Geist. Sie leben das Motto: 'Alles, alles über Deutschland' und sind idR. zugleich alimentierte Nutznießer dieses Landes und seiner noch deutschen Mehrheitsbevölkerung: Das schlimmste Schmarotzertum auf Erden, die geistig degenerierteste Pöbelherrschaft, die uns Deutsche jeden Tag aufs Neue als Feindbild schärft und in Grund und Boden regiert.

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Die 68er-Denkschule und Ihre Agitatoren waren die]]

**SPIEGEL-Notiz:** Gutachten Seite: 586

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