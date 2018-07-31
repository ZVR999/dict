# python dict.py
me = {
    'name':'Zach',
    'age':'26',
    'country of birth':'The United States',
    'favorite language':'JavaScript'
}
love = {
    'name':'Love',
    'age':'29',
    'country of birth':'The United States',
    'favorite language':'SQL'
}
def peopleReader(dic):
    dict_str = ''
    for x in range(0,1):
        dict_str +="My name is "+dic['name']+'\n'
        dict_str +="My age is "+dic['age']+'\n'
        dict_str +="My country of birth is "+dic['country of birth']+'\n'
        dict_str +="My favorite language is "+dic['favorite language']
    print dict_str
peopleReader(me)
peopleReader(love)