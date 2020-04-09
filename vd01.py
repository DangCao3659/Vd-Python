import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Nguyen Vo Dang Cao"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
