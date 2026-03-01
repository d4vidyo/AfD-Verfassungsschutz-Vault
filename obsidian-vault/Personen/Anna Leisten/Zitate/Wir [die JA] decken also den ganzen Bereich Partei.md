---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2022-06-19
topic: Sonstiges
page_bfv: 788
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 19.6.2022 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Wir [die JA] decken also den ganzen Bereich Parteipolitik ab [...] und das Vorfeld wird eben von anderen jungen Menschen abgedeckt, zum Beispiel, du hast es angesprochen, die Identitäre Bewegung. Ich persönlich habe überhaupt gar kein Problem mit diesen Vorfeldorganisationen. Ich unterstütze sie, wo ich nur kann. Wir arbeiten Hand in Hand zusammen. Wir brauchen alle Kräfte für dieses Land, wenn wir dieses Land noch retten wollen. Und ich arbeite seit Jahren hart, dass wir eben auch die Vorfeldorganisationen aktiv in die Arbeit einbinden und umgekehrt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 788

**Verfassungsschutz Kategorisierung:** Sonstiges.

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