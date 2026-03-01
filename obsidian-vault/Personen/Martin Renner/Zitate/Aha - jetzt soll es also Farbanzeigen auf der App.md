---
type: zitat
speaker: "[[Martin Renner]]"
date: 2022-08-13
topic: Demokratieprinzip
page_bfv: 616
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 13.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Aha - jetzt soll es also Farbanzeigen auf der App geben. [...] Na, so können die "Ordnungskräfte" - früher wurden die auch schon mal als Spitzel, als Blockwart, als Stasi oder noch früher als Gestapo bezeichnet - ihrer Arbeit leichter nachgehen und die so dringend nötigen Selektionen fürs Gemeinwohl vornehmen. [...] Viel einfacher wäre es doch, wenn wir zum Tragen unterschiedlich farbiger Oberarmbänder verpflichtet würden. Hatten wir doch alles schon einmal. Und hat doch auch bestens funktioniert. [...] Was kruschtelt und klaubt die Ampelregierung (Rot, Grün, Gelb) und die sie unterstützende Scheinopposition (Schwarz) sonst noch so an altbewährten faschistischen Instrumenten aus dem Giftschrank der politischen Instrumentarien raus, um den souveränen Bürgern ihre Freiheit und ihre Grundrechte zu nehmen? Nie wieder Faschismus, auch nicht im rot-grünen Kleidchen der Moralibans !!!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 616

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