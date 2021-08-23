import csv, os, io
from pandas import *
import numpy as np




class manage_data():
    
    def get_username(self, file):
        my_pandas = pandas.read_csv(file, header=None).to_dict()
        list_username = []
        for i in my_pandas[0]:
            list_username.append(str(my_pandas[0][i]))
            
        return list_username
    
    def get_password(self, file):
        my_pandas = pandas.read_csv(file, header=None).to_dict()
        list_password = []
        for i in my_pandas[1]:
            list_password.append(str(my_pandas[1][i]))
        
        return list_password
    
class manage_data_address():
    def read_file(self, files):
    # open the file in read mode
    # reading CSV file
        data = read_csv(files)
        data = data.replace(np.nan, '', regex=True)

        # converting column data to list
        first_name = data['first_name'].tolist()
        last_name = data['last_name'].tolist()
        address1 = data['address1'].tolist()
        address2 = data['address2'].tolist()
        city = data['city'].tolist()
        state = data['state'].tolist()
        zip_code = data['zip_code'].tolist()
        country = data['country'].tolist()
        birthday = data['birthday'].tolist()
        color = data['color'].tolist()
        age = data['age'].tolist()
        website = data['website'].tolist()
        picture = data['picture'].tolist()
        phone = data['phone'].tolist()
        interest_climb = data['interest_climb'].tolist()
        interest_dance = data['interest_dance'].tolist()
        interest_read = data['interest_read'].tolist()
        note = data['note'].tolist()
        #tp = data['toothpaste'].tolist()
        #sh = data['shampoo'].tolist()
        #for i in picture:
        #    i = i.replace('nan','1')

        # printing list data
        #print('first_name:', first_name)
        #print('last_name:', last_name)
        #print('address1:', address1)
        #print('address2:', address2)
        #print('city:', city)
        #print('state:', state)
        #print('zip_code:', zip_code)
        #print('country:', country)
        #print('birthday:', birthday)
        #print('color :', color)
        #print('age :', age)
        #print('website:', website)
        #print('picture:', picture)
        #print('phone:', phone)
        #print('interest_climb :', interest_climb)
        #print('interest_dance:', interest_dance)
        #print('interest_read:', interest_read)
        #print('note :', note)
        #
        return data
        #for i in range(len(data))
        #    print(data[i])
        
        #index = data.index
        #numberrow = len(index)
        #print(numberrow)
        
        
#if __name__ == "__main__":
#    manage_data_address().read_file("filecsv/address.csv")