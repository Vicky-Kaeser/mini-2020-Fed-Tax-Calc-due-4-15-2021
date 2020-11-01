
#create a class with respective objects/instances and populate taxable data with them
class Fed_Tax():
    #create methods/functions that return tax due
    def fed_tax_calc_separately_married(self, taxable_income):

        #create lists with values to use in the taxable income calculation
        separately_married_2020_brakets = [0.1, 9875.0, 0.12, 40125.0, 0.22, 85525.0, 0.24, 163300.0, 0.32, 207350.0, 0.35, 311025.0, 0.37, 311026.0] 
        rate1, max_amnt1, rate2, max_amnt2, rate3, max_amnt3, rate4, max_amnt4, rate5, max_amnt5, rate6, max_amnt6, rate7, max_amnt7 = [separately_married_2020_brakets[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)]
        
    

        #rate brakets labeled. the two commented out prints could be used to show the per rate amount
        #10% braket1
        if float(taxable_income) >= max_amnt1:
            braket1 = max_amnt1 * rate1 
            total_tax = braket1
        elif float(taxable_income) < max_amnt1:
            braket1 = float(taxable_income) * rate1
            total_tax = braket1
        #print("b1separately_married ", braket1)
        #print(total_tax)
            

        #12% braket2
        if float(taxable_income) > max_amnt1: 
            if float(taxable_income) >= max_amnt2:
                braket2 = (max_amnt2 - max_amnt1 )* rate2
                total_tax = total_tax + braket2
            elif float(taxable_income) < max_amnt2: 
                braket2 = (float(taxable_income) - max_amnt1) * rate2
                total_tax = total_tax + braket2
           #print("b2 ", braket2)
        #print(total_tax)
    
        #22% braket3
        if float(taxable_income) > max_amnt2: 
            if float(taxable_income) >= max_amnt3:
                braket3 = (max_amnt3 - max_amnt2)* rate3
                total_tax = total_tax + braket3
            elif float(taxable_income) < max_amnt3: 
                braket3 = (float(taxable_income) - max_amnt2) * rate3
                total_tax = total_tax + braket3
            #print("b3 ", braket3)
        #print(total_tax)
                
        #24% braket4
        if float(taxable_income) > max_amnt3: 
            if float(taxable_income) >= max_amnt4:
                braket4 = (max_amnt4 - max_amnt3) * rate4
                total_tax = total_tax + braket4 
            elif float(taxable_income) < max_amnt4: 
                braket4 = (float(taxable_income) - max_amnt3) * rate4 
                total_tax = total_tax + braket4
            #print("b4 ", braket4)
        #print(total_tax)
       
        #32% braket5
        if float(taxable_income) > max_amnt4: 
            if float(taxable_income) >= max_amnt5:
                braket5 = (max_amnt5 - max_amnt4) * rate5
                total_tax = total_tax + braket5 
            elif float(taxable_income) < max_amnt5: 
                braket5 = (float(taxable_income) - max_amnt4) * rate5
                total_tax = total_tax + braket5
            #print("b5 ", braket5)
        #print(total_tax)

        #35% braket6
        if float(taxable_income) > max_amnt5: 
            if float(taxable_income) >= max_amnt6:
                braket6 = (max_amnt6 - max_amnt5) * rate6
                total_tax = total_tax + braket6 
            elif float(taxable_income) < max_amnt6: 
                braket6 = (float(taxable_income) - max_amnt5) * rate6
                total_tax = total_tax + braket6
            #print("b6 ", braket6)
        #print(total_tax)
       

        #37% braket7
        #last braket might requires attention bc final taxable amnt given is 'or more'
        if float(taxable_income) >= max_amnt7:
            braket7 = (float(taxable_income) - max_amnt7) * rate7
            total_tax = total_tax + braket7
            #print("b7 ", braket7)

        return total_tax

