a=str(input("Enter the string:"))
b=a.split()
c=[]
for r in b:
    l=r.lower()
    c.append(l)
set1=set(c)
dic={}
for s in set1:
    count=c.count(s)
    dic.update({s:count})
dic2={}       
set2={1,2}
set2.clear()  
list2=[]     
if len(b)==1:
    
    for elements in a:
        list2.append(elements)
   
    for el in list2:
        set2.add(el.lower())
    
    string_l=a.lower()
    for elem in set2:
        
        dic2.update({elem:string_l.count(elem)})
    
    print("\nDictionary containing 'Letter':'Letter Count' is shown below:")
    print(dic2)

else:
    print("\nDictionary containing {'Word':'Word Count'} is shown below:")
    print(dic)      
