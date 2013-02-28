import json,urllib2

class accessAPI:

	def __init__ (self, host,text):
		self.host = host
		self.partial = list() #aux list
		self.results =  list() #list containing all the possible branches conducting to a result
		self.text=text

	def callAPI (self,text):
		jsonContent=  urllib2.urlopen(self.host +"/search?rel=HasPrerequisite&startLemmas="+text).read()
		return self.convert(json.loads(jsonContent))#json content in utf-8

	def convert(self,input): #in order to use the same format in the json
	    if isinstance(input, dict):
		return {self.convert(key): self.convert(value) for key, value in input.iteritems()}
	    elif isinstance(input, list):
		return [self.convert(element) for element in input]
	    elif isinstance(input, unicode):
		return input.encode('utf-8')
	    else:
		return input

	def fillBranch(self,branch):
		while True:
			deltaBranch = self.callAPI(branch[len(branch)-1])
			if (deltaBranch['numFound'] == 0):
				branch.reverse()
				return
			branch.append(deltaBranch['edges'][0]['endLemmas'])
			#for element in deltaBranch['edges']: 
			#	branch.append(element['endLemmas'])



	def getActions(self):
		content = self.callAPI(self.text)
		for element in content['edges']: #get all the final elements of each solution
			self.partial.append(element['endLemmas'])
			self.results.append(self.partial)
			self.partial = []
		for branch in self.results:
			self.fillBranch(branch)
		
		#print self.results #testing


