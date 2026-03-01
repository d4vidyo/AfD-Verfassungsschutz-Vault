---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-11-21
topic: Sonstiges
page_bfv: 731
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 21.11.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Da ihr alle beisammen seid, möchte ich nochmal darauf hinweisen. Auf den wichtigsten Termin in diesem Jahr. Und zwar nächster Samstag, 26.11., Ami go home-Demo ist Leipzig vor dem amerikanischen Konsulat. Ich habe versucht im Rahmen meiner Partei noch Busse zu organisieren [...] Aber wir müssen dann eben Fahrgemeinschaften organisieren, wir müssen schauen wie wir hinkommen [...]. Wichtig ist, wir müssen mit Mann und Maus am 26.11. nach Leipzig und wir müssen mit 10.000 Mann [...] Ami go home rufen

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 731. abweichendes Datum in der Fußnote des Berichts

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