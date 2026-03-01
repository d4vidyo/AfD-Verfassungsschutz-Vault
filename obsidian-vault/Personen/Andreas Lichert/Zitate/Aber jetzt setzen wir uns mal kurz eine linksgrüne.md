---
type: zitat
speaker: "[[Andreas Lichert]]"
date: 2025-02-01
topic: Demokratieprinzip
page_bfv: 969
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Andreas Lichert]] vom 1.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Aber jetzt setzen wir uns mal kurz eine linksgrüne Brille auf und sagen doch, doch, das stimmt alles, der Mensch ist schuld und überhaupt. Selbst dann müsste man den linksgrünen Ökosozialisten in Deutschland in den Arm fallen, denn die machen so unfassbar viel dummes Zeug, das nicht nur sauteuer ist, sondern vor allen Dingen dem Klima überhaupt nichts bringt. Überhaupt gar nichts.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 969

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