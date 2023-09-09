from index import HappyPy, Div, Button, H,State

# app obj
app = HappyPy()

# create file
app.htmlFile = 'index.html'
app.cssFile = 'style.css'

# add bootstrap
app.bootstrap()

# component


def myComponent():
    nameState = State('sajad')
    return Div(
        className="main",
        idTag="main-div",
        code=[
            H(
                # bootstrap class
                className='text-center text-warning',
                hSize='6',
                code=nameState.echo()
            )
        ]
    )


# match all components
match = app.match([myComponent()])

# render
app.init(match)
