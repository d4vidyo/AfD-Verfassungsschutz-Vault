---
type: zitat
speaker: "[[Ulrich Oehme]]"
date: 2021-05-14
topic: Menschenwürde
page_bfv: 345
source: 'None'
status: Unbewertet
---

# Zitat: [[Ulrich Oehme]] vom 14.5.2021 veröffentlicht auf: 'None'
> [!quote] Aussage
>Afro-Gruppenvergewaltigung einer 17jährigen - Deutsche Presse schützt Nationalität der Täter. Einzig die ,BZ‘ Berliner Zeitung (Springer) nennt am 12.05.2021 die Täternamen der brutalen Gruppenvergewaltigung eines 17jährigen Mädchens. Es waren ‚fünf Männer aus der afrikanischen Community. Alle geboren in Deutschland, alle aus gutem Hause.‘ Wie andere deutsche Medien gibt selbst die amtliche Deutsche Presseagentur die Nationalität der Täter nicht preis. Weil das so bequem ist, gibt die Justiz des Landes Berlin keine eigene Mitteilung dazu heraus, sondern bringt unkommentiert die anonymisierte Meldung der dpa. Doch ,BZ‘ macht aus den Namen der Verbrecher keinen Hehl: ,Million A. (20) ist Deutsch-Nigerianer. Oluwatobi Az. (20) Deutsch-Sierraleone. Jermaine G. (20) Deutsch-Togoer. Tita N. (21) Deutsch-Kameruner. Jermaine Az. (20) hat keine zweite Staatsangehörigkeit‘.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 345

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