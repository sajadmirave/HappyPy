class HappyPy:
    def __init__(self):
        # propertrir
        self.title = ""
        self.htmlFile = "index.html"
        self.cssFile = HappyStyle().cssFile
        self.jsFile = HappyJs().jsFile
        self.__alert = ''
        self.__bootstrap = False
        # self.div = ''

    def init(self, code=""):
        bootstrapCode = ""

        if self.__bootstrap == True:
            bootstrapCode += """
             <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
            """

        # template
        temp = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{self.title}</title>
        <link rel="stylesheet" href="{self.cssFile}">

        # bootstrap
        {bootstrapCode}

    </head>
    <body >
        <div id="root">
            {code}
        </div>
        
        <script src="{self.jsFile}">
            
        </script>
    </body>
</html>
            """
        file = open(self.htmlFile, 'w')
        file.write(temp)
        file.close()

    # match components to render with init function

    def match(self, component):
        allComponent = ''
        for i in component:
            allComponent += i + '\n'

        return allComponent

    def bootstrap(self):
        self.__bootstrap = True
        return


class HappyStyle:
    def __init__(self):
        self.cssFile = "style.css"
        self.backgroundColor = "background-color:"

    # add css files
    def css(self, code):
        file = open(self.cssFile, "w")
        file.write(code)
        file.close()


class HappyJs:
    def __init__(self):
        self.jsFile = "main.js"
        # self.alert = None

    def js(self, code):
        file = open(self.jsFile, 'w')
        file.write(code)
        file.close()

    # alert
    def Alert(self, message):
        return f"alert('{message}')"

    def match(self, component):
        allComponent = ''
        for i in component:
            allComponent += str(i)

        return allComponent
    

happyPy = HappyPy()


def Div(className='', idTag='', code=''):
    # if className != '':
    #     return f'<div class="{className}" >{code}</div>'
    # elif idTag != '':
    #     return f'<div id="{idTag}">{code}</div>'
    # else:
    #     return f'<div>{code}</div>'
    allComponent = ''

    for i in code:
        allComponent += i

    if className != '':
        return f'<div class="{className}">{allComponent}</div>'
    elif idTag != '':
        return f'<div id="{idTag}">{allComponent}</div>'

    return f'<div>{allComponent}</div>'


def H(hSize='', className='', code=''):
    if className == '':
        return f"<h{hSize}>{code}</h{hSize}>"

    return f"<h{hSize} class='{className}'>{code}</h{hSize}>"


def BreackLine():
    return "<br/>"


def Img():
    pass


def Button(className='', idTag='', code=''):
    if className != '':
        return f'<button class="{className}">{code}</button>'
    elif idTag != '':
        return f'<button id="{idTag}">{code}</button>'

    return f'<button>{code}</button'


def Form(action='', method=''):
    return f"<form action='{action}' method='{method}'></form>"


def Input(placeHolder='', type='text'):
    return f"<input type='{type}' placeholder='{placeHolder}' />"


class State:
    def __init__(self,value) -> None:
        self.value = value

    def update(self,newValue):
        self.value = newValue
    
    def echo(self):
        return self.value

    