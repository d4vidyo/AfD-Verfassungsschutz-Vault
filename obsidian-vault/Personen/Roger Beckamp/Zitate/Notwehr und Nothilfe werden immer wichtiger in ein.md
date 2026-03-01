---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2023-08-08
topic: Menschenwürde
page_bfv: 270
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 8.8.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Notwehr und Nothilfe werden immer wichtiger in einem Land, in dem sich immer weniger gut und gerne leben lässt. Eine Silvester-Nacht 2016 und ständige Übergriffe vorwiegend durch junge orientalische und afrikanische Migranten sollen der Vergangenheit angehören, allein weil diese 'jungen Männer' wissen, dass dies nicht mehr hingenommen wird. Selbstbewusstsein ist mehr denn je notwendig, um sich gegen linke und migrantische Gewalt zu wehren, zum Schutz aller Deutschen und aller anderen Einheimischen, gerade auch der rechtschaffenen Migranten, die besonders unter diesen 'jungen Männern' zu leiden haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 270

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