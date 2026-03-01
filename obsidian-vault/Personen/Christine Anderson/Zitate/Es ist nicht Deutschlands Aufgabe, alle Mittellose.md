---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2023-04-15
topic: Menschenwürde
page_bfv: 499
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 15.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Es ist nicht Deutschlands Aufgabe, alle Mittellosen dieser Welt bei sich aufzunehmen und mit deutschem Steuergeld dauerhaft zu alimentieren. Früher wusste das auch noch die CDU. Heute jedoch ist von der einstmals staatstragenden Partei nur noch ein Haufen politischer Hütchenspieler übriggeblieben, die ihre Wähler in Deutschland hinters Licht führen, während sie im vermeintlich fernen Brüssel vollmundig in das Lied der Migrations-Globalisten, der Asyl-Industrie und der Deutschland-Abschaffer einstimmen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 499

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