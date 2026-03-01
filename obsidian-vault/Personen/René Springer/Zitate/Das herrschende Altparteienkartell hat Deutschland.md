---
type: zitat
speaker: "[[René Springer]]"
date: 2023-03-12
topic: Demokratieprinzip
page_bfv: 571
source: 'Heimatkurier'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 12.3.2023 veröffentlicht auf: 'Heimatkurier'
> [!quote] Aussage
>Das herrschende Altparteienkartell hat Deutschland längst als Nation und souveränes Land aufgegeben. Die so verhasste eigene Nationalität wird dem EU-Zentralisierungswahn, dem Primat der Ökonomie, der Fremdenliebe und der Unterwürfigkeit gegenüber fremden Mächten geopfert. Dieser wahnhafte Drang, Deutschland nur noch als Siedlungsgebiet für fremde Völker zu betrachten und dieses überhebliche Sendungsbewusstsein, der ganzen Welt das eigene Übel aufzuzwingen, wird gern mit superhumanistischen Begründungen kaschiert. Aber die Wurzel des Ganzen ist die Verachtung des Eigenen. Auch den Einfluss wirtschaftlicher Akteure auf die etablierte Politik sollte man nicht außer Acht lassen. Es ist pathologisch. Mit einer politischen Leitlinie, die sich einerseits der Selbstverachtung und anderseits einem im wahrsten Sinne des Wortes entgrenzenden Globalismus verpflichtet hat, können die Krisen und die Überfremdung nur zum Normalzustand werden. Und das wird unter diesen politischen Kräften auch so weiter gehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 571

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