#the next four commented out tags could be use if the taxable status are shown seperately
#tax = Fed_Tax()    
#taxable_income = input("What is your taxable income? ")
#tax_due = tax.fed_tax_calc_separately_married(taxable_income)
#print("Your federal tax amount due is ${}.".format(tax_due))


    def fed_tax_calc_married(self, taxable_income):
        
        married_2020_brakets = [0.1, 19750.0, 0.12, 80250.0, 0.22, 171050.0, 0.24, 326600.0, 0.32, 414700.0, 0.35, 622050.0, 0.37, 622051.0] 
        rate1, max_amnt1, rate2, max_amnt2, rate3, max_amnt3, rate4, max_amnt4, rate5, max_amnt5, rate6, max_amnt6, rate7, max_amnt7 = [married_2020_brakets[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)]
        
        

        
        #10% braket1
        if float(taxable_income) >= max_amnt1:
            braket1 = max_amnt1 * rate1 
            total_tax = braket1
        elif float(taxable_income) < max_amnt1:
            braket1 = float(taxable_income) * rate1
            total_tax = braket1
        #print("b1married ", braket1)
        #print(total_tax)
            

        #12% braket2
        if float(taxable_income) > max_amnt1: 
            if float(taxable_income) >= max_amnt2:
                braket2 = (max_amnt2 - max_amnt1 )* rate2
                total_tax = total_tax + braket2
            elif float(taxable_income) < max_amnt2: 
                braket2 = (float(taxable_income) - max_amnt1) * rate2
                total_tax = total_tax + braket2
            #print("b2 ", braket2)
            
            
       # print(total_tax)
    
        #22% braket3
        if float(taxable_income) > max_amnt2: 
            if float(taxable_income) >= max_amnt3:
                braket3 = (max_amnt3 - max_amnt2)* rate3
                total_tax = total_tax + braket3
            elif float(taxable_income) < max_amnt3: 
                braket3 = (float(taxable_income) - max_amnt2) * rate3
                total_tax = total_tax + braket3
            #print("b3 ", braket3)
        #print(total_tax)
                
        #24% braket4
        if float(taxable_income) > max_amnt3: 
            if float(taxable_income) >= max_amnt4:
                braket4 = (max_amnt4 - max_amnt3) * rate4
                total_tax = total_tax + braket4 
            elif float(taxable_income) < max_amnt4: 
                braket4 = (float(taxable_income) - max_amnt3) * rate4 
                total_tax = total_tax + braket4
           #print("b4 ", braket4)
        #print(total_tax)
       
        #32% braket5
        if float(taxable_income) > max_amnt4: 
            if float(taxable_income) >= max_amnt5:
                braket5 = (max_amnt5 - max_amnt4) * rate5
                total_tax = total_tax + braket5 
            elif float(taxable_income) < max_amnt5: 
                braket5 = (float(taxable_income) - max_amnt4) * rate5
                total_tax = total_tax + braket5
            #print("b5 ", braket5)
        #print(total_tax)

        #35% braket6
        if float(taxable_income) > max_amnt5: 
            if float(taxable_income) >= max_amnt6:
                braket6 = (max_amnt6 - max_amnt5) * rate6
                total_tax = total_tax + braket6 
            elif float(taxable_income) < max_amnt6: 
                braket6 = (float(taxable_income) - max_amnt5) * rate6
                total_tax = total_tax + braket6
            #print("b6 ", braket6)
        #print(total_tax)
       

        #37% braket7
        #last braket might requires attention bc final taxable amnt given is 'or more'
        if float(taxable_income) >= max_amnt7:
            braket7 = (float(taxable_income) - max_amnt7) * rate7
            total_tax = total_tax + braket7
            #print("b7 ", braket7)

        return total_tax


