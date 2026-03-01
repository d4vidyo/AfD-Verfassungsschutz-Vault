---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2024-07-02
topic: Demokratieprinzip
page_bfv: 633
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 2.7.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Trauriger Alltag in Deutschland! Jeder, der die cduspdfdpgrünelinkebsw wählt, macht sich mitschuldig an zukünftigen Messermorden! Jeder, der am 01.09.2024 diese Einheitspartei wählt, wählt Mord, Totschlag und Vetgewaltigung auf Deutschlands Straßen und Plätzen! Nur die Alternative für Deutschland ist willens, diesen Zustand entschlossen und nachhaltig zu beenden!

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