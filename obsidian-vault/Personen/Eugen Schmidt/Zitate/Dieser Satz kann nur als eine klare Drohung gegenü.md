---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2025-01-20
topic: Menschenwürde
page_bfv: 892
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom 20.1.2025 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Dieser Satz kann nur als eine klare Drohung gegenüber all jenen verstanden werden, die - um es mit Merkels Worten zu sagen - schon ,etwas länger hier leben'. Was wir derzeit erleben, zeige wie diese ,Fakten" in die Tat umgesetzt werden: Schulklassen, in denen kaum noch Deutsch gesprochen wird, und Stadtviertel, die längst zu Parallelgesellschaften geworden sind. Über 35% der Jugendlichen in Deutschland haben bereits einen Migrationshintergrund - und die Zahlen steigen weiter. Der Bevölkerungsaustausch, vor dem die AfD seit Jahren warnt, ist keine Theorie mehr, sondern Realität, Und er wird gezielt gefördert - durch Vertreter der Asylindustrie und Aktivisten wie Chebli, die ihre Absichten nicht einmal mehr verbergen. Wir müssen uns entschieden gegen diese Entwicklung wehren! Es darf nicht passieren, dass kulturfremde Migranten mit Unterstützung antideutscher Akteure unser Land übernehmen. [...] Die AfD ist die einzige Partei, die sich dieser Herausforderung entschlossen stellt. Am 23. Februar haben Sie die Wahl: Setzen Sie Ihr Kreuz für Deutschland - für unsere Zukunft, unsere Kultur und unsere Kinder!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 892

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