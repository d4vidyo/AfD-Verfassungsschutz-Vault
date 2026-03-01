---
type: zitat
speaker: "[[Marlon Deter]]"
date: 2024-04-07
topic: Demokratieprinzip
page_bfv: 638
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Marlon Deter]] vom 7.4.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Wir werden das Imperium der Kartellparteien zum Einsturz bringen. Hier im Osten wird die Arroganz der Macht ins Rutschen kommen, hier in Brandenburg werden wir den roten Sumpf trockenlegen. All die Altparteien haben Verrat am deutschen Volk begangen. Grüne Ideologie, rote Idiotie, schwarze Verlogenheit und Gelbe, die mal vor langer, langer Zeit freiheitlich waren. Sie alle tragen die Verantwortung für die systematische Zerstörung unserer Wirtschaft, die systematische Zerstörung unseres Wohlstandes, die systematische Zerstörung unserer Kultur, unserer Identität und unserer Landschaft. Und die systematische Zerstörung der Zukunft folgender Generationen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 638

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