---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Demokratieprinzip
page_bfv: 567
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ich will am Schluss zwei Prinzipien noch mal kurz einordnen. [...] Das erste Prinzip lautet, Deutschland darf kein Beuteland mehr sein. Deutschland ist unter der Herrschaft der Kartellparteien zum Beuteland geworden. [...] Fast eine Milliarde bezahlen wir an Kindergeld für Kinder von Ausländern, die im Ausland leben. 30 Milliarden Euro für eine Energiewende, die unser Land deindustrialisiert und die Explosion der Preise, der Energiepreise bewirkt. 50 Milliarden bezahlen wir für die illegale Einwanderung. Freunde, summiert das bitte mal auf. 100, 150 Milliarden Euro jedes Jahr für Politik, die nicht im deutschen Interesse ist. Nein, die deutsche Interessen konterkariert und aushebelt und entgegenläuft. [...] Die zweite Prämisse ist, wir müssen uns aus der Fremdbestimmung befreien. Deutschland ist kein selbstbestimmtes Land.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 567

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