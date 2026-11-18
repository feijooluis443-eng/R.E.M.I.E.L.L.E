import unicodedata
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# DAN: Defensor Ambiental Natural | R.E.M.I.E.L.L.E: Red Ecológica de Monitoreo Inteligente y Estrategias Limpias para Lograr Equilibrio.
kb = [
    {
        'd': ['aire', 'atmosfera', 'humo', 'smog', 'co2'],
        'a': 'El aire se contamina por quema de combustibles fósiles en autos y fábricas.',
        'n': 'Usa bici, camina más y planta árboles para limpiar el aire.'
    },
    {
        'd': ['agua', 'rio', 'mar', 'oceano'],
        'a': 'El agua se contamina con desagües sin tratar, químicos y plásticos.',
        'n': 'Cierra el grifo, no tires aceite al desagüe y reduce el plástico.'
    },
    {
        'd': ['suelo', 'tierra', 'basura', 'plastico'],
        'a': 'El suelo se arruina por basura no biodegradable y químicos agrícolas.',
        'n': 'Aplica las 3R y recicla todo lo que puedas.'
    },
    {
        'd': ['nombre', 'significa', 'remielle', 'dan', 'eres'],
        'r': 'Soy DAN (Defensor Ambiental Natural) / Remielle: Red Ecológica de Monitoreo Inteligente y Estrategias Limpias para Lograr Equilibrio.'
    },
    {
        'd': ['hola', 'buenos', 'buenas', 'saludos'],
        'r': '¡Qué tal! Pregúntame sobre causas o soluciones ambientales.'
    }
]

def clean(txt):
    return ''.join(c for c in unicodedata.normalize('NFD', txt.lower()) if unicodedata.category(c) != 'Mn')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    msg = clean(request.get_json().get('mensaje', ''))
    ec = any(p in msg for p in ['porque', 'por que', 'causa', 'motivo', 'explica'])
    es = any(p in msg for p in ['como', 'evitar', 'solucion', 'ayudar', 'reducir'])
    
    rep = 'No capté esa. Pregúntame sobre aire, agua o suelo.'
    for t in kb:
        if any(w in msg for w in t['d']):
            if 'r' in t: rep = t['r']
            elif ec: rep = t['a']
            elif es: rep = t['n']
            else: rep = f"Causas: {t['a']} | Solución: {t['n']}"
            break
            
    return jsonify({'respuesta': rep})

if __name__ == '__main__':
    app.run(debug=True)