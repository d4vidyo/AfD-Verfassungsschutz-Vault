---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-05-01
topic: Demokratieprinzip
page_bfv: 544
source: 'ZUERST Magazin'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom Mai 2022 veröffentlicht auf: 'ZUERST Magazin'
> [!quote] Aussage
>Die Gerichte in unserem Land, zumal die entscheidenden, sind fest in der Hand der machthabenden Kartellparteien. [...] Dabei zählt anscheinend die korrekte Gesinnung mehr als die fachliche Qualifikation. [...] Die bittere Wahrheit ist: Es gab nie einen fairen Parteienwettbewerb in der Bundesrepublik Deutschland. Der erlaubte Rahmen dafür war von Anfang an von den Siegern sehr eng gezogen worden, die alliierten Lizenzparteien brauchten wirkliche Konkurrenz nie zu fürchten. [...] Und dabei ging es nicht nur um die Abwehr der Gefahr einer kommunistischen Unterwanderung zu Zeiten des Kalten Krieges. Eine steuerbare Linke war vielmehr willkommen, denn diese war nach ihrer richtigen Einschätzung wenig 'patriotismusanfällig'. [...] [E]ine antideutsche Kraft [Anm.: BÜNDNIS 90/DIE GRÜNEN] wurde damit strategisch im Parteiensystem der Republik plaziert.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Mai 2022

**SPIEGEL-Notiz:** Gutachten Seite: 544

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