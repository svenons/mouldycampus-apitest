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
    
def register(data):
    url = api_url + "register/"
    req = requests.post(url, data=data)
    if req.status_code == 200:
        try:
            return req.json()['token']
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code
    
def logout(token):
    url = api_url + "logout/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    req = requests.post(url, headers=headers)
    if req.status_code == 200:
        try:
            return req.json()
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

def fetchReviews(course_id):
    url = api_url + "reviews"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "course_id": course_id
    }
    req = requests.get(url, headers=headers, data=json.dumps(data))
    if req.status_code == 200:
        try:
            return req.json()
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code

def addReview(token, input_data):
    url = api_url + "createAReview/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    req = requests.post(url, headers=headers, data=json.dumps(input_data))
    if req.status_code == 200:
        try:
            return req.json()
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code
    
def deleteReview(token, review_id):
    url = api_url + "deleteAReview/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "review_id": review_id
    }
    req = requests.delete(url, headers=headers, data=json.dumps(data))
    if req.status_code == 200:
        try:
            return req.json()
        except json.JSONDecodeError:
            return req.text
    else:
        return req.status_code

if __name__ == "__main__":
    print("\nWelcome to MouldyCampus API Testing script")
    options = ["Login", "Update Profile", "Get All Courses", "Get All Professors", "Get Individual Course", "Get Individual Professor", "Fetch Reviews for a course", "Add a review", "Delete a review", "Exit"]
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
            print("Number of courses returned:")
            print("Last 3 courses:")
            for i in range(min(3, len(courses))):
                course_info = courses[i]['courseinfo']
                professors = courses[i].get('professors', [])
                professor_names = ', '.join([prof['name'] for prof in professors]) if professors else "N/A"
                print(f"Course: {course_info['name']} (ID: {course_info['id']}) | Professors: {professor_names} | Ratings: {len(courses[i]['ratings'])}")

        elif choice == 4:
            print("Attempting to get professors...")
            profs = getProfessors()
            print("Number of professors returned:", len(profs))
            print("Last 3 professors:")
            
            # Iterate over the first 3 professors (or fewer if there are less than 3)
            for i in range(min(3, len(profs))):
                professor = profs[i]['professor']
                courses = profs[i]['courses']
                ratings = profs[i]['ratings']

                # Professor's name
                print(f"Professor: {professor['name']}")

                # List of courses
                print("Courses:")
                for course in courses:
                    print(f"  - {course['name']}: {course['description']}")

                # Calculate average rating
                if ratings:
                    avg_rating = sum(float(rating['rating']) for rating in ratings) / len(ratings)
                    print(f"Average Rating: {avg_rating:.2f}")
                else:
                    print("Average Rating: No ratings available")

                print()  # Empty line for better readability

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

        elif choice == 7:
            print("Please enter the course ID:")
            id = input()
            print("Attempting to fetch reviews for course with ID:", id)
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
                reviews = fetchReviews(id)
                print("Number of reviews returned:", len(reviews))
                if len(reviews) == 0:
                    print("No reviews found.")
                else:
                    print("Last 3 reviews:")
                    for i in range(min(3, len(reviews))):
                        print(reviews[i]['review'], reviews[i]['rating'])
        elif choice == 8:
            if not token:
                print("You need to login first.")
            else:
                print("Please enter the course ID:")
                course_id = input()
                print("Please enter the review:")
                review = input()
                print("Please enter the rating:")
                rating = input()
                input_data = {
                    "course_id": course_id,
                    "rating": rating,
                    "review": review
                }
                print("Attempting to add a review with the following data:", input_data)
                response = addReview(token, input_data)
                print("Response:", response)

        elif choice == 9:
            if not token:
                print("You need to login first.")
            else:
                print("Please enter the review ID:")
                review_id = input()
                print("Attempting to delete review with ID:", review_id)
                response = deleteReview(token, review_id)
                print("Response:", response)
        
        else:
            print("Exiting...")
            break