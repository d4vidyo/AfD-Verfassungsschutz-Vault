---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-02-15
topic: Nationalsozialismus
page_bfv: 690
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 15.2.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Ich jedenfalls bin KONSERVATIV Weil es RECHT und RICHTIG ist. ...weil ich WERTE in mir trage, die mir von meinen Großeltern und Eltern mit auf den Lebensweg gegeben wurden und die ich verinnerlicht habe. Dies fehlt dem linken und woken Teil unserer Gesellschaft, die einer Ersatzideologie hinterherlaufen weil sie mit sich selbst nicht im Reinen sind. Weil ihnen der Schuldkult Identität und Nationalstolz genommen hat und sie tatsächlich glauben, im Internationalismus mit der Vermischung der Völker könnte ihre Seele Ruhe finden. Das Gegenteil wird der Fall sein. Diese Entwicklung schadet allen Völkern dieser Erde.

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Ich jedenfalls bin KONSERVATIV Weil es RECHT und R]]

**SPIEGEL-Notiz:** Gutachten Seite: 690

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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