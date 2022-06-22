from flask import Flask, jsonify, abort, request
import sqlite3
from random import choice
from sqlite3 import Error
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = Path(__file__).parent

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Не переводим русские символы в unicode
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR / 'test.db'}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PersonModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), unique=False)
    position = db.relationship('EmployeeModel', backref='person', lazy='dynamic')
    def __init__(self,fullname,position):
        self.fullname = fullname
        self.position = position


class EmployeeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey(PersonModel.id))
    fullname = db.Column(db.String(255), unique=False)
    position = db.Column(db.String(255), unique=False)

    def __init__(self, fullname, position):
        self.fullname = fullname
        self.position = position

    def __repr__(self):
        return f"Fullname: {self.fullname}, position: {self.position}"

    def to_dict(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "position": self.position
        }




@app.route("/employees")
def about_employees():
    employees = EmployeeModel.query.all()
    employees = [employee.to_dict() for employee in employees]
    return jsonify(employees)


@app.route("/employees", methods=['POST'])
def add_employee():
    new_employee = request.json
    e = EmployeeModel(**new_employee)
    db.session.add(e)
    db.session.commit()
    return jsonify(e.to_dict()), 201


@app.route("/employees/<int:id>")
def get_employee_by_id(id):
    employee = EmployeeModel.query.get(id)
    if employee is None:
        abort(404, f"Сотрудника с id={id} не существует.")
    return jsonify(employee.to_dict())


@app.route("/employees/<int:id>", methods=["PUT"])
def edit_employee(id):
    edit_emoloyee = request.json
    e = EmployeeModel.query.get(id)
    if e is None:
        abort(404, f"Сотрудник с id={id} не найден")

    if edit_emoloyee.get("fullname"):
        e.fullname = edit_emoloyee["fullname"]
    if edit_emoloyee.get("position"):
        e.position = edit_emoloyee["position"]
    db.session.commit()
    return jsonify(e.to_dict()), 200


@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(id):
    emp = EmployeeModel.query.get(id)
    if emp:
        db.session.delete()
        db.session.commit()
        return f"Сотрудник с id={id} был удален.", 200
    abort(404, f"Сотрудник с id={id} не был найден.")


@app.route("/employees/filter")
def get_filter_eployees():
    fullname = request.args.get("fullname")
    position = request.args.get("position")
    print(fullname)
    print((position))
    if fullname != None and position ==None:
        res = db.session.query(EmployeeModel).filter(EmployeeModel.fullname == fullname)
    elif position != None and fullname == None:
        res = db.session.query(EmployeeModel).filter(EmployeeModel.positiin == position)
    elif position != None and fullname != None:
        res = db.session.query(EmployeeModel).filter(EmployeeModel.fullname == fullname, EmployeeModel.position == position)

    return jsonify([obj.to_dict() for obj in res])







def create_connection(path):
    try:
        print('Connection to SQLite DB successlful')
        return sqlite3.connect(path)
    except Error as e:
        print(f'The error "{e}" occured')


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query executed successfully')
        return cursor.lastrowid
    except Error as e:
        print(f'The error "{e}" occured')


def execute_read_query(connection, query, only_one=False):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if only_one:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        return result
    except Error as e:
        print(f'The error "{e}" occured')


if __name__ == "__main__":
    app.run(debug=True)
