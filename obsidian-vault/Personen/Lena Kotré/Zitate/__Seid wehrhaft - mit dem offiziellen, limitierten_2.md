---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-09-13
topic: Rechtsstaatsprinzip
page_bfv: 655
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 13.9.2024 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>**Seid wehrhaft - mit dem offiziellen, limitierten Kubotan von Lena Kotré!** Während die Regierung den Opfern von Gewalt lächerliche Handlungsempfehlungen gibt, wie etwa anzufangen zu tanzen, zu singen oder sich krank zu stellen, setzen wir auf echte Sicherheit. In meinem Video präsentiere ich euch den **originalen 'Lena Kotré Kubotan'** - der persönliche Begleiter für mehr Selbstschutz. Denn echte Sicherheit gibt es nur mit der AfD! Gemeinsam sorgen wir für ein sicheres Brandenburg! **Jetzt ansehen und wehrhaft werden!**

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[__Seid wehrhaft - mit dem offiziellen, limitierten]]

**SPIEGEL-Notiz:** Gutachten Seite: 655

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Rechtsstaatsprinzip.

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