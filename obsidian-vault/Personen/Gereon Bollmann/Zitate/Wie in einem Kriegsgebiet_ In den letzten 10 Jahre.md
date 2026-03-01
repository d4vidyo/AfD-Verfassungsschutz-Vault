---
type: zitat
speaker: "[[Gereon Bollmann]]"
date: 2024-06-11
topic: Menschenwürde
page_bfv: 349
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gereon Bollmann]] vom 11.6.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wie in einem Kriegsgebiet: In den letzten 10 Jahren fast 7000 Gruppenvergewaltigungen in Deutschland Deutschland hat seit längerem ein Problem mit Gruppenvergewaltigungen. [...] Der Anteil nichtdeutscher Tatverdächtiger bei Gruppenvergewaltigungen liegt bei 48 Prozent -also weit über dem Ausländeranteil von 16,43 Prozent. Tatverdächtige aus Syrien, Afghanistan, dem Irak und der Türkei sind überdurchschnittlich oft vertreten. Hier sind noch nicht einmaldiejenigen Täter mit Migrationshintergrund eingerechnet, die in der Statistik als ,deutsche‘ Tatverdächtige gelten. [...] Die ausufernde Masseneinwanderung hat Gruppenvergewaltigungen zur traurigen Realität in Deutschland werden lassen. Dabei zählt als Gruppenvergewaltigung jedes dieser abscheulichen Verbrechen, an dem mindesten drei Männer beteiligt sind - ein Delikt, das in früheren Zeiten bei uns so gut wie unbekannt war, und an dessen seelischen Folgen die Frauen meist ihr Leben lang furchtbar leiden. Unser Land ähnelt immer mehr einem Kriegsgebiet: ob Gruppenvergewaltigungen, Messerkriminalität oder Gewaltverbrechen - die multikulturelle Gesellschaft hat die innere Sicherheit erodieren lassen. Wir als AfD fordern daher die konsequente Abschiebung straffällig gewordener Ausländer und härtere Strafen für Gruppenvergewaltigungen. Auch muss der Masseneinwanderung nach Europa und insbesondere nach Deutschland ein Riegel vorgeschoben und die Grenzen ohne Kompromisse verteidigt werden. Deutsche Frauen dürfen kein Freiwild sein, sondern müssen geschützt werden!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 349

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