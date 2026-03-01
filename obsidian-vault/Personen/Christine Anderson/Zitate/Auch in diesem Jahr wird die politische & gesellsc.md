---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2025-01-02
topic: Menschenwürde
page_bfv: 946
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 2.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Auch in diesem Jahr wird die politische & gesellschaftliche Achterbahnfahrt des Wahnsinns weitergehen. Die globalen Eliten werden nicht aufhören, unsere Freiheit, unsere Selbstbestimmung und unsere Nationen von innen heraus an zugreifen. Und wir werden niemals aufhören, uns mit aller Macht dagegen zu wehren. Die Dinge kommen in Bewegung. Der Wandel wird spürbar. Und das macht diese falschen Eliten noch gefährlicher, weil sie merken, daß die Zeit ab jetzt gegen sie läuft. Seien wir also weiter wehrhaft, trotzig und immun gegen das Gedankengift, welches sie uns über ihre Medien verabreichen wollen. Seien wir weiter Selbstdenker. Bleiben wir weiter kritisch und misstrauisch, jedoch ohne dabei in Paranoia zu verfallen. Trotz allem einen klaren Geist zu behalten ist essentiell. Denn Spaltung & Paranoia zu verbreiten gehört auch zu ihrem Plan. Bleiben wir daher alle zusammen weiter stark, wach und geistig unabhängig. Mehr als je zu vor bin ich mir heute sicher: WIR WERDEN GEWINNEN!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 946

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