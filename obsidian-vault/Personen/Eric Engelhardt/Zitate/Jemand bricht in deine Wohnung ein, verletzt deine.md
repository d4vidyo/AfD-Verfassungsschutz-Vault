---
type: zitat
speaker: "[[Eric Engelhardt]]"
date: 2025-03-01
topic: Demokratieprinzip
page_bfv: 962
source: 'X Video'
status: Unbewertet
---

# Zitat: [[Eric Engelhardt]] vom 1.3.2025 veröffentlicht auf: 'X Video'
> [!quote] Aussage
>Jemand bricht in deine Wohnung ein, verletzt deine Mutter und du sagst zum Einbrecher: "Du siehst aber traumatisiert aus. Hier, nimm noch etwas Geld." Das ist die Realität in Deutschland. Millionen brechen in dein Land ein, verletzen Deutsche und du bezahlst sie noch. Die politische Elite führt einen Kampf gegen das eigene Volk. Sie wollen, dass unser Land ruiniert, unsere Sicherheit zerstört und unsere Identität vernichtet wird. Das lassen wir nicht zu. Deutschland ist unsere Heimat, eine Heimat, die es nicht nochmal gibt. Deswegen wehren wir uns dagegen, damit auch deine Mutter wieder sicher leben kann.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 962

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