if __name__ == '__main__':
    N = int(input())
    output = [];
    for i in range(0,N):
        am = input().split();
        if am[0] == "print":
            print(output)
        elif am[0] == "insert":
            output.insert(int(am[1]),int(am[2]))
        elif am[0] == "remove":
            output.remove(int(am[1]))
        elif am[0] == "pop":
            output.pop();   
        elif am[0] == "append":
            output.append(int(am[1]))    
        elif am[0] == "sort":
            output.sort();
        else:
            output.reverse();    
              