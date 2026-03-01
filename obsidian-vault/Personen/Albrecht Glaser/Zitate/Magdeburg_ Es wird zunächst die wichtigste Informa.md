---
type: zitat
speaker: "[[Albrecht Glaser]]"
date: 2024-12-21
topic: Menschenwürde
page_bfv: 940
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Albrecht Glaser]] vom 21.12.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Magdeburg: Es wird zunächst die wichtigste Information unterschlagen. Er ist Saudi und das kann man sofort feststellen. Und er ist Arzt. Er ist also kein aufgehetzter Fußsoldat, der Befehle von seinem Iman ausführt, sondern Überzeugungstäter, der das große Ganze im Blick hat. Was ist das große Ganze? Der Kampf des Islam gegen Christen und Juden, wie es in vielen Suren des heiligen Koran steht. Ein ,göttlicher' Befehl an alle Muslime, dem sie weltweit nachzukommen haben. Dabei gehen sie taktisch schlau vor. Wenn sie in Staaten eine kleine Minderheit sind, verhalten sie sich möglichst unauffällig. Sie nennen das ,Taquia‘, d. h. Verstellung. Es ist ein bewußtes Täuschungsmanöver, das Teil des religiösen Verhaltenscodex ist. Ab einer gewissen numerischen Größe in einer nicht muslimischen Umgebung setzen sie die Nadelstich-Strategie ein. Sie provozieren und fordern lästig: Forderung nach Gebetsräumen überall, in Schulen, Universitäten und am Arbeitsplatz. Dann fordern sie Halal-Speisen in Kantinen, Schulen und Kindergärten. Dann kämpfen sie für Rechtsänderungen, um das Schächten zu legalisieren, das aus Tierschutzgründen in unserem Rechtsraum verboten ist. Dann bekämpfen sie die Manifestationen christlicher Kultur, wie das von Kreuzen als Schmuck, in öffentlichen Einrichtungen, eben auch Weihnachtsmärkte. Sie greifen sie solange physisch an, bis nach einem Zwischenstadium der Befestigungen, was sie bereits zur Farce werden läßt, dieser lange gepflegte Brauch als Provokation der islamischen Mitbürger stilisiert wird und sie danach endlich abgeschafft werden. Der saudische Arzt überblickt das Alles und leistet seinen Beitrag zur Eskalation des Glaubenskrieges, der in über 30 Suren des Korans mit den Beschreibungen von Tötungsmodalitäten illustriert wird. Die Meldung, es sei kein unterstützendes Umfeld bisher festgestellt worden, ist töricht und der Versuch, verharmlosende Parolen in die Welt zu setzen. Ein muslimischer Christenmörder hat immer ein unterstützendes Umfeld. Das ist die ,Umma‘, die Gemeinschaft der Muslime weltweit, die solche Mordtaten immer mit Wohlgefallen begleitet. Die abgeschmackten Formeln des Bedauerns, die den Standarterklärungen der etablierten Politiker sehr ähneln, von den Repräsentanten der Islam-Verbände sind Täuschungshandlungen, welche uns Abendländler einschläfern sollen. Bei dem Täter von Hanau, an dessen strafrechtlicher Schuldfähigkeit nach Aussagen eines erfahrenen Gerichtspsychiaters gezweifelt werden darf (er hat schließlich auch seine Mutter und sich selbst getötet), hatte jedoch keinerlei ,Umfeld‘. Er ist also weder ein Vertreter des militanten Rechtsradikalismus, als welchen die Politik und die Medien ihn mit Fleiß umdekorieren wollen, noch im strafrechtlichen Sinn ein Mörder. Das Ähnliche dürfte wohl auch für den Täter von Halle gelten. Von einem Umfeld ist auch dort nichts bekannt geworden. Wenn auch nur der Hauch eines solchen Verdachts sich hätte erweisen lassen, wäre davon unablässig in Politik und Medien die Rede gewesen. Da er sich ebenfalls selbst getötet hat, verbieten sich Spekulationen über seine Schuldfähigkeit und seine Motive. Dennoch war und ist er stets zitierter Beweis für den Antisemitismus in Deutschland. Wir erleben also wieder das Trauerspiel der Unterdrückung der tödlichen muslimischen Gefahr und damit der Täuschung der Angehörigen über den wahren Hintergrund des Leides, das ihnen zugefügt worden ist. Es kommt die nahe Wahl hinzu. Die Lebenslügen von nützlicher Migration und der im Prinzip friedlichen monotheistischen Religion des Islam, die zwar ein paar , Islamisten' hervorbringt. Aber die haben mit dem wahren Islam (zu deutsch: Unterwerfung) nichts zu tun.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 940

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