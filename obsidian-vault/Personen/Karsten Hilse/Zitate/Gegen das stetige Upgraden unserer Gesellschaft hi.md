---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2021-06-19
topic: Demokratieprinzip
page_bfv: 582
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 19.6.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Gegen das stetige Upgraden unserer Gesellschaft hin zur nächsten Diktatur, zur dann dritten sozialistischen Diktatur auf deutschem Boden, müssen wir hier - und wir tun es - wir müssen Widerstand leisten. Zwei sozialistische Diktaturen auf deutschem Boden sind genug. [...] Und natürlich trägt [...] diese ganze Misere, die wir heute sehen, diese andauernde Freiheitsberaubung, die Einschränkung der Meinungsfreiheit, die Ausgrenzung Andersdenkender - wir werden ja ausgegrenzt - mit teilweise linksfaschistischen Methoden eindeutig Züge eines totalitäres Regimes - ein totalitäres Regime kommt oft, nicht immer, aber oft, zustande, wenn menschenfeindliche Ideologie auf den Gleichmut eines großen Teils der Bevölkerung trifft. Das ist das, was wir heute sehen. Sophie Scholl hat mal gesagt, die große Schicht [...] der Bevölkerung müssen quasi den Mantel der Gleichmut ablegen und sich letztendlich informieren. Das ist das, was unsere Aufgabe heute ist. Wir müssen [...] die Menschen aufklären, dass wir eben auf dem Weg in so ein totalitäres Regime sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 582

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