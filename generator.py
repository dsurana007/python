def cubes(nums):
    for i in nums:
        yield i ** 3

def main():
    nums = [1,2,3,4,5,6]
    """ way1 
          cube below is a generator object , generator doesn't hold the entire result in memory , 
           it yields  one result at a time  
    """
    print("\n Way1")
    cube = cubes(nums)
    print(cube)
    print(next(cube))
    print(next(cube))
    print(next(cube))

    """ way2 """
    print("\n Way2")
    for num in cubes(nums):
        print(num,end =" ")

    """  way3 
    directly iterating over the captured generator object
    """
    print("\n Way3")
    cube = cubes(nums)
    for num in cube:
        print(num,end=" ")


#print(__name__)
if __name__ == '__main__':
    main()