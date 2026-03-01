---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-11-23
topic: Menschenwürde
page_bfv: 164
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 23.11.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Die Festung Europa ist ein Bild für eine strategische Zielsetzung. Für eine strategische Zielsetzung, die deutlich darauf hinweisen will, dass die Massenzuwanderung nach Europa Europa als das ausschalten wird, was es über Jahrtausende geworden ist. Wenn wir diese millionenfache Zuwanderung aus dem arabischen und afrikanischen Raum nach Europa nicht zum Stillstand bringen, dann wird Europa seine kulturelle Kernschmelze erleben. Dann werden wir einen historischen Kultur- und Zivilisationsbruch in Europa erleben. Und deswegen brauchen wir die Festung Europa. Deswegen brauchen wir zumindest eine temporäre Abschottung [...]. [...] Es kommt nicht nur auf die Quantität der Menschen an, es kommt auch auf die Qualität der Menschen an. [...] Wenn wir überleben wollen als europäische Zivilisation, dann müssen wir uns gegen die Masseneinwanderung abschotten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 164

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