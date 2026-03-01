---
type: zitat
speaker: "[[Gereon Bollmann]]"
date: 2023-08-21
topic: Menschenwürde
page_bfv: 196
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gereon Bollmann]] vom 21.8.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschland hat nicht nur ein Messerproblem. Auch Bahnhöfe und Züge sind längst zu Risikozonen geworden. Nach wie vor setzten die Altparteien auf den ungezügelten Bevölkerungsaustausch. [...] Die überwiegend ausländischen Tatverdächtigen sind Ausdruck von oben aufgezwungener, illegaler Migration. Mittlerweile herrscht auf deutschen Bahnhöfen und in den Zügen die nackte Gewalt. Dabei schauen Bundes- wie Landesregierungen nur zu, wie eingewanderte Gewalttäter Deutschlands Bahnhöfe unsicher machen. Doch unter einem Mantel des Schweigens wird der für den unbefangenen Beobachter offensichtliche Zusammenhang zwischen Masseneinwanderung und ausufernder Gewaltkriminalität sowohl von den Altparteien als auch den Mainstreammedien verdeckt. Es darf nicht sein, was nicht sein darf. Und so wird lieber das Narrativ des 'psychisch verwirrten Einzeltäters' ein fürs andere Mal hervorgeholt, als das Kind beim Namen zu nennen. Wir müssen diesem Bevölkerungsaustausch ein Ende setzen: Grenzen schließen gegen illegale Einwanderung und sofortige Abschiebung krimineller Ausländer.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 196

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