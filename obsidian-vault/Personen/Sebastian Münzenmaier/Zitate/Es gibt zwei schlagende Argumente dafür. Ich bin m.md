---
type: zitat
speaker: "[[Sebastian Münzenmaier]]"
date: 2025-01-12
topic: Sonstiges
page_bfv: 862
source: 'Phoenix'
status: Unbewertet
---

# Zitat: [[Sebastian Münzenmaier]] vom 12.1.2025 veröffentlicht auf: 'Phoenix'
> [!quote] Aussage
>Es gibt zwei schlagende Argumente dafür. Ich bin mit der Jungen Alternative sehr zufrieden, ich persönlich bin ja noch Mitglied der Jungen Alternative, darf das noch sein. Aber Punkt 1 ist, wir haben alle erlebt, wie Nancy Faeser momentan etwas durchdreht. Wenn Sie sich an das Compact-Verbot erinnern, ein Presseorgan, das einfach mal per Federstrich verboten wird unter Rückgriff aufs Vereinsrecht. Und das ist ja was, was sie rein theoretisch auch einfach mal machen könnte mit der JA, das wäre auch nicht rechtmäßig, da würden wir vielleicht danach vor Gericht gewinnen, aber erstmal hätten wir ein Riesenproblem. Das können wir vermeiden dadurch, dass die JA ein Teil der Partei wird. Und der zweite Punkt ist, wir haben viele junge Mitglieder auch in der AfD, die bisher aber noch nicht in der JA organisiert sind. Und wenn wir uns für so ein Modell entscheiden, wie es uns heute vorliegt, was wir später debattieren werden, dann haben wir automatisch die Mitgliedszahlen der [...] Jugendorganisation verdoppelt bis verdreifacht. Und das sorgt natürlich auch für mehr Schlagkraft bei den Jugendlichen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 862

**Verfassungsschutz Kategorisierung:** Sonstiges.

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