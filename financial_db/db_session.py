from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constants import logger


def start_session():
    logger.info('Starting database session......')
    engine = create_engine('postgres://localhost:5432/Financial', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session, engine


def close_session(session):
    logger.info('Committing changes and closing database session......')
    session.commit()
    session.close()
