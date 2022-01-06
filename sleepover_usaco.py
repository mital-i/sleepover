n = int(input())

seats = list(range(1, n+1))
tracker = [0]*n

finished_seat = None
def rotate(n, seats, current_seat, current_index, tracker):
    for i in range(2): 
        if seats[current_index%n]==0: 
            return current_seat
        tracker[current_seat-1]+=1
        count_seats = 0
        while count_seats < current_seat:
            current_index+=1
            current_index%=n
            #if tracker[current_index]==0 and seats[current_index]!=0: 
            count_seats+=1
        store = seats[current_index%n]
        seats[current_index] = current_seat
        print(current_index, store, seats, tracker)
        current_seat = store
    
    '''if current_index%n == 0: 
        finished_seat = current_seat
        return'''
    return
    
seats[0] = 0
rotate(n, seats, 1, 0, tracker)
print(rotate(n, seats, 1, 0, tracker))
