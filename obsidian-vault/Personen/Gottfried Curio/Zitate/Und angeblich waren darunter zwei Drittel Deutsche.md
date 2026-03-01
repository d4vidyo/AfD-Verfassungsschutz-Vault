---
type: zitat
speaker: "[[Gottfried Curio]]"
date: 2025-01-08
topic: Menschenwürde
page_bfv: 883
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Gottfried Curio]] vom 8.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und angeblich waren darunter zwei Drittel Deutsche. Aber wir haben nicht geruht und die Vornamen erfragt. Und unter diesen Vornamen zeigt sich wieder mal, dass diese Deutschen im Wesentlichen Mohammed, Ali, Yusuf, Hassan heißen. Das sind die Deutschen, die hier Randale machen, die Stress machen zu Silvester, die Silvester bewusst missverstehen als eine Lizenz zum Bürgerkrieg, anstatt zu einem fröhlichen Feiern und zum Begrüßen des neuen Jahres. Das brauchen wir hier nicht, meine Damen und Herren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 883

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