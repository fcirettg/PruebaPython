import plotly.express as px


def funcion(x, m, b):
    resultado = (m * x) + b
    return resultado


def main():
    m = 2
    b = 1
    X = [ -1, 0,1,2,3,4,5] 

    Y = [] #lista vacía 

    for x in X: 

        y = funcion(x,m,b) 

        Y.append(y) 


    print(Y) 

    fig = px.line(x=X, y=Y, title='For')
    fig.show()

    m = -4
    b = 10
    x_datos = [0, 5, 10, 15, 20]
    y_datos = [funcion(x,m,b) for x in x_datos]
    fig2 = px.line(x=x_datos, y=y_datos, title='List comprehension')
    fig2.show()


if __name__ == '__main__':
    main()