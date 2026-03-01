---
type: zitat
speaker: "[[Oliver Kirchner]]"
date: 2021-12-05
topic: Menschenwürde
page_bfv: 311
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Oliver Kirchner]] vom 5.12.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ich will, dass es so wird wie früher, vor 2015. Ohne Vergewaltigungen, die wir uns importiert haben, ohne Drogen, die wir uns importiert haben, ohne Messerkriminalität, die wir uns importiert haben, und ohne Terroranschläge, die hier in diesem Land kein Mensch braucht. [...] Mit der Zuwanderungspolitik haben sie uns unsere Sicherheit genommen, unsere Arbeit und unsere Zukunft, weil es nämlich Verteilungskämpfe geben wird bei den Arbeitnehmern. Sie nehmen uns die Freude. Sie nehmen uns die Würde und sie nehmen uns die Freiheit und die Sicherheit in unserem eigenen Land. Nehmen wir ihnen unser Vertrauen! Lasst uns für dieses Land alles tun, um es zu einem Besseren zu verändern. Ich bin bereit dafür, wenn auch ihr dafür bereit seid für unsere Heimat, für unser Volk, für unsere Zukunft in unserem Land!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 311

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