---
type: zitat
speaker: "[[Gereon Bollmann]]"
date: 2023-09-25
topic: Menschenwürde
page_bfv: 197
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gereon Bollmann]] vom 25.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Längst überfordert der Einwanderungs-Tsunami landauf, landab Städte und Gemeinden. Immer häufiger wenden sich die Gemeindevertreter händeringend an Bund und Länder - in aller Regel umsonst. Warum auch? Es läuft ja alles nach Plan, die Regierenden der Altparteien treiben ihre Politik des Bevölkerungsaustauschs ohne mit der Wimper zu zucken brachial voran.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 197

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