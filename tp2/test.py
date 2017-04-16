import xml.etree.cElementTree as ET

mots = ["absence","abraham"]

def test(fileName):
	dico = {}
	for motrecherche in mots:
	    context = ET.iterparse(fileName, events=("start", "end"))
	    context = iter(context)
	    event, root = context.next()
	    for event, elem in context:
	        if event == "end" and elem.tag == "mot":
	            mot = elem.findtext("contenu").encode('utf-8')
	            if mot == motrecherche:
	              	for page in elem.iter('page'):
	              		dico[page.attrib['id']] = elem.findtext("page")
	                	print page.attrib['id'] + " " + elem.findtext("page")
	    print dico
test("graph_granola.txt")               