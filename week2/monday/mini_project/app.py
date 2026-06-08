from flask import Flask,request,jsonify

app=Flask(__name__)

# Build a Flask application that manages a list of students and supports the four basic CRUD operations:

#         Create
#         Read
#         Update
#         Delete

#In-Memory list of students
students = [
    {
        "id": 1,
        "name": "Alice",
        "course": "Computer Science"
    },
    {
        "id": 2,
        "name": "Bob",
        "course": "Data Science"
    }
]

count=len(students)

# Display all Students
@app.get("/students")
def getStudents():
    return jsonify(students),200

@app.get("/students/<int:id>")
def getStudentById(id):
    student = next(filter(lambda s: s["id"] == id, students), None)
    if student is None:
        return jsonify({"ERROR": "Student not found"}), 404
    return jsonify(student),200


#Add a new student

@app.post("/students")
def addStudent():
    data=request.get_json()

    if not data:
        return jsonify({"ERROR": "Invalid request"}), 400
        
    global count
    count+=1

    student={
        "id": count,
        "name": data["name"],
        "course": data["course"]
    }
    students.append(student)

    return jsonify(student), 201

    
# Modify an existing students Details 
@app.put("/students/<int:id>")
def editStudentDetails(id):
    data=request.get_json()

    student = next(filter(lambda s: s["id"] == id, students), None)
    if student is None:
        return jsonify({"ERROR": "Student not found"}), 404
    
    student["name"]=data["name"]
    student["course"]=data["course"]
    

    return jsonify(student),200

# Delete a Student
@app.delete("/students/<int:id>")
def deleteStudent(id):
    student = next(filter(lambda s: s["id"] == id, students), None)

    if student is None:
        return jsonify({"ERROR": "Student not found"}), 404
    
    students.remove(student)
    return jsonify({"message": "Student deleted successfully"}), 204
    
        




    
            

    


    



if __name__=="__main__":
    app.run(debug=True)

