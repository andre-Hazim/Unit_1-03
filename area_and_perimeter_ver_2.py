# created by andre hazim
# created on Sept 2017
# created for ICS3U
# calculates any area and perimeter
import ui

def calculate_area_and_perimeter_touch_up_inside (sender):
    #calculate area and perimeter
    
    #input 
    length = int(view['length_textfield1'].text)
    width = int(view['width_textfield1'].text)
    
    #process
    area = length * width
    perimeter = 2*(length+width)
    
    #output
    view['area_answer_label1'].text = 'The area is :' + str(area) + 'cm^2'
    view['perimeter_answer_label1'].text = 'The perimeter is :' + str(perimeter) + 'cm'
view = ui.load_view()
view.present('sheet')
