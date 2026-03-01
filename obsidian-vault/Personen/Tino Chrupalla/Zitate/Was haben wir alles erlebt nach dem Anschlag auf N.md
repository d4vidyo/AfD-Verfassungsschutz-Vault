---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2024-08-29
topic: Demokratieprinzip
page_bfv: 538
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 29.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Was haben wir alles erlebt nach dem Anschlag auf Nord Stream? Da hieß es, der Russe war's, weil er uns Böses will. Jetzt heißt es, die Ukraine soll es gewesen sein und sie habe jedes Recht dazu. Tschechiens Präsident und Polens Ministerpräsidenten stimmen zu. Das sind also unsere Freunde. Und was macht die Bundesregierung? Sie reagiert darauf überhaupt nicht. Unsere Infrastruktur wird von sogenannten Freunden zerstört und wir, unsere Bundesregierung, steht da und zuckt mit den Achseln. Daran sieht man, dass dieses Land nicht souverän sein kann. Denn so reagiert man nicht, wenn man angegriffen wird, wenn unsere Infrastruktur zerstört wird. Und wir fordern die Aufklärung und wollen diejenigen zur Rechenschaft ziehen, die dafür verantwortlich sind, liebe Freunde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 538

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