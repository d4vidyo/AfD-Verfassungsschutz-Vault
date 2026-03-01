---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2024-08-25
topic: Menschenwürde
page_bfv: 474
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 25.8.2024 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Es kann nicht sein, dass wir in Westdeutschland an den Schulen, bei den Kindern schon mehrheitlich muslimische Kinder haben, die deutsche Kinder - im Übrigen das kann man überall nachlesen, es ist ja keine Behauptung - drangsalieren - junge Mädchen, die kein Kopftuch tragen. Diese Gesellschaft, die freiheitliche Gesellschaft erträgt diese repressiven Kulturen nicht und wir vertragen die Stammeskulturen nicht. Das ist überhaupt nicht vereinbar mit der freiheitlich demokratischen Grundordnung. Und darum dürfen wir das nicht weiter zulassen, dass wir durch eine Massenmigration - das ist eine Massenmigration - überrannt werden und diese Leute innerhalb unserer Landesgrenzen haben, die uns jetzt eben auch im Übrigen dschihadistisch zeigen, wer hier eigentlich die Hosen an hat [...], in Geiselhaft nehmen

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 474

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