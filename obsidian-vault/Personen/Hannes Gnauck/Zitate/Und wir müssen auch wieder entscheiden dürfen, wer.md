---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2024-08-11
topic: Menschenwürde
page_bfv: 122
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 11.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und wir müssen auch wieder entscheiden dürfen, wer überhaupt zu diesem Volk gehört und wer nicht. Es gehört mehr dazu, Deutscher zu sein, als einfach nur ‘ne Staatsbürgerurkunde in der Hand zu haben. Dieses Volk hier, das ist gewachsen durch jahrhundertelange Tradition, durch gemeinsame Brauchtümer, durch gemeinsame Geschichte und auch gemeinsame Schicksalsschläge. Und wir sind verpflichtet, diese Geschichte, diese Brauchtümer und diesen Geist des Deutschen zu bewahren. Uns alle hier auf diesem Marktplatz [...] verbindet viel mehr als nur eine gemeinsame Sprache. Uns verbindet ein unsichtbares Band, was man einfach nicht erklären muss. [...] Jeden Einzelnen von euch verbindet mehr mit mir als irgendeinen Syrer oder irgendein Afghane und das muss ich nicht erklären, das ist einfach ein Naturgesetz und darauf können wir alle verdammt stolz sein.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 122

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