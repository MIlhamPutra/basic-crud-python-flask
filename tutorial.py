from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)


# the class Movie will inherit the db.Model of SQLAlchemy
class Tutorial(db.Model):
    __tablename__ = 'tutorial'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    description = db.Column(db.String(80), nullable=False)
    published = db.Column(db.Boolean, nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'description': self.description, 'published': self.published}
        # this method we are defining will convert our output to json

    def add_tutorial(_title, _description, _published):
        '''function to add tutorial to database using _title, _description, _published
        as parameters'''
        # creating an instance of our tutorial constructor
        new_tutorial = Tutorial(title=_title, description=_description, published=_published)
        db.session.add(new_tutorial)  # add new tutorial to database session
        db.session.commit()  # commit changes to session

    def get_all_tutorial():
        '''function to get all tutorial in our database'''
        return [Tutorial.json(tutorial) for tutorial in Tutorial.query.all()]

    def get_tutorial(_id):
        '''function to get tutorial using the id of the tutorial as parameter'''
        return [Tutorial.json(Tutorial.query.filter_by(id=_id).first())]
        # Movie.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_tutorial(_id, _title, _description, _published):
        '''function to update the details of a tutorial using the id, title,
        description and published as parameters'''
        tutorial_to_update = Tutorial.query.filter_by(id=_id).first()
        tutorial_to_update.title = _title
        tutorial_to_update.description = _description
        tutorial_to_update.published = _published
        db.session.commit()

    def delete_tutorial(_id):
        '''function to delete a tutorial from our database using
           the id of the tutorial as a parameter'''
        Tutorial.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database
