from db_session import start_session, close_session, logger
from db_models import model_list


def create_table(engine, model):
    if model.__table__.exists(engine):
        model.__table__.drop(engine)
    model.__table__.create(engine)
    logger.info('Model created: {}'.format(model.__tablename__))


if __name__ == '__main__':
    session, engine = start_session()
    for model in model_list:
        create_table(engine, model)
    close_session(session)
