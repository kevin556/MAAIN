
    def granola_de_prince(self):
    	myfile = open("graph_granola.txt", "w+")
    	for key,value in mot_page.iteritems():
    		for i in value:
    			try:
    				myfile.write(key+" "+self.mot_page[key][i])
    			except KeyError:
    				continue