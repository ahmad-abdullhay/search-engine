
import tkinter as tk
import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'controllers'))
import query as q
import dataset_testing as dt
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'parsers'))
import dataset_reader as dr
import main as m
import config as con
import re
# buttons functions
def search ():
    errorCorrection()
    mylist2.delete(0,tk.END)
    results = q.searchByString(searchEntry.get())
    for index,r in enumerate(results):
        string =str(index+1)+' : document id = ' + str(r+1)
        mylist2.insert(tk.END, string)
        mylist2.insert(tk.END, documents[r].title)
        mylist2.insert(tk.END, '')

def onChange(sv):
    string = sv.get()
    if (string[-1] == ' ' and string[0] == '!'):
       results = q.querySuggestion(string)
       for index,widget in enumerate(my_label_frame.winfo_children()):
        if index >0:
            widget.destroy() 
       for index,result in enumerate(results):
           if (index>4):
            break
           correct = tk.Label(my_label_frame,text = result)
           correct.pack()  



def errorCorrection ():
    for index,widget in enumerate(my_label_frame.winfo_children()):
        if index >0:
            widget.destroy()
    hasCorrect = q.queryCorrection(searchEntry.get())
    if (hasCorrect != searchEntry.get()):
        correct = tk.Label(my_label_frame,text = "do you mean : "+str(hasCorrect))
        correct.pack()

def testButtonOnClick():
    mylist.delete(0,tk.END)
    results = m.test()
    precisionList = []
    recallList = []
    MPR = []
    MAP = []
    for x in results:
         precisionNumber = x['sumOfTrues']/x['@k']
         recallNumber =x['sumOfTrues']/len(x['queryResult'].result)
         index = 'query id = '+ str(x['queryModel'].id)
         precision = 'Precision  = '+str(x['sumOfTrues'])+' / '+str(x['@k'])
         recall = 'Recall = '+str(x['sumOfTrues']) +' / '+str(len(x['queryResult'].result))
         rr = 'RR = '+str(x['rr'])
         avp = 'AvP = '+str(x['avp'])
         precisionList.append(precisionNumber)
         recallList.append(recallNumber)
         MPR.append(x['rr'])
         MAP.append(x['avp'])
         mylist.insert(tk.END, index)
         mylist.insert(tk.END, precision)
         mylist.insert(tk.END, recall)
         mylist.insert(tk.END, rr)
         mylist.insert(tk.END, avp)
         mylist.insert(tk.END, ' ')
    mylist.insert(0, ' ')
    mylist.insert (0,'MRR = '+str(round(sum(MPR)/len(results),3)))
    mylist.insert (0,'MAP = '+str(round(sum(MAP)/len(results),3)))
    mylist.insert (0,'average recall = '+str(round(sum(recallList)/len(results),3)))
    mylist.insert (0,'average precision = '+str(round(sum(precisionList)/len(results),3)))


def topicButtonOnClick():
    topicmylist.delete(0,tk.END)
    results = m.topicDetect()
    for x in results:
         topic = ", ".join(re.findall("[a-zA-Z]+", x[1]))
         topicmylist.insert(tk.END, topic)

documents = q.initTfidf()  
window = tk.Tk()
window.title("LSI search engine "+con.getDatasetName()+" dataset")
window.minsize(1000, 500)
# main three columns

frame1 = tk.Frame(master=window, width=225, height=300)
frame1.pack_propagate(0)
frame1.pack(fill=tk.Y, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=500)
frame2.pack_propagate(0)
frame2.pack(fill=tk.Y, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=225)
frame3.pack_propagate(0)
frame3.pack(fill=tk.Y, side=tk.LEFT, expand=True)



# search text field
my_label_frame = tk.LabelFrame(frame2, text="Search")
my_label_frame.pack()
sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: onChange(sv))
searchEntry = tk.Entry(my_label_frame, font=("Helvetica", 18), width=47,textvariable=sv)
searchEntry.pack()


# Buttons
button_frame = tk.Frame(frame2)
button_frame.pack(pady=10)

search_button = tk.Button(button_frame, text="search", font=("Helvetica", 16),
 fg="#3a3a3a", command=search)
search_button.grid(row=0, column=1, padx=20)

test_button = tk.Button(button_frame, text="test", font=("Helvetica", 16),
 fg="#3a3a3a", command=testButtonOnClick)
test_button.grid(row=0, column=2, padx=20)

topic_button = tk.Button(button_frame, text="topic detect", font=("Helvetica", 16),
 fg="#3a3a3a", command=topicButtonOnClick)
topic_button.grid(row=0, column=0, padx=20)

# search results list view

searchResultframe = tk.LabelFrame(master=frame2, width=500,bg="white",text = 'search results')
searchResultframe.pack_propagate(0)
searchResultframe.pack(fill=tk.Y, side=tk.LEFT, expand=True)
scrollbar2 = tk.Scrollbar(searchResultframe)
scrollbar2.pack( side = tk.RIGHT, fill = tk.Y )
mylist2 = tk.Listbox(searchResultframe, yscrollcommand = scrollbar2.set ,width=200)
mylist2.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar2.config( command = mylist2.yview )

# topic detect
topicDetectLabel = tk.Label(frame1,text = 'topic detect results')
topicDetectLabel.pack()
topicscrollbar = tk.Scrollbar(frame1)
topicscrollbar.pack( side = tk.RIGHT, fill = tk.Y )
topicmylist = tk.Listbox(frame1, yscrollcommand = topicscrollbar.set ,width=200)
topicmylist.pack( side = tk.LEFT, fill = tk.BOTH )
topicscrollbar.config( command = topicmylist.yview )


# test results list view
testResultLabel = tk.Label(frame3,text = 'test results')
testResultLabel.pack()
scrollbar = tk.Scrollbar(frame3)
scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
mylist = tk.Listbox(frame3, yscrollcommand = scrollbar.set ,width=200)
mylist.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = mylist.yview )

window.mainloop()