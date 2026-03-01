---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-12-30
topic: Menschenwürde
page_bfv: 936
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 30.12.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und wir erleben sie jetzt dieses Silvester, wie seit Jahren Silvester, wo migrantische Gangs den Bürgerkrieg proben und proben dürfen. Und mit Böllern auf die Leute schießen dürfen. Wo der Staat eine unglaubliche Toleranz zeigt. Aber dieser Staat ist nicht tolerant, das ist kein liberaler, schwacher Staat. Das haben wir in den Corona-Zeiten gesehen. Und wir sehen es auch immer da, wo sich Widerstand gegen die Überfremdung regt. Wir sehen es zum Beispiel in dem Kalifat Nordrhein-Westfalen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 936

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