---
type: zitat
speaker: "[[Benjamin Nolte]]"
date: 2023-07-22
topic: Menschenwürde
page_bfv: 243
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Benjamin Nolte]] vom 22.7.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Was hier stattfindet, hat nichts zu tun mit notwendigen Sparmaßnahmen. Das, was hier stattfindet, ist einfach Vernichtungskrieg von Kulturmarxisten gegen die traditionelle Familie. Wenn ich sowas höre, bin ich ja froh, dass der sogenannte Große Austausch nur eine Verschwörungstheorie ist, weil sonst könnte einen das wirklich beunruhigen. Denn während der eigenen Bevölkerung wo es nur geht Steine in den Weg gelegt werden wenn es darum geht eine Familie zu gründen oder Kinder groß zu ziehen, geht die illegale Masseneinwanderung unvermindert weiter.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 243

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