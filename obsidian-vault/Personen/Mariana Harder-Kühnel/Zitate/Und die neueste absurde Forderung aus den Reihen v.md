---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2024-02-22
topic: Menschenwürde
page_bfv: 184
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 22.2.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und die neueste absurde Forderung aus den Reihen von SPD und Grünen nach einem Ausländerwahlrecht legt nahe, was eigentlich zukünftig bezweckt ist: Ein neues Wahlvolk. Als ob die langfristig die Grünen oder die SPD wählen würden. Die machen einfach ihre eigene Partei auf und dann Gnade uns Gott, liebe Freunde. Mit der AfD wird es kein neues Wahlvolk geben. Sonst wird Deutschland zu einem Kalifat und wir wollen kein Kalifat. Wir wollen ein Deutschland, das deutsch bleibt, liebe Freunde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 184

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