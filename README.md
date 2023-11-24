# Meals Rater API

---

---

### => Business requirements as per the mockup

##### 1. Meals list screen has the following information

- **Meal name**
- **Meal number of stars**
- **Meal average rate**
- **Login**
- **Register**
- **Display already logged in user**

##### 2. Popup error if the user already rated

##### 3. Add rate screen, stars 1 to 5 only and SAVE

---

### => Technical requirements

**_Using REST framework implement the followings:_**

##### 1. Models

- **Meal**
- **Stars**
- **User**

##### 2. validation if the user already rated the meal

##### 3. validate rating MIN 1 and MAX 5

##### 4. CRUD API for Meals

    http://127.0.0.1:8000/api/meals/
    it should return the average rating and number of rates a long with the meal name and details

##### 5. CRUD API for stars

    http://127.0.0.1:8000/api/stars/
    no one should be able to use this CRUD for rating !!!

##### 6. Rate API

    http://127.0.0.1:8000/api/meals/MEAL_PK/rate_meal/
    create and update API

##### 7. Token Authentication

##### 8. Login and Register API

##### 9. Token request API

##### 10. Deploy on Heroku
