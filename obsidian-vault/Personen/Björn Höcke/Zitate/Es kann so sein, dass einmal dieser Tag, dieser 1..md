---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Demokratieprinzip
page_bfv: 566
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Es kann so sein, dass einmal dieser Tag, dieser 1. September 2024 von Historikern, die die Geschichte der Bundesrepublik Deutschland einst schreiben werden, als politische Zäsur eingeordnet wird. Es kann sein, dass Historiker in der Zukunft so berichten werden, dass es eine Zeit davor gab und eine Zeit danach. Und die Zeit davor werden sie vielleicht die Zeit der Kartellparteienherrschaft nennen. Ja, Freunde, wir sind unter einer Kartellparteienherrschaft gefangen oder in einer Kartellparteienherrschaft gefangen. Es ist egal, ob ihr schwarz wählt, ob ihr rot wählt, ob ihr grün wählt oder irgendeine andere Farbe wählt. Ihr kriegt mehr EU, ihr kriegt mehr Zahlungen aus Berlin nach Brüssel, ihr kriegt mehr Euro-Rettung, ihr kriegt mehr Multikulti, ihr kriegt mehr Zerfall der inneren Sicherheit, mehr Plünderung der sozialen Sicherungssysteme, ihr kriegt mehr Gendergaga, ihr kriegt mehr Kriegsrhetorik in unerträglicher Art und Weise gegen Russland, das nicht im deutschen Interesse ist, ihr kriegt weniger deutsche Identität, liebe Freunde. Es ist egal, was ihr wählt, ihr kriegt immer weniger Deutschland. Die Kartellparteien lösen unser Deutschland auf wie ein Stück Seife unter einem lauwarmen Wasserstrahl und wir werden morgen diesen Hahn abdrehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 566

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