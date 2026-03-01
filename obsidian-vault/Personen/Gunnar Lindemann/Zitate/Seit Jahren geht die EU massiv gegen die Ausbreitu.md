---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2024-09-26
topic: Menschenwürde
page_bfv: 153
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 26.9.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Seit Jahren geht die EU massiv gegen die Ausbreitung von Waschbären vor, da sie diese als 'invasive Art' identifiziert hat. Das bedeutet, dass die Ausbereitung der Waschbären eine Bedrohung für das heimische Ökosystem darstellen soll. Wenn wir diese Erkenntnisse auf die europäischen Gesellschaften übertragen, müssen wir leider feststellen, dass die EU hier weitaus weniger Sorgfalt walten lässt. Ob das nun Absicht oder einfach nur Dummheit ist, überlassen wir Ihrer Phantasie. Es bleibt jedoch die Erkenntnis, dass die unkontrollierte Ausbereitung kulturfremder Spezies immer eine Gefahr für die jeweils heimischen Ökosysteme darstellt. Und das gilt eben nicht nur im Tier- und Pflanzenreich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 153

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