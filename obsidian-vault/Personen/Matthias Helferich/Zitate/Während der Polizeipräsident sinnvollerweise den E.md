---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2022-11-05
topic: Menschenwürde
page_bfv: 431
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 5.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Während der Polizeipräsident sinnvollerweise den Einsatz mobiler Videoüberwachungsanlagen bekannt gab, verkündete Westphal in seiner Stellungnahme den Einsatz von mobilen Wanderbäumen und den Anbau von Sportgeräten. [...] Leider vergisst Westphal dabei, dass sich dadurch nur die Aufenthaltsqualität und Attraktivität für nachtschwärmerische Straftäter erhöhen wird, die sich dann abends an den vom Steuerzahler bezahlten Sportgeräten körperlich ertüchtigen können. Ein Ort an dem man sich gerne aufhält, wird die Gegend um die Kampstraße jedoch nur durch weitgehende Kompetenzen der Polizei, was auch die Errichtung einer Waffenverbotszone beinhaltet sowie die konsequente Abschiebung der teils migrantischen Delinquenten. 'Wir brauchen die konsequente Remigration Krimineller statt innerstädtischer Wohlfühloase für Kriminelle', forderte der AfD-Bundestagsabgeordnete und Ratsherr Matthias Helferich. \<Bild OB Westphal meint DAS ernst: Mit Bäumen und Sportgeräten will er die Kampstraße sicher machen\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 431. Illustration zeigt eine nicht-weiße Person mit blutiger Machete vor Sportgerät

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