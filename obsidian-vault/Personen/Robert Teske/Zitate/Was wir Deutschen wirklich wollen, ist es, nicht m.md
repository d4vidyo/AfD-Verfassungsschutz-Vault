---
type: zitat
speaker: "[[Robert Teske]]"
date: 2024-08-24
topic: Menschenwürde
page_bfv: 352
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Robert Teske]] vom 24.8.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Was wir Deutschen wirklich wollen, ist es, nicht mehr abgestochen zu werden. Wir wollen nicht zum Freiwild in unserem Land werden. Über die Bluttat von Solingen ist jetzt schon viel geschrieben worden. So viele Worte will ich darüber gar nicht mehr verlieren. Eins zeigt sie noch mal deutlich: Multikulturelle Gesellschaften werden zwangsläufig zu multikriminellen Gesellschaften. Liebe Thüringer, ihr habt am 01.09. die Wahl. Höcke oder Solingen. AfD oder Massenzuwanderung. AfD oder Zerfall der inneren Sicherheit. Wählt weise!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 352

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