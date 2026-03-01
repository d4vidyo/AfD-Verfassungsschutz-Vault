---
type: zitat
speaker: "[[Lars Hünich]]"
date: 2023-12-04
topic: Demokratieprinzip
page_bfv: 612
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lars Hünich]] vom 4.12.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Solange eine gründliche Aufarbeitung der diktatorischen Corona-Maßnahmen von #SPD, #CDU, #Grüne und auch #FDP verhindert wird, sollten wir uns immer wieder in Erinnerung rufen, mit welcher antidemokratischen Energie unsere Regierungen die Bürger drangsaliert haben! Mit Hilfe der Mehrheit unserer 'Qualitätsjournalisten', aber auch Personen des öffentlichen Lebens, wurden Kritiker eingeschüchtert, gesellschaftlich ausgegrenzt und bei der Diskussion um ärztliche Versorgung beinahe für vogelfrei erklärt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 612

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