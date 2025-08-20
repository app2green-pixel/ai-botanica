from flask import Flask, request, jsonify

app = Flask(__name__)

# Knowledge base con tutte le informazioni integrate
knowledge_base = {
    "pianta": {
        "albero": {
            "descrizione": "Pianta legnosa con un tronco principale e rami.",
            "habitat": "Foreste, parchi, giardini",
            "esempi": "Quercia, Pino, Faggio",
            "uso": "Legname, ombra, decorazione"
        },
        "fiore": {
            "descrizione": "Pianta che produce fiori come organi riproduttivi.",
            "habitat": "Giardini, prati, serre",
            "esempi": "Rosa, Tulipano, Margherita",
            "uso": "Decorazione, profumi, simbolismo"
        },
        "erba": {
            "descrizione": "Pianta non legnosa, spesso di piccole dimensioni.",
            "habitat": "Prati, campi, giardini",
            "esempi": "Grano, Mais, Orzo",
            "uso": "Alimentazione, foraggio"
        },
        "pianta carnivora": {
            "descrizione": "Pianta che cattura e digerisce piccoli animali.",
            "habitat": "Zone umide e paludose",
            "esempi": "Dionaea muscipula, Nepenthes",
            "cibo": "Insetti, piccoli artropodi",
            "uso": "Collezionismo, studio botanico"
        },
        "felce": {
            "descrizione": "Pianta vascolare senza semi che si riproduce tramite spore.",
            "habitat": "Foreste umide, zone ombrose",
            "esempi": "Felce aquilina, Felce di Boston",
            "uso": "Decorativo, alcune specie medicinali"
        },
        "orchidea": {
            "descrizione": "Pianta da fiore spesso epifita, famosa per i suoi fiori ornamentali.",
            "habitat": "Foreste tropicali, serre",
            "esempi": "Phalaenopsis, Cattleya",
            "uso": "Decorativo, collezionismo"
        },
        "alga": {
            "descrizione": "Organismo fotosintetico acquatico, unicellulare o pluricellulare.",
            "habitat": "Acque dolci e marine",
            "esempi": "Alghe rosse, Alghe verdi, Kelp",
            "uso": "Alimentazione, fertilizzanti, cosmetici"
        },
        "fungo": {
            "descrizione": "Organismo eterotrofo che non effettua fotosintesi, spesso simile a piante.",
            "habitat": "Boschi, terreni umidi, materia in decomposizione",
            "esempi": "Funghi commestibili: Porcini, Champignon; Tossici: Amanita",
            "uso": "Alimentazione, medicina, biotecnologia"
        },
        "piante aromatiche": {
            "descrizione": "Piante usate per aromi e spezie.",
            "esempi": "Basilico, Rosmarino, Timo, Menta",
            "uso": "Cucina, tisane, oli essenziali"
        },
        "piante grasse": {
            "descrizione": "Piante che immagazzinano acqua nei tessuti.",
            "habitat": "Zone aride, deserti",
            "esempi": "Aloe, Echeveria, Sedum",
            "uso": "Decorazione, alcune medicinali"
        }
    }
}

# Funzione per interrogare la knowledge base
def ask_bot(topic, subtopic=None, detail=None):
    try:
        if subtopic:
            data = knowledge_base[topic][subtopic]
            if detail:
                return data.get(detail, f"Nessuna informazione su '{detail}'")
            return data
        return knowledge_base.get(topic, "Argomento non trovato")
    except KeyError:
        return "Argomento o sottoargomento non trovato"

# Endpoint per App Inventor
@app.route('/ask', methods=['GET'])
def ask():
    topic = request.args.get('topic')
    subtopic = request.args.get('subtopic')
    detail = request.args.get('detail')
    response = ask_bot(topic, subtopic, detail)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
