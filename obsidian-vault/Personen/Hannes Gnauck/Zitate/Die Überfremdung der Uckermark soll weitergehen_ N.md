---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2023-06-08
topic: Menschenwürde
page_bfv: 384
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 8.6.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Überfremdung der Uckermark soll weitergehen? Nicht mit uns! Kein Asylheim in Angermünde! Erneut will uns die Landrätin Dörk die Ansiedlung von Fremden aufdrängen. [...] Als AfD-Fraktion werden wir erneut eine namentliche Abstimmung beantragen, damit die Bürger sehen können, wer in ihrem Interesse abstimmt und wer sich dem Masseneinwanderungsdiktat aus Potsdam und Berlin beugt! Wir haben bereits geschlossen gegen das Asylheim in Prenzlau gestimmt Wir werden natürlich auch in Angermünde dagegen stimmen! Für die Uckermark und ganz Brandenburg ist längst klar: Nur die AfD wird sich der Überfremdung entgegenstellen. Wir stehen geschlossen für euch ein! Liebe heimatverbundene Uckermärker, wir stehen an Eurer Seite!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 384

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