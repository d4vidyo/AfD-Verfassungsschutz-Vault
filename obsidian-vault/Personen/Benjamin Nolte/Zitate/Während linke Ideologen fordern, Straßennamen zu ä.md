---
type: zitat
speaker: "[[Benjamin Nolte]]"
date: 2025-02-18
topic: Nationalsozialismus
page_bfv: 977
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Benjamin Nolte]] vom 18.2.2025 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Während linke Ideologen fordern, Straßennamen zu ändern, Denkmäler abzureißen und alles, was nach deutscher Geschichte riecht, auszulöschen, klatschen CDU und CSU artig Beifall. Brauchtum und Tradition, für diese Leute nur etwas, das stört. Stattdessen schwelgt man lieber in multikulturellen Utopien und belehrt uns, warum wir uns für unsere eigene Geschichte schämen sollten. Wir von der AfD sagen, es reicht. Unser Brauchtum und unsere Tradition sind kein Relikt aus der Vergangenheit. Sie sind Teil unserer Identität und unserer Zukunft. Wir stehen für den Schutz von Denkmälern und Traditionen. Abrissbirnen gehören auf Baustellen, aber nicht an unsere Geschichte. Gedenkkultur ohne Schuldkult. Wir gedenken mit Respekt unserer Ahnen Werk und das ohne uns ständig auf Knien zu entschuldigen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 977

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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