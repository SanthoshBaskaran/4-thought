list2=[1,1,2,1,2,1,2,1,1,2,2,3,2,3,2,3,2,2,3,3,4,3,4,3,4,3,3,4,4,1,4,1,4,1,4,4,1,1,3,1,3,1,3,1,1,2,2,4,2,4,2,4,2,2,3,3,1,3,1,3,1,3,3,4,4,2,4,2,4,2,4,4,1,1,4,1,4,1,4,1,1,2,2,1,2,1,2,1,2,2,3,3,2,3,2,3,2,3,3,4,4,3,4,3,4,3,4,4,1,2,3,1,3,2,1,2,4,1,4,2,1,3,4,1,4,3,2,3,4,2,4,3,2,3,1,2,1,3,2,4,1,2,1,4,3,4,1,3,1,4,3,2,4,3,4,2,3,2,1,3,1,2,4,1,2,4,2,1,4,2,3,4,3,2,4,3,1,4,1,3,1,1,1,2,2,2,3,3,3,4,4,4]                                                 
size=int(input())
solution_list=[]
count=0
i=0
for r in range(size):
    n=int(input())
    list3=list2.copy()
    while(count<=63):
        list1=[4,' ',4,' ',4,' ',4]
        st=""
        expression=""
        dict1={1:'//',2:'*',3:'+',4:'-'}
        a=list3[0]
        b=list3[1]
        c=list3[2]
        list1[1]=dict1[a]
        list1[3]=dict1[b]
        list1[5]=dict1[c]
        count=count+1
        for i in list1:
            st=st+str(i)
        st=int((eval(st)))
        if(st==n):
            for c in list1:
                if(c=='//'):
                    index1=list1.index(c)
                    list1[index1]='/'
            for k in list1:
                expression=expression+str(k)+' '
            eval(expression)
            expression=expression+'= '+str(n)
            solution_list.append(expression)
            count=0
            break
        else:
            list3.remove(a)
            list3.remove(b)
            list3.remove(c)
        if(count==64):
            solution_list.append('no solution')
            count=0
            break
s=0
while(s<=len(solution_list)-1):
    print(solution_list[s])
    s=s+1
