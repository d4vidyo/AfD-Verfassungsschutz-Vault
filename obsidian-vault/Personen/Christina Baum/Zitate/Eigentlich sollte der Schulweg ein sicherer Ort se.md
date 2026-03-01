---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-12-20
topic: Menschenwürde
page_bfv: 301
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 20.12.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Eigentlich sollte der Schulweg ein sicherer Ort sein. Für die junge \<xxx\> war es der Weg in ihren Tod. Obwohl bekannt war, dass die Migranten des dortigen Asylheims die Schüler belästigen, wurde nichts unternommen. Das junge Mädchen musste die desaströse #Migrationspolitik von #Politikern, die Männer aus archaischen, frauenverachtenden Kulturen nicht nur 'willkommen heißen' sondern auch noch mit einer Rundum-Vollversorgung ins paradiesische #Deutschland einladen, mit ihrem Leben bezahlen. Diese #Ersatzmigration muß ein Ende finden, damit wir in Deutschland wieder in Sicherheit leben können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 301. Der im Original erwähnte Name wurde durch den SPIEGEL mit \<xxx\> ersetzt.

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