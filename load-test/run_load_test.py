#!

import getopt, sys, time, requests, random, string

web_ip = str(sys.argv[2])
baseUrl = 'http://' + web_ip + ':8000'


def randomString(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def userNameLength():
    return random.randint(5, 15)


def recipeNameLength():
    return random.randint(15, 50)


def recipeContentLength():
    return random.randint(200, 1000)


def emailLength():
    return random.randint(20, 35)


def random_seconds(low, high):
    return random.uniform(low, high)


def randomUserId(users):
    try:
        return random.choice(users)
    except:
        return ''


def randomRecipe(recipes):
    try:
        return random.choice(recipes)
    except:
        return ''


def randomUserEmail(emails):
    try:
        return random.choice(emails)
    except:
        return ''


def appendUser(user, users):
    if user is None:
        return
    users.append(user)


def appendRedipe(recipe, recipes):
    if recipe is None:
        return
    recipes.append(recipe)


def header(user_id=None):
    if user_id is None:
        return {'Content-Type': 'application/json'}
    else:
        return {'Content-Type': 'application/json', 'RequestingUser': user_id}


def getRecipeList(user_id):
    try:
        requests.get(baseUrl + '/api/recipe', headers=header(user_id=user_id))
    except:
        return


def getUserRecipeBook(user_id):
    try:
        requests.get(baseUrl + '/api/user/' + user_id + '/recipe-book', headers=header(user_id=user_id))
    except:
        return


def getUserByEmail(email):
    try:
        requests.get(baseUrl + '/api/user?email=' + email, headers=header())
    except:
        return


def postUser(users, emails):
    try:
        post_data = {"userName": randomString(userNameLength()), "userEmail": randomString(emailLength())}
        response = requests.post(baseUrl + '/api/user', json=post_data, headers=header())
        users.append(response.json()['userId'])
        emails.append(response.json()['userEmail'])
    except:
        return


def postRecipe(user_id, recipes):
    try:
        post_data = {"recipeName": randomString(recipeNameLength()), "recipeContent": randomString(recipeContentLength())}
        response = requests.post(baseUrl + '/api/recipe', json=post_data, headers=header(user_id=user_id))
        recipes.append(response.json()['recipeId'])
    except:
        return


def putRecipe(recipe_id, user_id):
    try:
        put_data = {"recipeName": randomString(recipeNameLength()), "recipeContent": randomString(recipeContentLength())}
        requests.put(baseUrl + '/api/recipe/' + recipe_id, json=put_data, headers=header(user_id=user_id))
    except:
        return


def getRecipe(recipe_id, user_id):
    try:
        requests.get(baseUrl + '/api/recipe/' + recipe_id, headers=header(user_id=user_id))
    except:
        return


def getUserById(user_id):
    try:
        requests.get(baseUrl + '/api/user/' + user_id, headers=header())
    except:
        return


def postUserRecipeBook(user_id, recipe_id):
    try:
        post_data = {"recipe_id": recipe_id}
        requests.post(baseUrl + '/api/user/' + user_id + '/recipe-book', json=post_data, headers=header(user_id=user_id))
    except:
        return


def deleteRecipeFromRecipeBook(user_id, recipe_id):
    try:
        requests.delete(baseUrl + '/api/user/' + user_id + '/recipe-book/' + recipe_id, headers=header(user_id=user_id))
    except:
        return


def main():
    num_users = str(sys.argv[1])
    web_ip = str(sys.argv[2])
    time_between_new_users = str(sys.argv[3])

    users = []
    recipes = []
    emails = []

    print('Running Test against ' + web_ip + ' with ' + num_users + ' user thread(s), with a new user starting approximately every ' + time_between_new_users + ' seconds.')
    postUser(users, emails)
    time.sleep(random_seconds(2, 5))

    getRecipeList(user_id=None)
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(2, 6))

    getRecipeList(randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(2, 6))

    getUserByEmail(randomUserEmail(emails))
    time.sleep(random_seconds(1, 3))

    postUser(users, emails)
    time.sleep(random_seconds(1, 3))

    postRecipe(randomUserId(users), recipes)
    getRecipe(randomRecipe(recipes), randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(10, 18))

    postRecipe(randomUserId(users), recipes)
    getRecipe(randomRecipe(recipes), randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(10, 18))

    getUserById(randomUserId(users))
    getRecipeList(randomUserId(users))
    time.sleep(random_seconds(2, 6))

    getRecipeList(randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(2, 4))

    postUserRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(1, 3))

    postUserRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(1, 3))

    postUserRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(2, 4))

    getRecipeList(randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(2, 5))

    getRecipe(randomRecipe(recipes), randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(1, 3))

    getRecipeList(randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(6, 10))

    getUserById(randomUserId(users))
    getRecipeList(randomUserId(users))
    time.sleep(random_seconds(1, 4))

    deleteRecipeFromRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(1, 3))

    getUserById(randomUserId(users))
    getRecipeList(randomUserId(users))
    time.sleep(random_seconds(2, 5))

    deleteRecipeFromRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    getRecipeList(randomUserId(users))
    time.sleep(random_seconds(3, 6))

    getRecipe(randomRecipe(recipes), randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(1, 3))

    deleteRecipeFromRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(1, 2))

    postUserRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(3, 7))

    getUserByEmail('asdfasdf')
    time.sleep(random_seconds(3, 7))

    getUserById(randomUserId(users))
    getRecipeList(randomUserId(users))
    time.sleep(random_seconds(1, 4))

    getRecipe(randomRecipe(recipes), randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(3, 7))

    putRecipe(randomRecipe(recipes), randomUserId(users))
    time.sleep(random_seconds(1, 4))

    getUserById(randomUserId(users))
    getRecipeList(randomUserId(users))
    time.sleep(random_seconds(1, 4))

    getRecipe(randomRecipe(recipes), randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(3, 7))

    deleteRecipeFromRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(1, 2))

    postUserRecipeBook(randomUserId(users), randomRecipe(recipes))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(2, 4))

    getUserById(randomUserId(users))
    getRecipeList(randomUserId(users))
    time.sleep(random_seconds(1, 3))

    getRecipeList(randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(2, 4))

    getRecipeList(randomUserId(users))
    getUserRecipeBook(randomUserId(users))
    time.sleep(random_seconds(2, 4))

    print('users:')
    for user in users:
        print('     ' + user)
    print('recipes')
    for recipe in recipes:
        print('     ' + recipe)
    print('emails')
    for email in emails:
        print('     ' + email)
    print('Done Running Test')


if __name__ == "__main__":
    main()