#tax = Fed_Tax()    
#taxable_income = input("What is your taxable income? ")
#tax_due = tax.fed_tax_calc_married(taxable_income)
#print("Your federal tax amount due is ${}.".format(tax_due))


    def fed_tax_calc_head_of_hhold(self, taxable_income):
        
        head_of_hhold_2020_brakets = [0.1, 14100.0, 0.12, 53700.0, 0.22, 85500.0, 0.24, 163300.0, 0.32, 207350.0, 0.35, 518400.0, 0.37, 518401.0] 
        rate1, max_amnt1, rate2, max_amnt2, rate3, max_amnt3, rate4, max_amnt4, rate5, max_amnt5, rate6, max_amnt6, rate7, max_amnt7 = [head_of_hhold_2020_brakets[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)]
        
        

        
        #10% braket1
        if float(taxable_income) >= max_amnt1:
            braket1 = max_amnt1 * rate1 
            total_tax = braket1
        elif float(taxable_income) < max_amnt1:
            braket1 = float(taxable_income) * rate1
            total_tax = braket1
        #print("b1head_of_hhold ", braket1)
        #print(total_tax)
            

        #12% braket2
        if float(taxable_income) > max_amnt1: 
            if float(taxable_income) >= max_amnt2:
                braket2 = (max_amnt2 - max_amnt1 )* rate2
                total_tax = total_tax + braket2
            elif float(taxable_income) < max_amnt2: 
                braket2 = (float(taxable_income) - max_amnt1) * rate2
                total_tax = total_tax + braket2
            #print("b2 ", braket2)
            
            
        #print(total_tax)
    
        #22% braket3
        if float(taxable_income) > max_amnt2: 
            if float(taxable_income) >= max_amnt3:
                braket3 = (max_amnt3 - max_amnt2)* rate3
                total_tax = total_tax + braket3
            elif float(taxable_income) < max_amnt3: 
                braket3 = (float(taxable_income) - max_amnt2) * rate3
                total_tax = total_tax + braket3
            #print("b3 ", braket3)
        #print(total_tax)
                
        #24% braket4
        if float(taxable_income) > max_amnt3: 
            if float(taxable_income) >= max_amnt4:
                braket4 = (max_amnt4 - max_amnt3) * rate4
                total_tax = total_tax + braket4 
            elif float(taxable_income) < max_amnt4: 
                braket4 = (float(taxable_income) - max_amnt3) * rate4 
                total_tax = total_tax + braket4
            #print("b4 ", braket4)
        #print(total_tax)
       
        #32% braket5
        if float(taxable_income) > max_amnt4: 
            if float(taxable_income) >= max_amnt5:
                braket5 = (max_amnt5 - max_amnt4) * rate5
                total_tax = total_tax + braket5 
            elif float(taxable_income) < max_amnt5: 
                braket5 = (float(taxable_income) - max_amnt4) * rate5
                total_tax = total_tax + braket5
            #print("b5 ", braket5)
        #print(total_tax)

        #35% braket6
        if float(taxable_income) > max_amnt5: 
            if float(taxable_income) >= max_amnt6:
                braket6 = (max_amnt6 - max_amnt5) * rate6
                total_tax = total_tax + braket6 
            elif float(taxable_income) < max_amnt6: 
                braket6 = (float(taxable_income) - max_amnt5) * rate6
                total_tax = total_tax + braket6
            #print("b6 ", braket6)
        #print(total_tax)
       

        #37% braket7
        #last braket might requires attention bc final taxable amnt given is 'or more'
        if float(taxable_income) >= max_amnt7:
            braket7 = (float(taxable_income) - max_amnt7) * rate7
            total_tax = total_tax + braket7
            #print("b7 ", braket7)

        return total_tax


