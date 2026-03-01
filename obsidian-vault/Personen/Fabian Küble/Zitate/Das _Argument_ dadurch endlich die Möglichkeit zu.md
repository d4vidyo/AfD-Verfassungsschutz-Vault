---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2024-12-03
topic: Sonstiges
page_bfv: 864
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 3.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Das "Argument" dadurch endlich die Möglichkeit zu bekommen JA Mitglieder sanktionieren zu können, hört man öfter und auch schon länger, wird deshalb jedoch nicht sinnvoller. Fakt ist: Alle Vorstände der JA und damit letztlich alle relevanten Personen, müssen seit jeher laut Satzung auch in der AfD sein. Diese unterliegen daher bereits heute der AfD Schiedsgerichtsbarkeit. Ledeglich normale Mitglieder, die keine Funktionäre sind, müssen nicht in der AfD sein und könnten daher im Zweifel auch nicht durch diese sanktioniert werden. ABER: mir ist kein Fall bekannt, in dem Mitglieder der JA nach grobem Fehlverhalten nicht sanktioniert worden wären, zumal nach expliziter Aufforderung durch die Mutterpartei. Ebenfalls Fakt ist: die Parteigerichtsbarkeit braucht auf Grund der durch das Parteiengesetz gestellten hohen Anforderungen sehr viel länger um Personen zu sanktionieren oder im Zweifel sogar auszuschließen, als es die JA als Verein kann. In den meisten mir bekannten Fällen hat die #JA sogar schneller gehandelt als die #AfD, die teils sogar garnicht gehandelt hat (wegen den hohen rechtlichen Voraussetzungen), während die JA Sanktionen ergriffen hat. Daher ist dieses "Argument" ebenso alt wie unsinnig und hat mit der realen Praxis nur sehr wenig zu tun.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 864

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