---
type: zitat
speaker: "[[Irmhild Boßdorf]]"
date: 2024-12-31
topic: Menschenwürde
page_bfv: 904
source: 'Gastkommentar'
status: Unbewertet
---

# Zitat: [[Irmhild Boßdorf]] vom 31.12.2024 veröffentlicht auf: 'Gastkommentar'
> [!quote] Aussage
>Ob in den Niederlanden, in Frankreich, in Deutschland oder in Österreich: Die Gewalt auf den Straßen erreicht ein neues Höchstmaß. Es geht dabei nicht, nur' um Überfälle, nicht,nur' um Schläge ins Gesicht. Es geht auch um Vergewaltigungen, oft sogar in der Gruppe. Es geht um erbarmungslose Bandenkriege von Wien bis Brüssel. Es geht um materielle Verteilungskämpfe. Ein Phänomen nichteuropäischer männlicher Migranten Ob man das rasant an Fahrt aufnehmende Phänomen, das immer jüngere Täter gebiert, nun als Gewalt von Cliquen, Banden, Rackets oder Gangs beschreibt: Es ist in der Regel ein Phänomen nichteuropäischer männlicher Migranten. Einheimische Opfer, fremde Täter - das ist die eine Konstante, die uns zeigt, dass zunehmende Migration zunehmende Unsicherheit schafft.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 904

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