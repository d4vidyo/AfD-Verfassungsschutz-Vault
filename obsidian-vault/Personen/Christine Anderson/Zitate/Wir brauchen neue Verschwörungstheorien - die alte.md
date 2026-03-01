---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2024-08-01
topic: Demokratieprinzip
page_bfv: 590
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 1.8.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wir brauchen neue Verschwörungstheorien - die alten sind alle wahr geworden!' Diesen Satz wiederhole ich nun bereits seit der Hochphase der Covid-19 P(L)andemie unablässig, als es jedem klar- und selbstdenkenden Menschen dämmern musste, daß so einiges am gleichgeschalteten Panik-Narrativ der Regierung(en) nicht stimmen konnte. [...] Denn jeder mit Durchblick weiß: Die heutige sog. Zivilgesellschaft ist nichts anderes als das mit Steuergeld angefütterte politische Vorfeld der Regierungs- und Altparteien. Durchsetzt mit staatlich finanzierten Vereinen, Bündnissen, Medienschaffenden und NGOs ist dies nichts anderes als das, was einst in der DDR die Massenorganisationen der SED waren: Kettenhunde und Speichellecker des Establishments. Wer hier ernsthafte Aufklärung erwartet, dem ist nicht mehr zu helfen. [...] Auch weil die Mitläufer, die vielen kleinen Vollstrecker, Hetzer, Denunzianten und Feiglinge von damals noch immer unter uns sind. Auch in der staatlichen Administration. Wenn ihre übergriffigen Dienstherren heute ungeschoren bleiben, dann wird sich dieser spezielle Menschenschlag im Schutze seiner Behörden-Schreibtische beim nächsten Mal noch heftiger austoben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 590

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