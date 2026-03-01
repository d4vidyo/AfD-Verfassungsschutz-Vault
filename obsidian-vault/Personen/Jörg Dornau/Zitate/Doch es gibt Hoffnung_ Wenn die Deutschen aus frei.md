---
type: zitat
speaker: "[[Jörg Dornau]]"
date: 2022-12-01
topic: Demokratieprinzip
page_bfv: 555
source: 'Dornaus Wahlkreis-Post'
status: Unbewertet
---

# Zitat: [[Jörg Dornau]] vom 1.12.2022 veröffentlicht auf: 'Dornaus Wahlkreis-Post'
> [!quote] Aussage
>Doch es gibt Hoffnung: Wenn die Deutschen aus freiem Willen bereit sind, über ihre Geschicke wieder selbstbestimmt zu entscheiden, gibt es niemanden, der sie daran hindern kann. Wann und wo die Souveränität der Deutschen verloren ging, dürfte allen, die bereit sind darüber nachzudenken, schon bald klar werden! [...] Manch Älterer mag sich beim Lesen grüner Grusel-Ideen an den puritanischen Agrarsozialismus der 'Roten Khmer' erinnern, der in der Zeit zwischen 1975-79 etwa einem Viertel des kambodschanischen Volkes das Leben kostete. [...] Auch hier sind die Altparteien tief von der tödlichen Ideologie der 'grünen Khmer' durchsetzt, was in der schwarz-grün-roten Regierungskoalition zum Ausdruck kommt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 555

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