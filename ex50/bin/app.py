import web

urls = (
	'/', 'index',
	'/hello', 'hello'
)

greeting = "Hello World"

app = web.application(urls, globals())

render = web.template.render('/templates')

class hello:
	def GET(self): 
		return greeting

class index:
	def GET(self): 
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()