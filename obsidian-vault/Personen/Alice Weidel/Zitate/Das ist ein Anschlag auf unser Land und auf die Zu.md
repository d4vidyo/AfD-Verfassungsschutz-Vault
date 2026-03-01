---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2024-06-27
topic: Menschenwürde
page_bfv: 454
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 27.6.2024 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Das ist ein Anschlag auf unser Land und auf die Zusammensetzung unseres Staatsvolkes, was nicht einfach abgeändert werden darf. Dass wir hier jetzt Nicht- Brechtigte einbürgern wollen, das ist etwas, das ist skandalös. Im letzten Jahr wurden rund 200.000 Leute eingebürgert - so viele wie noch nie. Hauptsächlich Syrer, Türken und - glaube ich - Iraker. Da wissen wir, wohin die Reise hier geht. Hier geht es nicht mehr um eine qualifizierte Einwanderung in unser Land, sondern um eine Einwanderung von Unqualifizierten. [...] Dieses ganze Geheule jetzt, weil man sich ja wundert, dass die Ausländerkriminalität in diesem Land durch die Decke geht. Überall werden Jugendliche jetzt auch verprügelt, tot getreten, Messerattacken passieren hier täglich, Frauen werden gruppenvergewaltigt. Das ist ja ein Phänomen, was man nur aus muslimischen Kulturen gegenüber Ungläubigen kennt. Das ist ja eine Entehrung - gehört auch mit zum Dschihad, das muss man einfach ganz klar so sagen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 454

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