---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2023-03-10
topic: Demokratieprinzip
page_bfv: 589
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 10.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Zum Anderen bedeutet es gleichzeitig auch, so wie es hier die Frau Baerbock in ihren Leitlinien festlegt eine Säuberung. Der Auswärtige Dienst wird gesäubert. Sie sagt ganz klar, neu eingestellt werden nur Menschen mit - also, Gender-Kompetenz und Kompetenz für Diversity und auch innerhalb des Dienstes werden Schulungen diesbezüglich angeboten. Ganz perfide, es wird eine Botschafterin für feministische Außenpolitik installiert und eine Anlaufstelle für eben diese besagte Art der Politik. Nicht nur in allen Abteilungen des Auswärtigen Dienstes sondern eben auch in den Auslandsabteilungen. Das ist nichts anderes als ein Kommissar-System, wie wir es in der Sowjetunion erlebt haben, in der, in der Roten Armee damals. Völlig klar, wer da also ausschert, 'ne andere Meinung hat, der kriegt gleich einen Punkt in der Akte und dessen Beförderung ist dann passé. Das ist nichts anderes als eine Säuberung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 589

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