#def comments_info(comments_qty, day):
   # print(f'{comments_qty} comments were posted on {day}')

#(comments_qty = 50, day = 'monday')
#(day = 'tuesday', comments_qty = 43)
#comments_info(50, day = 'thursday')
#positional arguments matter;
#to fix this we can use keyword arguments
# can mix positional arguments with keyword arguments
# but if we were to swap this around we would get error
# can not do comment_info(day = 'thursday', 50) as this is in the wrong place compared to function parameters

def comments_info(*args):
    print(f'{args[0]} comments were posted on {args[1]}')

comments_info(50, 'Monday')
# single parameter with * in front, can not use keyword arguments
