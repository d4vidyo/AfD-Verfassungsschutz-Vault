---
type: zitat
speaker: "[[René Springer]]"
date: 2023-03-10
topic: Menschenwürde
page_bfv: 497
source: 'Freilich Magazin'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 10.3.2023 veröffentlicht auf: 'Freilich Magazin'
> [!quote] Aussage
>Dem aufmerksamen Beobachter unserer Zeit muss allerdings auffallen, dass die Kluft zwischen Erzählung und Wirklichkeit immer größer wird. Unsere Demokratie - das ist heute keine Volksherrschaft, kein repräsentierter Volkswille, sondern das genaue Gegenteil: die Herrschaft einer kleinen global vernetzten Elite, die sich gegen die Interessen der Völker und Nationalstaaten richtet und auch bereit ist, diese gegeneinander auszuspielen, um die eigenen Interessen effektiver durchsetzen zu können. In den letzten Jahren sind die Vertreter dieser globalen Elite immer sichtbarer geworden. Immer öfter präsentieren sie uns ungeniert ihre antidemokratischen Pläne: Great Reset, [...], Transformation traditioneller Völker und gewachsener Gemeinschaften, globaler Migrationspakt, [...]. Sie wollen Mensch und Gesellschaft grundlegend verändern [...]. Doch was wäre ein nachhaltiges Davos ohne die Rekrutierung des entsprechenden Nachwuchses, der frühzeitig auf die globale Agenda eingeschworen wird und diese für künftige Regierungsverantwortung verinnerlicht?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 497

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