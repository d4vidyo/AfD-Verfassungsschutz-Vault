---
type: zitat
speaker: "[[Franz Bergmüller]]"
date: 2022-11-09
topic: Demokratieprinzip
page_bfv: 633
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Franz Bergmüller]] vom 9.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Bei der Anhörung der Chefs der Nachrichtendienste am 17.10.2022 hat Herr Haldenwang, Präsident des Verfassungsschutzes, erklärt: "... Eine Gefahr besteht auch - ich habe es vorhin schon angesprochen - dass Oppositionellen-Beobachtung sehr viel stärker stattfinden wird. Und dass möglicherweise auch energisches Vorgehen gegen Oppositionelle bis hin zur Tötung vorstellbar erscheint." ... energisches Vorgehen gegen Oppositionelle bis hin zur Tötung ... Für wen arbeitet dieser von Merkel berufene Mann? Wie lange geht das so weiter? Wer deckt ihn?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 633

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