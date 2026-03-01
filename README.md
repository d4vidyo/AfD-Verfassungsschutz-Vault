# Der AfD-Verfassungsschutz-Vault

## Worum geht es hier?
Das Bundesamt für Verfassungsschutz hat in einem 1108 Seiten starken Gutachten zahlreiche Aussagen von AfD-Funktionären gesammelt, welche die Verfassungsfeindlichkeit der AfD belegen sollen. Das Nachrichtenmagazin **Der Spiegel** hat im Mai 2025 eine geleakte Version dieses Gutachtens zugespielt bekommen und die dort aufgeführten Zitate in mühseliger Handarbeit digitalisiert. Diese Daten wurden dann u. a. in Form einer [interaktiven Webanwendung](https://www.spiegel.de/politik/deutschland/afd-ist-rechtsextrem-hier-sind-die-belege-des-verfassungsschutzes-a-b5fa40e4-a54e-410a-8cc7-ade35d09f77c) veröffentlicht.

Dieses Repository stellt die Daten vom Spiegel in Form eines Obsidian-Vaults bereit. Das bedeutet: Zu jedem Zitat können eigene Kommentare und Bewertungen hinzugefügt werden. Dies ermöglicht eine dynamische Sortierung und dadurch ein strukturiertes Durcharbeiten der Zitatsammlung, um sich ein eigenes, fundiertes Urteil darüber zu bilden, ob die gesammelten Zitate eine Verfassungsfeindlichkeit der AfD belegen.

## Struktur dieses Repositories
Das Repository ist in zwei Teile aufgeteilt:
1. _Der fertige Obsidian-Vault:_ Enthält den kompletten Obsidian-Vault, bereit zur sofortigen Verwendung.
2. _Das Parser-Skript:_ Enthält den Python-Code, welcher die Daten vom Spiegel in das passende Markdown-Format umwandelt.

## Das Parser-Skript
Das Parser-Skript erzeugt aus den Daten vom Spiegel für jedes Zitat und für jede Person eine Datei. Die beiden Templates `Person_template.md` und `Quote_template.md` definieren deren Aufbau.
Zusätzlich wird in `Person_ranking.json` eine "Rangordnung" der Personen angegeben, welche die Relevanz einer Person in der AfD zuordnet und eine Sortierung in Obsidian ermöglicht.

**Requirements:** Keine

Das Python-Skript kann einfach durch `python main.py` ausgeführt werden. Dies beginnt mit einer Aufforderung zur Auswahl der Spiegel-Quelldatei, gefolgt von einer Aufforderung zur Auswahl des Zielordners.
Vor Ausführung des Skriptes sollte im Zielordner der Ordner `Personen` - falls vorhanden - gelöscht werden, um Duplikate zu vermeiden.

# Verwendung

## Schnellstart
1. Installiere [Obsidian](https://obsidian.md/download).
2. Lade dieses Repository herunter (oben auf `< > Code` -> `Download ZIP`) und lege den darin enthaltenen Ordner `obsidian-vault` an einen beliebigen Ort.
3. Starte Obsidian und wähle mit "Ordner als Vault öffnen" den Ordner `obsidian-vault` aus.
4. Klicke bei der Nachricht "Vertraust Du dem Ersteller dieses Vaults?" auf "Dem Ersteller vertrauen und Erweiterungen aktivieren".
5. Starte Obsidian neu.

Nach einem erstmaligen Indexing-Vorgang (dauert ein paar Sekunden bis ~1 Minute) werden jetzt alle 1146 Zitate in der Tabelle "Unbewertete Aussagen" im Dashboard angezeigt. Hier lassen sich auch Tabellen für bewertete Aussagen und Personen aufklappen.

## Empfohlener Ablauf
1. Öffne das Dashboard und klicke dort auf die oberste Datei der Tabelle "Unbewertete Aussagen".
2. Lies das Zitat und ggf. die Notizen dazu.
3. Entscheide, ob diese Aussage 'Legitim', 'Fragwürdig' oder 'Nicht legitim' ist.
4. Schreibe ggf. einen Kommentar, um deine Bewertung zu begründen.
5. Klicke im unteren Bereich "Nächste Aussage" auf die oberste Datei.


# Quellen, Credits & Lizenzen
- **Datenquelle:** Die aufbereiteten Zitate und redaktionellen Notizen stammen aus dem Artikel des Spiegel: [Rechtsextreme AfD – hier sind die Belege des Verfassungsschutzes](https://www.spiegel.de/politik/deutschland/afd-ist-rechtsextrem-hier-sind-die-belege-des-verfassungsschutzes-a-b5fa40e4-a54e-410a-8cc7-ade35d09f77c). Die verwendete JSON-Datei wurde über den Netzwerkanalyse-Tab im Browser beim Laden des Artikels extrahiert. Die Urheberrechte für die redaktionelle Aufbereitung der JSON-Daten liegen beim Spiegel.
- **Inhaltliche Basis:** Die Zitate selbst stammen aus dem Gutachten des Bundesamtes für Verfassungsschutz.
- **Python-Skript:** Der Code zum Parsen der JSON im Ordner `parser-script` ist unter der **MIT-Lizenz** veröffentlicht und darf frei verwendet werden.
- **Personen Rang:** Die Datei `Person_ranking.json`, welche die Relevanz einer Person innerhalb der AfD vorgibt, wurde durch die KI Gemini generiert. 

## Obsidian Erweiterungen
Der fertige Obsidian-Vault enthält die Plugins:
- [Obsidian Dataview](https://github.com/blacksmithgu/obsidian-dataview) von [Michael "Tres" Brenan](https://github.com/blacksmithgu)
- [Obsidian Meta Bind](https://github.com/mProjectsCode/obsidian-meta-bind-plugin) von [Moritz Jung](https://github.com/mProjectsCode)
- [Obsidian Style Settings](https://github.com/mgmeyers/obsidian-style-settings) von [Matthew Meyers](https://github.com/mgmeyers)
sowie ein CSS-Snippet:
- [MCL Multi Column](https://github.com/efemkay/obsidian-modular-css-layout) von [Faiz Khuzaimah](https://github.com/efemkay)