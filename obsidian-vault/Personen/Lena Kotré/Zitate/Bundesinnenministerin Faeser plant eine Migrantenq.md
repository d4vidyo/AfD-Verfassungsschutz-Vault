---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-10-01
topic: Menschenwürde
page_bfv: 202
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 1.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Bundesinnenministerin Faeser plant eine Migrantenquote im öffentlichen Dienst oder im Richterdienst. Ja, wie deutschenfeindlich kann man eigentlich sein, Frau Faeser? Das schlägt doch dem Fass den Boden aus. Man möchte also tatsächlich Migranten vor Deutschen bevorzugen? Das alles unter dem Deckmantel der sogenannten Vielfalt. Aber liebe Freunde, ich sage euch eins, die Vielfalt, die damit gemeint ist, ist nichts anderes als der Versuch, die Deutschen in der öffentlichen Wahrnehmung immer weiter unsichtbar zu machen. Nichts anderes ist das. Ich habe es satt, ständig Benachteiligung von Deutschen hinnehmen zu müssen. [...] Und ich sage euch eins, das ist eine Prognose, in 10 bis 20 Jahren, wenn Migranten diese Posten besetzt haben, wisst ihr, was sie dann sagen? Dann werden sie uns sagen, na ja, ihr habt so viele Migranten in diesen öffentlichen Dienstverhältnissen, ihr könnt ja gar nicht mehr ohne Migration. Das ist genau das Ziel von solchen Leuten wie Innenministerin Faeser. Und dieses Ziel müssen wir durchkreuzen. Liebe Freunde, nehmt diesen Bevölkerungsaustausch durch die Hintertür genauso wenig hin wie ich. Zeigen wir es der Ampel, was wir von ihr halten. Diese Ampel muss weg, diese Regierung muss weg!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 202

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