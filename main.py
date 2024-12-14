import requests
import json

api_url = "http://127.0.0.1:8000/api/"

def textInterface(options):
    print("\nPlease select an option:")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(options)+1:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid choice, please try again.")

def login(data):
    url = api_url + "login/"
    req = requests.post(url, data=data)
    if req.status_code == 200:
        try:
            return req.json()['token']
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code
    
def updateProfile(token, data):
    url = api_url + "updateUserProfile/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    req = requests.put(url, headers=headers, data=json.dumps(data))
    if req.status_code == 200:
        try:
            return req.json()
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code
    
def getCourses():
    url = api_url + "courses/"
    req = requests.get(url)
    if req.status_code == 200:
        try:
            return req.json()
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code

def getProfessors():
    url = api_url + "professors/"
    req = requests.get(url)
    if req.status_code == 200:
        try:
            return req.json()
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code

def getIndividualCourse(id):
    url = api_url + "course"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "id": id
    }
    req = requests.get(url, headers=headers, data=json.dumps(data))
    if req.status_code == 200:
        try:
            return req.json()
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code

def getIndividualProfessor(id):
    url = api_url + "professor"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "id": id
    }
    req = requests.get(url, headers=headers, data=json.dumps(data))
    if req.status_code == 200:
        try:
            return req.json()
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code

if __name__ == "__main__":
    print("\nWelcome to MouldyCampus API Testing script")
    options = ["Login", "Update Profile", "Get All Courses", "Get All Professors", "Get Individual Course", "Get Individual Professor", "Exit"]
    token = None

    while True:
        choice = textInterface(options)
        if choice == 1:
            data = {
                "email": "testuser@student.sdu.dk",
                "password": "testUserPassowrd@",
            }
            print("Attempting to login with the following data:", data)
            token = login(data)
            print("Token:", token)

        elif choice == 2:
            if not token:
                print("You need to login first.")
            else:
                data = {
                    "name": "New Name",
                    "email": "testuser@student.sdu.dk",
                    "password": "testUserPassowrd@",
                    "password_confirmation": "testUserPassowrd@",
                }
                print("Attempting to update profile with the following data:", data)
                response = updateProfile(token, data)
                print("Response:", response)

        elif choice == 3:
            print("Attempting to get courses...")
            courses = getCourses()
            print("Number of courses returned:", len(courses))
            print("Last 3 courses:")
            for i in range(3):
                print(courses[i]['name'], courses[i]['id'])

        elif choice == 4:
            print("Attempting to get professors...")
            profs = getProfessors()
            print("Number of professors returned:", len(profs))
            print("Last 3 professors:")
            for i in range(3):
                print(profs[i]['name'], profs[i]['id'])
        
        elif choice == 5:
            print("Please enter the course ID:")
            id = input()
            print("Attempting to get course with ID:", id)
            if not id.isnumeric():
                print("ID must be a number.")
                continue
            elif int(id) < 1:
                print("ID must be greater than 0.")
                continue
            elif id == "":
                print("ID cannot be empty.")
                continue
            else:
                course = getIndividualCourse(id)
                print("Course:", course)

        elif choice == 6:
            print("Please enter the professor ID:")
            id = input()
            print("Attempting to get professor with ID:", id)
            if not id.isnumeric():
                print("ID must be a number.")
                continue
            elif int(id) < 1:
                print("ID must be greater than 0.")
                continue
            elif id == "":
                print("ID cannot be empty.")
                continue
            else:
                prof = getIndividualProfessor(id)
                print("Professor:", prof["professor"]["name"])
                print("Average rating:", prof["average_rating"])
        
        else:
            print("Exiting...")