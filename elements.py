from flask import Flask, jsonify, render_template
from flask import abort
from flask import make_response
from flask import request
import mysql.connector as mysql
from flask_cors import CORS
import rdflib

app = Flask(__name__)
CORS(app)


@app.route('/',methods =["GET", "POST"])
def frontend():
    return render_template('index.html')
    

@app.route('/api/docs',methods =["GET", "POST"])
def swagger_docs():
    return render_template('swagger_documentation.html')

@app.route('/periodictable/standard_states/', methods=['GET'])
def get_standard_states():
    g = rdflib.Graph()
    g.parse("Periodictable.owl")
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?n) as ?state)
        { 
        ?n rdf:type table:StandardState;
        }""")
    result = []
    for r in qres:
        result.append(r.state.split("#")[1])
    res = {"states":result}
    return jsonify(res)

@app.route('/periodictable/standard_state/<string:state>/', methods=['GET'])
def get_element_state(state):
    g = rdflib.Graph()
    g.parse("Periodictable.owl")
    qres = g.query(
    """
    PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT (str(?s) as ?ele) (str(?sym) as ?sym)
    { 
    ?n rdf:type table:Element;
    table:standardState table:"""+state+""";
    table:name ?s;
    table:symbol ?sym.
    }""")
    result = []
    for r in qres:
            result.append({"name":r.ele.split("('")[0],"symbol":r.sym.split("('")[0]})
    res = {"elements":result}
    return jsonify(res)

@app.route('/periodictable/classifications/', methods=['GET'])
def get_classifications():
    g = rdflib.Graph()
    g.parse("Periodictable.owl")
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?n) as ?cls)
        { 
        ?n rdf:type table:Classification;
        }""")
    result = []
    for r in qres:
        result.append(r.cls.split("#")[1])
    res = {"classifications":result}
    return jsonify(res)

@app.route('/periodictable/classification/<string:clss>/', methods=['GET'])
def get_element_classification(clss):
    g = rdflib.Graph()
    g.parse("Periodictable.owl")

    qres = g.query(
    """
    PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT (str(?s) as ?ele) (str(?sym) as ?sym)
    { 
    ?n rdf:type table:Element;
    table:classification table:"""+clss+""";
    table:name ?s;
    table:symbol ?sym.
    }""")
    result = []
    for r in qres:
            result.append({"name":r.ele.split("('")[0],"symbol":r.sym.split("('")[0]})
    res = {"elements":result}
    return jsonify(res)

@app.route('/periodictable/blocks/', methods=['GET'])
def get_blocks():
    g = rdflib.Graph()
    g.parse("Periodictable.owl")
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?n) as ?block)
        { 
        ?n rdf:type table:Block;
        }""")
    result = []
    for r in qres:
        result.append(r.block.split("#")[1])
    res = {"blocks":result}
    return jsonify(res)

@app.route('/periodictable/block/<string:blk>/',methods=['GET'])
def get_element_block(blk):
    g = rdflib.Graph()
    g.parse("Periodictable.owl")

    qres = g.query(
    """
    PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT (str(?s) as ?ele) (str(?sym) as ?sym)
    { 
    ?n rdf:type table:Element;
    table:block table:"""+blk+""";
    table:name ?s;
    table:symbol ?sym.
    }""")
    result = []
    for r in qres:
            result.append({"name":r.ele.split("('")[0],"symbol":r.sym.split("('")[0]})
    res = {"elements":result}
    return jsonify(res)

@app.route('/periodictable/groups/', methods=['GET'])
def get_groups():
    g = rdflib.Graph()
    g.parse("Periodictable.owl")
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?n) as ?group)
        { 
        ?n rdf:type table:Group;
        }""")
    result = []
    for r in qres:
        result.append(r.group.split("#")[1])
    res = {"groups":result}
    return jsonify(res)

@app.route('/periodictable/group/<string:gnum>/', methods=['GET'])
def get_element_group(gnum):
    g = rdflib.Graph()
    g.parse("Periodictable.owl")

    qres = g.query(
    """
    PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT (str(?s) as ?ele) (str(?sym) as ?sym)
    { 
    ?n rdf:type table:Element;
    table:group table:"""+gnum+""";
    table:name ?s;
    table:symbol ?sym.
    }""")
    result = []
    for r in qres:
            result.append({"name":r.ele.split("('")[0],"symbol":r.sym.split("('")[0]})
    res = {"elements":result}
    return jsonify(res)

@app.route('/periodictable/periods/', methods=['GET'])
def get_periods():
    g = rdflib.Graph()
    g.parse("Periodictable.owl")
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?p) as ?period) (str(?n) as ?num)
        { 
        ?p rdf:type table:Period;
        table:number ?n.
        }""")
    result = []
    for r in qres:
        result.append({"period":r.period.split("#")[1], "number":r.num.split("(")[0]})
    res = {"periods":result}
    return jsonify(res)

@app.route('/periodictable/period/<int:pnum>/', methods=['GET'])
def get_element_period(pnum):
    g = rdflib.Graph()
    g.parse("Periodictable.owl")
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?n) as ?ele) (str(?sym) as ?sym)
        { 
        ?p rdf:type table:Period;
        table:number """+str(pnum)+""";
        table:element ?e.
        ?e rdf:type table:Element;
        table:name ?n;
        table:symbol ?sym.
        }""")
    result = []
    for r in qres:
        result.append({"name":r.ele,"symbol":r.sym})
    res = {"elements":result}
    return jsonify(res)

@app.route('/periodictable/element/<string:sym>/', methods=['GET'])
def get_element(sym):
    g = rdflib.Graph()
    g.parse("Periodictable.owl")
    js = ""
    qres = g.query(
            '''
            PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
            PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#> 
            PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
            SELECT (str(?n) as ?name) (str(?ss) as ?state) (str(?p) as ?period)
            (str(?aw) as ?aw) (str(?c) as ?color) (str(?an) as ?an) 
            (str(?b) as ?block) (str(?cls) as ?cls) (str(?g) as ?group)
            { 
            ?e rdf:type table:Element;
            table:symbol "'''+sym+'''"^^xsd:string;
            table:name ?n;
            table:atomicNumber ?an;
            table:block ?b;
            table:group ?g;
            table:period ?p;
            table:standardState ?ss;
            OPTIONAL { ?e table:classification ?cls }
            OPTIONAL { ?e table:atomicWeight ?aw }
            OPTIONAL { ?e table:color ?c }
            }''')
    classification = ''
    for r in qres:
        if r.cls != None:
                classification = r.cls.split("#")[1]
        else:
                classification = r.cls
        js = {"Name":r.name.split('(')[0],
        "Atomic Number":r.an.split('(')[0],
        "Atomic Weight":r.aw,
        "Block":r.block.split("#")[1],
        "Classification":classification,
        "Color":r.color,
        "Group":r.group.split("#")[1],
        "Period":r.period.split("#")[1],
        "Standard State":r.state.split("#")[1],
        "Symbol": sym}
    return jsonify(js)

if __name__== '__main__':
	app.run(host='localhost',debug=True)