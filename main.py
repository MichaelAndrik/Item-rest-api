import pytest
from flask.cli import FlaskGroup

from apps import run_app

app = run_app()
manager = FlaskGroup(app)


@manager.command('test')
def test():
    return pytest.main(['-v', './app/test'])


if __name__ == '__main__':
    app.run(debug=True)
