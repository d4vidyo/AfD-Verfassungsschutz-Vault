---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-03-29
topic: Demokratieprinzip
page_bfv: 565
source: 'Rede/Facebook Livestream'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 29.3.2022 veröffentlicht auf: 'Rede/Facebook Livestream'
> [!quote] Aussage
>Und ich muss vor allen Dingen zu Beginn noch mal zu Corona reden, weil der Klabautermann in Berlin mit der mit der Plandemie ja immer noch nicht fertig ist. [...] Hinter dieser Pandemie steckt der Ansatz einer Plandemie. Und dann wurde die heilige Inzidenz geboren. Die heilige Inzidenz, der alles geopfert wurde, unsere wirtschaftliche Wohlfahrt. Unsere Demokratie wurde geschreddert. Unser Rechtsstaat wurde geschreddert, unsere Freiheit wurde uns genommen. [...] Dieses politische Establishment, das zu einem Kartell zusammengewachsen. Alle Teilnehmer wollten diese Pandemie nutzen und haben das in den vergangenen zwei Jahren auch gemacht. [...] Und wenn ein Klabautermann an dieser Gentherapie festhält und weiter Werbung für die Pflichtimpfung macht, dann tut er das nicht, weil er sich um eure Gesundheit sorgt. Er macht das nicht, weil er die Volksgesundheit irgendwie [Unverständlich], er macht das, weil er weiß, dass er damit die Zahl darüber bekommt, wie viele Oppositionelle im Land es gibt und wieviel Regierungstreue es im Land gibt [...]. Die Spritze ist nichts anderes als ein Zeichen für Regierungstreue, aber sie schützt euch nicht vor Erkrankungen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 565

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