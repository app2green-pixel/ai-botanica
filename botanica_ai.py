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
        },
        "Fasi di crescita": {
            "Germinazione": "Il seme assorbe acqua, rompe il tegumento e spunta la radichetta.",
            "Crescita vegetativa": "La pianta sviluppa radici, fusto e foglie.",
            "Fioritura": "Produzione dei fiori per la riproduzione sessuale.",
            "Fruttificazione": "Produzione di frutti contenenti semi."
        },
        "Pianta da frutto": {
            "Definizione": "Pianta che produce frutti commestibili.",
            "Esempi": ["Melo", "Pero", "Ciliegio", "Fragola"],
            "Cura": {
                "Annaffiatura": "Regolare, evitando ristagni d'acqua.",
                "Concimazione": "Fertilizzante equilibrato in primavera.",
                "Potatura": "Rimuovere rami secchi o malati per favorire frutti."
            }
        },
        "Fotosintesi": {
            "Definizione": "Processo tramite cui le piante producono glucosio e ossigeno usando luce solare, acqua e CO2.",
            "Formula chimica": "6 CO2 + 6 H2O + luce → C6H12O6 + 6 O2",
            "Luogo": "Cloroplasti delle cellule vegetali."
        },
        "Radice": {
            "Funzione": "Ancorare la pianta al terreno e assorbire acqua e nutrienti.",
            "Tipi": {
                "Pivotante": "Radice principale più spessa con radici secondarie, es. carota.",
                "Fascicolata": "Molte radici sottili simili tra loro, es. grano."
            }
        },
        "Foglia": {
            "Funzione": "Organo fotosintetico principale della pianta, permette scambio di gas.",
            "Tipi": {
                "Semplice": "Foglia con una sola lamina, es. quercia.",
                "Composta": "Foglia divisa in più foglioline, es. trifoglio."
            },
            "Adattamenti": {
                "Spine": "Foglie trasformate in spine per difesa, es. cactus.",
                "Succhianti": "Foglie modificate per assorbire acqua, es. piante carnivore acquatiche."
            },
        },
        "Fusto": {
            "Funzione": "Sostiene la pianta, trasporta acqua e nutrienti tra radici e foglie.",
            "Tipi": {
                "Erbaceo": "Fusto morbido e verde, breve durata, es. girasole.",
                "Legnoso": "Fusto duro e persistente, es. quercia."
            }
        },
        "Fiore": {
            "Funzione": "Organo riproduttivo della pianta.",
            "Parti": {
                "Sepali": "Proteggono il fiore in boccio.",
                "Petali": "Attraggono gli insetti impollinatori.",
                "Stami": "Organi maschili, producono polline.",
                "Carpello": "Organo femminile, contiene ovuli."
            },
            "Tipi di impollinazione": {
                "Abiotic": "Impollinazione tramite vento o acqua.",
                "Biotic": "Impollinazione tramite animali, es. api, farfalle."
            }
        },
        "Frutto": {
            "Definizione": "Struttura derivata dall’ovario del fiore contenente semi.",
            "Tipi": {
                "Secco": "Non carnoso, es. nocciola.",
                "Carnoso": "Polposo, es. mela, pesca."
            },
            "Funzione": "Protegge il seme e favorisce la dispersione."
        },
        "Seme": {
            "Definizione": "Struttura contenente embrione e riserve nutritive per la germinazione.",
            "Parti": {
                "Embrione": "Futuro germoglio della pianta.",
                "Endosperma": "Riserva nutritiva per l’embrione.",
                "Testa o tegumento": "Rivestimento protettivo esterno."
            },
            "Strategie di dispersione": {
                "Vento": "Semi leggeri con strutture alari, es. acero.",
                "Acqua": "Semi galleggianti, es. cocco.",
                "Animali": "Semi con uncini o frutti commestibili, es. lampone."
            }
        },
        "Terreno": {
            "Tipi": {
                "Argilloso": "Trattiene molta acqua, compatto.",
                "Sabbioso": "Drena velocemente, povero di nutrienti.",
                "Limoso": "Fertile, trattenimento equilibrato d’acqua.",
                "Torba": "Acido e povero di nutrienti, ideale per piante carnivore."
            },
            "Nutrienti principali": ["Azoto", "Fosforo", "Potassio", "Magnesio", "Calcio"]
        },
        "Malattie comuni": {
            "Marciume radicale": "Causato da funghi, le radici diventano molli e nere.",
            "Oidio": "Fungo che forma polvere bianca sulle foglie.",
            "Peronospora": "Fungo che provoca macchie gialle e marroni sulle foglie.",
            "Virus del mosaico": "Causa macchie verdi e gialle irregolari sulle foglie."
        },
        "Tecniche di coltivazione": {
            "Semina diretta": "Piantare i semi direttamente nel terreno.",
            "Trapianto": "Coltivare piantine in vasi e poi spostarle nel terreno.",
            "Propagazione per talea": "Tagliare e radicare parti di pianta madre.",
            "Coltivazione idroponica": "Coltivazione senza terra, nutrienti disciolti in acqua.",
            "Coltivazione aeroponica": "Radici sospese in aria nebulizzate con nutrienti."
        },
        "Piante officinali": {
            "Camomilla": {
                "Uso": "Calmante, digestivo, antinfiammatorio.",
                "Parte utilizzata": "Fiori."
            },
            "Menta": {
                "Uso": "Digestivo, rinfrescante, aromaterapia.",
                "Parte utilizzata": "Foglie."
            },
            "Lavanda": {
                "Uso": "Rilassante, antibatterico, cosmetico.",
                "Parte utilizzata": "Fiori."
            },
            "Aloe Vera": {
                "Uso": "Cicatrizzante, idratante, digestivo.",
                "Parte utilizzata": "Gel interno foglia."
            }
        },
        "Alberi comuni": {
            "Quercia": {
                "Tipo": "Legnoso, deciduo.",
                "Usi": "Legname, ombra, estetico.",
                "Foglie": "Lobate, alterne."
            },
            "Pino": {
                "Tipo": "Legnoso, sempreverde.",
                "Usi": "Legname, resina, estetico.",
                "Foglie": "Ago, gruppi di 2-5."
            },
            "Betulla": {
                "Tipo": "Legnoso, deciduo.",
                "Usi": "Estetico, legno leggero.",
                "Foglie": "Cuoriformi, margine seghettato."
            }
        },
        "Erbe comuni": {
            "Basilico": {
                "Uso": "Cucina, aromatica.",
                "Parte utilizzata": "Foglie."
            },
            "Rosmarino": {
                "Uso": "Cucina, aromatico, medicinale.",
                "Parte utilizzata": "Foglie."
            },
            "Origano": {
                "Uso": "Cucina, aromatico, antibatterico.",
                "Parte utilizzata": "Foglie."
            }
        },
        "Nutrienti specifici": {
            "Azoto (N)": "Favorisce crescita fogliare e colore verde intenso.",
            "Fosforo (P)": "Favorisce radici e fioritura.",
            "Potassio (K)": "Favorisce resistenza a stress e qualità frutti.",
            "Magnesio (Mg)": "Componente della clorofilla, essenziale per fotosintesi.",
            "Calcio (Ca)": "Favorisce struttura cellulare e crescita."
        },
        "Insetti utili": {
            "Ape": "Impollinatore, aumenta produzione di frutti e semi.",
            "Coccinella": "Mangia afidi e parassiti fogliari.",
            "Bombus": "Impollinatore di piante di grandi dimensioni e serre."
        },
        "Parassiti": {
            "Afide": "Insetto succhiatore, provoca accartocciamento foglie e indebolimento.",
            "Tripide": "Piccolo insetto che danneggia foglie e fiori.",
            "Nematodi": "Piccoli vermi che attaccano radici, riducendo crescita.",
            "Mosca bianca": "Insetto succhiatore che indebolisce foglie e diffonde virus."
        },
        "Piante carnivore": {
            "Venere acchiappamosche": {
                "Cibo": "Insetti piccoli, mosche, formiche.",
                "Meccanismo": "Foglie che si chiudono rapidamente al contatto."
            },
            "Nepenthes": {
                "Cibo": "Insetti, piccoli animali caduti nella trappola.",
                "Meccanismo": "Trappola a forma di brocca con liquido digestivo."
            },
            "Drosera": {
                "Cibo": "Insetti piccoli.",
                "Meccanismo": "Foglie coperte di peli ghiandolari appiccicosi."
            }
        },
        "Piante acquatiche": {
            "Loto": {
                "Ambiente": "Acqua dolce stagnante, laghi, stagni.",
                "Parti": "Fiori, foglie, radici commestibili.",
                "Curiosità": "Foglie idrorepellenti."
            },
            "Ninfea": {
                "Ambiente": "Acqua dolce stagnante.",
                "Parti": "Fiori decorativi.",
                "Curiosità": "Galleggia grazie a rizomi."
            },
            "Ceratophyllum": {
                "Ambiente": "Acqua dolce, acquari.",
                "Funzione": "Ossigenazione acqua."
            }
        },
        "Piante ornamentali": {
            "Rosa": {
                "Uso": "Decorativa e profumata.",
                "Colore fiori": "Variabile (rosso, rosa, bianco)."
            },
            "Orchidea": {
                "Uso": "Decorativa.",
                "Ambiente": "Tropicale, umidità alta."
            },
            "Giglio": {
                "Uso": "Decorativa e profumata.",
                "Fioritura": "Primavera-estate."
            }
        },
        "Ciclo vitale delle piante":{
            "Semi": "Germinazione dipende da acqua, temperatura, luce.",
            "Germoglio": "Sviluppo radici e foglie.",
            "Pianta giovane": "Crescita vegetativa e fotosintesi.",
            "Fioritura": "Formazione fiori e riproduzione sessuata.",
            "Frutti e semi": "Produzione di semi per nuova generazione.",
            "Morte": "Termine ciclo vitale, ritorno sostanze al suolo."
        },
        "Condizioni di crescita": {
            "Luce": "Necessaria per fotosintesi; intensità e durata dipendono da specie.",
            "Acqua": "Regolazione idrica essenziale; troppa o poca può uccidere.",
            "Suolo": "pH, nutrienti, drenaggio influenzano salute.",
            "Temperatura": "Specie tropicali, temperate o alpine hanno diverse tolleranze.",
            "Umidità": "Influenza evaporazione, crescita e fioritura."
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

@app.route('/add_info', methods=['POST'])
def add_info():
    data = request.json
    argomento = data.get("argomento", "").lower()
    sottoargomento = data.get("sottoargomento", "").lower()
    info = data.get("info", {})

    if not argomento or not sottoargomento or not info:
        return jsonify({"errore": "Devi specificare argomento, sottoargomento e info"}), 400

    if argomento not in knowledge_base:
        knowledge_base[argomento] = {}

    knowledge_base[argomento][sottoargomento] = info
    return jsonify({"successo": f"Informazioni su '{sottoargomento}' aggiunte correttamente"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)