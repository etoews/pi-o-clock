import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True
    LOG_FILE = os.path.join(basedir, 'pi-clock-test.log')
    DB_FILE = os.path.join(basedir, 'pi-clock-test.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_FILE


class ProductionConfig(Config):
    LOG_FILE = os.path.join(basedir, 'pi-clock.log')
    DB_FILE = os.path.join(basedir, 'pi-clock.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_FILE


config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
}