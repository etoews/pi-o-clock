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
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'pi-clock-test.sqlite')


class ProductionConfig(Config):
    LOG_FILE = os.path.join(basedir, 'pi-clock.log')
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'pi-clock.sqlite')


config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
}