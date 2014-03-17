import Tkinter
from Tkinter import *
root = Tk( )
labelfont = ('times', 100, 'italic')
labelfont2 = ('times', 10, 'italic')

widget = Label(root, text='bananpaj', font=labelfont)
widget2 = Label(root, text='Ingredients \n For custard filling:\n5 large egg yolks\n1/4 cup cornstarch\n3 to 3 1/2 cups heavy cream\n2 cups sugar\n1 vanilla bean, split and scraped\n\nFor pie crust:\n3 cups graham cracker crumbs\n1/2 cup sugar\n1/2 ripe banana, mashed\n1/4 pound (1 stick) unsalted butter, melted\n3 pounds bananas, cut crosswise into 1/2 inch slices\nFor drizzled toppings:\n3/4 cup caramel sauce, recipe follows\n1 cup chocolate sauce, recipe follows\nFor whipped cream topping:\n2 cups heavy cream whipped to stiff peaks\n1/2 teaspoon pure vanilla extract\n2 teaspoons granulated sugar\nGarnishes:\nShaved chocolate\nPowdered sugar', font=labelfont2)
widget.Label=('times', 10, 'bold')
widget.config(bg='black', fg='red')
widget.pack(expand=YES, fill=BOTH)
widget2.pack(expand=YES, fill=BOTH)


widget2.Label=('times', 10, 'bold')
widget2.config(bg='black', fg='red')
root.mainloop( )
