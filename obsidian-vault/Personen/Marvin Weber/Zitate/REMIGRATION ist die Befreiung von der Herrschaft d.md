---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2024-01-11
topic: Menschenwürde
page_bfv: 422
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 11.1.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>REMIGRATION ist die Befreiung von der Herrschaft des Unrechts und zugleich die Befreiung Deutschlands von Millionen Illegalen, die gemäß unseres Asylrechts niemals hier sein dürften. Gewalttäter, Klaubanden, Clans, Sozialstaatsplünderer, Intensivtäter und sonstige Raketenwissenschaftler der Dritten Welt müssen schnellstmöglich zurück in ihre Heimat gebracht werden. Wir Deutschen haben es satt mit Millionen Leuten aus Nahost und Afrika übervölkert zu werden, die zum Teil keinerlei Dankbarkeit zeigen, sich nicht integrieren und uns auf allen Ebenen nach unten ziehen wie ihr Land, aus dem sie gekommen sind! Statt freiheitliches Denken herrscht der Islam, statt Sicherheit regiert Unsicherheit, statt Wohlstand regiert die Zerstörung des Sozialstaats, der deutschen Kultur und des Zusammenhalts hin zu einer zersplitterten, 'bunten' Gesellschaft ohne Identität!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 422

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