#tax = Fed_Tax()    
#taxable_income = input("What is your taxable income? ")
#tax_due = tax.fed_tax_calc_head_of_hhold(taxable_income)
#print("Your federal tax amount due is ${}.".format(tax_due))


    def fed_tax_calc_single(self, taxable_income):
        
        single_2020_brakets = [0.1, 9875.0, 0.12, 40125.0, 0.22, 85525.0, 0.24, 163300.0, 0.32, 207350.0, 0.35, 518400.0, 0.37, 518401.0] 
        rate1, max_amnt1, rate2, max_amnt2, rate3, max_amnt3, rate4, max_amnt4, rate5, max_amnt5, rate6, max_amnt6, rate7, max_amnt7 = [single_2020_brakets[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)]
               

        
        #10% braket1
        if float(taxable_income) >= max_amnt1:
            braket1 = max_amnt1 * rate1 
            total_tax = braket1
        elif float(taxable_income) < max_amnt1:
            braket1 = float(taxable_income) * rate1
            total_tax = braket1
        #print("b1single ", braket1)
        #print(total_tax)
            

        #12% braket2
        if float(taxable_income) > max_amnt1: 
            if float(taxable_income) >= max_amnt2:
                braket2 = (max_amnt2 - max_amnt1 )* rate2
                total_tax = total_tax + braket2
            elif float(taxable_income) < max_amnt2: 
                braket2 = (float(taxable_income) - max_amnt1) * rate2
                total_tax = total_tax + braket2
            #print("b2 ", braket2)
            
            
        #print(total_tax)
    
        #22% braket3
        if float(taxable_income) > max_amnt2: 
            if float(taxable_income) >= max_amnt3:
                braket3 = (max_amnt3 - max_amnt2)* rate3
                total_tax = total_tax + braket3
            elif float(taxable_income) < max_amnt3: 
                braket3 = (float(taxable_income) - max_amnt2) * rate3
                total_tax = total_tax + braket3
            #print("b3 ", braket3)
        #print(total_tax)
                
        #24% braket4
        if float(taxable_income) > max_amnt3: 
            if float(taxable_income) >= max_amnt4:
                braket4 = (max_amnt4 - max_amnt3) * rate4
                total_tax = total_tax + braket4 
            elif float(taxable_income) < max_amnt4: 
                braket4 = (float(taxable_income) - max_amnt3) * rate4 
                total_tax = total_tax + braket4
            #print("b4 ", braket4)
        #print(total_tax)
       
        #32% braket5
        if float(taxable_income) > max_amnt4: 
            if float(taxable_income) >= max_amnt5:
                braket5 = (max_amnt5 - max_amnt4) * rate5
                total_tax = total_tax + braket5 
            elif float(taxable_income) < max_amnt5: 
                braket5 = (float(taxable_income) - max_amnt4) * rate5
                total_tax = total_tax + braket5
            #print("b5 ", braket5)
        #print(total_tax)

        #35% braket6
        if float(taxable_income) > max_amnt5: 
            if float(taxable_income) >= max_amnt6:
                braket6 = (max_amnt6 - max_amnt5) * rate6
                total_tax = total_tax + braket6 
            elif float(taxable_income) < max_amnt6: 
                braket6 = (float(taxable_income) - max_amnt5) * rate6
                total_tax = total_tax + braket6
            #print("b6 ", braket6)
        #print(total_tax)
       

        #37% braket7
        #last braket might requires attention bc final taxable amnt given is 'or more'
        if float(taxable_income) >= max_amnt7:
            braket7 = (float(taxable_income) - max_amnt7) * rate7
            total_tax = total_tax + braket7
            #print("b7 ", braket7)

        return total_tax

#count down to April 15, 2021  
from datetime import datetime

def calculate_dates(txdate, now):
    delta1 = datetime(now.year, txdate.month, txdate.day)
    delta2 = datetime(now.year+1, txdate.month, txdate.day)
    return ((delta1 if delta1 > now else delta2) - now).days

now = datetime.now()
taxday = datetime(2021,4,15)
c = calculate_dates(taxday, now)+ 1





tax = Fed_Tax()
print("1 =single, 2 = married, 3 = head of household, 4 = married filling seperately")
status = input("What is your taxable status? Select a number and press enter. ")
taxable_income = input("What is your taxable income? ")

if status == "2":
    tax_due = tax.fed_tax_calc_married(taxable_income)
    print(" Filling as Married, the federal tax amount due is ${}.".format(tax_due))
elif status == "4":
    tax_due = tax.fed_tax_calc_separately_married(taxable_income)
    print("Filling as Married Filling Separately, the federal tax amount due is ${}.".format(tax_due))
elif status == "1":
    tax_due = tax.fed_tax_calc_single(taxable_income)
    print("Filling as Single, the federal tax amount due is ${}.".format(tax_due))
elif status == "3":
    tax_due = tax.fed_tax_calc_head_of_hhold(taxable_income)
    print("Filling as Head of Household, the federal tax amount due is ${}.".format(tax_due))
else:
    print("Error - Please enter 1-4 to select taxable status.")





print("There are {} days before tax day, April 15, 2021.".format(c))













    













    




                                 














    













    




                                 














    













    




                                 














    













    




                                 
