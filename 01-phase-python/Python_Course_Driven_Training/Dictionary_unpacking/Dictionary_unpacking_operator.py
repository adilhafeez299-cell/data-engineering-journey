button = {
   'width': 200,
    'text': 'Buy'
}

red_button = {
    **button,
    'color': 'red'
}

print(red_button)
print(button)

#example_2
button_info = {
    'text':'buy'
}


button_style = {
    'color' : 'yello',
    'width' : 200,
    'height' : 300,
}

button = {
    **button_info,
    **button_style

}

print(button)

# ways of unpacking merging lists together 
# example 3

button_info2 = {
    'text2' : 'buy2'
}
button_style2 = {
    'color2' : 'yello',
    'width2' : 200,
    'height2' : 300,

}
button2 = button_info2 | button_style2
print(button2)
