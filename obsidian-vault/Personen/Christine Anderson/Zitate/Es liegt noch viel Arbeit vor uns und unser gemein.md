---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2023-01-02
topic: Menschenwürde
page_bfv: 498
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 2.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Es liegt noch viel Arbeit vor uns und unser gemeinsamer Kampf gegen die technokratische Agenda der globalen Eliten ist in vollem Gange. [...] Überall auf der Welt sehen Bürger und verstehen ganze Völker, wie ihnen ihre Freiheit ihre Grundrechte und ihre Selbstbestimmung durch willfährige und marionettenhafte Regierungen genommen werden. Einstige Freiheiten und Rechte, die nun nach dem Willen einer globalistischen und falschen Elite an supranationale Gremien wie die WHO, die UN oder das WEF übertragen werden sollen. [...] Digitale Kontrolle, elektronische Gesundheits-Zertifikate, Klima-Hysterie, Zerstörung von Wohlstand durch künstliche Energieverknappung, Deindustrialisierung und Existenzvernichtung von landwirtschaftlichen Betrieben, Zerstörung der traditionellen Familie als Kraftquelle und Keimzelle einer jeden Nation, aggressive LGTBQ-Propaganda zur vorsätzlichen Zerstörung von Kinderseelen und einer natürlichen Geschlechtsidentität sowie die Abschaffung des Bargelds, die Kontrolle der Medien, die übertriebene Reglementierung des Internets sowie das staatliche Bespitzeln selbst privatester Kommunikation durch Vorratsdatenspeicherung und Chatkontrollen, sollen aus einst freien Bürgern eine entmündigte, widerstandslose und vollständig steuerbare Verfügungsmasse im Würgegriff der globalistischen Eliten machen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 498

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