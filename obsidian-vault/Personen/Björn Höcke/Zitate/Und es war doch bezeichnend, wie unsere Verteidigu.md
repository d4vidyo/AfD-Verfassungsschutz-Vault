---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-05-21
topic: Demokratieprinzip
page_bfv: 544
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 21.5.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und es war doch bezeichnend, wie unsere Verteidigungsministerin, die Frau Lambrecht [...], wie die den Befehl bekommen hat, Waffen zu liefern und ukrainische Soldaten an diesen Waffen auszubilden. Wisst ihr, wo das passiert ist? Wisst ihr, wo die Befehlsübergabe vonstattengegangen ist? Die deutsche Verteidigungsministerin, die wurde aus Berlin nach Ramstein befohlen. Nach Ramstein, auf die größte US-amerikanische Militärbasis außerhalb der USA. Und da haben hochrangige Regierungsvertreter der USA der Frau Lambrecht den Marsch geblasen. Was ist das denn für ein Bild, dass die Ministerin eines Landes im eigenen Land von einer fremden Macht die Order bekommt, wie sie sich außenpolitisch, wie sie sich wehrpolitisch zu verhalten hat. Liebe Freunde, dieses Land ist immer noch nicht vollständig souverän. Dieses Land ist nach wie vor fremdbestimmt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 544

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