---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-08-27
topic: Menschenwürde
page_bfv: 517
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 27.8.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Rechtzeitig vor der Landtagswahl hat Bayern seinen 'Skandal': Der stellvertretende Ministerpräsident und Freie-Wähler-Chef soll als Jugendlicher ein antisemitisches Flugblatt verfaßt haben. Das Machwerk wurde im Zusammenhang mit der Berichterstattung neu verbreitet, und wer das liest, erkennt sofort, daß es sich dabei um einen geschmacklosen und morbiden Schüler-Scherz handelt, der nur so vor pubertären Allmachtsphantasien trieft. Es ist primitiv und dumm, nicht sonderlich lustig – aber eben auch kein politisches Manifest. Das ist eine klassische Jugendsünde, und es ist davon auszugehen, daß sich Hubert Aiwanger seitdem sittlich weiterentwickelt hat. Über 35 Jahre ist es her: Als er das verfaßt haben soll, hieß die Partei „Die Linke“ noch SED und hat auf Menschen schießen lassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 517

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