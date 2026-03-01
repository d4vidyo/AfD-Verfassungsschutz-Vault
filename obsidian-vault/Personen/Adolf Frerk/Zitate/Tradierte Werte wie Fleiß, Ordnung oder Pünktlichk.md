---
type: zitat
speaker: "[[Adolf Frerk]]"
date: 2024-06-01
topic: Nationalsozialismus
page_bfv: 678
source: 'www.afd-kleve.de'
status: Unbewertet
---

# Zitat: [[Adolf Frerk]] vom Juni 2024 veröffentlicht auf: 'www.afd-kleve.de'
> [!quote] Aussage
>Tradierte Werte wie Fleiß, Ordnung oder Pünktlichkeit gelten inzwischen als überholt. Mit ihnen ließe sich auch ein KZ betreiben, heißt es. [...] Alle Verantwortlichen – deren Kreis ist weit anzusetzen – sollten mit ihrem gesamtem privatem Vermögen einschließlich ihrer Versorgungsansprüche für die skandalösen Verluste der Bürger herangezogen werden. Zu dieser Abrechnung mit den Schuldigen wird es nicht kommen, denn diese Herrschaften haben eine alte Masche neu entdeckt. Wer im Dritten Reich Kritik an den Mächtigen übte, wirkte 'zersetzend' und wurde aus dem Verkehr gezogen. Manchmal erhielt der 'Zersetzer' gnadenhalber einen Jagdschein', d. h. er wurde für unzurechnungsfähig erklärt und blieb unbehelligt. [...] Kritiker der aktuellen Politklasse wirken 'delegitimierend', es wird ihnen also unterstellt, dass sie die Demokratie beseitigen wollen. Für solche Untermenschen gibt es keinen Jagdschein, sondern den Staatsschutz. Ihm kommt die Rolle des willigen Helfers gegen missliebige Argumente und unbequeme Parteien zu. So erklären sich die wüsten Attacken des Parteienkartells auf die AfD, die als einzige die Machenschaften der Abwickler Deutschlands zu entlarven sucht.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Juni 2024

**SPIEGEL-Notiz:** Gutachten Seite: 678. in der Fußzeile-Datum: 16.06.2022

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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