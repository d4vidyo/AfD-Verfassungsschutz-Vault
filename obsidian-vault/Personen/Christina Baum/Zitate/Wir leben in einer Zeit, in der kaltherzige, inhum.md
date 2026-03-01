---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-07-16
topic: Demokratieprinzip
page_bfv: 549
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 16.7.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir leben in einer Zeit, in der kaltherzige, inhumane, antideutsche Politiker unser Volk regieren, die aus Dummheit oder mit Absicht den von den Nachkriegsgenerationen durch großen Fleiß, einen hohen Arbeitsethos und viele Entbehrungen geschaffenen Lebensstandard seit Jahrzehnten sukzessive vernichten, durch diesen Raubbau den sozialen Frieden gefährden und die den frei geborenen Menschen nun vollständig zum Arbeitssklaven des Staates machen wollen. [...] Ich träume mit vielen von euch den Traum eines souveränen, freien, selbstbestimmten deutschen Volkes, das seine Geschicke wieder selber in die Hand nimmt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 549

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