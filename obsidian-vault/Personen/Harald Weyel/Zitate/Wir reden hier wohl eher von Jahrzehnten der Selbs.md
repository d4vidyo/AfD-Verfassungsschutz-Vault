---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2023-01-01
topic: Sonstiges
page_bfv: 794
source: 'ZUERST!'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom Januar 2023 veröffentlicht auf: 'ZUERST!'
> [!quote] Aussage
>Wir reden hier wohl eher von Jahrzehnten der Selbstaufgabe beziehungsweise des (un)freiwilligen Souveränitätsverzichtes. [...] Es würde zunächst reichen, wenn Deutschland eine 'Führungsrolle' in Deutschland übernähme. Vielleicht denkt Klingbeil aber an die 'dienende Führungsrolle' seines Mitkoalitionärs Habeck, also eine führende Rolle bei der devoten Umsetzung der Pläne supranationaler Instanzen oder fremder Mächte oder doktrinärer Parteiideologie. Eine solche Rolle füllt Deutschland jetzt schon aus.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Januar 2023

**SPIEGEL-Notiz:** Gutachten Seite: 794

**Verfassungsschutz Kategorisierung:** Sonstiges.

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