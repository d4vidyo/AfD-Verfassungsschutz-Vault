---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2024-04-04
topic: Menschenwürde
page_bfv: 236
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 4.4.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Der deutsche Untertan, ausgedünnt ausgeplündert, entrechtet und verhöhnt, malocht doch gerne bald bis 80, um seine ewigliche historische Schuld in ewiger Sippenhaft zu sühnen und unsere über zig sichere Länder ins Sozialstaatsparadies illegal eingereisten Säulenheiligen des Deutschland zersetzenden Kartells zu alimentieren. [...] Diese Kultur- und Staatszersetzer an der Macht setzen aber in ihrer Umsiedlungspolitik noch einen drauf, die sie als Lakaien umzusetzen haben, nämlich die Aufnahme von ganz Kalkutta, möglicherweise damit der Souverän bald Arabisch spricht, Moslem ist und sich einen neuen Staat im Siedlungsgebiet für die Dritte Welt aufbauen kann und die Souveränität und Identität des deutschen Volkes historisch ad acta legt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 236

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