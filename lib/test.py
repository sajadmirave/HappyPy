from index import HappyPy, Div, Button, H

# app obj
app = HappyPy()

# create file
app.htmlFile = 'index.html'
app.cssFile = 'style.css'

# add bootstrap
app.bootstrap()

# component


def myComponent():
    return Div(
        className="main",
        idTag="main-div",
        code=[
            H(
                # bootstrap class
                className='text-center text-warning',
                hSize='6',
                code='Hello World!'
            )
        ]
    )


# match all components
match = app.match([myComponent()])

# render
app.init(match)
