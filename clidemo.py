import typer


def print_color(good: bool = True):
    message_start = "everything is "
    if good:
        typer.secho("good", fg="green")
        #or in one line
        #typer.secho(message_start + "good", fg="green")
    else:
        typer.secho("bad", fg="white", bg="red", blink = True)
    message = message_start + ending
    typer.echo(message)


def main():
    typer.echo(f"Here is something written to standard error", err=True)

if __name__ == "__main__":
    typer.run(main)
