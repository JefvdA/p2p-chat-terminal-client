#!/usr/bin/env python3
import typer

app = typer.Typer()


@app.command()
def hello():
    print("Hello world!")


@app.command()
def goodbye():
    print("Goodbye world!")


if __name__ == '__main__':
    app()
