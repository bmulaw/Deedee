
def parseContentTo2D():
    # TODO: convert non-str strings into its original datatype (timestamp/int)
    data = []
    tempInputStr = input()
    isUserFollows = False
    while tempInputStr:
        curr_input = tempInputStr.split(', ')
        if len(curr_input) == 1:
            isUserFollows = True
        if isUserFollows:
            data.append(curr_input)
        else:
            curr_input[3] = int(curr_input[3])
            curr_input[4] = int(curr_input[4])
            data.append(curr_input)
        try:
            tempInputStr = input()
        except:
            break
    # returns an array where first item of array is a 2D array (excludes separator and userFollows)
                           # second item of array is just userFollows array
    return [data[:-2], data[-1]]

# ['Snap news, news, ghostnews, 1609598670, 23'] => ['Snap news', 'news', ...]
# print(parseContentTo2D())

def contentForUser():
    contents = parseContentTo2D()
    # print(contents)
    userFollows = contents[-1]
    setOfCreatorsUserFollows = set()
    result = []
    for i in range(1, len(userFollows)):
        setOfCreatorsUserFollows.add(userFollows[i])
    
    contents = contents[0]
    for item in contents:
        creator = item[2]
        if creator in setOfCreatorsUserFollows:
            result.append(item)
            # print(item)
    return result
        
# contentForUser()

def sortByTimestampOrGenre(content, sortByMain, sortBySecondary, asc):
    
    for i in range(len(content)):
        for j in range(len(content)-1):
            if (content[j][sortByMain]) > (content[j+1][sortByMain]):
                temp = content[j]
                content[j] = content[j+1]
                content[j+1] = temp
            if (content[j][sortByMain] == content[j+1][sortByMain]):
                if (content[j][sortBySecondary] > content[j+1][sortBySecondary]):
                    temp = content[j]
                    content[j] = content[j+1]
                    content[j+1] = temp
    
    if asc:
        content = content[::-1]
        
    return content
                
# sortByTimestampOrGenre(contentForUser(), 1, reverse=True)



##################### TESTS #####################

def test_isIntDataType(data):
    for content in data:
        if type(content[3]) != int or type(content[4]) != int:
            return False
    return True 


def test_parseContentTo2D():
    data = parseContentTo2D()
    print("Returns a 2D array" , type(data[0][0]) == list)
    print("Correctly has int type for timestamp and viewCount" , test_isIntDataType(data[0]))
    
# test_parseContentTo2D()

# def test_contentForUsers():
    

def test_sortByTimestampOrGenre():
    content = contentForUser()
    EXPECTED_TIMESTAMP_ASC = [['Snap news', 'news', 'ghostnews', 1609598670, 23], ["Inclusive Camera is the future", "news", "ghostnews", 1609598670, 10000], ["How to make a living selling Peanut Butter", "finance", "mrbillion", 1609598670, 0]]
    
    print("Sorts by Timestamp in asc order", sortByTimestampOrGenre(content, 3, 4, asc=False)[:3])

    
test_sortByTimestampOrGenre()
"""

[ 
  [
     ['Ghost ball', ' sports', ' ghostfaceballers', 1623749538, 350], ['Please do not watch3…', ' Anime', ' ghostfaceballers', 1620172791, 10000000000], ['War Ready', ' Games', ' ghostrecon', 1611849496, 350], ['Please do not watch1…', ' Anime', ' ghostfaceballers', 1620172799, 10000000000], ['Love my chicken', ' Food', ' gordenramsey', 1620172794, 198], ['Please do not watch…', ' Anime', ' ghostfaceballers', 1628205274, 10000000000], ['Buy Dodge coin', ' Finance', ' elonmusk', 1615999632, 999999999], ['Please do not watch2…', ' Anime', ' ghostfaceballers', 1620172793, 10000000000], ['Inclusive Camera is the future', ' news', ' ghostnews', 1609598670, 10000], ['OBJ has been traded for 20th time', ' sports', ' ghostfaceballers', 1618914901, 350], ['unlimited amo for everyone', ' games', ' ghostrecon', 1613796631, 35240], ['Candy Crush Cheats', ' games', ' winnersneverlose', 1620372144, 87], ['How to take care of your console', ' games', ' winnersneverlose', 1611082481, 456], ['Get a PS5 for free', ' games', ' winnersneverlose', 1620067462, 0], ['How to eat like a gamer', ' food', ' winnersneverlose', 1620067462, 0], ['Love my chicken', ' food', ' gordenramsey', 1640617522, 198], ['Snap will be $1 million per share by 2023', ' finance', ' woody', 1619380713, 999999999], ['Please watch!!!!', ' anime', ' princevega', 1636816917, 52], ['How to make a living selling Peanut Butter', ' finance', ' mrbillion', 1609598670, 0], ['Visit Wood Goods in Venice', ' food', ' woody', 1611082481, 879], ['Game of the year goes to', ' games', ' sergio', 1624092165, 10], ['Kendrick Lamar is actually dropping an album', ' news', ' ghostnews', 1639357554, 220], ['Food is an art', ' food', ' gordenramsey', 1624372144, 31415], ['Vegan Vegan Vegan', ' food', ' gordenramsey', 1615999632, 6636], ['Bone licking goodness', ' food', ' gordenramsey', 1611849496, 8555], ['Food War', ' food', ' ghostfaceballers', 1637090932, 123456], ['famous cocktail', ' food', ' ghostfaceballers', 1422128325, 741], ['the earth is flat', ' news', ' elonmusk', 1628205274, 854], ['Love those rockets', ' news', ' elonmusk', 1609598670, 357], ['fake news is not great', ' news', ' princevega', 1620372144, 1110], ['Top dunks of 2021', ' sports', ' jonah', 1627872144, 42420], ['Stuntin is a habit', ' finance', ' mrbillion', 1624372144, 320394], ['What you need to know about Log4j', ' news', ' sergio', 1624372144, 3000], ['These jerk chicken tacos are amazing', ' food', ' jonah', 1620372144, 100000], ['Snap teams host volleyball tournament', ' sports', ' ghostfaceballers', 1639357554, 324], ['This food competition is crazy!', ' sports', ' jonah', 1620372144, 12]
   ], 
    
    ['Evan', ' mrbillion', ' ghostnews', ' jonah', ' woody', ' sergio']
]

"""

