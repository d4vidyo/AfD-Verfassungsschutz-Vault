---
type: zitat
speaker: "[[Martin Renner]]"
date: 2024-05-04
topic: Menschenwürde
page_bfv: 495
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 4.5.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Heute einmal etwas Erbauliches von Hermann Hesse. Das Gedicht 'Stufen' wurde von ihm genau am 4. Mai 1941 geschrieben. Am Vorabend des Geburtstages von Korl Morx und meiner Wenigkeit. Das Gedicht sagt uns, dass wir nie an einer erreichten Lebensstufe festhalten sollen, sondern bereit sein mögen, das 'Neue', das 'Nächste', das 'Zukünftige' geistvoll anzunehmen und als positive Entwicklung zu verstehen. Auf unsere schlimme und desaströse politische und gesellschaftliche Situation übertragen, heißt das, dass wir auf die uns zukommende Änderung zum Besseren – auch durch die glasklar antithetische Positionierung und die energiesatte und widerständige Tatkraft der 'Alternative für Deutschland' – frohen Mutes und mit inniger Erwartung bauen dürfen. Der ökosozialistische, bolschewoke und nationalstaatsfeindliche Irrweg der letzten Jahrzehnte wird überwunden und auf dem Müllhaufen der Geschichte entsorgt sein. Der 'Great Reset' wird realisiert werden, aber genau in die gegensätzliche Richtung, hin zum Normalen, und nicht in die Richtung, die von den herrschaftssüchtigen und nimmersatten Pseudo-Eliten aus POLITIK und BIG MONEY geplant ist. Wir müssen dringend zurück in die Zukunft. Und jedem Anfang wohnt ein Zauber inne. Wohlan denn, Herz, nimm Abschied und gesunde!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 495

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