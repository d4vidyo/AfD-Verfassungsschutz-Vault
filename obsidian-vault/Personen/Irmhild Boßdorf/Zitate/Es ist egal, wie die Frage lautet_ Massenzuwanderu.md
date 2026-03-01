---
type: zitat
speaker: "[[Irmhild Boßdorf]]"
date: 2023-07-30
topic: Menschenwürde
page_bfv: 247
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Irmhild Boßdorf]] vom 30.7.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Es ist egal, wie die Frage lautet: Massenzuwanderung ist immer das Problem und niemals eine Lösung. [...] Aber was wir wirklich fürchten müssen, das ist nicht der menschengemachte Klimawandel. Nein, wir sollten uns viel eher fürchten vor dem menschengemachten Bevölkerungswandel, der das [...] alte Europa in eine Siedlungsregion für Millionen Afrikaner und Araber umwandeln soll.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 247

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