---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-09-26
topic: Menschenwürde
page_bfv: 459
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 26.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Massenweise junge Männer, die von klein auf durch eine frauenverachtende und archaische Ideologie geprägt wurden, sind mit Beginn der unkontrollierten, illegalen Masseneinwanderung nach Deutschland ,importiert' worden. Und unsere jungen Frauen waren ihnen ohne Vorwarnung, ohne Hinweise auf die andere Sozialisation und durch die Verinnerlichung einer blauäugigen Ideologie der Gleichheit aller Menschen schutzlos ausgeliefert. Welche fatalen Konsequenzen diese mittelalterliche Religion hat, dafür steht nun auch Mahsa Amini mit ihrem Namen als weiteres, trauriges Opfer. Die junge Frau musste sterben, weil sie ihr Kopftuch nicht richtig trug. Für uns europäische Frauen (noch) unvorstellbar, zugleich ist es aber auch eine Warnung, wohin sich Europa und insbesondere Deutschland bei weiterer Aufnahme muslimischer Migranten entwickeln könnte

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 459

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