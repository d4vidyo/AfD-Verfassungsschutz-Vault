---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2023-01-03
topic: Menschenwürde
page_bfv: 277
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 3.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Migrantenkrawalle an Silvester: Wer verharmlost, macht sich mitschuldig! +++ Was längst klar war, wird nun auch offiziell bestätigt: Die Silvesterkrawalle gingen in der Hauptsache von Migranten aus. [...] Im Gegenteil ist die 'Party- & Eventszene‘, als die die Ansammlung von gewaltbereiten Migranten schon im Jahr 2020 von der Stuttgarter Polizei verharmlosend bezeichnet wurde, seit 2015 in Deutschland zur alltäglichen Bedrohung geworden. Und auch an Silvester kommt es jeweils seit 2015 in steigender Zahl zu Vorfällen, bei denen ganze Straßenzüge in Flammen aufgehen und Einsatzkräfte bedroht, verletzt oder regelrecht gejagt werden. [...] Wo von 'Feierwütigen‘ oder pauschal 'Jugendlichen‘ gesprochen wird, die die Bürger bedrohen, verweigert man sich der abermals ersichtlich werdenden Realität, dass die Migrations- und Integrationspolitik vollends gescheitert ist. Statt Böllerverboten brauchen wir harte Strafen für die Täter, eine Abschiebungsoffensive und zuvörderst einen vollumfänglichen Schutz unserer Grenzen, statt Asylbewerber auch noch selbst ins Land einzufliegen. Nur so stellen wir sicher, dass unkontrollierbare Zustände vermieden werden. Denn schon jetzt lässt sich prognostizieren: Handelt die Politik nicht, werden die Gefahren für die Bürger immer größer. Wer sich dieser Erkenntnis verweigert, macht sich mitschuldig.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 277

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