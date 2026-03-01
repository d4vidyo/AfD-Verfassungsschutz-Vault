---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2022-03-25
topic: Menschenwürde
page_bfv: 414
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom 25.3.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gute Idee aus #Frankreich: Der französische Präsidentschaftskandidat Eric #Zemmour hat die Bildung eines Ministeriums für Remigration vorgeschlagen, welches jährlich rund 100.000 'unerwünschter Ausländer' abschieben soll. #Zemmour sagte, dass er die französische Identität durch den ungebremsten Bevölkerungsaustausch bedroht sieht und diesen deshalb sofort stoppen will. Ich übe scharfe Kritik an Zemmour. Frankreich sollte nicht 100.000, sondern 150.000 illegale Migranten pro Jahr abschieben! [...] Auch hierzulande leben Hunderttausende Migranten, die nicht zu unserer Kultur passen und den Sozialstaat massiv belasten. Die deutsche Identität ist durch die Masseneinwanderung massiv bedroht. [...] Wir wünschen unseren Freunden in Frankreich bei den anstehenden Wahlen viel Erfolg und hoffen, dass auch bei uns mehr Menschen beginnen, die alles zerstörende Migrationspolitik zu hinterfragen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 414

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