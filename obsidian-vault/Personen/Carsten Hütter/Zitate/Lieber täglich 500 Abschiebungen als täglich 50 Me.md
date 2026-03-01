---
type: zitat
speaker: "[[Carsten Hütter]]"
date: 2022-10-19
topic: Menschenwürde
page_bfv: 267
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Carsten Hütter]] vom 19.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Lieber täglich 500 Abschiebungen als täglich 50 Messerattacken! Und wieder hat ein Migrant in einer deutschen Stadt wahllos Menschen getötet: Am Dienstag erstach ein Somalier zwei Männer in Ludwigshafen und verletzte einen weiteren schwer. [...] Unsere Bürger haben schon so viel für Flüchtlinge hergeben müssen, die sich im Nachhinein als Gewalttäter entpuppten: Geld, Wohnraum, Essen – und immer wieder ihr Leben. Der Traum von den goldenen Fachkräften hat sich längst aufgelöst in einer Spur aus Blut und Tränen. [...] Fangen wir endlich an, solche Leute in großem Stil abzuschieben. Und dabei sollte nicht gelten 'im Zweifel für den Angeklagten', sondern im Zweifel für unser Land und unsere Bürger!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 267

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