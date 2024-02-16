obj = [1,2,3]

print(obj)

len(obj)

# function
# syntax:
# def [NAME]([PARAMETERS]):

def talk():
    print('...')
    print('yapa yapa yapa')
    print('...')
    print('done talking')

def blender(fruit1, fruit2):
    print('...blending...')
    smoothie = 'You made a ' + fruit1 + ' and ' + fruit2 + ' smoothie!'
    return smoothie

s1 = blender('strawberry', 'banana')
s2 = blender('kiwi', 'mango')
s3 = blender('blueberry', 'rasberry')

print(s1)
print(s2)
print(s3)

print(blender('passionfruit', 'watermelon'))





def print_up_to(num):
    for num in range(num + 1):
        print(num)

print_up_to(15)

print_up_to(8)


def area(length, width):
    return length * width

print(area(10,20))
print(area(11,11))


def get_posts(user):
    pass

def creat_post(user, data):
    pass

def like_post(post, user):
    pass



def get_max(nums):
    current_biggest = None
    for num in nums:
        if current_biggest == None:
            current_biggest = num

        if current_biggest < num:
            current_biggest = num
    return current_biggest


        
    


big = [100,200,111,222,333,9]

print(max(big))
print(get_max(big))