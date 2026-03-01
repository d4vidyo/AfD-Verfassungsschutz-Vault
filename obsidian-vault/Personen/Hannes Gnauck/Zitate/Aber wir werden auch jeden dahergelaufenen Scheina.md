---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2024-09-15
topic: Menschenwürde
page_bfv: 421
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 15.9.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Aber wir werden auch jeden dahergelaufenen Scheinasylanten wieder konsequent wieder in sein Heimatland zurückführen, wenn er hier Straftaten begeht. [...] Deswegen haben diese Leute [Anm.: Migranten der zweiten und dritten Generation] nämlich auch keine Lust auf Sozialschmarotzer und wählen eben auch die AfD. [...] Und mittlerweile wird ja auch wieder über irgendwelche Obergrenzen diskutiert. Diese patriotische CDU, CSU, diese Vaterlandsverräter, die diskutieren über eine Obergrenze von 200.000 neuen Leuten im Jahr. Söder sagt 100.000 Neue. Ja, Chinesen oder Japaner, das wäre ja noch in Ordnung. Ich sage euch mal, wo meine Obergrenze ist. Meine Obergrenze, die ist nicht bei 200.000, meine Obergrenze ist nicht bei null im Jahr, meine Obergrenze ist bei minus einer halben Million im Jahr!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 421. vom Familienfest in Neuruppin

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