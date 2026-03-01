---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2023-02-10
topic: Menschenwürde
page_bfv: 324
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 10.2.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Die CDU ist der größte Produzent von Unsicherheit in diesem Land. Kanzlerin Merkel hat unsere Sicherheit 2015 mit der Grenzöffnung dauerhaft beschädigt. Fast 2 Millionen Asylbewerber sind damals in unser Land geströmt. Die Folgen sind immer noch desaströs und auch noch nicht abgeändert worden. Jeder 50. Einwohner, aber jeder 5. Messerangreifer ist Zuwanderer, das bedeutet, um das Zehnfache überrepräsentiert. In Berlin nehmen Messerangriffe jedes Jahr zu. Welche schrecklichen Schicksale hinter solche Taten stecken, das müssen wir mittlerweile in ganz Deutschland sehen. Einige Bespiele: In Würzburg – ein Somalier tötet drei Frauen; Illerkirchberg – ein Eritreer tötet die 14-jährige \<xxx\>, also ein Schulkind auf dem Schulweg. So was hätte man sich vor zehn Jahren in Deutschland niemals vorstellen können. Und wir wollen uns an diese Dinge niemals gewöhnen, das darf nicht Tagespolitik werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 324. Der im Original erwähnte Name wurde durch den SPIEGEL mit \<xxx\> ersetzt.

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