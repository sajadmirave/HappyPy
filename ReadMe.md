# Usage

usage example

```
from index import HappyPy

# app obj
app = HappyPy()

# create file
app.htmlFile = 'index.html'
app.cssFile = 'style.css'

# add bootstrap
app.bootstrap()

# component
def myComponent():
    pass

# match all components
match = app.match()

# render
app.init()
```

create components

```
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
```

### rendering

```
# match all components
match = app.match([myComponent()])

# render
app.init(match)
```