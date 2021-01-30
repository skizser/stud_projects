from app import app, db
from app.models import Competition, Horses, Jockeys, Owners, CompetitionDetail

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 
        'Competition' : Competition,   
        'Horses' : Horses, 
        'Jockeys' : Jockeys, 
        'Owners' : Owners, 
        'CompetitionDetail' : CompetitionDetail
        }