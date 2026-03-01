---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2025-01-23
topic: Menschenwürde
page_bfv: 912
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 23.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Deutschland steht am Abgrund der inneren Sicherheit. Oeynhausen, Solingen, Mannheim, Magdeburg und jetzt Aschaffenburg. Wir haben unsere innere Sicherheit verloren. Schuld daran ist die Grenzöffnung. Schuld daran sind all diejenigen, die uns einreden wollen, unsere Gesellschaft müsse sich multi-kulturell öffnen und kulturfremde Menschen in unser Land lassen. Das ist Schuld daran. Und wir sehen, wie wird das jetzt kaschiert. Natürlich würde ich nicht gern in der Haut der linksgrün-Woken stecken, die mitverantwortlich für die Morde sind, die geleugnet haben, dass mit der fremden Kultur eben auch die Kriminalität und die Morde mit ins Land kommen. Wir hatten es schon vor Jahren im Deutschen Bundestag formuliert, Einwanderung ist immer auch Messereinwanderung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 912

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