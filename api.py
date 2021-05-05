from tutorial import *


# route to get all tutorial
@app.route('/tutorial', methods=['GET'])
def get_tutorial():
    '''Function to get all the tutorial in the database'''
    return jsonify({'Tutorial': Tutorial.get_all_tutorial()})


# route to get tutorial by id
@app.route('/tutorial/<int:id>', methods=['GET'])
def get_tutorial_by_id(id):
    return_value = Tutorial.get_tutorial(_id)(id)
    return jsonify(return_value)


# route to add new tutorial
@app.route('/tutorial', methods=['POST'])
def add_tutorial():
    '''Function to add new tutorial to our database'''
    request_data = request.get_json()  # getting data from client
    Tutorial.add_tutorial(request_data["title"], request_data["description"],
                    request_data["published"])
    response = Response("Tutorial added", 201, mimetype='application/json')
    return response


# route to update tutorial with PUT method
@app.route('/tutorial/<int:id>', methods=['PUT'])
def update_tutorial(id):
    '''Function to edit tutorial in our database using tutorial id'''
    request_data = request.get_json()
    Tutorial.update_tutorial(_id, _title, _description, _published)(id, request_data['title'], request_data['description'], request_data['published'])
    response = Response("tutorial Updated", status=200, mimetype='application/json')
    return response


# route to delete tutorial using the DELETE method
@app.route('/tutorial/<int:id>', methods=['DELETE'])
def remove_tutorial(id):
    '''Function to delete tutorial from our database'''
    Tutorial.delete_tutorial(id)
    response = Response("Tutorial Deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)
