#MODES- 
# read(r)[this is the default mode if no mode is given]
# write(w)[creates a new file if the file doesn't exist| it erases the already present content and writes the new content]
# appending(a)[creates a new file if the file doesn't exist | doesn't erase the existing content]
# create(x)[creates a file and throws an error if the file already exists]
# text(t)[used to handle text files | no diff btwr and rt , w and wt as t is default]
# binary(b)[used to handle binary files]

# ---------READING A FILE-----------------
# f=open("myfile.txt","r")    #open function requires 2 arguments-filename and mode of opening
# text=f.read()   #read function is to read a file
# print(text)
# f.close()

# ------------WRITING INTO A FILE-------------
f=open('file.txt','w')      #use a for appending 
f.write("Heyloo World!")
f.close()

#by using 'with' we don't need to close the file
with open('file.txt','a') as f:
    f.write("Hey I'm inside with")