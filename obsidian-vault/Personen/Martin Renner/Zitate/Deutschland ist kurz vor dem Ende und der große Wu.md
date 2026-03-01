---
type: zitat
speaker: "[[Martin Renner]]"
date: 2025-02-04
topic: Demokratieprinzip
page_bfv: 959
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 4.2.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschland ist kurz vor dem Ende und der große Wumms wird in Bälde Deutschland endgültig in den Abgrund stürzen. Deshalb darf am 23.2.2025 keine Partei dieses Altparteien-Kartells mehr gewählt werden. Wie konnte es passieren, dass in unserem Deutschland alle Parteien der "Neuen Sozialistischen Einheitspartei Deutschlands (N-SED)" - außer der AfD - so irre, so undemokratisch und so totalitär geworden sind. Ich erkläre das seit 12 Jahren ständig und leicht nachvollziehbar in Hunderten von Vorträgen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 959

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