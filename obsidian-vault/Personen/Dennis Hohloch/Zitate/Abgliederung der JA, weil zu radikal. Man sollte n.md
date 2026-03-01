---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2024-12-03
topic: Sonstiges
page_bfv: 858
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 3.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Abgliederung der JA, weil zu radikal. Man sollte nicht jede Meldung der Presse wortwörtlich übernehmen. Eine Jugendorganisation muss eine scharfe Zunge haben und Akzente setzen. Der vom Regierungsschutz unterstellte Extremismus ist für mich kein Entscheidungskriterium. Fakt ist: Der Bundesvorstand hat beschlossen, einen Satzungsänderungsantrag auf dem kommenden Bundesparteitag einzubringen. Ziel ist eine stärkere, gut aufgestellte und besser finanzierte Jugendorganisation mit größerer Bindung zwischen Partei und Jugend. Gleichzeitig ist es wichtig, die Fürsorgepflicht der Partei gegenüber ihrer Jugend, die sich in diesen Zeiten besonders ins Feuer stellt, ernst zu nehmen. Das neue Modell bietet diesen Schutz. Wer von Meuthianern spricht, versucht mit alten Methoden, unlautere parteipolitische Vergleichen zu ziehen, um Jeden Reformprozess zu unterbinden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 858

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